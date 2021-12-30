from odoo import models, fields, api


class CareTeam(models.Model):
    _name = "care.team"
    _description = "Details about Care Team"

    care_Team_status=fields.Selection(selection=[
        ("proposed", "Proposed"),
        ("active", "Active"),
        ("suspended", "Suspended"),
        ("inactive", "Inactive"),("inactive", "Inactive"),("entered-in-error","Entered-in-error")] ,name="Status of Care Team")

    care_Team_name = fields.Char(String="Care Team Name")

    care_Team_subject = fields.Reference([('patient', "Patient's Name")], string="Care Team")

    care_Team_telecom = fields.Reference([('contact.point', 'Phone')], string="Contact")







