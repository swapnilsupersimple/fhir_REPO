from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class DiagnosticReport(http.Controller):

    @http.route('/create_diagnostic_report', type='json', auth='user')
    def create_diagnostic_report(self, **rec):

        if request.jsonrequest:

            values_for_diagnostic_report = {
                "status": rec["status"],

                "category": [],

                "code": [],

                "effectiveDateTime": rec["effectiveDateTime"],

                "issued": rec["issued"],
                # "specimen": [],

                "conclusionCode": [],

                # "conclusion": rec["diagnosticReport_conclusion"],
                # "imagingStudy":[],

                # "result":[],
                "presentedForm": [],
                "media":[]

            }


            for inp_for_media_comment in rec["media"]:
                print("inp_for_media_comment-->",inp_for_media_comment)
                for key in values_for_diagnostic_report:

                    if key == "media":
                        values_for_diagnostic_report["media"].append((0, 0,inp_for_media_comment
                                                                     ))

            # for inp_for_presented_form in rec["presentedForm"]:
            #
            #     for key in values_for_diagnostic_report:
            #
            #         if key == "presentedForm":
            #             values_for_diagnostic_report["presentedForm"].append((0, 0, inp_for_presented_form
            #                                                                   ))




            for inp_for_code in rec["code"]["coding"]:

                for key in values_for_diagnostic_report:

                    if key == "code":
                        values_for_diagnostic_report["code"].append((0, 0, inp_for_code
                                                                     ))

            for inp_conclusionCode in rec["conclusionCode"]:

                for key in values_for_diagnostic_report:

                    if key == "conclusionCode":
                        values_for_diagnostic_report["conclusionCode"].append((0, 0, {"display": inp_conclusionCode
                                                                                      }))

            for inp_category in rec["category"]:
                for key in values_for_diagnostic_report:

                    if key == "category":
                        values_for_diagnostic_report["category"].append((0, 0, {"display": inp_category
                                                                                }))
            for inp_for_presented_form in rec["presentedForm"]:

                for key in values_for_diagnostic_report:

                    if key == "presentedForm":
                        values_for_diagnostic_report["presentedForm"].append((0, 0, inp_for_presented_form
                                                                              ))

            # for inp_for_imagingStudy in rec["imagingStudy"]:
            #
            #     for key in values_for_diagnostic_report:
            #
            #         if key == "imagingStudy":
            #             values_for_diagnostic_report["imagingStudy"].append((0, 0, inp_for_imagingStudy
            #                                                                   ))
            #
            # for inp_for_result in rec["result"]:
            #
            #     for key in values_for_diagnostic_report:
            #
            #         if key == "result":
            #             values_for_diagnostic_report["result"].append((0, 0, inp_for_result
            #                                                                  ))
            # for inp_for_specimen in rec["specimen"]:
            #
            #     for key in values_for_diagnostic_report:
            #
            #         if key == "specimen":
            #             values_for_diagnostic_report["specimen"].append((0, 0, inp_for_specimen))

        print("this is new change")
        new_diagnostic_report = request.env['diagnostic.report'].sudo().create(values_for_diagnostic_report)

        args = {'success': True, 'message': 'Success', 'id': new_diagnostic_report.id}

        return args
