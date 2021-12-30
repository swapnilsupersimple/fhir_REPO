from odoo import fields,models,api

class PractitionerRole(models.Model):
    _name = "practitioner.role.fhir"
    _description = "Details about Practitioner role"

    is_practitioner_role_active=fields.Boolean(string="Record Active?")

    practitioner_role_practitioner=fields.Reference([('practitioner.fhir', 'Practitioner Name')], string="Practitioner's Name")

    practitioner_role_organization=fields.Reference([('organization', 'Organization Name')], string="Organization's Name")

    practitioner_role_telecom=fields.Reference([('contact.point', 'Phone')], string="Contact")

    practitioner_days_Of_week=fields.Many2many(comodel_name="days.week",string="Days Of Week")

    practitioner_availableTime_allDay=fields.Boolean(string="Available 24 Hours?")

    practitioner_availableTime_availableStartTime=fields.Datetime(string="Start Time ")

    practitioner_role_availableTime_availableEndTime=fields.Datetime(string="End Time ")

    practitioner_role_not_available_description=fields.Char(string="UnAvailability Reason")

    practitioner_role_notAvailable_during_start=fields.Datetime(string=" Start Time")

    practitioner_role_notAvailable_during_end=fields.Datetime(string="End Time")

    practitioner_role_availability_Exceptions=fields.Char(string="Unavailability exception reason")




class DaysOfWeek(models.Model):
    _name = "days.week"
    _description = "days of week"
    _rec_name = "days_of_week"

    days_of_week = fields.Selection([
        ("mon","Monday"),
        ("tue","Tuesday"),
        ("wed","Wednesday"),
        ("thu","Thursday",),
        ("fri","Friday",),
        ("sat","Saturday",), ("sun","Sunday",)],
        string="Week")























