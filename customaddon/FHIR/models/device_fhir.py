from odoo import models, fields, api


class Device(models.Model):
    _name = "device.fhir"
    _description = "Details about Device"

    device_status = fields.Selection(selection=[
        ("active", "Active"),
        ("entered-in-error", "Entered-in-error"),
        ("inactive", "Inactive"), ("unknown", "Unknown")
    ], string="Device Status")

    device_status_Reason = fields.Selection(selection=[
        ("online", "Online"), ("paused", "Paused"), ("standby", "Standby"), ("offline", "Offline"),
        ("not-ready ", "Not-ready "),("transduc-disco","Transducer Disconnected	"),("hw-discon","Hardware Disconnected"),
        ("off","Off")], string="Device Status Reason")

    device_distinct_Identifier=fields.Char(string="Distinct Identifier")

    device_manufacturer = fields.Char(string="Manufacturer")

    device_manufacture_Date=fields.Datetime(string="Manufacture Date")

    device_expiration_Date = fields.Datetime(string="Expiration Date")

    device_lot_Number=fields.Char(string="Device lot number")

    device_serial_Number=fields.Char(string="Device Serial number")


    device_modelNumber=fields.Char(string="Model Number")

    device_partNumber=fields.Char(string="Part Number")

    device_patient=fields.Reference([('patient', "Patient's Name")], string="Patient's Name",
                                    help="Patient to whom Device is affixed")

    device_owner=fields.Reference([('organization', 'Organization Name')], string="Organization's Name" , help="Organization responsible for device")

    device_contact=fields.Reference([('contact.point', 'Phone')], string="Contact Telecom",
                                    help="Details for human/organization for support")

    device_deviceName=fields.Many2many(comodel_name="device.name",help="The name of the device as given by the manufacturer",string="Device Name")


class DeviceName(models.Model):
    _name="device.name"
    _rec_name = "device_deviceName_name"

    device_deviceName_name = fields.Char(string="Name of the device",help="The name of the device")

    device_deviceName_type = fields.Selection(selection=[
        ("udi-label-name", "UDI Label name"), ("user-friendly-name", "User Friendly name"),
        ("patient-reported-name", "Patient Reported name"), ("manufacturer-name", "Manufacturer name"),
        ("model-name", "Model name"), ("other", "other")], string="Device type",help="The type of deviceName")






    






















