from odoo import models, fields, api


class Group(models.Model):
    _name = "group"
    _description = "details about group"

    group_active = fields.Boolean(string="Group Active?")
    group_type = fields.Selection(selection=[('person', 'Person'),
                                             ('animal', 'Animal'),
                                             ('practitioner', 'Practitioner'),
                                             ('device', 'Device'),
                                             ('medication', 'medication'),
                                             ('substance', 'Substance')],
                                  string="Group Type")

    group_actual = fields.Selection(selection=[('descriptive', 'Descriptive'),
                                               ('actual', 'Actual')],
                                    string="Group Actual")

    group_name=fields.Char(string="Group Name")

    group_quantity=fields.Integer(string="Group Quantity")

    group_member_entity=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                       ('patient', 'Patient Name'),
                                       ('organization', 'organization Name'),
                                       ('related.person', 'Related Person Name') ],

                                       string="Group Member Entity")

    group_member_inactive=fields.Boolean(string="Group member active?")

    group_member_period_start=fields.Datetime(string="Period(Start)")

    group_member_period_end=fields.Datetime(string="Period(End)")








