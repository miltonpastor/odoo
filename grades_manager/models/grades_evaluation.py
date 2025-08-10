from odoo import models, fields, api

# Declaración de un modelo
# Hereda todas las funcionalidades de models
class GradesEvaluation(models.Model):
    _name = 'grades.evaluation' # nombre del modelo

    name = fields.Char(string = 'Name')
    date = fields.Date(string = 'Date')
    description = fields.Text(string = 'Description')
    course_id = fields.Many2one('grades.course', string = 'Curso', ondelete='cascade')
    grade_ids = fields.One2many('grades.grade', 'evaluation_id', string='Grades')

    @api.model_create_multi
    def create(self, vals):
        result = super(GradesEvaluation, self).create(vals) # Llama al metodo create del padre (models.Model)
        for student in result.course_id.student_ids:
            self.env['grades.grade'].create({
                'student_id': student.id,
                'evaluation_id': result.id,
                'value': 0.0,  # Valor inicial de la nota
            })
        return result