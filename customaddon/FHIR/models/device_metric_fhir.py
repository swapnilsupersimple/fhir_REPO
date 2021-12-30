from odoo import models, fields, api


class DeviceMetric(models.Model):
    _name = "device.metric"
    _description = "Details about Device Metric"

    deviceMetric_source = fields.Reference([('device.fhir', 'Device')], string="Source")

    deviceMetric_parent = fields.Reference([('device.fhir', 'Device')], string="Source")

    deviceMetric_operationalStatus = fields.Selection(selection=[
        ("on", "On"),
        ("off", "Off"),
        ("booked", "Standby"),

        ("entered in error", "Entered in error"),

    ], string="Operational Status")

    deviceMetric_color=fields.Selection(selection=[
        ("black", "black"),
        ("red", "red"),
        ("green", "green"),
        ("yellow", "yellow"), ("blue", "blue"), ("magenta", "magenta"),
        ("cyan", "cyan"),
        ("white", "white"),
    ], string="Color")

    deviceMetric_category=fields.Selection(selection=[
        ("measurement", "Measurement"),
        ("setting", "Setting"),
        ("calculation", "Calculation"),
        ("unspecified", "Unspecified"),
    ], string="category")

    deviceMetric_measurementPeriod=fields.Datetime(string="Measurement Period")

    deviceMetric_calibration_type=fields.Selection(selection=[
        ("Unspecified", "unspecified"),
        ("Offset", "offset"),
        ("Gain", "gain"),
        ("Two-point", "two-point")
    ], string="Calibration Type")

    deviceMetric_calibration_state=fields.Selection(selection=[
        ("not -calibrated", "not -calibrated |"),
        ("calibration - required", "calibration - required"),
        ("calibrated", "calibrated"),
        ("unspecified", "unspecified")
    ], string="Calibration State")

    deviceMetric_calibration_time=fields.Datetime(string="Calibration Time")













