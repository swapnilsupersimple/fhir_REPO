
from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from typing import List


class Patient(http.Controller):

    @http.route('/create_patient', type='json', auth='user')
    def create_patient(self, **rec):

        if request.jsonrequest:
            # CODE_FOR_PATIENT_NAME

            # values_for_patient_identifier=[{
            #     "use":rec["use_patient_identifier"],
            #     "value":rec["value_patient_identifier"],
            #     "start":rec["value_patient_identifier_period_start"],
            #     "end":rec["value_patient_identifier_end"],
            # }]
            #
            # for values in values_for_patient_identifier:
            #     new_patient_identifier = request.env['identifier'].sudo().create(values)

            #CODE_FOR_PATIENT_NAME

            values_for_patient_name = [{
                # "use": rec["use_patient_name"],
                "text": rec["text_patient_name"],
                "family": rec["family_patient_name"],
                "given": [],
                "prefix": [],
                "suffix": [],
                # "period":[
                #     {
                #         "start": "",
                #         # "end": rec["patient_name_period_end"]
                #     }
                # ]

                    "start": rec["start"],


                # "end": rec["patient_name_period_end"]


            }]


            for inp_given in rec["given_name_text_patient_name"]:
                for key in values_for_patient_name[0]:

                    if key == "given":
                        values_for_patient_name[0]["given"].append((0, 0, {"given_name_text": inp_given
                                                                           }))

            for inp_prefix in rec["prefix_name_patient_name"]:
                for key in values_for_patient_name[0]:

                    if key == "prefix":
                        values_for_patient_name[0]["prefix"].append(
                            (0, 0, {"prefix_name": inp_prefix,
                                    }))

            for inp_suffix in rec["suffix_name_patient_name"]:
                for key in values_for_patient_name[0]:

                    if key == "suffix":
                        values_for_patient_name[0]["suffix"].append((0, 0, {"suffix_name": inp_suffix
                                                                           }))



            for values in values_for_patient_name:
                new_patient_name = request.env['human.name'].sudo().create(values)

            # CODE_FOR_PATIENT_CONTACT_NAME

            # values_for_patient_contact_name = [{
            #     "use": rec["use_patient_contact_name"],
            #     "text": rec["text_patient_contact_name"],
            #     "family": rec["family_patient_contact_name"],
            #     "given": [],
            #     "prefix": [],
            #     "suffix": [],
            #     "start": rec["period_start_patient_contact_name"],
            #     "end": rec["period_end_patient_contact_name"]
            #
            # }]
            #
            # for inp_given in rec["given_name_text_patient_contact_name"]:
            #     for key in values_for_patient_contact_name[0]:
            #
            #         if key == "given":
            #             values_for_patient_contact_name[0]["given"].append((0, 0, {"given_name_text": inp_given
            #                                                                }))
            #
            # for inp_prefix in rec["prefix_name_patient_contact_name"]:
            #     for key in values_for_patient_contact_name[0]:
            #
            #         if key == "prefix":
            #             values_for_patient_contact_name[0]["prefix"].append(
            #                 (0, 0, {"prefix_name": inp_prefix,
            #                         }))
            #
            # for inp_suffix in rec["suffix_name_patient_contact_name"]:
            #     for key in values_for_patient_contact_name[0]:
            #
            #         if key == "suffix":
            #             values_for_patient_contact_name[0]["suffix"].append((0, 0, {"suffix_name": inp_suffix
            #                                                                }))
            #
            #
            # for values in values_for_patient_contact_name:
            #     new_patient_contact_name = request.env['human.name'].sudo().create(values)
            #
            # #CODE_FOR_PATIENT_ADDRESS
            #
            # values_for_patient_address=[{
            #     "use":rec["use_patient_address"],
            #     "type":rec["type_patient_address"],
            #     "text":rec["text_patient_address"],
            #     "country":rec["country_patient_address"],
            #     "state":rec["state_patient_address"],
            #     "city":rec["city_patient_address"],
            #     "postalCode":rec["postal_code_patient_address"],
            #     "start":rec["period_start_patient_address"],
            #     "end":rec["period_end_patient_address"],
            #     "line":[(0, 0, {"lines": rec["lines_for_patient_address"]
            #                           })]
            # }]
            #
            # for inp_address_line in rec["lines_for_patient_address"]:
            #     for key in values_for_patient_address[0]:
            #
            #         if key == "line":
            #             values_for_patient_address[0]["line"].append((0, 0, {"lines": inp_address_line
            #                                                                }))
            #
            #
            # for values in values_for_patient_address:
            #     new_patient_address = request.env['address.fhir'].sudo().create(values)
            #
            # #CODE_FOR_PATIENT_CONTACT_ADDRESS
            #
            # values_for_patient_contact_address=[{
            #     "use": rec["use_patient_contact_address"],
            #     "type": rec["type_patient_contact_address"],
            #     "text": rec["text_patient_contact_address"],
            #     "country": rec["country_patient_contact_address"],
            #     "state": rec["state_patient_contact_address"],
            #     "city": rec["city_patient_contact_address"],
            #     "postalCode": rec["postal_code_patient_contact_address"],
            #     "start": rec["period_start_patient_contact_address"],
            #     "end": rec["period_end_patient_contact_address"],
            #     "line": [(0, 0, {"lines": rec["lines_for_patient_contact_address"]
            #                                  })]
            #
            # }]
            #
            # for inp_address_line in rec["lines_for_patient_address"]:
            #     for key in values_for_patient_address[0]:
            #
            #         if key == "line":
            #             values_for_patient_address[0]["line"].append((0, 0, {"lines": inp_address_line
            #                                                                  }))
            #
            #
            #
            # for values in values_for_patient_contact_address:
            #     new_patient_contact_address = request.env['address.fhir'].sudo().create(values)
            #
            # # #CODE_FOR_patient_contact
            #
            # values_for_patient_contact=[{
            #     "use":rec["use_patient_contact"],
            #     "system":rec["system_patient_contact"],
            #     "value":rec["value_patient_contact"],
            #     "start":rec["telecom_period_start_patient_contact"],
            #     "end":rec["telecom_period_end_patient_contact"]
            #
            # }]
            #
            # for values in values_for_patient_contact:
            #     new_patient_contact = request.env['contact.point'].sudo().create(values)
            #
            # # #CODE_FOR_patient_contact_telecom
            #
            # values_for_patient_contact_telecom = [{
            #         "use": rec["use_patient_contact"],
            #         "system": rec["system_patient_contact"],
            #         "value": rec["value_patient_contact"],
            #         "start": rec["telecom_period_start_patient_contact"],
            #         "end": rec["telecom_period_end_patient_contact"]
            #
            # }]
            #
            # for values in values_for_patient_contact_telecom:
            #     new_patient_contact_telecom = request.env['contact.point'].sudo().create(values)

            # CODE_for_PATIENT
            values_for_patient = {
                # "patient_identifier":'identifier'+str(new_patient_identifier.id),

                    "patient_name": 'human.name,' + str(new_patient_name.id),


                # "patient_address":"address.fhir,"+ str(new_patient_address.id),
                # "patient_contact":'contact.point'+str(new_patient_contact.id),
                # 'patient_active': rec['patient_active'],
                # 'patient_gender': rec['patient_gender'],
                # "patient_birthDate":rec["patient_birthDate"],
                # "is_deceased":rec["is_deceased"],
                # "deceased_date":rec["deceased_date"],
                # "marital_status_patient":rec["marital_status_patient"],
                # "patient_is_partOf_multiple_birth":rec["patient_is_partOf_multiple_birth"],
                # "patient_multiple_birth_order":rec["patient_multiple_birth_order"],
                "patient_communication":rec["patient_communication"],
                #

                # "patient_contact_name": 'human.name,' + str(new_patient_contact_name.id),
                # "patient_contact_address":"address.fhir,"+ str(new_patient_contact_address.id),
                # "patient_contact_telecom":'contact.point'+str(new_patient_contact_telecom.id),
                # "patient_contact_gender":rec["patient_contact_gender"]

            }

            new_patient = request.env['patient'].sudo().create(values_for_patient)

            args = {'success': True, 'message': 'Success', 'id': new_patient.id}

            return args
