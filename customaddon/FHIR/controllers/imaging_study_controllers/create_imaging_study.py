from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ImagingStudy(http.Controller):

    @http.route('/create_imaging_study', type='json', auth='user')
    def create_imaging_study(self, **rec):

        if request.jsonrequest:

            values_for_imaging_study = {
                "description": rec["description"],
                "reasonCode":[],
                "series":[

                ]
            }

            #start_of_code_for_reason_code

            for inp_for_reasonCode in rec["reasonCode"][0]["coding"]:

                for key in values_for_imaging_study:

                    if key == "reasonCode":
                        values_for_imaging_study["reasonCode"].append((0, 0, inp_for_reasonCode
                                                                              ))
            #end_of_code_for_reason_code

            # start_of_code_for_series
            for inp_for_series in rec["series"]:
                print("inp_for_series-->",inp_for_series)

            for key, value in rec["series"][0]["modality"].items():
                print("inp_for_series_modality-->",key, value)
                x=dict(zip(["system","code"], [value,value]))
                print(x)

                for key in values_for_imaging_study:

                    if key == "series":
                        values_for_imaging_study["series"].append((0, 0, inp_for_series,x))


                # for key in values_for_imaging_study["series"]:
                #     if key == "series":
                #         values_for_imaging_study["series"].append((0, 0, inp_for_series
                #                                                               ))













        new_imaging_study = request.env['imaging.study'].sudo().create(values_for_imaging_study)

        args = {'success': True, 'message': 'Success', 'id': new_imaging_study.id}

        return args


#time_date_format_for '%Y-%m-%d %H:%M:%S'"