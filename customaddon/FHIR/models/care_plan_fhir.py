from odoo import models, fields, api
from datetime import datetime


class CarePlan(models.Model):
    _name = "care.plan"
    _description = "Details About care plan"
    _rec_name = "carePlan_title"

    carePlan_status=fields.Selection(selection=[
        ("draft", "Draft"),
        ("active", "Active"),
        ("on-hold", "On-hold"),
        ("revoked", "Revoked"), ("completed", "Completed"), ("unknown", "Unknown"),
        ("entered in error", "Entered in error"),
    ], string="Status")

    carePlan_intent=fields.Selection(selection=[
        ("proposal", "Proposal"),
        ("plan", "Plan"),
        ("order", "Order"), ("option", "Option"),
    ], string="Intent")

    carePlan_title=fields.Char(string="Care plan name")

    carePlan_description=fields.Char(string="Description")


    carePlan_subject=fields.Reference([('patient', "Patient's Name"),
                                       ('group_name',"Group Name")], string="Subject")

    carePlan_period_start=fields.Datetime(string="Start Date time")

    carePlan_period_end=fields.Datetime(string="End Date time")

    carePlan_created=fields.Datetime(string="Creation Date", readonly=True,
                                     default=lambda self: fields.datetime.now())

    carePlan_author=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name'),('organization_name','Organization Name')],
                                                     string="Care Plan Author")

    carePlan_contributor=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Role'),
                                                      ('device.fhir', 'Device Name'),('organization_name','Organization Name')],
                                                     string="Care Plan Contributor")
    






















