from odoo import models, fields, api


class Encounter(models.Model):
    _name = "encounter"
    _description = "Details about Encounter"
    # _rec_name = "appointment_status"

    encounter_status = fields.Selection(selection=[
        ("planned", "planned"),
        ("arrived", "arrived"),
        ("triaged", "triaged"),
        ("in-progress", "in-progress"), ("onleave", "onleave"), ("finished", "finished"),
        ("cancelled", "Cancelled"), ("entered in Error", "Entered in Error"), ("unknown", "Unknown")
    ], string="Status")

    encounter_type = fields.Many2many(comodel_name="encounter.type", string="Encounter type")

    encounter__service_type = fields.Many2one(comodel_name="encounter.service.type", string="Encounter Service type")

    encounter_priority = fields.Many2one(comodel_name="encounter.priority", string="Encounter Priority")

    encounter_subject = fields.Reference([('patient', "Patient's Name"),
                                          ('group_name', "Group Name")], string="Subject")

    encounter_participant_type = fields.Many2one(comodel_name="encounter.participant.type", string="Participant Type")

    encounter_requestedPeriod_start = fields.Datetime(string="Start Date time")

    encounter_requestedPeriod_end = fields.Datetime(string="End Date time")

    encounter_participant_individual = fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                                         ('related.person', 'Related Person Name'),
                                                         ('practitioner.role.fhir', 'Practitioners Name'),
                                                         ],
                                                        string="Appointment Actor")

    Encounter_Hospitalization_Admit_Source = fields.Many2one(comodel_name="encounter.hospitalization.admit.source",
                                                             string="Admit Source")

    Encounter_Hospitalization_Diet_Preference = fields.Many2many(
        comodel_name="encounter.hospitalization.diet.preference", string="Diet Preference")

    encounter_hospitalization_special_courtesy = fields.Many2many(
        comodel_name="encounter.hospitalization.special.courtesy", string="Special Courtesy")

    encounter_Hospitalization_special_arrangement = fields.Many2many(
        comodel_name="encounter.hospitalization.special.arrangement", string="Special Arrangment")

    encounter_hospitalization_discharge_disposition = fields.Many2many(
        comodel_name="encounter.hospitalization.discharge.disposition", string="Discharge Diposition")

    encounter_hospitalization_destination = fields.Reference([('location.fhir', 'Location Name'),
                                                              ('organization', 'Organization Name'),
                                                              ],
                                                             string="Appointment Actor")

    encounter_location_location = fields.Reference([('location.fhir', 'Location Name')],
                                                   string="Location")

    encounter_location_status = fields.Selection(selection=[
        ("planned", "Planned"),
        ("active", "Active"),
        ("reserved", "Reserved"),
        ("completed", "Completed"),
    ], string="Status")

    encounter_location_physical_type=fields.Many2one(comodel_name="encounter.location.physical.type",string="Type")

    encounter_location_period_start = fields.Datetime(string="Start Date time")

    encounter_location_period_end = fields.Datetime(string="End Date time")

    encounter_service_provider=fields.Reference([('organization','Organization Name')],
                                                   string="Service Provider")
    
    diagnostic_Report_encounter=fields.Many2one("diagnostic.report",string="diagnostic_Report_encounter")

    reference=fields.Char(string="reference")


class EncounterType(models.Model):
    _name = "encounter.type"
    _description = "Details about Encounter Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class EncounterServiceType(models.Model):
    _name = "encounter.service.type"
    _description = "Details about Encounter Service Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")


class EncounterPriority(models.Model):
    _name = "encounter.priority"
    _description = "Details about Encounter Priority"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterParticipantType(models.Model):
    _name = "encounter.participant.type"
    _description = "Details about Encounter Participant Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterHospitalizationAdmitSource(models.Model):
    _name = "encounter.hospitalization.admit.source"
    _description = "Details about Encounter hospitalization admit Source"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterHospitalizationDietPreference(models.Model):
    _name = "encounter.hospitalization.diet.preference"
    _description = "Details about Encounter hospitalization diet preference"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterHospitalizationSpecialCourtesy(models.Model):
    _name = "encounter.hospitalization.special.courtesy"
    _description = "Details about Encounter Hospitalization Special Courtesy"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterHospitalizationSpecialArrangement(models.Model):
    _name = "encounter.hospitalization.special.arrangement"
    _description = "Details about Encounter Hospitalization Special Arrangement"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterHospitalizationDischargeDisposition(models.Model):
    _name = "encounter.hospitalization.discharge.disposition"
    _description = "Details about Encounter Hospitalization Discharge Disposition"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")
    defination = fields.Char("defination")


class EncounterLocationPhysicalType(models.Model):
    _name = "encounter.location.physical.type"
    _description = "Details about Encounter Location Physical Type"
    _rec_name = "display"

    display = fields.Char("Display")
    code = fields.Char("Code")





