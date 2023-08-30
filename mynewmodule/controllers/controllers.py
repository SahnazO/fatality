# -*- coding: utf-8 -*-
# from odoo import http


# class Mynewmodule(http.Controller):
#     @http.route('/mynewmodule/mynewmodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mynewmodule/mynewmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mynewmodule.listing', {
#             'root': '/mynewmodule/mynewmodule',
#             'objects': http.request.env['mynewmodule.mynewmodule'].search([]),
#         })

#     @http.route('/mynewmodule/mynewmodule/objects/<model("mynewmodule.mynewmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mynewmodule.object', {
#             'object': obj
#         })
