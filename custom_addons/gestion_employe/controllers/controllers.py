# -*- coding: utf-8 -*-
# from odoo import http


# class GestionEmploye(http.Controller):
#     @http.route('/gestion_employe/gestion_employe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_employe/gestion_employe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_employe.listing', {
#             'root': '/gestion_employe/gestion_employe',
#             'objects': http.request.env['gestion_employe.gestion_employe'].search([]),
#         })

#     @http.route('/gestion_employe/gestion_employe/objects/<model("gestion_employe.gestion_employe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_employe.object', {
#             'object': obj
#         })

