from odoo import models, fields, api


class MedicationRequest(models.Model):
    _name = "medication.request"
    _description = "Details about Medication"

    medication_Request_status = fields.Selection(selection=[
        ("draft", "Draft"),
        ("active", "Active"),
        ("on-hold", "On-hold"),
        ("cancelled", "Cancelled"), ("completed", "Completed"), ("unknown", "Unknown"),
        ("entered in error", "Entered in error"), ("stopped", "Stopped")
    ], string="Status")

    medicationRequest_intent = fields.Selection(selection=[
        ("proposal", "Proposal"),
        ("lan", "Plan"),
        ("order", "Order"),
        ("original Order", "Original Order"), ("reflex Order", "Reflex Order"), ("filler Order", "Filler Order"),
        ("instance Order", "Instance Order"), ("option", "Option")
    ], string="Intent")

    medicationRequest_doNotPerform = fields.Boolean(string="Do no perform?")

    medicationRequest_reported = fields.Boolean(string="Reported")

    medicationRequest_reportedReference = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                            ('patient', 'Patient Name'),
                                                            ('related.person', 'Related Person Name'),
                                                            ('practitioner.role.fhir', 'Practitioners Name'),
                                                            ('organization', 'Organization')
                                                            ],
                                                           string="Reference")

    medicationRequest_subject = fields.Reference([('group', 'Group'),
                                                  ('patient', 'Patient Name')], string="Subject")

    medicationRequest_encounter = fields.Reference([('encounter', 'Encounter')
                                                    ], string="Encounter")

    medicationRequest_authoredOn = fields.Datetime(string="Authored On")

    MedicationRequest_requester = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                    ('patient', 'Patient Name'),
                                                    ('related.person', 'Related Person Name'),
                                                    ('practitioner.role.fhir', 'Practitioners Name'),
                                                    ('device.fhir', 'Device Name'),
                                                    ('organization', 'Organization Name')
                                                    ],
                                                   string="Requester")


    medicationRequest_performer=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                    ('patient', 'Patient Name'),
                                                    ('related.person', 'Related Person Name'),
                                                    ('practitioner.role.fhir', 'Practitioners Name'),
                                                    ('device.fhir', 'Device Name'),
                                                    ('organization', 'Organization Name'),('care.team','care.team')
                                                    ],
                                                   string="Requester")




