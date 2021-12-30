from odoo import models, fields, api


class EpisodeOfCare(models.Model):
    _name = "episode.of.care"
    _description = "Details about Episode Of Care"
    # _rec_name = "appointment_status"

    episode_Of_Care_status=fields.Selection(selection=[
        ("planned", "Planned"),
        ("waitlist", "Waitlist"),
        ("active", "Active"),
        ("onhold", "Onhold"), ("finished", "Finished"), ("cancelled", "Cancelled"),

    ], string="Status")

    episode_Of_Care_statusHistory_status=fields.Selection(selection=[
        ("planned", "Planned"),
        ("waitlist", "Waitlist"),
        ("active", "Active"),
        ("onhold", "Onhold"), ("finished", "Finished"), ("cancelled", "Cancelled"),
    ], string="Status")

    EpisodeOfCare_statusHistory_period_start=fields.Datetime(string="Start Date time")

    EpisodeOfCare_statusHistory_period_end=fields.Datetime(string="End Date time")

    episode_Of_Care_type=fields.Many2many(comodel_name="episode.of.care.type",string="Care Type")

    episodeOfCare_diagnosis_role=fields.Many2one(comodel_name="episode.of.care.diagnosis.role",string="Diagnosis Role")

    episodeOfCare_diagnosis_rank=fields.Integer(string="Diagnosis Rank")

    episodeOfCare_diagnosis_condition = fields.Reference([('condition', 'Condition')],string="Condition")

    episodeOfCare_patient=fields.Reference([('patient', 'Patient Name')],string="Patient")

    episodeOfCare_managingOrganization=fields.Reference([('organization', 'Organization Name')],
                                                 string="Organization")

    episodeOfCare_careManager=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name')],
                                                     string="Care Manager")

    episodeOfCare_team=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ],
                                                     string="Care Team")

    episodeOfCare_period_start=fields.Datetime(string="Start Date time")

    episodeOfCare_period_end=fields.Datetime(string="End Date time")


class EpisodeOfCareType(models.Model):
    _name = "episode.of.care.type"
    _description = "details about Episode Of Care Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class EpisodeOfCareDiagnosisRole(models.Model):
    _name = "episode.of.care.diagnosis.role"
    _description = "details about Episode Of Care Diagnosis Role"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")




