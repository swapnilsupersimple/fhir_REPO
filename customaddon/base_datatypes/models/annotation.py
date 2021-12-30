from odoo import models, fields , api


class Annotation(models.Model):
    _name="annotation"
    _rec_name = "annotation_text"
    _description = "Details about Annotation"

    annotation_time=fields.Datetime(string="Time")

    annotation_text=fields.Text(string="Text")

    annotation_author=fields.Reference([('practitioner.fhir', 'Practitioner Name'),
                                       ('patient', 'Patient Name'),
                                       ('organization', 'organization Name'),
                                       ('related.person', 'Related Person Name') ],

                                       string="Author")





