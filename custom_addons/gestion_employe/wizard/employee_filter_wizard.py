from odoo import models, fields, api

class EmployeeFilterWizard(models.TransientModel):
    _name = 'gestion.employe.filter.wizard'
    _description = 'Assistant de Filtrage des Employés'

    # Champ de sélection pour l'état (actif ou inactif)
    status_filter = fields.Selection([
        ('active', 'Actif'),
        ('inactive', 'Inactif'),
        ('all', 'Tous'),
    ], string="Statut de l'employé", default='active', required=True)

    # Champ d'action (méthode qui va retourner la vue filtrée)
    def action_apply_filter(self):
        # 1. Construire le domaine (critère de filtre)
        domain = []
        if self.status_filter == 'active':
            domain = [('actif', '=', True)]
        elif self.status_filter == 'inactive':
            domain = [('actif', '=', False)]
        # Si 'all', le domaine reste vide, ce qui signifie pas de filtre sur 'actif'.

        # 2. Retourner l'action de la vue liste avec le domaine appliqué
        return {
            'name': 'Liste des Employés Filtrés',
            'type': 'ir.actions.act_window',
            'res_model': 'gestion.employe',
            'view_mode': 'tree,form',
            'domain': domain,
            'target': 'main', # Ouvre dans la fenêtre principale, pas un popup
        }