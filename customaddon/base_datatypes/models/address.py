from odoo import models, fields , api

class AddressFhir(models.Model):
    _name = 'address.fhir'
    _description = 'Address'
    # _rec_name= "state"

    use = fields.Selection(string="Use", selection=[
        ("home", "Home"),
        ("work", "Work"),
        ("temp", "Temp"),
        ("old", "Old"),
        ("billing", "Billing")], default="home")

    type = fields.Selection(string="type", selection=[
        ("postal", "Postal"),
        ("physical", "Physical"),
        ("both", "Both")]

                            )
    country = fields.Many2one("res.country", string="Country")
    state = fields.Many2one("res.country.state", string="State")
    district = fields.Char(string="District")
    city = fields.Char(string="City")
    postalCode = fields.Char(string="Postal Code")
    line=fields.One2many("address","address_line_id", string="Address")
    text=fields.Char(string="Text")
    start=fields.Date(string="Start Period")
    end=fields.Date(string="End Period")


class Address(models.Model):
    _name = "address"
    _rec_name ="lines"


    lines = fields.Char(string="Address lines")
    address_line_id=fields.Many2one("address.fhir" ,string="Address_line_id")

















