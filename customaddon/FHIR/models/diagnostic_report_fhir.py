from odoo import models, fields, api


class DiagnosticReport(models.Model):
    _name = "diagnostic.report"
    _description = "Details about Diagnostic Report"

    identifier = fields.Reference(selection=[('identifier', 'Identifier')], string="Dignostic Report Identifier")

    status = fields.Selection(selection=[
        ("registered", "Registered"),
        ("partial", "Partial"),
        ("preliminary", "Preliminary"),
        ("final", "Final"), ("amended", "Amended"), ("cancelled", "Cancelled"),
        ("appended", "Appended"), ("entered in error", "Entered in error"),
        ("corrected", "Corrected"), ("unknown", "Unknown"),
    ], string="Status")

    category = fields.One2many("diagnostic.report.category", "dagnostic_Report_Category_id", string="Category")


    code = fields.One2many("diagnostic.report.code", "diagnostic_Report_code_id",string="Code")


    subject = fields.Reference([('group', 'Group '),
                                ('patient', 'Patient Name'),
                                ('location.fhir', 'Location'),
                                ('device.fhir', 'Device Name'),
                                ],
                               string="Subject")

    encounter = fields.Reference([('encounter', "Encounter")], string="Encounter")

    effectiveDateTime = fields.Datetime(string="Effective")

    issued = fields.Date(string="Issued")

    performer = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                  ('organization', 'Organization'),
                                  ('care.team', 'Care Team'),
                                  ('practitioner.role.fhir', 'Practitioners Name'),
                                  ],
                                 string="Performer")

    resultsInterpreter = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                           ('organization', 'Organization'),
                                           ('care.team', 'Care Team'),
                                           ('practitioner.role.fhir', 'Practitioners Name'),
                                           ],
                                          string="Interpreter")


    specimen = fields.One2many("specimen", "diagnostic_Report_specimen", string="Specimen" )

    result = fields.One2many("observation", "diagnostic_Report_observation", string="Result")





    conclusion = fields.Char(string="Conclusion")

    conclusionCode = fields.One2many("diagnostic.report.conclusion.code", "dagnostic_Report_Conclusion_Code_id",
                                     sting="Conclusion Code")

    start = fields.Date(string="Start")

    end = fields.Date(string="End")


    imagingStudy = fields.One2many("imaging.study.diagnostic", "diagnostic_Report_imaging_study", string="imagingStudy" )



    presentedForm = fields.One2many("attachment.model", "attachment_id", string="Attachment")

    media=fields.One2many("media", "diagnostic_Report_media", string="media" )


class DiagnosticReportCategory(models.Model):
    _name = "diagnostic.report.category"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    dagnostic_Report_Category_id = fields.Many2one("diagnostic.report", string="DiagnosticReportConclusionCode")


class DiagnosticReportCode(models.Model):
    _name = "diagnostic.report.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    diagnostic_Report_code_id = fields.Many2one("diagnostic.report", string="DiagnosticReportCode")



class DiagnosticReportConclusionCode(models.Model):
    _name = "diagnostic.report.conclusion.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    dagnostic_Report_Conclusion_Code_id = fields.Many2one("diagnostic.report", string="DiagnosticReportConclusionCode")


class Attachment(models.Model):
    _name = "attachment.model"
    _rec_name = "title"

    # language = fields.char(comodel_name="res.lang",
    #                           string="Language")

    data = fields.Binary(string="Data")

    url = fields.Char(string="URL")

    size = fields.Integer(string="size")

    title = fields.Char(string="title")

    creation = fields.Datetime(string="Effective")

    attachment_id = fields.Many2one("diagnostic.report", string="Attchment")


# MODEL FOR OBSERVATION

