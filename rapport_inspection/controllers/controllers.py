# -*- coding: utf-8 -*-
from openerp import http

# class RapportInspection(http.Controller):
#     @http.route('/rapport_inspection/rapport_inspection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rapport_inspection/rapport_inspection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rapport_inspection.listing', {
#             'root': '/rapport_inspection/rapport_inspection',
#             'objects': http.request.env['rapport_inspection.rapport_inspection'].search([]),
#         })

#     @http.route('/rapport_inspection/rapport_inspection/objects/<model("rapport_inspection.rapport_inspection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rapport_inspection.object', {
#             'object': obj
#         })