# -*- coding: utf-8 -*-
# from odoo import http


# class Protrain(http.Controller):
#     @http.route('/protrain/protrain', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/protrain/protrain/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('protrain.listing', {
#             'root': '/protrain/protrain',
#             'objects': http.request.env['protrain.protrain'].search([]),
#         })

#     @http.route('/protrain/protrain/objects/<model("protrain.protrain"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('protrain.object', {
#             'object': obj
#         })