class Observation(models.Model):
    _name = "observation"
    _rec_name = "title"

    title = fields.Char(string="Title")
    diagnostic_Report_observation = fields.Many2one("diagnostic.report", string="DiagnosticReportObservation")

    observation_status = fields.Selection(selection=[
        ("registered", "Registered"),
        ("preliminary", "Preliminary"),
        ("final", "Final"),
        ("amended", "Amended"), ("corrected", "Corrected"), ("cancelled", "Cancelled"),
        ("entered in error", "Entered in error"),
        ("unknown", "Unknown"),
    ], string="Status")

    observation_category = fields.Many2many(comodel_name="observation.category", string="Category")

    observation_code = fields.Many2one(comodel_name="observation.code", string="Code")

    observation_subject = fields.Reference([('location.fhir', 'Location Name'),
                                            ('patient', 'Patient Name'),
                                            ('group', 'Group Name'),
                                            ('device.fhir', 'Device Name'),
                                            ],
                                           string="Appointment Actor")

    observation_encounter = fields.Reference([('encounter', 'Encounter')], string="Encounter")

    observation_issued = fields.Datetime(string="Issued")

    observation_performer = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                              ('patient', 'Patient Name'),
                                              ('related.person', 'Related Person Name'),
                                              ('practitioner.role.fhir', 'Practitioners Name'),
                                              ('organization', 'Organization Name'),
                                              ('care.team', 'Care Team')
                                              ],
                                             string="Performer")

    observation_dataAbsentReason = fields.Many2one(comodel_name="observation.data.absent.reason",
                                                   string="Data Absent Reason")

    observation_interpretation = fields.Many2many(comodel_name="observation.interpretation", string="Abnormal Flag")

    observation_bodySite = fields.Many2one(comodel_name="observation.body.site", string="Body Site")

    observation_method = fields.Many2one(comodel_name="observation.method", string="Method")

    observation_device = fields.Reference([('device.fhir', 'Device Name')], string="Device")

    observation_referenceRange_type = fields.Many2one(comodel_name="observation.reference.range.type",
                                                      string="Reference range Type")

    observation_referenceRange_appliesTo = fields.Many2many(comodel_name="observation.reference.range.appliesto",
                                                            string="Range Applies To")

    observation_referenceRange_text = fields.Char(string="Range Text")

    observation_component_code = fields.Many2one(comodel_name="observation.component.code", string="Code")

    class ObservationCategory(models.Model):
        _name = "observation.category"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        defination = fields.Char("defination")

    class ObservationCode(models.Model):
        _name = "observation.code"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class ObservationDataAbsentReason(models.Model):
        _name = "observation.data.absent.reason"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        defination = fields.Char("Defination")

    class ObservationInterpretation(models.Model):
        _name = "observation.interpretation"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        defination = fields.Char("Defination")

    class ObservationBodySite(models.Model):
        _name = "observation.body.site"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class ObservationMethod(models.Model):
        _name = "observation.method"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class ObservationReferenceRangeType(models.Model):
        _name = "observation.reference.range.type"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        defination = fields.Char("Defination")

    class ObservationReferenceRangeAppliesTo(models.Model):
        _name = "observation.reference.range.appliesto"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")
        defination = fields.Char("Defination")

    class ObservationComponentCode(models.Model):
        _name = "observation.component.code"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")


