from odoo import models, fields, api


class ServiceRequest(models.Model):
    _name = "service.request"
    _description = "Details of Service Request"

    serviceRequest_status = fields.Selection(selection=[
        ("draft", "Draft"),
        ("active", "Active"),
        ("on Hold", "On Hold"),
        ("revoked", "Revoked"), ("completed", "Completed"), ("unknown", "Unknown"),
        ("entered in error", "Entered in error")
    ], string="Status")

    serviceRequest_intent = fields.Selection(selection=[
        ("Proposal", "Proposal"),
        ("Plan", "Plan"),
        ("Directive", "Directive"),
        ("Order", "Order"), ("Original Order", "Original Order"), ("Reflex Order", "Reflex Order"),
        ("Filler Order", "Filler Order"), ("Instance Order", "Instance Order"), ("Option", "Option")
    ], string="Status")

    serviceRequest_category = fields.Many2many(comodel_name="service.request.category", string="Category")

    serviceRequest_priority = fields.Selection(selection=[
        ("Proposal", "Routine"),
        ("Plan", "Urgent"),
        ("Directive", "ASAP"),
        ("Order", "STAT")
    ], string="Priority")

    serviceRequest_doNotPerform = fields.Boolean(string="Do not Perform")

    serviceRequest_code = fields.Many2one(comodel_name="service.request.code", string="Code")

    serviceRequest_OrderDetail = fields.Many2many(comodel_name="service.request.order.detail", string="Order Detail")

    serviceRequest_requester = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                 ('patient', 'Patient Name'),
                                                 ('related.person', 'Related Person Name'),

                                                 ('oraganization', ' Oragnization Name'),

                                                 ('device.fhir', 'Device Name')],
                                                string="Requester")

    serviceRequest_performer = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                 ('patient', 'Patient Name'),
                                                 ('related.person', 'Related Person Name'),
                                                 ('care.team', 'Care Team'),

                                                 ('oraganization', ' Oragnization Name'),

                                                 ('device.fhir', 'Device Name')],
                                                string="Performer")

    serviceRequest_locationReference=fields.Reference([('location.fhir', 'Location')],string="Location")

    ServiceRequest_reasonReference=fields.Reference([('condition', 'Condition'),
                                                 ('observation', 'Observation'),
                                                 ('diagnostic.report', 'Diagnostic Report'),
                                                 ('document.reference', 'Document Reference')],
                                               string="Reason Reference")

    serviceRequest_specimen=fields.Reference([('specimen', 'Specimen')],string="Specimen")

    serviceRequest_patientInstruction=fields.Char(string="Instruction")

    serviceRequest_quantity=fields.Integer(string="Quantity")

    serviceRequest_authoredOn=fields.Datetime(string="Authored On")

    serviceRequest_bodySite=fields.Many2many(comodel_name="service.request.body.site",string="Body Site")

    serviceRequest_reasonCode=fields.Many2many(comodel_name="service.request.reason.code",string='Reason Code')

    serviceRequest_locationCode=fields.Many2many(comodel_name="service.request.location.code",string='Reason Code')


class ServiceRequestCategory(models.Model):
    _name = "service.request.category"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class ServiceRequestCode(models.Model):
    _name = "service.request.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class ServiceRequestOrderDetail(models.Model):
    _name = "service.request.order.detail"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ServiceRequestBodySite(models.Model):
    _name = "service.request.body.site"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ServiceRequestReasonCode(models.Model):
    _name = "service.request.reason.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")

class ServiceRequestLocationCode(models.Model):
    _name = "service.request.location.code"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination=fields.Char("Defination")




