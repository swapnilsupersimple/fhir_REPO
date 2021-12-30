from urllib import request


from odoo import models, fields, api
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT

from datetime import datetime, timedelta, date
from odoo import http
from odoo.http import request


class Patient(models.Model):
    _name = "patient"
    _description = "Details of patient"
    _rec_name = 'patient_name'

    patient_identifier=fields.Reference(selection=[('identifier', 'Identifier')], string="Patient Identifier")


    patient_name = fields.Reference(selection=[('human.name', 'Full Name')], string="Patient's Name")

    patient_gender = fields.Selection(selection=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
        ("unknown", "Unknown")])

    patient_birthDate = fields.Date(string="Birth Date")

    patient_is_partOf_multiple_birth = fields.Boolean(
        string="Multiple Birth",
        help="Whether patient is part of a multiple birth.")

    # patient_multiple_birth_count = fields.Integer(
    #     string="Multiple Birth Count",
    #     help="Number of births in a multiple birth.")

    patient_multiple_birth_order = fields.Integer(
        string="Multiple Birth Order",
        help="The actual birth order in a multiple birth.")

    is_deceased = fields.Boolean(string="Deceased ?")

    deceased_date = fields.Date(string="Deceased Date")

    marital_status_patient = fields.Selection(selection=[
        ("single", "Single"),
        ("married", "Married"),
        ("widowed", "Widowed"),
        ("divorced", "Divorced"),
        ("separated", "Separated")], string="Martial Status")

    patient_contact = fields.Reference([('contact.point', 'Phone')], string="Contact")

    patient_communication = fields.Many2one(comodel_name="res.lang",
                                            string="Language")

    patient_address = fields.Reference([('address.fhir', 'Address')], string="Address")

    patient_contact_name = fields.Reference([('human.name', 'Full Name')], string="Contact Name")

    patient_contact_gender = fields.Selection(selection=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
        ("unknown", "Unknown")], string="Gender")

    patient_contact_telecom = fields.Reference([('contact.point', 'Phone')], string="Contact Telecom ")

    patient_contact_address = fields.Reference([('address.fhir', 'Address')], string="Contact Address")

    patient_photo = fields.Binary(string="Photo")

    patient_active = fields.Boolean(striing="Is record active ?")

    patient_contact_organization = fields.Reference([('organization', 'Organization')],
                                                    string="Patient Contact Organization")

    patient_contact_period_start = fields.Date(string="Patient contact period start" ,help="The period during which this contact person or organization is valid to be contacted relating to this patient.")


    patient_contact_period_end = fields.Date(string="Patient contact period end",
                                             help="The period during which this contact person or organization is valid to be contacted relating to this patient.")




    def button_click(self):
        # converting string date value into python date object
        patient_birthDate = datetime.strptime(self.date_start, '%Y-%m-%d').date()

    def get_data(self):
        # random=self.env['human.name'].search([])
        result = []
        for rec in self.patient_name.given:
            print(rec.given_name)
        return result

    # @api.model
    # def create(self, values):
    #     print("create method started !!!! ")
    #
    #
    #     values["patient_name"]= 'human.name,' + str(3)
    #
    #
    #     rtn1 = super(Patient,self).create(values)
    #
    #     return rtn1
