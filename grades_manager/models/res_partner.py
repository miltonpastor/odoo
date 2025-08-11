from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string = 'Is Teacher')
    is_freelance = fields.Boolean(string = 'Is Freelance')
    is_student = fields.Boolean(string = 'Is Student')
    var = fields.Char(required=True, copy=False)

    # Si se elimina el teacher main cambiar de teacher en todos sus cursos
    def unlink(self):
        for partner in self:
            if partner.email == 'mainTeacher@gmail.com':
                courses = self.env['grades.course'].search([('teacher_id', '=', partner.id)])
                secondary_teacher = self.env['res.partner'].search([('is_teacher', '=', True), ('email', '=', 'secondaryTeacher@gmail.com')])
                courses.write({'teacher_id': secondary_teacher.id})
        result = super(ResPartner, self).unlink()  # Llama al metodo unlink del padre (models.Model)
        return result

    def copy(self, default=None):
        default = default or {}
        if self.is_teacher:
            default['name'] = 'Teacher Copy of ' + self.name
        elif self.is_student:
            default['name'] = 'Student Copy of ' + self.name
        return super(ResPartner, self).copy(default)
