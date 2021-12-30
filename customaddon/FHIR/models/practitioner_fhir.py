from odoo import fields,models,api

class Practitioner(models.Model):
    _name = "practitioner.fhir"
    _description = "Details about Practitioner"
    _rec_name = "practitioner_name"

    practitioner_name = fields.Reference([('human.name', 'Full Name')], string="Practitioner's Name")

    is_practitioner_active=fields.Boolean(string="Practitioner Active?")

    practitioner_gender = fields.Selection(selection=[
        ("male", "Male"),
        ("Female", "Female"),
        ("other", "Other"),
        ("unknown", "Unknown")],string="Gender")

    practitioner_birthDate = fields.Date(string="Birth Date")

    practitioner_contact = fields.Reference([('contact.point', 'Phone')], string="Contact")

    practitioner_address = fields.Reference([('address.fhir', 'Address')], string="Address")



