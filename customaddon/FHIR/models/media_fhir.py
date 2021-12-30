from odoo import models, fields, api

from datetime import datetime



class Media(models.Model):
    _name="media"
    _description = "Details about media"
    # _rec_name = "location_name"

    media_status=fields.Selection(selection=[
        ("preparation", "Preparation"),
        ("In -progress", "in -progress"),
        ("not -done", "Not-done"),
        ("on - hold", "on-hold"), ("stopped", "Stopped"), ("completed", "Completed"),
        ("entered in error", "Entered in error"),
        ("unknown", "unknown"),
    ], string="Status")

    media_type=fields.Many2one(comodel_name="media.type",string="Media Type")

    media_modality=fields.Many2one(comodel_name="media.modality",string="Media Modality")

    media_view=fields.Many2one(comodel_name="media.view",string="Media View")

    media_subject=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name'),('device.fhir', 'Device Name'),
                                                      ('location.fhir','Location Name')],
                                                     string="Subject")

    media_encounter=fields.Reference([('encounter', 'Encounter Name')] , string="Encounter")

    media_created=fields.Datetime(string="Media Creation Date", readonly=True,
                                          default=lambda self: fields.datetime.now())

    media_issued=fields.Datetime(string="Issued data")

    media_operator=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name'),('device.fhir', 'Device Name'),
                                                      ('organization','Organization Name')],
                                                     string="Operator")

    media_reason_code=fields.Many2many(comodel_name="media.reason.code",string="Reason")

    media_body_site=fields.Many2one(comodel_name="media.body.site",string="Body Site")

    media_device_Name = fields.Char(string="Device Name")

    media_device_used=fields.Reference([('device.fhir', 'Device Name')],string="Device Used")

    media_height=fields.Integer(string="Height")

    media_width=fields.Integer(string="Width")

    media_frames=fields.Integer(string="Frames")

    media_duration=fields.Float(string="Duration")

    media_annotaion=fields.Reference([('annotation', 'Note')],string="Annotation")




class MediaType(models.Model):
    _name = "media.type"
    _description = "Details about Media Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class MediaModality(models.Model):
    _name = "media.modality"
    _description = "Details about Media Modality"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class MediaView(models.Model):
    _name = "media.view"
    _description = "Details about Media Views"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class MediaReasonCode(models.Model):
    _name = "media.reason.code"
    _description = "Details about Media Views"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class MediaBodySite(models.Model):
    _name = "media.body.site"
    _description = "Details about Body Site"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")








