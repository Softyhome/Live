# -*- coding: utf-8 -*-
# from odoo import http


# class SaleInvoiceCustomization(http.Controller):
#     @http.route('/sale_invoice_customization/sale_invoice_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_invoice_customization/sale_invoice_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_invoice_customization.listing', {
#             'root': '/sale_invoice_customization/sale_invoice_customization',
#             'objects': http.request.env['sale_invoice_customization.sale_invoice_customization'].search([]),
#         })

#     @http.route('/sale_invoice_customization/sale_invoice_customization/objects/<model("sale_invoice_customization.sale_invoice_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_invoice_customization.object', {
#             'object': obj
#         })
