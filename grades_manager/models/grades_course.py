from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Declaración de un modelo
# Hereda todas las funcionalidades de models
class GradesCourse(models.Model):
    _name = 'grades.course' # nombre del modelo

    def _default_teacher_id(self):
        teacher = self.env['res.partner'].search([('is_teacher', '=', True), ('email', '=', 'mainT@gmail.com')], limit=1)
        return teacher


    name = fields.Char(string = 'Course Name')
    student_qty = fields.Integer(string = 'Student Quantity', compute='_compute_student_qty', store=True)
    grase_avarage = fields.Float(string = 'Grade Avarage')
    description = fields.Text(string = 'Description')
    is_active = fields.Boolean(string = 'Is active')
    course_start = fields.Datetime(string = 'Course Start Date', default=fields.Datetime.now)
    course_end = fields.Datetime(string = 'Course End Date')
    last_evaluation_date = fields.Date(string = 'Last Evaluation Date', compute='_compute_last_evaluation_date', store=True)
    course_image = fields.Binary(string = 'Course Image')
    course_shift = fields.Selection([('day', 'Day'), ('night', 'Night')], string = 'Course Shift')
    teacher_id = fields.Many2one('res.partner', string = 'Teacher', default=_default_teacher_id)
    teacher_email = fields.Char(related='teacher_id.email', string='Teacher Email', readonly=True)
    grades_evaluation_ids = fields.One2many('grades.evaluation', 'course_id', string = 'Evaluations')
    student_ids = fields.Many2many('res.partner', 'courses_students_rel' ,string = 'Students')
    state = fields.Selection([['register', 'Register'],
                              ['in_progress', 'In Progress'],
                              ['finished', 'Finished']],
                             string = 'State',
                             default = 'register',
                             required = True,
                             help = 'State of the course')
    invalid_dates = fields.Boolean(string = 'Invalid Dates')


    def write(self, vals):
        if vals and "grades_evaluation_ids" in vals and not self.student_ids:
            raise ValidationError("You cannot write to a course without students.")

        result = super(GradesCourse, self).write(vals)  # Llama al metodo write del padre (models.Model)
        return result

    @api.onchange('course_start', 'course_end')
    def onchange_dates(self):
        if self.course_start and self.course_end:
            self.invalid_dates = self.course_start > self.course_end
        else:
            self.invalid_dates = False

    @api.depends('grades_evaluation_ids.date')
    def _compute_last_evaluation_date(self):
        for course in self:
            if course.grades_evaluation_ids:
                evaluation = course.grades_evaluation_ids[-1]
                course.last_evaluation_date = evaluation.date
            else:
                course.last_evaluation_date = False


    @api.depends('student_ids')
    def _compute_student_qty(self):
        for course in self:
            course.student_qty = len(course.student_ids)