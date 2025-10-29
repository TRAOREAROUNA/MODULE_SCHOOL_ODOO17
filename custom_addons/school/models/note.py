from email.policy import default
from odoo import _, api, fields, tools, models

class SchoolNote(models.Model):
    _name = "school.note"
    _description = "Note Eleve"
    _rec_name = "course_id"


    # name =fields.Char(string = "Note Eleve",required=True)
    classe_note = fields.Float(string="Note de classe")
    exam_note = fields.Float(string="Note Examean")

    course_id =fields.Many2one("school.course",string="Cours")
    student_id=fields.Many2one("school.student",string="Student")




