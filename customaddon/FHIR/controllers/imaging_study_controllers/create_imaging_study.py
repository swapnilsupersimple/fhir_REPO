from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ImagingStudy(http.Controller):
    @http.route('/create_imaging_study', type='json', auth='user')
    def create_imaging_study(self, **rec):

        if request.jsonrequest:





            values_for_imaging_study = {
                "status": rec["status"],
                "modality":[],
                "procedureCode":[],
                "procedureReference":[]


            }

            inp_for_procedureReference=rec["procedureReference"]["reference"]
            # for inp_for_procedureCode in rec["procedureReference"]:
            #     print("inp_for_procedureCode-->",inp_for_procedureCode["reference"])

            for key in values_for_imaging_study:
                    if key == "procedureReference":
                        values_for_imaging_study["procedureReference"].append((0,0,{"reference":inp_for_procedureReference} ))



# start_of_code_for_inp_for_procedureCode

            for inp_for_procedureCode in rec["procedureCode"][0]["coding"]:
                print(inp_for_procedureCode)

                for key in values_for_imaging_study:
                    if key == "procedureCode":
                        values_for_imaging_study["procedureCode"].append((0, 0, inp_for_procedureCode))

# end_of_code_for_inp_for_procedureCode

# start_of_code_for_modality

                    for inp_for_modality in rec["modality"]:
                        print("inp_for_modality-->",inp_for_modality)
                    # for key in values_for_imaging_study:
                    #         if key == "modality":
                    #             values_for_imaging_study["modality"].append((0, 0, inp_for_modality))

# end_of_code_for_modality



        new_imaging_study = request.env['imaging.study'].sudo().create(values_for_imaging_study)

        args = {'success': True, 'message': 'Success', 'id': new_imaging_study.id}



        return args

# time_date_format_for '%Y-%m-%d %H:%M:%S'

# extract dictionary from input dictionary , apppend to series.Do same for endpoint



from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ImagingStudy(http.Controller):
    @http.route('/create_imaging_study', type='json', auth='user')
    def create_imaging_study(self, **rec):

        if request.jsonrequest:

            values_for_endpoint={
                "endpoint": []
            }
            values_for_modality={
                "system":"",
                "code":""
            }

            values_for_imaging_study_series_instance_sopClass={
                "system":"",
                "code":""
            }
            values_for_imaging_study_series_instance={
                "uid": "",
                "number":"" ,
                "title": "",
                "sopClass":[(0,0,values_for_imaging_study_series_instance_sopClass)]
            }
            values_for_imaging_study_series_bodysite={
                "system": "",
                "code": "",
                "display": ""
            }
            values_for_imaging_study_series_laterality={
                "system": "",
                "code": "",
                "display": ""
            }

            values_for_imaging_study_series={
                "description": "",
                "modality":[(0,0,values_for_modality)],
                "bodySite":[(0,0,values_for_imaging_study_series_bodysite)],
                "laterality":[(0,0,values_for_imaging_study_series_laterality)],
                "endpoint": [],
                "instance":[(0,0,values_for_imaging_study_series_instance)],

            }


            values_for_imaging_study = {
                "status": rec["status"],
                "series":[(0,0,values_for_imaging_study_series)]
            }


            inp_for_description = rec["series"][0]["description"]
            for inp_for_endpoint in rec["series"][0]["endpoint"]:
                for key in values_for_imaging_study:
                        if key=="series":
                            values_for_imaging_study_series["endpoint"].append((0,0,inp_for_endpoint))
                            values_for_imaging_study_series["description"] = inp_for_description

#start_of_code_for_imaging_study_series_modality
            inp_for_series_modality_system=rec["series"][0]["modality"]["system"]
            inp_for_series_modality_code=rec["series"][0]["modality"]["code"]

            for key in values_for_imaging_study:
                    if key == "series":
                        values_for_modality["system"]=inp_for_series_modality_system
                        values_for_modality["code"] = inp_for_series_modality_code
#end_of_code_for_imaging_study_series_modality

#start_of_code_for_imaging_study_series_instance
            inp_for_imaging_study_series_instance_uid=rec["series"][0]["instance"][0]["uid"]
            inp_for_imaging_study_series_instance_number=rec["series"][0]["instance"][0]["number"]
            inp_for_imaging_study_series_instance_title=rec["series"][0]["instance"][0]["title"]

            for key in values_for_imaging_study:
                if key == "series":
                    values_for_imaging_study_series_instance["uid"]=inp_for_imaging_study_series_instance_uid
                    values_for_imaging_study_series_instance["number"] = inp_for_imaging_study_series_instance_number
                    values_for_imaging_study_series_instance["title"] = inp_for_imaging_study_series_instance_title



            inp_for_series_instance_sopClass_system = rec["series"][0]["instance"][0]["sopClass"]["system"]
            inp_for_series_instance_sopClass_code = rec["series"][0]["instance"][0]["sopClass"]["code"]
            for key in values_for_imaging_study:
                if key == "series":
                    values_for_imaging_study_series_instance_sopClass["system"] = inp_for_series_instance_sopClass_system
                    values_for_imaging_study_series_instance_sopClass["code"] = inp_for_series_instance_sopClass_code
#end_of_code_for_imaging_study_series_instance

#Start_of_code_for_imaging_study_series_bodysite
            inp_for__imaging_study_series_bodysite_system = rec["series"][0]["bodySite"]["system"]
            inp_for__imaging_study_series_bodysite_code =rec["series"][0]["bodySite"]["code"]
            inp_for__imaging_study_series_bodysite_display=rec["series"][0]["bodySite"]["display"]
            for key in values_for_imaging_study:
                if key == "series":
                    values_for_imaging_study_series_bodysite["system"]=inp_for__imaging_study_series_bodysite_system
                    values_for_imaging_study_series_bodysite["code"]=inp_for__imaging_study_series_bodysite_code
                    values_for_imaging_study_series_bodysite["display"]=inp_for__imaging_study_series_bodysite_display


#End_of_code_for_imaging_study_series_laterality
                    # Start_of_code_for_imaging_study_series_bodysite
                    inp_for__imaging_study_series_laterality_system = rec["series"][0]["laterality"]["system"]
                    inp_for__imaging_study_series_laterality_code = rec["series"][0]["laterality"]["code"]
                    inp_for__imaging_study_series_laterality_display = rec["series"][0]["laterality"]["display"]
                    for key in values_for_imaging_study:
                        if key == "series":
                            values_for_imaging_study_series_laterality[
                                "system"] = inp_for__imaging_study_series_laterality_system
                            values_for_imaging_study_series_laterality[
                                "code"] = inp_for__imaging_study_series_laterality_code
                            values_for_imaging_study_series_laterality[
                                "display"] = inp_for__imaging_study_series_laterality_display

        # End_of_code_for_imaging_study_series_laterality



            # for inp_for_description in rec["series"]:
            #     # inp_for_description.pop("endpoint")
            #     print(inp_for_description
            #     for key in values_for_imaging_study:
            #         if key=="series":
            #             values_for_imaging_study["series"].append((0,0,inp_for_description))

            # for inp_for_endpoint in rec["series"][0]["endpoint"]:
            #     for key in values_for_imaging_study:
            #         if key=="series":
            #             values_for_endpoint["endpoint"].append((0,0,inp_for_endpoint))




        new_imaging_study = request.env['imaging.study'].sudo().create(values_for_imaging_study)

        args = {'success': True, 'message': 'Success', 'id': new_imaging_study.id}



        return args

# time_date_format_for '%Y-%m-%d %H:%M:%S'

# extract dictionary from input dictionary , apppend to series.Do same for endpoint
