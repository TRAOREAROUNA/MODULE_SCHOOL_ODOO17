from odoo import _,api,fields,models,tools

class PrinStudentList(models.TransientModel):
    _name ="print.student.list"
    _description = "Print Student List"

    student_ids = fields.Many2many("school.student")


    def print_student_list(self):
        data ={}

        list_to_print = []
        for student_id in self.student_ids:
            vals = {
                "matricule": student_id.matricule,
                "name" : student_id.name,
                "birth_date" : student_id.birth_date,
                "description" : student_id.description
            }
            list_to_print.append(vals)
        data["list_to_print"] = list_to_print
        return self.env.ref("school.action_print_student_list_report").report_action(self, data)

