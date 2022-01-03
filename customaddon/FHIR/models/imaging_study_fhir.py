from odoo import models, fields, api


class ImagingStudy(models.Model):
    _name = "imaging.study"
    _description = "Details about Imaging Study"
    # _rec_name = "location_name"

    status = fields.Selection(selection=[
        ("registered", "Registered"),
        ("available", "Available"),
        ("cancelled", "Cancelled"),
        ("entered in error", "Entered in Error"),
        ("unknown", "Unknown")], string="Status")

    subject = fields.Reference([('group', 'Group '),
                                             ('patient', 'Patient Name'),
                                             ('device.fhir', 'Device Name'),
                                             ],
                                            string="Subject")

    encounter = fields.Reference([('encounter', "Encounter")], string="Encounter")

    started = fields.Datetime(string="Study Start date")

    basedOn = fields.Reference([('care.plan', 'Care Plan '),
                                             ('patient', 'Service Request'),
                                             ('appointment', 'Appointment'),
                                             ('appointment.response', 'AppointmentResponse'),
                                             ('task', 'Task')],
                                            string="Based on")

    referrer = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                             ('practitioner.role.fhir', 'Practitioners Name'),
                                              ],
                                             string="Referrer")

    interpreter=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                             ('practitioner.role.fhir', 'Practitioners Name'),
                                              ],
                                             string="Interpreter")

    endpoint=fields.Reference([('endpoint', 'Endpoint')
                                              ],
                                             string="Interpreter")

    numberOfSeries=fields.Integer(string="numberOfSeries")

    numberOfInstances=fields.Integer(string="numberOfInstances")

    procedureReference=fields.Reference([('procedure.fhir', 'Procedure')],
                                             string="Procedure")

    location=fields.Reference([('location.fhir', 'Location')],
                                             string="Location")

    reasonReference=fields.Reference([('condition', 'Condition'),
                                             ('observation', 'Observation'),
                                             ('media','Media'),
                                             ('diagnostic.report', 'Diagnostic Report'),
                                             ('document.reference', 'Document Reference')],
                                            string="Reason")


    note = fields.One2many("imaging.study.annotation","ImagingStudy_annotation",string="note")

    description=fields.Char(string="Description")

    SeriesInstanceUID=fields.Integer(string="SeriesInstanceUID")

    SeriesNumber=fields.Integer(string="SeriesNumber")

    SeriesDescription=fields.Char(string="SeriesDescription")

    NumberOfSeriesRelatedInstances=fields.Integer(string="NumberOfSeriesRelatedInstances")

    imagingStudy_series_endpoint=fields.Reference([('endpoint', 'Endpoint')
                                              ],
                                             string="Endpoint")

    BodyPartExamined=fields.One2many("imaging.study.series.body.site","ImagingStudy_BodySite",string="BodyPartExamined")

    seriesSpecimen=fields.Reference([('specimen','Specimen')],string="Specimen")

    seriesStarted=fields.Datetime(string="Series Started")

    SOPInstanceUID=fields.Integer(string="SeriesInstanceUID")

    InstanceNumber=fields.Integer(string="InstanceNumber")

    instanceTitle=fields.Char(string="instanceTitle")


    class Annotation(models.Model):
            _name="imaging.study.annotation"
            _rec_name = "text"
            _description = "Details about Annotation"

            time=fields.Datetime(string="Time")

            text=fields.Text(string="Text")

            ImagingStudy_annotation = fields.Many2one("imaging.study", string="ImagingStudy_annotation")




class ImagingStudySeriesBodySite(models.Model):
    _name = "imaging.study.series.body.site"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    ImagingStudy_BodySite = fields.Many2one("imaging.study", string="ImagingStudy_BodySite")



















