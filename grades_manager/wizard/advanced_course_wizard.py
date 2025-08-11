from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AdvancedCourseWizard(models.TransientModel):
    _name = 'advanced.course.wizard'
    _description = 'Advanced Course Wizard'

    def _default_available_student_ids(self):
        course_ids = self._context.get('active_ids') # cursos con el check activo
        courses = self.env['grades.course'].browse(course_ids)
        students = self.env['res.partner']
        for course in courses:
            students |= course.student_ids
        return students

    course_name = fields.Char(string='Course Name', required=True)
    teacher_id = fields.Many2one('res.partner', string='Teacher', required=True, domain=[('is_teacher', '=', True)])
    available_student_ids = fields.Many2many('res.partner', string='Available Students', domain=[('is_student', '=', True)],
                                             default=_default_available_student_ids)
    student_ids = fields.Many2many('res.partner', 'wizard_students_rel', string='Selected Students')


    def create_course(self):
        if not self.student_ids:
            raise ValueError("You must select at least one student for the course.")

        course = self.env['grades.course'].create({'name': self.course_name ,'teacher_id': self.teacher_id.id, 'type': 'advanced',  'student_ids': self.student_ids.ids})
        return course