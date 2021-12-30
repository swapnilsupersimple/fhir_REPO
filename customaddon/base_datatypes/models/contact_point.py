from odoo import models, fields ,api


class ContactPoint(models.Model):
    _name = 'contact.point'
    _description = 'Contact Point'
    _rec_name = "value"

    rank = fields.Integer(string="Rank")

    use = fields.Selection(
        string="Use",
        selection=[
            ("home", "Home"),
            ("work", "Work"),
            ("temp", "Temp"),
            ("old", "Old")],
        default="home"

    )

    system = fields.Selection(
        string="Type",
        selection=[
            ("phone", "Phone"),
            ("fax", "Fax"),
            ("email", "Email"),
            ("url", "Url")],
        default="phone",
        help="Telecommunications form for contact point - what communications system is required to make use of the contact.")

    value = fields.Char(string="Value")

    start=fields.Date(string="Start Period")

    end=fields.Date(string="End Period")