class Specimen(models.Model):
    _name = "specimen"
    _description = "Details about specimen"

    specimen_status = fields.Selection(selection=[
        ("available", "Available"),
        ("unavailable", "Unavailable"),
        ("unsatisfactory", "Unsatisfactory"),
        ("entered in Error", "Entered in Error"),
    ], string="Status")

    title = fields.Char(string="Title")

    diagnostic_Report_specimen = fields.Many2one("diagnostic.report", string="DiagnosticReportSpecimen")

    specimen_type = fields.Many2one(comodel_name="specimen.type", string="Type")

    specimen_subject = fields.Reference([('group', 'Group '),
                                         ('patient', 'Patient Name'),
                                         ('location.fhir', 'Location'),
                                         ('device.fhir', 'Device Name'),
                                         ],
                                        string="Subject")

    specimen_receivedTime = fields.Datetime(string="Received Time")

    specimen_collection_collector = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('practitioner.role.fhir', 'Practitioner Role'),
                                                     ],
                                                     string="Collector")

    specimen_collection_collected=fields.Datetime(string="Collected Date")

    specimen_collection_quantity=fields.Integer(string="Quantity")

    specimen_collection_method=fields.Many2one(comodel_name="specimen.collection.method",string="Collection Method")

    specimen_collection_bodySite=fields.Many2one(comodel_name="specimen.collection.body.site",string="Body Site")

    specimen_collection_fastingStatus=fields.Many2one(comodel_name="specimen.collection.fasting.status",string="Fasting Status")

    specimen_processing_description=fields.Char(string="Processing")

    specimen_processing_procedure=fields.Many2one(comodel_name="specimen.processing.procedure",string="Procedure")

    specimen_processing_time=fields.Datetime(string="Processing Time")

    specimen_container_description=fields.Char(string="Description")

    specimen_container_type=fields.Many2one(comodel_name="specimen.container.type",string="Type")

    specimen_container_capacity=fields.Integer(string="Container Capacity")

    specimen_container_specimenQuantity=fields.Integer(string="Specimen Quantity")

    specimen_container_additive=fields.Many2one(comodel_name="specimen.container.additive",string="Additive")

    specimen_condition=fields.Many2many(comodel_name="specimen.condition",string="Condition")


    class SpecimenType(models.Model):
        _name = "specimen.type"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class SpecimenCollectionMethod(models.Model):
        _name = "specimen.collection.method"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class SpecimenCollectionBodySite(models.Model):
        _name = "specimen.collection.body.site"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class SpecimenCollectionFastingStatus(models.Model):
        _name = "specimen.collection.fasting.status"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")


    class SpecimenProcessingProcedure(models.Model):
        _name = "specimen.processing.procedure"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class SpecimenContainerType(models.Model):
        _name = "specimen.container.type"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class SpecimenContainerAdditive(models.Model):
        _name = "specimen.container.additive"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")

    class SpecimenCondition(models.Model):
        _name = "specimen.condition"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")




class ImagingStudy(models.Model):
    _name = "imaging.study.diagnostic"
    _description = "Details about Imaging Study"
    # _rec_name = "location_name"

    imagingStudy_status = fields.Selection(selection=[
        ("registered", "Registered"),
        ("available", "Available"),
        ("cancelled", "Cancelled"),
        ("entered in error", "Entered in Error"),
        ("unknown", "Unknown")], string="Status")

    diagnostic_Report_imaging_study = fields.Many2one("diagnostic.report", string="DiagnosticReportImagingStudy")

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

    imagingStudy_interpreter = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                 ('practitioner.role.fhir', 'Practitioners Name'),
                                                 ],
                                                string="Interpreter")

    imagingStudy_endpoint = fields.Reference([('endpoint', 'Endpoint')
                                              ],
                                             string="Interpreter")

    imagingStudy_numberOfSeries = fields.Integer(string="Number Of Study Related Series")

    imagingStudy_numberOfInstances = fields.Integer(string="Number Of Study Related Instances")

    imagingStudy_procedureReference = fields.Reference([('procedure.fhir', 'Procedure')],
                                                       string="Procedure")

    imagingStudy_location = fields.Reference([('location.fhir', 'Location')],
                                             string="Location")

    imagingStudy_reasonReference = fields.Reference([('condition', 'Condition'),
                                                     ('observation', 'Observation'),
                                                     ('media', 'Media'),
                                                     ('diagnostic.report', 'Diagnostic Report'),
                                                     ('document.reference', 'Document Reference')],
                                                    string="Reason")

    imagingStudy_note = fields.Reference([('annotation', 'Annotation')], string="Annotation")

    imagingStudy_description = fields.Char(string="Description")

    imagingStudy_series_number = fields.Integer(string="Number")

    imagingStudy_series_description = fields.Char(string="Description")

    imagingStudy_series_numberOfInstances = fields.Integer(string="Number Of Series Related Instances")

    imagingStudy_series_endpoint = fields.Reference([('endpoint', 'Endpoint')
                                                     ],
                                                    string="Endpoint")

    imagingStudy_series_bodySite = fields.Many2one(comodel_name="imaging.study.series.body.site", string="Body Site")

    imagingStudy_series_specimen = fields.Reference([('specimen', 'Specimen')], string="Specimen")

    imagingStudy_series_started = fields.Datetime(string="Series Started")


    class ImagingStudySeriesBodySite(models.Model):
        _name = "imaging.study.series.body.site"
        _rec_name = "display"

        display = fields.Char("Display")
        code = fields.Char("Code")



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

    diagnostic_Report_media = fields.Many2one("diagnostic.report", string="DiagnosticReportMedia")

    media_comment = fields.Char(string="Comment")



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








