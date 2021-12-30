from odoo import models, fields, api


class Organization(models.Model):
    _name = "organization"
    _description = "Details about organization"
    _rec_name = "organization_name"

    organization_name = fields.Char(string="Organization Name")

    is_organization_active=fields.Boolean(string="Organization Active?")

    organization_alias_ids= fields.One2many("organization.alias","oraganization_alias_id",string="Alias")

    organization_telecom = fields.Reference([('contact.point', 'Phone')], string="Organization Contact ")

    organization_address = fields.Reference([('address.fhir', 'Address')], string="Organization Address")

    organization_contact_name = fields.Reference([('human.name', 'Full Name')], string="Contact Name")

    organization_contact_telecom = fields.Reference([('contact.point', 'Phone')], string="Contact Telecom info")

    organization_contact_address=fields.Reference([('address.fhir', 'Address')], string="Contact Address")

class OrganizationAlias(models.Model):
    _name ="organization.alias"
    _description = 'Organization Alias'
    _rec_name = "organization_alias_new"

    organization_alias_new= fields.Char(string="alias")
    oraganization_alias_id=fields.Many2one("organization",string="Organization alias id")









