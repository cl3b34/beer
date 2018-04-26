# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestBeerModel(TransactionCase):
    
    def test_create(self):
        "Create basic fields needed for reporting on beer sales"
        BeerReport = self.env['beer.beer_report']
        beer = BeerReport.create({'alcohol_pct': 3,'liters': 0.33})
        self.assertEqual(beer.alcohol_pct, 3)
        self.assertEqual(beer.liters, 0.33)
        
