from odoo import models, fields, api


class Appointment(models.Model):
    _name = "appointment"
    _description = "Details about Appointment"
    _rec_name = "appointment_status"

    appointment_status = fields.Selection(selection=[
        ("proposed", "Proposed"),
        ("pending", "Pending"),
        ("booked", "Booked"),
        ("arrived", "Arrived"), ("fulfilled", "Fulfilled"), ("cancelled", "Cancelled"),
        ("no show", "No Show"), ("entered in error", "Entered in error"), ("Checked In", "Checked In"),
        ("waitlist", "Waitlisted"),
    ], string="Appointment Status")

    appointment_priority = fields.Integer(string="Appointment Priority")

    appointment_description = fields.Char(string="Appointment Description")

    appointment_display_text = fields.Char(string="Text")

    appointment_start = fields.Datetime(string="Appointment Start")

    appointment_end = fields.Datetime(string="Appointment End")

    appointment_minutesDuration = fields.Integer(string="Appointment Duration")

    appointment_created = fields.Datetime(string="Appointment Creation Date", readonly=True,
                                          default=lambda self: fields.datetime.now())

    appointment_comment = fields.Text(string="Additional Comment")

    appointment_patientInstruction = fields.Char(string="Instruction to Patient")

    appointment_requestedPeriod_start = fields.Datetime(string="Start Date time")

    appointment_requestedPeriod_end = fields.Datetime(string="End Date time")

    appointment_cancelationReason = fields.Many2one(comodel_name="appointment.cancelation.reason",
                                                    string="Appointment Cancelation Reason")

    # Appointment_ServiceCategory=fields.Many2many(comodel_name="appointment.service.category",string="Appointment Service Category")
    Appointment_Participant = fields.Many2many(comodel_name="appointment.participant.type",
                                               string="Participant Type")

    appointment_participant_actor = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name'),
                                                      ],
                                                     string="Appointment Actor")

    appointment_participant_required=fields.Selection(selection=[
        ("required", "Required"),
        ("optional", "Optional"),
        ("information-only", "Information-only"),
    ], string="Participant required")

    appointment_participant_status=fields.Selection(selection=[
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("tentative", "Tentative"),
        ("needs-action", "Needs-action"),
    ], string="Participant Status")

    participant_Period_start = fields.Datetime(string="Start Date time")

    participant_Period_end = fields.Datetime(string="End Date time")


class AppointmentCancelationReason(models.Model):
    _name = "appointment.cancelation.reason"
    _rec_name = "display"

    display = fields.Char("Display")

    code = fields.Char("Code")


class AppointmentParticipantType(models.Model):
    _name = "appointment.participant.type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
