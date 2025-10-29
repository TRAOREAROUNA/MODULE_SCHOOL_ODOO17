from odoo import _, api, fields, tools, models

class SchoolRendezvous(models.Model):
    _name = "school.rendezvous"
    _description = "Rendez-vous"
    _rec_name = "student_id"

    date_debut = fields.Date()
    date_fin = fields.Date()
    student_id = fields.Many2one("school.student",string="student")
    description = fields.Char()


