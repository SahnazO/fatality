from odoo import models, fields, api


class LostReason(models.Model):
    _name= "lost.reason"
    _description="Lost Reason"

    name = fields.Char(string='Description' , required=True)
    count =fields.Integer()
    count2 =fields.Float('Reason Count' ,compute="_campute_count2", store=True)

    # @api.depends('count')
    # def _compute_count2(self):
    #     for record in self:
    #         record.count2 = float(record.count1) / 10    

    @api.depends('count')
    def _campute_count2(self):
        for record in self:
            record.count2 = float(record.count) / 100