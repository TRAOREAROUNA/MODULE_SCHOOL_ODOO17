from odoo import models, fields, api

class Contrat(models.Model):
    _name = 'gestion.contrat'
    _description = 'Contrat'


    type_contrat = fields.Selection([
        ("cdd","CDD"),
        ("cdi","CDI"),
        ("stage","STAGE"),
        ("interim","INTERIM"),
    ],string="Type de Contrat",default="cdd")
    date_debut = fields.Date(string="Date debut")
    date_fin = fields.Date(string="Date fin")
    employe_id= fields.Many2one("gestion.employe",string="Employé")
