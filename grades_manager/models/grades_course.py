from odoo import models, fields

# Declaración de un modelo
# Hereda todas las funcionalidades de models
class GradesCourse(models.Model):
    _name = 'grades.course' # nombre del modelo

    name = fields.Char(string = 'Course Name')
    student_qty = fields.Integer(string = 'Student Quantity')
    grase_avarage = fields.Float(string = 'Grade Avarage')
    description = fields.Text(string = 'Description')
    is_active = fields.Boolean(string = 'Is active')
    course_start = fields.Datetime(string = 'Course Start Date')
    course_end = fields.Datetime(string = 'Course End Date')
    last_evaluation_date = fields.Datetime(string = 'Last Evaluation Date')
    course_image = fields.Binary(string = 'Course Image')
    course_shift = fields.Selection([('day', 'Day'), ('night', 'Night')], string = 'Course Shift')
    teacher_id = fields.Many2one('res.partner', string = 'Teacher')
    grades_evaluation_ids = fields.One2many('grades.evaluation', 'course_id', string = 'Evaluations')
    student_ids = fields.Many2many('res.partner', 'courses_students_rel' ,string = 'Students')
    state = fields.Selection([['register', 'Register'],
                              ['in_progress', 'In Progress'],
                              ['finished', 'Finished']],
                             string = 'State',
                             default = 'register',
                             required = True,
                             help = 'State of the course')