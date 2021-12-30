from odoo import models, fields, api


class DocumentReference(models.Model):
    _name = "document.reference"
    _description = "Details about Document Reference"
    # _rec_name = "appointment_status"

    document_Reference = fields.Selection(selection=[
        ("current", "Current"),
        ("superseded", "Superseded"),
        ("entered in error", "Entered in error"),
    ], string="Reference Status")

    document_Reference_docStatus = fields.Selection(selection=[
        ("preliminary", "Preliminary"),
        ("final", "Final"),
        ("amended", "Amended"),
        ("entered in error", "Entered in error"),
    ], string="Document Status")

    document_Reference_type = fields.Many2one(comodel_name="document.reference.type", string="Type")

    document_reference_category = fields.Many2many(comodel_name="document.reference.category", string="Category")

    document_reference_subject = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                   ('patient', 'Patient Name'),
                                                   ('group', 'Group Name'),
                                                   ('device.fhir', 'Device Name')],
                                                  string="Subject")

    document_Reference_date = fields.Datetime(string="Creation Date", readonly=True,
                                              default=lambda self: fields.datetime.now())

    document_Reference_author = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                  ('patient', 'Patient Name'),
                                                  ('group', 'Group Name'),
                                                  ('device.fhir', 'Device Name'),
                                                  ('related.person', 'Related Person Name'),
                                                  ('practitioner.role.fhir', 'Practitioners Name'),
                                                  ('organization', 'organization Name'),
                                                  ],
                                                 string="Author")

    document_Reference_authenticator=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                  ('practitioner.role.fhir', 'Practitioners Name'),
                                                  ('organization', 'organization Name'),
                                                  ],
                                                 string="Authenticator")

    document_Reference_custodian=fields.Reference([('organization', 'organization Name'),
                                                  ],
                                                 string="Custodian")
    document_Reference_relatesTo_code=fields.Selection(selection=[
        ("replaces", "Replaces"),
        ("transforms", "Transforms"),
        ("signs", "Signs"),
        ("appends", "Appends"),
    ], string="Realates To")

    document_Reference_description=fields.Char(string="Description")

    document_reference_security_label=fields.Many2many(comodel_name="document.reference.security.label",string="Security Label")

    document_reference_context_event=fields.Many2many(comodel_name="document.reference.context.event",string="Event")

    document_reference_context_facility_type=fields.Many2one(comodel_name="document.reference.context.facility.type",string="Facility Type")

    document_reference_context_practice_setting=fields.Many2one(comodel_name="document.reference.context.practice.setting",string="Practice Setting")

    document_reference_context_source_patient_info=fields.Reference([('patient', 'Patient Name')],string="Source Patient Info")

    document_reference_context_period_start=fields.Datetime(string="Start Date time")

    document_reference_context_period_end=fields.Datetime(string="End Date time")







class DocumentReferenceType(models.Model):
    _name = "document.reference.type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class DocumentReferenceCategory(models.Model):
    _name = "document.reference.category"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class DocumentReferenceSecurityLabel(models.Model):
    _name = "document.reference.security.label"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class DocumentReferenceContextEvent(models.Model):
    _name = "document.reference.context.event"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class DocumentReferenceContextFacilityType(models.Model):
    _name = "document.reference.context.facility.type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class DocumentReferenceContextPracticeSetting(models.Model):
    _name = "document.reference.context.practice.setting"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")





