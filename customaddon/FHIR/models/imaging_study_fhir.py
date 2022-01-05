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

    series=fields.One2many("imaging.study.series","ImagingStudy_Series",string="Series")

    reasonCode=fields.One2many("imaging.study.reasoncode","ImagingStudy_ReasonCode",string="reasonCode")

    modality=fields.One2many("imaging.study.modality","ImagingStudy_modality",string="modality")



    class Annotation(models.Model):
            _name="imaging.study.annotation"
            _rec_name = "text"
            _description = "Details about Annotation"

            time=fields.Datetime(string="Time")

            text=fields.Text(string="Text")

            ImagingStudy_annotation = fields.Many2one("imaging.study", string="ImagingStudy_annotation")

    class ReasonCode(models.Model):
        _name = "imaging.study.reasoncode"
        _rec_name = "display"


        system = fields.Char(string="system")

        code = fields.Text(string="code")

        display = fields.Char("Display")

        ImagingStudy_ReasonCode= fields.Many2one("imaging.study", string="ImagingStudy_ReasonCode")

    class Modality(models.Model):
        _name = "imaging.study.modality"
        _rec_name = "code"

        system = fields.Char(string="system")

        code = fields.Text(string="code")



        ImagingStudy_modality = fields.Many2one("imaging.study", string="ImagingStudy_modality")









class Series(models.Model):
    _name = "imaging.study.series"

    ImagingStudy_Series = fields.Many2one("imaging.study", string="ImagingStudy_series")


    uid = fields.Integer(string="SeriesInstanceUID")

    number = fields.Integer(string="SeriesNumber")

    description = fields.Char(string="SeriesDescription")

    numberOfInstances = fields.Integer(string="NumberOfSeriesRelatedInstances")

    endpoint = fields.Reference([('endpoint', 'Endpoint')
                                                     ],
                                                    string="Endpoint")

    bodySite = fields.One2many("imaging.study.series.body.site", "ImagingStudy_BodySite",
                                       string="BodyPartExamined")

    specimen = fields.Reference([('specimen', 'Specimen')], string="Specimen")

    started = fields.Datetime(string="Series Started")

    instance=fields.One2many("sop.instance.series","ImagingStudy_SOP_instance_series",string="Instance")

    laterality=fields.One2many("imaging.study.series.laterality","ImagingStudy_laterality",string="Laterality")

    modality=fields.One2many("imaging.study.series.modality","ImagingStudy_series_modality",string="modality")


    class Modality(models.Model):
        _name = "imaging.study.series.modality"
        _rec_name = "code"

        system = fields.Char(string="system")

        code = fields.Text(string="code")

        ImagingStudy_series_modality = fields.Many2one("imaging.study.series", string="ImagingStudy_modality")




    class Instance(models.Model):
        _name = "sop.instance.series"

        ImagingStudy_SOP_instance_series = fields.Many2one("imaging.study.series", string="ImagingStudy_SOP_instance_series")

        SOPInstanceUID = fields.Integer(string="SeriesInstanceUID")

        InstanceNumber = fields.Integer(string="InstanceNumber")

        instanceTitle = fields.Char(string="instanceTitle")

        SOPClassUID=fields.One2many("sop.instance.series.sop.class.uid","ImagingStudy_sopClassUID",string="SOPClassUID")

        class sopClassUID(models.Model):
            _name = "sop.instance.series.sop.class.uid"

            ImagingStudy_sopClassUID = fields.Many2one("sop.instance.series", string="ImagingStudy_sopClassUID", invisible=1)

            system = fields.Char("system")
            code = fields.Char("Code")


    class ImagingStudySeriesBodySite(models.Model):
        _name = "imaging.study.series.body.site"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        ImagingStudy_BodySite = fields.Many2one("imaging.study.series", string="ImagingStudy_BodySite", invisible=1)

    class Laterality(models.Model):
        _name = "imaging.study.series.laterality"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        ImagingStudy_laterality = fields.Many2one("imaging.study.series", string="ImagingStudy_laterality")






















