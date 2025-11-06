
from odoo import models, fields, api,_

class PartenaireEtendu(models.Model):
    _inherit = "res.partner"

    status_partenaire = fields.Selection([
        ("silver","Silver"),
        ("gold","Gold"),
        ("platinum","Platinum"),
    ],string="Status Partenaire",default="silver",required=True)

    commercial_id = fields.Many2one("res.users",string="Commercial",required=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

