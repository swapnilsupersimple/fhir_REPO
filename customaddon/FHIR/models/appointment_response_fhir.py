from odoo import models, fields, api


class AppointmentResponse(models.Model):
    _name = "appointment.response"
    _description = "Details about Appointment Response"
    # _rec_name = "appointment_status"

    appointmentResponse_start= fields.Datetime(string="Start Date time")

    appointmentResponse_end= fields.Datetime(string="End Date time")

    appointmentResponse_participantStatus=fields.Selection(selection=[
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("tentative", "Tentative"),
        ("needs-action", "Needs-action"),
    ], string="Participant Status")

    appointmentResponse_comment=fields.Char(string="Additional Comment")

    appointment_participant_actor = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('patient', 'Patient Name'),
                                                      ('related.person', 'Related Person Name'),
                                                      ('practitioner.role.fhir', 'Practitioners Name'),
                                                      ('device.fhir', 'Device Name')],
                                                     string="Appointment Actor")

    Appointment_Participant = fields.Many2many(comodel_name="appointment.participant.type",
                                               string="Participant Type")




class AppointmentParticipantType(models.Model):
    _name = "appointment.participant.type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class DocumentReferenceContextEvent(models.Model):
    _name = "document.reference.context.event"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")



    