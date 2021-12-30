from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class DiagnosticReport(http.Controller):

    @http.route('/create_diagnostic_report', type='json', auth='user')
    def create_diagnostic_report(self, **rec):

        if request.jsonrequest:



            values_for_diagnostic_report = {
                "status": rec["diagnosticReport_status"],

                "category": [],

                # "code":rec["diagnosticReport_code"],

                "effectiveDateTime": rec["diagnosticReport_effectiveDateTime"],

                "issued": rec["diagnosticReport_issued"],
                "specimen": [],

                "conclusionCode": [],

                # "conclusion": rec["diagnosticReport_conclusion"],
                "imagingStudy":[],

                "result":[],
                "presentedForm": []

            }

            for inp_conclusionCode in rec["display_name_for_diagnosticReport_conclusionCode"]:
                for key in values_for_diagnostic_report:

                    if key == "conclusionCode":
                        values_for_diagnostic_report["conclusionCode"].append((0, 0, {"display": inp_conclusionCode
                                                                                      }))

            for inp_category in rec["display_name_for_diagnosticReport_category"]:
                for key in values_for_diagnostic_report:

                    if key == "category":
                        values_for_diagnostic_report["category"].append((0, 0, {"display": inp_category
                                                                                }))
            for inp_for_presented_form in rec["presentedForm"]:

                for key in values_for_diagnostic_report:

                    if key == "presentedForm":
                        values_for_diagnostic_report["presentedForm"].append((0, 0, inp_for_presented_form
                                                                              ))

            for inp_for_imagingStudy in rec["imagingStudy"]:

                for key in values_for_diagnostic_report:

                    if key == "imagingStudy":
                        values_for_diagnostic_report["imagingStudy"].append((0, 0, inp_for_imagingStudy
                                                                              ))

            for inp_for_result in rec["result"]:

                for key in values_for_diagnostic_report:

                    if key == "result":
                        values_for_diagnostic_report["result"].append((0, 0, inp_for_result
                                                                             ))
            for inp_for_specimen in rec["specimen"]:

                for key in values_for_diagnostic_report:

                    if key == "specimen":
                        values_for_diagnostic_report["specimen"].append((0, 0, inp_for_specimen
                                                                       ))

        new_diagnostic_report = request.env['diagnostic.report'].sudo().create(values_for_diagnostic_report)

        args = {'success': True, 'message': 'Success', 'id': new_diagnostic_report.id}

        return args
