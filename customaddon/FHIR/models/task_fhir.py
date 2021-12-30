from odoo import models, fields, api


class Task(models.Model):
    _name = "task"
    _description = "Details about Task"
    # _rec_name = "appointment_status"

    task_status=fields.Selection(selection=[
        ("draft", "Draft"),
        ("requested", "Requested"),
        ("received", "Received"),
        ("accepted", "Accepted"), ("rejected", "Rejected"), ("ready", "Ready"),
        ("cancelled", "Cancelled"), ("entered in error", "Entered in error"), ("in Progress", "In Progress"),
        ("on Hold", "On Hold"),("failed", "Failed"),("completed", "Completed"),
    ], string="Task Status")

    task_intent=fields.Selection(selection=[
        ("unknown", "Unknown"),
        ("proposal", "Proposal"),
        ("plan", "Plan"),
        ("order", "Order"), ("original - order", "Original - order"), ("reflex - order", "Reflex - order"),
        ("filler - order", "filler - Order"),
        ("instance - order", "Instance - order"),("option", "Option"),
    ], string="Task Intent")

    task_priority=fields.Selection(selection=[
        ("routine", "Unknown"),
        ("urgent", "Proposal"),
        ("asap", "Plan"),
        ("stat", "Order")
    ], string="Task Priority")

    task_code=fields.Many2one(comodel_name="task.code",string="Task Code")

    task_description=fields.Char(string="Description")

    task_authoredOn=fields.Datetime(string="Created Date", readonly=True,
                                          default=lambda self: fields.datetime.now())

    Task_lastModified=fields.Datetime(string="Updated Date")

    task_performer_type=fields.Many2one(comodel_name="task.performer.type", string="Performer type")

    task_execution_start=fields.Datetime(string="Execution Start time")

    task_execution_end= fields.Datetime(string="Execution End time")

    task_requester=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name'),
                                                      ('organization','Organization Name')
                                                      ],
                                                     string="Task Requester")

    task_owner=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name'),
                                                      ('organization','Organization Name')
                                                      ],
                                                     string="Task Requester")
    task_location = fields.Reference([('location.fhir', 'Location Name')], string = "Location")

    task_restriction_repetitions=fields.Integer(string="Task repetitions")

    task_restriction_start_time=fields.Datetime(string="Start time")

    task_restriction_end_time = fields.Datetime(string="End time")

    task_restriction_recipient=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('group','Group Name'),
                                                      ('organization','Organization Name')
                                                      ],
                                                     string="Task Recipient")


class TaskCode(models.Model):
    _name = "task.code"
    _description = "Details about Task Code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    definition=fields.Char("Definition")

class TaskPerformerType(models.Model):
    _name = "task.performer.type"
    _description = "Details about Task Performer Type"
    _rec_name = "display"

    display = fields.Char("Display")













