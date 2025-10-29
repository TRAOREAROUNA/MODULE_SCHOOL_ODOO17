from email.policy import default
from odoo import _, api, fields, tools, models


class SchoolClasse(models.Model):
    _name = "school.classe"
    _description = "Classe"


    name =fields.Char(string = "Classe Name",required=True)
    student_ids = fields.One2many("school.student","classe_id")
    description = fields.Text()
    student_count = fields.Integer(string="Total Eleve",compute="_get_student_count")

    def _get_student_count(self):
        self.student_count = len(self.student_ids)

    def student_list(self):
        return{
            "name":"Liste des eleves",
            "domain":[("classe_id","=",self.id)],
            "res_model":"school.student",
            "view_id": False,
            "view_mode": "tree,form",
            "context": {"default_class_id": self.id},
            "type":"ir.actions.act_window",

        }




