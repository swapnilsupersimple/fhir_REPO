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
                "modality": [],

                "started": rec.started,

                "numberOfSeries": rec.numberOfSeries,

                "numberOfInstances": rec.numberOfInstances,

                "description": rec.description,

                "note": [],

                "series": [],

                "reasonCode": [
                    {
                        "coding": []

                    }
                ],

            }

        list_for_note = [dict(zip(["text"], [rec.text])) for rec in imaging_study_rec.note]

        for key in vals:
            if key == "note":
                vals.update({"note": list_for_note})


        list_for_reasoncode = [dict(zip(["system","code","display"], [rec.system,rec.code,rec.display])) for rec in imaging_study_rec.reasonCode]

        print("list_for_reasoncode-->",list_for_reasoncode)

        for key in vals["reasonCode"][0]:
            print("key-->",key)
            if key == "coding":
                vals["reasonCode"][0].update({"coding": list_for_reasoncode})





        # code_for_series

        for rec in imaging_study_rec.series.bodySite:
            bodySite=dict(zip(["display","code"], [rec.display,rec.code]))

        for rec in imaging_study_rec.series.laterality:
            laterality = dict(zip(["display", "code"], [rec.display, rec.code]))

        for rec in imaging_study_rec.series.instance.SOPClassUID:
            SOPClassUID=dict(zip(["system", "code"], [rec.system, rec.code]))

        for rec in imaging_study_rec.series.modality:
            series_modality=dict(zip(["system", "code"], [rec.system, rec.code]))
            print("series_modality-->",series_modality)

            list_for_instance = [dict(zip(["uid","number","title","sopClass"], [rec.SOPInstanceUID,rec.InstanceNumber,rec.instanceTitle,SOPClassUID])) for rec in imaging_study_rec.series.instance]


        list_for_series = [dict(zip(["uid", "number","modality", "description", "numberOfInstances", "started","instance","bodySite","laterality"],
                                    [rec.uid, rec.number,series_modality, rec.description,
                                     rec.numberOfInstances,
                                     rec.started,list_for_instance,rec.bodySite,laterality])) for rec in imaging_study_rec.series]

        for key in vals:
            if key == "series":
                vals.update({"series": list_for_series})


        #code_for_modailty

        list_for_modality=[dict(zip(["system","code"], [rec.system,rec.code])) for rec in imaging_study_rec.modality]

        for key in vals:
            if key == "modality":
                vals.update({"modality": list_for_modality})



        imaging_Study.append(vals)

        data = {'status': 200, 'response': imaging_Study}
        return data


