from odoo import models, fields, api

class Employe(models.Model):
    _name = 'gestion.employe'
    _description = 'Employé'

    name = fields.Char(string='Nom complet', required=True)
    prenom = fields.Char(string='Prenom complet', required=True)
    email = fields.Char(string='Email professionnel',required=True)
    phone = fields.Char(string='Téléphone')
    date_embauche = fields.Date(string='Date d embauche')

    actif = fields.Boolean(string='Actif', default=True)
    photo = fields.Binary(string='Photo')
    service_id = fields.Many2one('gestion.service', string='Service')
    _sql_constraints = [
        ('email_uniq', 'unique (email)', "Cette adresse e-mail est déjà utilisée par un autre employé !"),
    ]



class Service(models.Model):
    _name = 'gestion.service'
    _description = 'Service / Département'

    name = fields.Char(string='Nom du service', required=True)
    description = fields.Text(string='Description')
    employe_ids = fields.One2many('gestion.employe', 'service_id', string='Employés')