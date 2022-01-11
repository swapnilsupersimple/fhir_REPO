from odoo import models, fields, api


class Endpoint(models.Model):
    _name = "endpoint"
    _description = "Details about Endpoint"
    # _rec_name = "appointment_status"

    endpoint_status = fields.Selection(selection=[
        ("active", "Active"),
        ("suspended", "Suspended"),
        ("error", "Error"),
        ("off", "Off"), ("test", "Test"),
        ("entered in error", "Entered in Error"),
    ], string="Status")

    endpoint_name=fields.Char(string="Name")

    endpoint_managing_organization=fields.Reference([('organization', "Organization Name")], string="Organization Name")

    endpoint_period_start=fields.Datetime(string="Start Time")

    endpoint_period_end=fields.Datetime(string="End Time")

    endpoint_payload_type=fields.Many2many(comodel_name="endpoint.payload.type",string="Payload Type")

    endpoint_header=fields.Char(sting="Header")

    endpoint_address=fields.Char(string="Address")

    endpoint_contact=fields.Reference([('contact.point','Phone')],

        string="Contact")

    imagingStudy_endpoint= fields.Many2one("imaging.study", string="imagingStudyEndpoint")

    imagingStudySeries_endpoint= fields.Many2one("imaging.study.series", string="imagingStudyEndpoint")

    reference = fields.Char(string="reference")
    display = fields.Char(string="display")





class EndpointPayloadType(models.Model):
    _name = "endpoint.payload.type"
    _description = "details about Endpoint Payload Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")














