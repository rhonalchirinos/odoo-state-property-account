# -*- coding: utf-8 -*-
# from odoo import http


# class RegionalizacionAccount(http.Controller):
#     @http.route('/regionalizacion_account/regionalizacion_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/regionalizacion_account/regionalizacion_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('regionalizacion_account.listing', {
#             'root': '/regionalizacion_account/regionalizacion_account',
#             'objects': http.request.env['regionalizacion_account.regionalizacion_account'].search([]),
#         })

#     @http.route('/regionalizacion_account/regionalizacion_account/objects/<model("regionalizacion_account.regionalizacion_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('regionalizacion_account.object', {
#             'object': obj
#         })

