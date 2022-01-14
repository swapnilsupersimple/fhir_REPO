from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ImagingStudy(http.Controller):
    @http.route('/create_imaging_study', type='json', auth='user')
    def create_imaging_study(self, **rec):

        if request.jsonrequest:



            # values_for_imaging_study_series = []
            #
            values={
                "description": "",
                "endpoint": []
            }


            values_for_imaging_study = {
                "status": rec["status"],
                "reasonCode": [],
                "endpoint": [],
                "series":[(0,0,values)]
                # "series":[]

            }

            # start_of_code_for_reason_code

            for inp_for_reasonCode in rec["reasonCode"][0]["coding"]:
                print("inp_for_reasonCode-->", inp_for_reasonCode)

                for key in values_for_imaging_study:

                    if key == "reasonCode":
                        values_for_imaging_study["reasonCode"].append((0, 0, inp_for_reasonCode))

            # end_of_code_for_reason_code

            # start_of_code_for_endpoint
            for inp_for_endpoint in rec["endpoint"]:
                print("inp_for_reasonCode-->", inp_for_endpoint)

                for key in values_for_imaging_study:

                    if key == "endpoint":
                        values_for_imaging_study["endpoint"].append((0,0,inp_for_endpoint))

            # end_of_code_for_endpoint

            for x in rec["series"][0]["endpoint"]:
                for key in values_for_imaging_study:
                        if key=="series":
                            values["endpoint"].append((0,0,x))

            y=rec["series"][0]["description"]
            print(y)

            for key in values_for_imaging_study:
                    if key == "series":
                        values["description"]=y


        new_imaging_study = request.env['imaging.study'].sudo().create(values_for_imaging_study)

        args = {'success': True, 'message': 'Success', 'id': new_imaging_study.id}



        return args

# time_date_format_for '%Y-%m-%d %H:%M:%S'

# extract dictionary from input dictionary , apppend to series.Do same for endpoint
