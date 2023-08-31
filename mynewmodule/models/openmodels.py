from odoo import models, fields, api


class TestModelA(models.Model):
    _name= "test.modela"
    _description="testmodela"

    name = fields.Char(string='Name')
    teacher = fields.Many2one('res.users', string="Teacher")
    age = fields.Integer(string="Age")