from odoo import _, api, fields, tools, models
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    confirmed_user_id = fields.Many2one("res.users", string="Utilisateur ayant Confirmé")

    city_id = fields.Many2one("sale.city", string="Ville")


    def action_quotation_send(self):
        if not self.confirmed_user_id:
            raise UserError(_("impossible d envoyer le mail si utilisateur n'est pas renseigné"))
        # print("envoie mail impossible")
        # raise UserError(_('Impossible d envoyer le mail'))
        result = super().action_quotation_send()
        return result

class SaleCity(models.Model):
    _name = "sale.city"
    _description = "Ville"

    name= fields.Char(string="Ville")


