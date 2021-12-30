from odoo import models, fields, api


class Observation(models.Model):
    _name = "observation"
    _description = "Details about organization"
    # _rec_name = "organization_name"

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

    observation_dataAbsentReason=fields.Many2one(comodel_name="observation.data.absent.reason",string="Data Absent Reason")

    observation_interpretation=fields.Many2many(comodel_name="observation.interpretation",string="Abnormal Flag")

    observation_bodySite=fields.Many2one(comodel_name="observation.body.site",string="Body Site")

    observation_method=fields.Many2one(comodel_name="observation.method",string="Method")

    observation_device=fields.Reference([('device.fhir', 'Device Name')],string="Device")

    observation_referenceRange_type=fields.Many2one(comodel_name="observation.reference.range.type",string="Reference range Type")

    observation_referenceRange_appliesTo=fields.Many2many(comodel_name="observation.reference.range.appliesto",string="Range Applies To")

    observation_referenceRange_text=fields.Char(string="Range Text")

    observation_component_code=fields.Many2one(comodel_name="observation.component.code",string="Code")








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




