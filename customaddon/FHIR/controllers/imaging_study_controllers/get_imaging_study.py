from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ImagingStudy(http.Controller):

    @http.route('/get_imaging_study', type='json', auth='user')
    def get_imaging_study(self, **kws):
        imaging_study_rec = request.env['imaging.study'].sudo().search([])
        imaging_Study = []

        for rec in imaging_study_rec:
            vals = {
                "status":rec.status,

                "started":rec.started,

                "numberOfSeries":rec.numberOfSeries,

                "numberOfInstances":rec.numberOfInstances,

                "description":rec.description,

                "note":[]
            }

        list_for_note = [dict(zip(["text"],
                                        [rec.text]))
                               for rec in imaging_study_rec.note]

        for key in vals:
            if key == "note":
                vals.update({"note": list_for_note})

        imaging_Study.append(vals)

        data = {'status': 200, 'response': imaging_Study}
        return data