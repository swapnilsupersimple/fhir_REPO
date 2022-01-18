from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class DiagnosticReport(http.Controller):

    @http.route('/get_diagnostic_report', type='json', auth='user')
    def get_diagnostic_report(self, **kws):
        diagnostic_Report_rec = request.env['diagnostic.report'].sudo().search([])
        diagnostic_Report = []

        for rec in diagnostic_Report_rec:
            vals = {


                "status": rec.status,


                "category": [
                    {
                        "coding": ""
                    }
                ],


                "code":
                    {
                        "coding": ""

                    }
                ,

                "effectiveDateTime": rec.effectiveDateTime,

                "issued": rec.issued,

                "specimen": [],

                "result":[],

                "imagingStudy": [],

                "media": [],


                "conclusion": rec.conclusion,

                "conclusionCode": [
                    {
                        "coding": ""
                    }
                ],

                # "subject": [
                #     {
                #         "reference": rec.subject.patient_name.text,
                #
                #     }
                # ],

                # "encounter":[
                #     {
                #         "reference":rec.encounter.encounter_status
                #     }
                # ],



                "presentedForm": ""

            }
#start_of_code_for_category:

        list_for_category = [dict(zip(["display", "system"], [rec.display, rec.system])) for rec in
                             diagnostic_Report_rec.category]

        for key in vals["category"][0]:
            if key == "coding":
                vals["category"][0].update({"coding": list_for_category})
#End_of_code_for_category



# start_of_code_for_CODEField:
        list_for_code = [dict(zip(["system", "code", "display"], [rec.system, rec.code, rec.display])) for rec in
                         diagnostic_Report_rec.code]

        for key in vals["code"]:

            if key == "coding":
                vals["code"].update({"coding": list_for_code})
#End_of_code_for_CODEField

# start_of_code_for_specimen:
                list_for_specimen = [dict(zip(["display"], [ rec.display])) for rec
                                 in
                                 diagnostic_Report_rec.specimen]

                for key in vals:

                    if key == "specimen":
                        vals["specimen"].append(( list_for_specimen))
# End_of_code_for_specimen



# start_of_code_for_result:
        list_for_observation_result = [dict(zip(["reference"],
                                                [rec.reference]))
                                       for rec in diagnostic_Report_rec.result]

        for key in vals:
            if key == "result":
                vals["result"].append((list_for_observation_result))


# End_of_code_for_result

# start_of_code_for_imaging_study:
        list_for_imaging_study = [dict(zip(["display"],
                                                [rec.display]))
                                       for rec in diagnostic_Report_rec.imagingStudy]

        for key in vals:
            if key == "imagingStudy":
                vals["imagingStudy"].append((list_for_imaging_study))
# End_of_code_for_imaging_study

# start_of_code_for_conclusionCode:

        list_for_conclusionCode = [dict(zip(["system", "code","display"], [rec.system,rec.display, rec.code])) for rec in
                                   diagnostic_Report_rec.conclusionCode]

        for key in vals["conclusionCode"][0]:

            if key == "coding":
                vals["conclusionCode"][0].update({"coding": list_for_conclusionCode})

# start_of_code_for_conclusionCode

        list_for_attachemnt = [dict(zip(["data", "url", "size", "title", "creation"],
                                        [rec.data, rec.url, rec.size, rec.title, rec.creation]))
                               for rec in diagnostic_Report_rec.presentedForm]

        for key in vals:
            if key == "presentedForm":
                vals.update({"presentedForm": list_for_attachemnt})





      #code_for_media

        for x in diagnostic_Report_rec.media:
            inp_for_comment=x.comment

        for rec in diagnostic_Report_rec.media:
            inp_for_link=dict(zip(["reference" ,"display"], [rec.reference,rec.display]))

            for key in vals:
                if key == "media":
                    vals["media"].append({"comment":inp_for_comment,"link":inp_for_link})



        diagnostic_Report.append(vals)

        data = {'status': 200, 'response': diagnostic_Report}
        return data
