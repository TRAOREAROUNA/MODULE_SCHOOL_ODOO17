from odoo import _,api,fields,tools,models

class CreateStudent(models.TransientModel):

    _name="create.student"
    _description = "Creation eleve"

    name =fields.Char()
    date =fields.Date()

    def create_student(self):
        vals = {
            "name" : self.name,
            "birth_date" : self.date
        }
        student = self.env['school.student'].create(vals)
        return student