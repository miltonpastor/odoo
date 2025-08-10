from odoo import models, fields

# Declaración de un modelo
# Hereda todas las funcionalidades de models
class GradesCourse(models.Model):
    _name = 'grades.course' # nombre del modelo

    def _default_teacher_id(self):
        teacher = self.env['res.partner'].search([('is_teacher', '=', True), ('email', '=', 'mainT@gmail.com')], limit=1)
        return teacher


    name = fields.Char(string = 'Course Name')
    student_qty = fields.Integer(string = 'Student Quantity')
    grase_avarage = fields.Float(string = 'Grade Avarage')
    description = fields.Text(string = 'Description')
    is_active = fields.Boolean(string = 'Is active')
    course_start = fields.Datetime(string = 'Course Start Date', default=fields.Datetime.now)
    course_end = fields.Datetime(string = 'Course End Date')
    last_evaluation_date = fields.Datetime(string = 'Last Evaluation Date')
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