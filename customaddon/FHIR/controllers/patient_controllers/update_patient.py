from odoo import http
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class Patient(http.Controller):

    @http.route('/update_patient', type='json', auth='user')
    def update_patient(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                human_name=request.env['human.name'].sudo().search([('id', '=', rec['id'])])

            if rec['id']:
                contact_point = request.env['contact.point'].sudo().search([('id', '=', rec['id'])])

            if [id('human.name')==id('contact.point')]:
                    if rec["text"]:
                        human_name=request.env['human.name'].sudo().search([('text', '=', rec['text'])])
                        if human_name:
                            human_name.sudo().write(rec)



            args = {'success': True, 'message': 'Patient Updated'}
        return args

        # # patient = request.env['patient'].sudo().search([('id', '=', rec['id'])])
        # human_name = request.env['human.name'].sudo().search([('id', '=', rec['id'])])
        #
        # # address=request.env['address.fhir'].sudo().search([('id', '=', rec['id'])])
        # contact_point = request.env['contact.point'].sudo().search([('id', '=', rec['id'])])
        # # if patient:
        # #     patient.sudo().write(rec)
        # if human_name:
        #     human_name.sudo().write(rec)
        # # if address:
        # #     address.sudo().write(rec)
        # if contact_point:
        #     contact_point.sudo().write(rec)