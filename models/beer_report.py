
from odoo import models, fields, api

class BeerProduct(models.Model):
    _inherit = 'product.template'
   # _name = 'beer.beer_product'
    alcohol_pct = fields.Float('Alcohol %', (3, 2))
    liter = fields.Float('Liters', (3, 2))
    alcohol_cl = fields.Float(compute="_alcohol_cl",store=False)
    

    @api.multi
    def do_calculate_cl(self):
        for beerReport in self:
            self.alcohol_cl = float((self.liters * (self.alcohol_pct /100))*100)



class BeerPartner(models.Model):
	_inherit = 'res.partner'
	excise_liable = fields.Boolean('Excise Liable', required=True, default=True)
	excise_number = fields.Char('Excise Number')
	excise_warehouse = fields.Char('Excise Warehouse Number')
	alcohol_license = fields.Char('Alcohol license')
            
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
