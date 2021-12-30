from odoo import models, fields, api


class Condition(models.Model):
    _name = "condition"
    _description = "details about condition"

    condition_clinical_Status=fields.Selection(selection=[
        ("active", "Active"),
        ("recurrence", "Recurrence"),
        ("relapse", "Relapse"),
        ("inactive", "Inactive"),("remission", "Remission"),("resolved","Resolved")] ,string="Clinical Status")

    condition_verificationStatus=fields.Selection(selection=[
        ("unconfirmed", "Unconfirmed"),
        ("provisional", "Provisional"),
        ("differential", "Differential"),
        ("confirmed", "Confirmed"),("refuted", "Refuted"),("entered-in-error","entered-in-error")] ,string="Clinical Verification Status")


    condition_category=fields.Selection(selection=[('problem-list-item','Problem-list-item'),
                                                             ('encounter-diagnosis','encounter-diagnosis')],string="Condition Category")

    condition_severity=fields.Selection(selection=[('severe','Severe'),
                                                             ('moderate','Moderate'),('mild','Mild')],string="Condition Severity")

    condition_subject=fields.Reference([('patient', "Patient's Name"),('group','group_name')], string="Name of Patient/Group")

    code_condition=fields.Many2one(comodel_name="condition.code",string="Condition Code")

    condition_recordedDate=fields.Datetime(string="Recorded Date")

    condition_recorder=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                       ('patient', 'Patient Name'),
                                       ('related.person', 'Related Person Name') ],

                                       string="Condition Reocorder")

    condition_asserter=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                       ('patient', 'Patient Name'),
                                       ('related.person', 'Related Person Name') ],

                                       string="Condition Asserter")

    condition_note=fields.Reference([('annotation','Text')],string="Note")


class ConditionCode(models.Model):
    _name = "condition.code"

    code = fields.Char(string="Code")

    display=fields.Char(string="Display")














