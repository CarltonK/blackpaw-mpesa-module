# -*- coding: utf-8 -*-
# from odoo import http


# class BlackpawMpesaPayment(http.Controller):
#     @http.route('/blackpaw_mpesa_payment/blackpaw_mpesa_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blackpaw_mpesa_payment/blackpaw_mpesa_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('blackpaw_mpesa_payment.listing', {
#             'root': '/blackpaw_mpesa_payment/blackpaw_mpesa_payment',
#             'objects': http.request.env['blackpaw_mpesa_payment.blackpaw_mpesa_payment'].search([]),
#         })

#     @http.route('/blackpaw_mpesa_payment/blackpaw_mpesa_payment/objects/<model("blackpaw_mpesa_payment.blackpaw_mpesa_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blackpaw_mpesa_payment.object', {
#             'object': obj
#         })

