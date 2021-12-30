from odoo import models, fields, api


class ImagingStudy(models.Model):
    _name = "imaging.study"
    _description = "Details about Imaging Study"
    # _rec_name = "location_name"

    imagingStudy_status = fields.Selection(selection=[
        ("registered", "Registered"),
        ("available", "Available"),
        ("cancelled", "Cancelled"),
        ("entered in error", "Entered in Error"),
        ("unknown", "Unknown")], string="Status")

    imagingStudy_subject = fields.Reference([('group', 'Group '),
                                             ('patient', 'Patient Name'),
                                             ('device.fhir', 'Device Name'),
                                             ],
                                            string="Subject")

    imagingStudy_encounter = fields.Reference([('encounter', "Encounter")], string="Encounter")

    imagingStudy_started = fields.Datetime(string="Study Start date")

    imagingStudy_basedOn = fields.Reference([('care.plan', 'Care Plan '),
                                             ('patient', 'Service Request'),
                                             ('appointment', 'Appointment'),
                                             ('appointment.response', 'AppointmentResponse'),
                                             ('task', 'Task')],
                                            string="Based on")

    imagingStudy_referrer = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                             ('practitioner.role.fhir', 'Practitioners Name'),
                                              ],
                                             string="Referrer")

    imagingStudy_interpreter=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                             ('practitioner.role.fhir', 'Practitioners Name'),
                                              ],
                                             string="Interpreter")

    imagingStudy_endpoint=fields.Reference([('endpoint', 'Endpoint')
                                              ],
                                             string="Interpreter")

    imagingStudy_numberOfSeries=fields.Integer(string="Number Of Study Related Series")

    imagingStudy_numberOfInstances=fields.Integer(string="Number Of Study Related Instances")

    imagingStudy_procedureReference=fields.Reference([('procedure.fhir', 'Procedure')],
                                             string="Procedure")

    imagingStudy_location=fields.Reference([('location.fhir', 'Location')],
                                             string="Location")

    imagingStudy_reasonReference=fields.Reference([('condition', 'Condition'),
                                             ('observation', 'Observation'),
                                             ('media','Media'),
                                             ('diagnostic.report', 'Diagnostic Report'),
                                             ('document.reference', 'Document Reference')],
                                            string="Reason")

    imagingStudy_note=fields.Reference([('annotation', 'Annotation')], string="Annotation")

    imagingStudy_description=fields.Char(string="Description")

    imagingStudy_series_number=fields.Integer(string="Number")

    imagingStudy_series_description=fields.Char(string="Description")

    imagingStudy_series_numberOfInstances=fields.Integer(string="Number Of Series Related Instances")

    imagingStudy_series_endpoint=fields.Reference([('endpoint', 'Endpoint')
                                              ],
                                             string="Endpoint")

    imagingStudy_series_bodySite=fields.Many2one(comodel_name="imaging.study.series.body.site",string="Body Site")

    imagingStudy_series_specimen=fields.Reference([('specimen','Specimen')],string="Specimen")

    imagingStudy_series_started=fields.Datetime(string="Series Started")


class ImagingStudySeriesBodySite(models.Model):
    _name = "imaging.study.series.body.site"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")



















