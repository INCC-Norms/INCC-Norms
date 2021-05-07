# -*- coding: utf-8 -*-
from openerp import http

# class Distance(http.Controller):
#     @http.route('/distance/distance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/distance/distance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('distance.listing', {
#             'root': '/distance/distance',
#             'objects': http.request.env['distance.distance'].search([]),
#         })

#     @http.route('/distance/distance/objects/<model("distance.distance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('distance.object', {
#             'object': obj
#         })