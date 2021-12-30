
from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class Patient(http.Controller):

    @http.route('/get_patients', type='json', auth='user')
    def get_patients(self, **kws):
        patients_rec = request.env['patient'].sudo().search([])
        patients = []

        for rec in patients_rec:
            vals = {
                'identifer': [
                    {
                        "use": rec.patient_identifier.use,
                        "value": rec.patient_identifier.value,
                        "period":
                            {
                                "start": rec.patient_identifier.start,
                                "end": rec.patient_identifier.end,
                            },
                        "assigner": [
                            {
                            "assignerName": rec.patient_identifier.assigner.organization_name
                        }
                        ]
                    }
                ],
                'active': rec.patient_active,

                'name': [
                    {
                        'use': rec.patient_name.use,
                        'prefix': "",
                        'text': rec.patient_name.text,
                        'family': rec.patient_name.family,
                        "given": "",
                        'suffix': "",
                        "period": {
                            "start": rec.patient_name.start,
                            "end": rec.patient_name.end
                        }
                    },

                ],

                'telecom': [{
                    'use': rec.patient_contact.use,
                },
                    {
                        "system": rec.patient_contact.system,
                        "value": rec.patient_contact.value,
                        "rank": rec.patient_contact.rank,
                        "period": {
                            "start": rec.patient_contact.start,
                            "end": rec.patient_contact.end
                        }
                    }
                ],

                "address": [
                    {
                        "use": rec.patient_address.use,
                        "type": rec.patient_address.type,
                        "text": rec.patient_address.text,
                        "line": "",
                        "country": rec.patient_address.country.name,
                        "state": rec.patient_address.state.name,
                        "district": rec.patient_address.district,
                        "city": rec.patient_address.city,
                        "postalCode": rec.patient_address.postalCode,
                        "period": {
                            "start": rec.patient_address.start,
                            "end": rec.patient_address.end,
                        }
                    }
                ],

                'gender': rec.patient_gender,
                'birthdate': rec.patient_birthDate,
                "deceasedBoolean": rec.is_deceased,

                "martialStatus": rec.marital_status_patient,

                "contact": [
                    {
                        'name': [
                            {
                                # 'use': rec.patient_contact_name.use,
                                'prefix': "",
                                'text': rec.patient_contact_name.text,
                                'family': rec.patient_contact_name.family,
                                'given': "",
                                'suffix': "",
                                "period": {
                                    "start": rec.patient_contact_name.start,
                                    "end": rec.patient_contact_name.end,
                                }

                            }
                        ],

                        'telecom': [{
                            # 'use': rec.patient_contact_telecom.use,
                        },
                            {
                                "system": rec.patient_contact_telecom.system,
                                "value": rec.patient_contact_telecom.value,
                                "rank": rec.patient_contact_telecom.rank,
                                "period": {
                                    "start": rec.patient_contact_telecom.start,
                                    "end": rec.patient_contact_telecom.end
                                }
                            },
                        ],

                        "address": [
                            {
                                "use": rec.patient_contact_address.use,
                                "type": rec.patient_contact_address.type,
                                "text": rec.patient_contact_address.text,
                                "line": "",
                                "country": rec.patient_contact_address.country.name,
                                "state": rec.patient_contact_address.state.name,
                                "district": rec.patient_contact_address.district,
                                "city": rec.patient_contact_address.city,
                                "postalCode": rec.patient_contact_address.postalCode,
                                "period": {
                                    "start": rec.patient_contact_address.start,
                                    "end": rec.patient_contact_address.end,
                                }
                            }
                        ],
                        "managingorganzation": [
                            {
                                "name": rec.patient_contact_organization.organization_name
                            }
                        ],
                        # "period": [
                        #     {
                        #         "start": rec.start,
                        #         "end": rec.end,
                        #     }
                        # ]

                    }
                ],
                "communication": [{
                    "language": rec.patient_communication.name,

                }]

            }
        random = request.env['human.name'].sudo().search([])
        random1 = request.env['address.fhir'].sudo().search([])
        # CODE_FOR_HUMAN_NAME_GIVEN
        cat1 = []
        cat2 = []

        for rec in patients_rec.patient_name.given:
            cat1.append(rec.given_name_text)

        for rec in patients_rec.patient_contact_name.given:
            cat2.append(rec.given_name_text)

        for key in vals["name"][0]:

            if key == "given":
                vals["name"][0].update({"given": cat1})
        for key in vals["contact"][0]["name"][0]:

            if key == "given":
                vals["contact"][0]["name"][0].update({"given": cat2})
        # CODE_FOR_HUMAN_NAME_SUFFIX
        cat3 = []
        cat4 = []

        for rec in patients_rec.patient_name.suffix:
            cat3.append(rec.suffix_name)

        for rec in patients_rec.patient_contact_name.suffix:
            cat4.append(rec.suffix_name)

        for key in vals["name"][0]:

            if key == "suffix":
                vals["name"][0].update({"suffix": cat3})
        for key in vals["contact"][0]["name"][0]:

            if key == "suffix":
                vals["contact"][0]["name"][0].update({"suffix": cat4})
        # CODE_FOR_HUMAN_NAME_PREFIX
        cat5 = []
        cat6 = []

        for rec in patients_rec.patient_name.prefix:
            cat5.append(rec.prefix_name)

        for rec in patients_rec.patient_name.prefix:
            cat6.append(rec.prefix_name)

        for key in vals["name"][0]:

            if key == "prefix":
                vals["name"][0].update({"prefix": cat5})
        for key in vals["contact"][0]["name"][0]:

            if key == "prefix":
                vals["contact"][0]["name"][0].update({"prefix": cat6})

        # CODE_FOR_ADDRESS_LINE

        cat7 = []
        cat8 = []

        for rec in patients_rec.patient_address.line:
            cat7.append(rec.lines)

        for rec in patients_rec.patient_contact_address.line:
            cat8.append(rec.lines)

        for key in vals["address"][0]:

            if key == "line":
                vals["address"][0].update({"line": cat7})
        for key in vals["contact"][0]["address"][0]:

            if key == "line":
                vals["contact"][0]["address"][0].update({"line": cat8})

        patients.append(vals)

        data = {'status': 200, 'response': patients}
        return data
