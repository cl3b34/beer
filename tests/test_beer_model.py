# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestBeerModel(TransactionCase):
    
    def test_create(self):
        "Create basic fields needed for reporting on beer sales"
        BeerReport = self.env['beer.beer_report']
        beer = BeerReport.create({'alcohol_pct': 5.5,'liters': 0.33})
        self.assertEqual(BeerReport.alcohol_pct, 5.5)
        self.assertEqual(BeerReport.liters, 0.33)
        
