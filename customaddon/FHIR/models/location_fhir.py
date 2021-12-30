from odoo import models, fields, api

from datetime import datetime



class Location(models.Model):
    _name="location.fhir"
    _description = "Details about location"
    _rec_name = "location_name"

    location_status=fields.Selection(selection=[
        ("active", "Active"),
        ("suspended", "Suspended"),
        ("inactive", "Inactive")],string="Location Status")

    location_name=fields.Char(string="Name of Location")

    location_alias=fields.Char(string="Location Alias")

    location_description=fields.Char(string="Location description")

    location_mode=fields.Selection(selection=[
        ("instance", "Instance"),
        ("kind","Kind")] , string="Location Status")

    location_hoursOfOperation_daysOfWeek=fields.Many2many(comodel_name="day.week",string="Days")

    Location_hoursOfOperation_allDay=fields.Boolean(string="Open All Day?")

    location_hoursOfOperation_openingTime=fields.Float(string="Opening time")

    location_hoursOfOperation_closingTime=fields.Float(string="Closing Time")

    location_position_longitude=fields.Float(string="Longitude")

    location_position_latitude=fields.Float(string="Latitude")

    location_position_altitude=fields.Float(string="Altitude")

    location_availabilityExceptions=fields.Char(string="UnAvailability Reason")

    location_telecom=fields.Many2many(comodel_name="location.telecom",string="Contact")

    location_address = fields.Reference([('address.fhir', 'Address')], string="Address")


class DayOfWeek(models.Model):
    _name = "day.week"
    _description = "days of week"
    _rec_name = "day_of_week"

    day_of_week = fields.Selection([
        ("mon","Monday"),
        ("tue","Tuesday"),
        ("wed","Wednesday"),
        ("thu","Thursday",),
        ("fri","Friday",),
        ("sat","Saturday",), ("sun","Sunday",)],
        string="Week")

class LocationTelecom(models.Model):
    _name = "location.telecom"

    location_Contact_point=fields.Reference([('contact.point', 'Phone')], string="Telecom")










