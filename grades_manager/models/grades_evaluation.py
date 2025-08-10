from odoo import models, fields

# Declaración de un modelo
# Hereda todas las funcionalidades de models
class GradesEvaluation(models.Model):
    _name = 'grades.evaluation' # nombre del modelo

    name = fields.Char(string = 'Course Name')
    date = fields.Date(string = 'Date')
    description = fields.Text(string = 'Description')
    course_id = fields.Many2one('grades.course', string = 'Curso', ondelete='cascade')


