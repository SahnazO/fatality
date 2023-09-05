# -*- coding: utf-8 -*-
# from odoo import http


# class AliAddon(http.Controller):
#     @http.route('/ali_addon/ali_addon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ali_addon/ali_addon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ali_addon.listing', {
#             'root': '/ali_addon/ali_addon',
#             'objects': http.request.env['ali_addon.ali_addon'].search([]),
#         })

#     @http.route('/ali_addon/ali_addon/objects/<model("ali_addon.ali_addon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ali_addon.object', {
#             'object': obj
#         })
