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
                "status": rec.status,

                "started": rec.started,

                "numberOfSeries": rec.numberOfSeries,

                "numberOfInstances": rec.numberOfInstances,

                "description": rec.description,

                "note": [],

                "series": []

                # "series":[]
            }

        list_for_note = [dict(zip(["text"], [rec.text])) for rec in imaging_study_rec.note]

        for key in vals:
            if key == "note":
                vals.update({"note": list_for_note})

        # code_for_series

        for rec in imaging_study_rec.series.BodyPartExamined:
            BodyPartExamined=dict(zip(["display"], [rec.display]))




        # list_for_BodyPartExamined=[dict(zip(["display"], [rec.display])) for rec in imaging_study_rec.series.BodyPartExamined]

        # print("list_for_BodyPartExamined-->",list_for_BodyPartExamined)

        list_for_instance = [dict(zip(["uid","number","title"], [rec.SOPInstanceUID,rec.InstanceNumber,rec.instanceTitle])) for rec in imaging_study_rec.series.instance]

        list_for_series = [dict(zip(["uid", "number", "description", "numberOfInstances", "started","instance","bodySite"],
                                    [rec.SeriesInstanceUID, rec.SeriesNumber, rec.SeriesDescription,
                                     rec.NumberOfSeriesRelatedInstances,
                                     rec.seriesStarted,list_for_instance,BodyPartExamined])) for rec in imaging_study_rec.series]


        for key in vals:
            if key == "series":
                vals.update({"series": list_for_series})




        imaging_Study.append(vals)

        data = {'status': 200, 'response': imaging_Study}
        return data


  # list_for_instance = [dict(zip(["uid"], [rec.SOPInstanceUID])) for rec in imaging_study_rec.series.instance]
        # print("list_for_instance-->", list_for_instance)
        #
        # for key in vals:
        #     print("key-->", key)
        #     if key == "series":
        #         print("key found")
        #         vals.update({"series": list_for_instance})