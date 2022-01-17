from odoo import fields, models, api


class Procedure(models.Model):
    _name = "procedure.fhir"
    _description = "Details about Procedure"
    # _rec_name = "practitioner_name"

    procedure_status = fields.Selection(selection=[
        ("preparation", "Preparation"),
        ("in -progress", "In-progress"),
        ("not -done", "Not-done"),
        ("on - hold", "On-hold"), ("stopped", "Stopped"), ("completed", "Completed"),
        ("entered in error", "Entered in error"),
        ("unknown", "Unknown"),
    ], string="Status")

    procedure_status_Reason = fields.Many2one(comodel_name="procedure.status.reason", string="Status Reason")

    procedure_category = fields.Many2one(comodel_name="procedure.category", string="Category")

    procedure_code = fields.Many2one(comodel_name="procedure.code", string="Code")

    procedure_subject = fields.Reference([('group', 'Group Name'),
                                          ('patient', 'Patient Name')],
                                         string="Subject")

    procedure_encounter = fields.Reference([('encounter', 'Encounter'),
                                            ], string="Encounter")

    procedure_recorder = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                           ('patient', 'Patient Name'),
                                           ('related.person', 'Related Person Name'),
                                           ('practitioner.role.fhir', 'Practitioners Name'),

                                           ],
                                          string="Recorder")

    procedure_asserter = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                           ('patient', 'Patient Name'),
                                           ('related.person', 'Related Person Name'),
                                           ('practitioner.role.fhir', 'Practitioners Name'),

                                           ],
                                          string="Asserter")

    procedure_performer_function = fields.Many2one(comodel_name="procedure.performer.function",
                                                   string="Performer Function")

    procedure_performer_actor = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                  ('patient', 'Patient Name'),
                                                  ('related.person', 'Related Person Name'),
                                                  ('practitioner.role.fhir', 'Practitioners Name'),
                                                  ('device.fhir', 'Device Name'),
                                                  ],
                                                 string="Actor")

    procedure_performer_onBehalfOf=fields.Reference([('organization','Organization Name')], string="On Behalf Of")

    procedure_location=fields.Reference([('location.fhir','Location Name')], string="Location")

    procedure_reasonCode=fields.Many2many(comodel_name="procedure.reason.code",string="Reason Code")

    procedure_reasonReference=fields.Reference([('condition', 'Condition'),
                                                              ('document.reference', 'Document Reference'),
                                                              ], string="Reason Reference")

    procedure_bodySite=fields.Many2many(comodel_name="procedure.body.site",string="Body Site")

    procedure_outcome=fields.Many2one(comodel_name="procedure.outcome",string="outcome")

    procedure_complicationDetail=fields.Reference([('condition', 'Condition'),

                                                              ], string="Complication detail")

    procedure_complication=fields.Many2one(comodel_name="procedure.complication",string="Complication")

    procedure_followUp=fields.Many2many(comodel_name="procedure.follow.up",string="Follow Up")

    procedure_note=fields.Char(string="Additional Note")

    procedure_focalDevice_action=fields.Many2one(comodel_name="procedure.focal.device.action",string="Action")

    procedure_focalDevice_manipulated = fields.Reference([('device.fhir', 'Device Name')], string="Device")

    procedure_usedCode=fields.Many2many(comodel_name="procedure.used.code",string="Used Code")

    reference=fields.Char(string="reference")

    ImagingStudy_procedureReference=fields.Many2one("imaging.study",string="ImagingStudy_procedureReference")



class ProcedureStatusReason(models.Model):
    _name = "procedure.status.reason"
    _rec_name = "display"

    display = fields.Char("Display")

    code = fields.Char("Code")


class ProcedureCategory(models.Model):
    _name = "procedure.category"
    _rec_name = "display"

    display = fields.Char("Display")

    code = fields.Char("Code")


class ProcedureCode(models.Model):
    _name = "procedure.code"
    _rec_name = "display"

    display = fields.Char("Display")

    code = fields.Char("Code")


class ProcedurePerformerFunction(models.Model):
    _name = "procedure.performer.function"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ProcedureReasonCode(models.Model):
    _name = "procedure.reason.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class ProcedureBodySite(models.Model):
    _name = "procedure.body.site"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class ProcedureOutcome(models.Model):
    _name = "procedure.outcome"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ProcedureComplication(models.Model):
    _name = "procedure.complication"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ProcedureFollowUp(models.Model):
    _name = "procedure.follow.up"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ProcedureFocalDeviceAction(models.Model):
    _name = "procedure.focal.device.action"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ProcedureUsedCode(models.Model):
    _name = "procedure.used.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")




