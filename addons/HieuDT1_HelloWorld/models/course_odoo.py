from odoo import _,models, fields

class Course(models.Model):
    _name = 'course.odoo'
    _description = 'Khóa học'
    
    name = fields.Char(string='Tên khoá học')
    is_active = fields.Boolean(string='Khoá học có mở hay không', copy=False,
                               readonly=True, default=False, help="Khoá học có mở hay không?")

    lesson_ids = fields.One2many(
        comodel_name='lesson.odoo', inverse_name='parent_id', string='Bài học')

    def set_is_active_course(self):
        for item in self:
            item.is_active = False if item.is_active else True
        return {}