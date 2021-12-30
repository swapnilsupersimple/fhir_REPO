from odoo import models,fields,api

class CodeableConcept(models.Model):
    _name = 'codeable.concept'
    _description = 'details about Codeable Concept'

    codeable_concept_text=fields.Char(string="")




