from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class GestionConge(models.Model):
    _name = 'gestion.conge'
    _description = 'Demande de Congé Employé'

    name = fields.Char(string="Description de la Demande", required=True)
    employe_id = fields.Many2one(
        'gestion.employe',
        string="Employé",
        required=True
    )
    date_debut = fields.Date(string="Date de Début", required=True)
    date_fin = fields.Date(string="Date de Fin", required=True)

    # Champ calculé simple pour la durée (en jours)
    duree_jours = fields.Float(string="Durée (Jours)", compute='_compute_duree', store=True)

    # État du congé : Brouillon, Soumis, Approuvé, Refusé
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('approved', 'Approuvé'),
        ('refused', 'Refusé'),
    ], default='draft', string="Statut")

    # Méthode simple de calcul de la durée
    @api.depends('date_debut', 'date_fin')
    def _compute_duree(self):
        for record in self:
            if record.date_debut and record.date_fin:
                # Calcul de la différence en jours (simplifié)
                delta = record.date_fin - record.date_debut
                record.duree_jours = delta.days + 1  # +1 pour inclure le jour de début
            else:
                record.duree_jours = 0.0

    @api.constrains('date_debut', 'date_fin')
    def _date_coherance(self):
        for record in self:
            if record.date_debut and record.date_fin and record.date_fin < record.date_debut:
                raise ValidationError("La date de fin ne doit pas etre inferieure à la date de debut")
            if record.duree_jours <= 0:
                raise ValidationError("La duree du congé ne peut pas etre inferieure ou egale à 0")



    @api.model
    def action_submit(self):
        # Utiliser un for loop est une bonne pratique, même si self contient souvent un seul enregistrement
        for record in self:
            record.write({'state': 'submitted'})
        return True  # Il est bon de retourner True ou un action dict



    @api.model
    def action_approve(self):
        for record in self:
            record.write({'state': 'approved'})
        return True
    #
    # @api.model
    # def action_refuse(self):
    #     for record in self:
    #         record.write({'state': 'refused'})
    #     return True
