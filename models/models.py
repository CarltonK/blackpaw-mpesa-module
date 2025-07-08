# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class blackpaw_mpesa_payment(models.Model):
#     _name = 'blackpaw_mpesa_payment.blackpaw_mpesa_payment'
#     _description = 'blackpaw_mpesa_payment.blackpaw_mpesa_payment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

