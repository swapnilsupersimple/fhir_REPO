from odoo import models, fields , api
from datetime import datetime

class Period(models.Model):
    _name = 'period.fhir'
    _description = 'Period'

    opened_field=fields.Datetime(string="Start Time")

    closed_field=fields.Datetime(string="End Time")

    # diff = fields.Float(string="Period")
    #
    # @api.onchange('opened_field', 'closed_field', 'Period')
    # def calculate_date(self):
    #     if self.opened_field and self.closed_field:
    #         t1 = datetime.strptime(str(self.opened_field), '%Y-%m-%d %H:%M:%S')
    #         t2 = datetime.strptime(str(self.closed_field), '%Y-%m-%d %H:%M:%S')
    #         t3 = t2 - t1
    #         self.diff = str(t3.days)






