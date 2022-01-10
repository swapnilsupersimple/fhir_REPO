from odoo import models,fields,api


class Attachment(models.Model):
    _name = "attachment"
    _rec_name = "title"

    # language = fields.char(comodel_name="res.lang",
    #                           string="Language")

    data = fields.Binary(string="Data")

    url = fields.Char(string="URL")

    size = fields.Integer(string="size")

    title = fields.Char(string="title")

    creation = fields.Datetime(string="Effective")

    attachment_id= fields.Many2one("diagnostic.report", string="DiagnosticReportAttachment")


