from odoo import models, fields, api


class RelatedPerson(models.Model):
    _name = "related.person"
    _description = "Details of realated person"

    relatedPerson_active=fields.Boolean(string="Record Active ? ")

    relatedPerson_patient=fields.Reference([('patient', "Patient's Name")], string="Related")


    relatedPerson_name=fields.Many2many(comodel_name="related.person.human.name",string="Person's name")

    related_person_contact_point=fields.Many2many(comodel_name="related.person.telecom",string="Contact Point")

    related_Person_gender=fields.Selection(selection=[
        ("male", "Male"),
        ("Female", "Female"),
        ("other", "Other"),
        ("unknown", "Unknown")] ,string="Gender")

    related_Person_birthDate=fields.Date(string="Birth Date")

    relatedPerson_address=fields.Many2many(comodel_name="related.person.address",string="Address")

    relatedPerson_photo=fields.Image(string="Photo")

    relatedPerson_communication_language=fields.Many2many(comodel_name="res.lang",
                                            string="Language")



class RelatedPersonName(models.Model):
    _name = "related.person.human.name"
    _rec_name = "related_personHumanName"

    related_personHumanName=fields.Reference([('human.name', 'Full Name')], string="Related Person's Name")

class RelatedPersonTelecom(models.Model):
    _name = "related.person.telecom"

    related_personContact_point=fields.Reference([('contact.point', 'Phone')], string="Contact Telecom")

class RelatedPersonAddress(models.Model):
    _name="related.person.address"
    _rec_name="new_relatedPerson_address"

    new_relatedPerson_address=fields.Reference([('address.fhir', 'Address')], string="Address")











