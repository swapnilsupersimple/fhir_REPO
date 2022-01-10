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


    imagingStudy = fields.One2many("imaging.study", "diagnosticReport_imaging_study_", string="imagingStudy" )



    presentedForm = fields.One2many("attachment", "attachment_id", string="Attachment")

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













