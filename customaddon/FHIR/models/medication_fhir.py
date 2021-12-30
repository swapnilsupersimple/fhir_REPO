from odoo import models, fields, api


class Medication(models.Model):
    _name = "medication"
    _description = "Details about Medication"
    # _rec_name = "location_name"

    medication_status = fields.Selection(selection=[
        ("Active", "Active"),
        ("inactive", "Inactive"),
        ("entered in error", "Entered in error")
    ], string="Status")

    medication_manufacturer=fields.Reference([('organization', 'organization')], string="Manufacturer")

    medication_batch_lotNumber=fields.Char(string="Lot Number")

    medication_batch_expirationDate=fields.Datetime(string="Expiration Date")

    medication_code=fields.Many2one(comodel_name="medication.code",string="code")


class MedicationCode(models.Model):
    _name = "medication.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")













