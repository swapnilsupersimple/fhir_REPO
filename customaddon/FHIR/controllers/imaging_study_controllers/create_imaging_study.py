from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ImagingStudy(http.Controller):

    @http.route('/create_imaging_study', type='json', auth='user')
    def create_imaging_study(self, **rec):

        if request.jsonrequest:


            # vals={
            #     "reference":[]
            # }
            # for inp_for_enpoint in rec["series"][0]["endpoint"]:
            #     print("inp_for_series-->", inp_for_enpoint)
            #
            #
            #     for key in vals:
            #
            #         if key == "reference":
            #             vals["reference"].append(inp_for_enpoint)


            values_for_imaging_study = {
                "status":rec["status"],
                "modality":[],
                "note":[],
                "procedureCode":[],
                "numberOfSeries": rec["numberOfSeries"],
                "numberOfInstances": rec["numberOfInstances"],
                "description": rec["description"],
                "started":rec["started"],
                "reasonCode":[],
                "endpoint":[],
                "series":[ ]

            }

            #start_of_code_for_reason_code

            for inp_for_reasonCode in rec["reasonCode"][0]["coding"]:
                print("inp_for_reasonCode-->",inp_for_reasonCode)

                for key in values_for_imaging_study:

                    if key == "reasonCode":
                        values_for_imaging_study["reasonCode"].append((0,0,inp_for_reasonCode))

            #end_of_code_for_reason_code

            # start_of_code_for_endpoint
            for inp_for_endpoint in rec["endpoint"]:
                print("inp_for_reasonCode-->", inp_for_endpoint)

                for key in values_for_imaging_study:

                    if key == "endpoint":
                        values_for_imaging_study["endpoint"].append((0, 0, inp_for_endpoint))

            # end_of_code_for_endpoint

            # start_of_code_for_modality
            for inp_for_modality in rec["modality"]:
                print("inp_for_reasonCode-->", inp_for_modality)

                for key in values_for_imaging_study:

                    if key == "modality":
                        values_for_imaging_study["modality"].append((0, 0, inp_for_modality))

            # end_of_code_for_modality

            # start_of_code_for_note
            for inp_for_note in rec["note"]:
                print("inp_for_reasonCode-->", inp_for_note)

                for key in values_for_imaging_study:
                    if key == "note":
                            values_for_imaging_study["note"].append((0, 0, inp_for_note))

            # end_of_code_for_note

            for inp_for_procedureCode in rec["procedureCode"][0]["coding"]:
                print("inp_for_reasonCode-->", inp_for_procedureCode)

                for key in values_for_imaging_study:

                    if key == "procedureCode":
                        values_for_imaging_study["procedureCode"].append((0, 0, inp_for_procedureCode))


            # for inp_for_endpoint in rec["series"]:
            #
            #     print("x-->",inp_for_endpoint)
            #     for key in values_for_imaging_study:
            #
            #         if key == "series":
            #             values_for_imaging_study["series"].append((0,0,inp_for_endpoint))

            # for inp_for_series in rec["series"]:
            #     inp_for_series.pop('endpoint')
            #     print("inp_for_series-->",inp_for_series)
            #
            #     for key in values_for_imaging_study:
            #
            #         if key == "series":
            #             values_for_imaging_study["series"].append((0, 0, inp_for_series))






        new_imaging_study = request.env['imaging.study'].sudo().create(values_for_imaging_study)

        args = {'success': True, 'message': 'Success', 'id': new_imaging_study.id}


        return  args


#time_date_format_for '%Y-%m-%d %H:%M:%S'

#extract dictionary from input dictionary , apppend to series.Do same for endpoint