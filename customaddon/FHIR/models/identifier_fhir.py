from odoo import models, fields, api


class Identifier(models.Model):
    _name = 'identifier'
    _description = 'Identifier'
    _rec_name = 'value'

    use = fields.Selection(
        string="Identifier Use",
        selection=[
            ("usual", "Usual"),
            ("official", "Official"),
            ("temp", "Temporary"),
            ("secondary", "Secondary")],
        help="The purpose of this identifier record.")

    value = fields.Char(
        string="Value",
        help="Value of this identifier record.")

    start=fields.Date(string="Start Period")

    end=fields.Date(string="End Period")

    assigner=fields.Reference([('organization', 'Organization')],
                                                    string="Identifier Assigner")

    imagingStudy_identifier=fields.Many2one("imaging.study",string="imagingStudy_identifier")




