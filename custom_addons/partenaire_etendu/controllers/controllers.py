# -*- coding: utf-8 -*-
# from odoo import http


# class PartenaireEtendu(http.Controller):
#     @http.route('/partenaire_etendu/partenaire_etendu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partenaire_etendu/partenaire_etendu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partenaire_etendu.listing', {
#             'root': '/partenaire_etendu/partenaire_etendu',
#             'objects': http.request.env['partenaire_etendu.partenaire_etendu'].search([]),
#         })

#     @http.route('/partenaire_etendu/partenaire_etendu/objects/<model("partenaire_etendu.partenaire_etendu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partenaire_etendu.object', {
#             'object': obj
#         })

