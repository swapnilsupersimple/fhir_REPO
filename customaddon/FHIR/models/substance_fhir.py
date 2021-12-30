from odoo import models, fields, api


class Substance(models.Model):
    _name = "substance"
    _description = "Details about Substance"
    # _rec_name = "appointment_status"

    substance_status = fields.Selection(selection=[
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("entered in error", "Entered in error"),
    ], string="Task Status")

    substance_description=fields.Char(string="Description")

    substance_instance_expiry=fields.Datetime(string="Expiry Date")

    substance_instance_quantity=fields.Integer(string="Quantity")

    substance_category=fields.Many2one(comodel_name="substance.category",string="category")

    substance_code=fields.Many2one(comodel_name="substance.code",string="Code")


class SubstanceCategory(models.Model):
    _name = "substance.category"
    _description = "Details about Substance Category"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    definition = fields.Char("Definition")

class SubstanceCode(models.Model):
    _name = "substance.code"
    _description = "Details about Substance Code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    definition = fields.Char("Definition")







