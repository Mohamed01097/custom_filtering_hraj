# -*- coding: utf-8 -*-
# from odoo import http


# class CustomFiltering(http.Controller):
#     @http.route('/custom_filtering/custom_filtering', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_filtering/custom_filtering/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_filtering.listing', {
#             'root': '/custom_filtering/custom_filtering',
#             'objects': http.request.env['custom_filtering.custom_filtering'].search([]),
#         })

#     @http.route('/custom_filtering/custom_filtering/objects/<model("custom_filtering.custom_filtering"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_filtering.object', {
#             'object': obj
#         })
