# -*- coding: utf-8 -*-
# from odoo import http


# class BaseDatatypes(http.Controller):
#     @http.route('/base_datatypes/base_datatypes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_datatypes/base_datatypes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_datatypes.listing', {
#             'root': '/base_datatypes/base_datatypes',
#             'objects': http.request.env['base_datatypes.base_datatypes'].search([]),
#         })

#     @http.route('/base_datatypes/base_datatypes/objects/<model("base_datatypes.base_datatypes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_datatypes.object', {
#             'object': obj
#         })
