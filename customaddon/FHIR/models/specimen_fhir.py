from odoo import models, fields, api


class Specimen(models.Model):
    _name = "specimen"
    _description = "Details about specimen"

    specimen_status = fields.Selection(selection=[
        ("available", "Available"),
        ("unavailable", "Unavailable"),
        ("unsatisfactory", "Unsatisfactory"),
        ("entered in Error", "Entered in Error"),
    ], string="Status")

    specimen_type = fields.Many2one(comodel_name="specimen.type", string="Type")

    specimen_subject = fields.Reference([('group', 'Group '),
                                         ('patient', 'Patient Name'),
                                         ('location.fhir', 'Location'),
                                         ('device.fhir', 'Device Name'),
                                         ],
                                        string="Subject")

    specimen_receivedTime = fields.Datetime(string="Received Time")

    specimen_collection_collector = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                      ('practitioner.role.fhir', 'Practitioner Role'),
                                                     ],
                                                     string="Collector")

    specimen_collection_collected=fields.Datetime(string="Collected Date")

    specimen_collection_quantity=fields.Integer(string="Quantity")

    specimen_collection_method=fields.Many2one(comodel_name="specimen.collection.method",string="Collection Method")

    specimen_collection_bodySite=fields.Many2one(comodel_name="specimen.collection.body.site",string="Body Site")

    specimen_collection_fastingStatus=fields.Many2one(comodel_name="specimen.collection.fasting.status",string="Fasting Status")

    specimen_processing_description=fields.Char(string="Processing")

    specimen_processing_procedure=fields.Many2one(comodel_name="specimen.processing.procedure",string="Procedure")

    specimen_processing_time=fields.Datetime(string="Processing Time")

    specimen_container_description=fields.Char(string="Description")

    specimen_container_type=fields.Many2one(comodel_name="specimen.container.type",string="Type")

    specimen_container_capacity=fields.Integer(string="Container Capacity")

    specimen_container_specimenQuantity=fields.Integer(string="Specimen Quantity")

    specimen_container_additive=fields.Many2one(comodel_name="specimen.container.additive",string="Additive")

    specimen_condition=fields.Many2many(comodel_name="specimen.condition",string="Condition")

    diagnostic_Report_specimen = fields.Many2one("diagnostic.report", string="DiagnosticReportSpecimen")

    imaging_Study_Series_specimen=fields.Many2one("imaging.study.series",string="imagingStudyseries_specimen")

    reference = fields.Char(string="reference")
    display = fields.Char(string="display")



class SpecimenType(models.Model):
    _name = "specimen.type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class SpecimenCollectionMethod(models.Model):
    _name = "specimen.collection.method"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class SpecimenCollectionBodySite(models.Model):
    _name = "specimen.collection.body.site"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class SpecimenCollectionFastingStatus(models.Model):
    _name = "specimen.collection.fasting.status"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class SpecimenProcessingProcedure(models.Model):
    _name = "specimen.processing.procedure"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class SpecimenContainerType(models.Model):
    _name = "specimen.container.type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class SpecimenContainerAdditive(models.Model):
    _name = "specimen.container.additive"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class SpecimenCondition(models.Model):
    _name = "specimen.condition"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")





