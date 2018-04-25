# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BeerReport(models.Model):
#    _inherit = 'product.product'
    _name = 'beer.beer_report'
    alcohol_pct = fields.Float('Alcohol %', (3, 2))
    liters = fields.Float('Liters', (3, 2))
    alcohol_cl = fields.Float(compute="_alcohol_cl",store=True)
    

    @api.multi
    def do_calculate_cl(self):
        for beerReport in self:
            self.alcohol_cl = float((self.liters * (self.alcohol_pct /100))*100)

            
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
