from email.policy import default
from odoo import _, api, fields, tools, models


class SchoolCourse(models.Model):
    _name = "school.course"
    _description = "Cours"


    name =fields.Char(string = "Course Name",required=True)




