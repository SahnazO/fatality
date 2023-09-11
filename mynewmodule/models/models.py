# -*- coding: utf-8 -*-

#   from odoo import models

#   class TestingModel(models.Model)
#     _name = "testing_model"
#     _description = "Testing Model"


#  class LfinxClass(models.LfinxClass):
#     _name = 'lfinx.class'
#      _description = 'lfinx.class'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = sfloat(record.value) / 100
