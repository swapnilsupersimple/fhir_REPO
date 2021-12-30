from odoo import models, fields, api


class Slot(models.Model):
    _name = "slot"
    _description = "details about slot"
    # _rec_name = ""

    slot_status=fields.Selection(selection=[
        ("busy", "Busy"),
        ("free", "Free"),
        ("busy-unavailable", "Busy-unavailable"),
        ("busy-tentative", "Busy-tentative"),
        ("entered-in-error", "Entered-in-error"),
    ], string="Slot Status")

    slot_start=fields.Datetime(string="Slot Start Time")

    slot_end = fields.Datetime(string="Slot End Time")

    slot_overbooked=fields.Boolean(string="Is slot overbooked?")

    slot_comment=fields.Char(string="Additional Comment")



