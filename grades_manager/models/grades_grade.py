from odoo import models, fields

class GradesGrade(models.Model):
    _name = 'grades.grade'
    _description = 'Grade'

    student_id = fields.Many2one('res.partner', string='Student', required=True, domain=[('is_student', '=', True)])
    value = fields.Float(string='Value', required=True)
    date = fields.Date(string='Date', default=fields.Date.context_today)
    evaluation_id = fields.Many2one('grades.evaluation', string='Evaluation', readonly=True)

