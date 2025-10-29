# from custom_addons.school.models import student
from odoo import http
from odoo.http import request


class SchoolStudentController(http.Controller):

    @http.route('/students<int:student_id>', auth="public", type="http", website=True, methods=['POST', 'GET'])
    def student_by_id(self, student_id):
        student = request.env["school.student"].search([('id', '=', int(student_id))])

        if student:
            return student.age
        else:
            return "Eleve n existe pas"


    @http.route("/students", auth="public", type="http", website=True, methods=['POST', 'GET'])
    def student(self):
        students = request.env["school.student"].search_read([])

        return request.render("school.student_template_id", {'students': students})

        # return request.render("school.student_template_id", {'students': students})

    @http.route("/students/create", auth="public", type="http", website=True, methods=['POST', 'GET'], csrf=True)
    def create_student(self, **kwargs):
        if request.httprequest.method == "POST":
            student = request.env["school.student"].create(kwargs)
        return request.render('school.student_form_template')