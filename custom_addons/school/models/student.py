from email.policy import default

from dateutil.utils import today

from odoo import _, api, fields, tools, models
from datetime import date,datetime

from odoo.odoo.tools.populate import compute


class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Student"

    matricule = fields.Char(string="Matricule",readonly=True)
    name =fields.Char(string = "Last Name",required=True,tracking=True)
    birth_date =fields.Date(string = "Birthdate", default=date.today(),tracking=True)
    # description =fields.Text(string = "Description")
    photo =fields.Binary(string = "Photo")
    description = fields.Html()
    is_former_student = fields.Boolean(string="Est un ancien eleve")
    sexe = fields.Selection([
        ("Masculin","Masculin"),
        ("Feminin","Feminin")

    ],default="Masculin",tracking=True)
    age = fields.Integer(string="Age",store=True, compute="_compute_age",tracking=True)

    classe_id= fields.Many2one('school.classe',string="Classe")
    course_ids = fields.Many2many("school.course",string="Cours")
    note_ids = fields.One2many("school.note","student_id")

    email = fields.Char(string="Email")
    phone = fields.Char(string="Telephone")
    progression = fields.Float(string="Progression",default=20)
    course_time = fields.Float(string="Heure de cours")

    date_start = fields.Datetime(string="Date et heure de début",default=datetime.now())
    couleur = fields.Char(string="Couleur")
    other_color = fields.Integer(string="Autre Couleur")

    priority = fields.Selection([
        ("moyen","Moyen"),
        ("normal","Normal"),
        ("élevé","Elevé"),
        ("très elevé","Très Elevé")
    ],default="élevé")

    state = fields.Selection([
        ("preinscription", "Preinscription"),
        ("inscription", "Inscription"),
        ("abandonne", "Abandonne"),
        ("exclu", "Exclu"),
    ], default="preinscription", tracking=True)

    # Archivage de student
    active= fields.Boolean(default=True)

    @api.model
    def create(self,values):
        values['matricule']= self.env['ir.sequence'].next_by_code('school.student')
        result=super().create(values)
        return result

    # @api.model
    # def create(self,values):
    #     result=super().create(values)
    #     print("Creation11")
    #     return result

    #
    # def write(self,values):
    #     result=super().write(values)
    #     print("Modification....",values)
    #     return result

    @api.depends("birth_date","age")
    @api.onchange("birth_date")
    def _compute_age(self):
        today = date.today()
        # birth_date = self.birth_date
        for rec in self:
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age=0

    def compute_preinscription(self):
        for rec in self:
            rec.state = "preinscription"

    def compute_abandonne(self):
        for rec in self:
            rec.state = "abandonne"

    def compute_inscription(self):
        for rec in self:
            self.state = "inscription"

    def compute_exclu(self):
        self.state = "exclu"

    def compute_progress(self):
        self.progression += 5









