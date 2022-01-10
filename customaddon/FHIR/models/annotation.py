from odoo import models, fields, api


class Annotation(models.Model):
    _name = "annotation"
    _rec_name = "text"
    _description = "Details about Annotation"

    time = fields.Datetime(string="Time")

    text = fields.Text(string="Text")



    ImagingStudy_annotation = fields.Many2one("imaging.study", string="ImagingStudy_annotation")
