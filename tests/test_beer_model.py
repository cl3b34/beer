# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestBeerModel(TransactionCase):

    def setUp(self, *args, **kwargs):
        result=super(TestBeerModel, self).setUp(*args, **kwargs)
        user_demo=self.env.ref('base.user_demo')
        self.env=self.env(user=user_demo)
        return result
    
    def test_create(self):
        "Create basic fields needed for reporting on beer sales"
        BeerReport = self.env['beer.beer_report']
        Product = self.env['product.template']
        product = Product.create({'name':'test'})
        beer = BeerReport.create({'alcohol_pct': 3,'liters': 0.33, 'product': product})
        self.assertEqual(beer.alcohol_pct, 3)
        self.assertEqual(beer.liters, 0.33)
        # Test alcohol CL
        self.assertEqual(beer.alcohol_cl, 0.00)
        beer.do_calculate_cl()
        self.assertAlmostEqual(beer.alcohol_cl, 0.99, places=3)


    def test_record_rule(self):
        "Test per-user record rules"
        BeerReport = self.env['beer.beer_report']
        beer = BeerReport.sudo().create({'alcohol_pct': 99, 'liters': 99})
        with self.assertRaises(AccessError):
            BeerReport.browse([beer.id]).alcohol_pct
