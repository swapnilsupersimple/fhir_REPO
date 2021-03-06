# -*- coding: utf-8 -*-
{
    'name': "FHIR",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
            'views/patient.xml',
        # 'data/appointment.service.category.csv',

        'Diagnostic_codeable_concept/diagnostic.report.category.csv',
        'Diagnostic_codeable_concept/diagnostic.report.code.csv',
        'Diagnostic_codeable_concept/diagnostic.report.conclusion.code.csv',
        # 'data/appointment.cancelation.reason.csv',
        # 'data/appointment.participant.type.csv',
        'Encounter_codeable_concept/encounter.type.csv',
        'Encounter_codeable_concept/encounter.service.type.csv',
        'Encounter_codeable_concept/encounter.priority.csv',
        'Encounter_codeable_concept/encounter.participant.type.csv',
        'Encounter_codeable_concept/encounter.hospitalization.admit.source.csv',
        'Encounter_codeable_concept/encounter.hospitalization.diet.preference.csv',
        'Encounter_codeable_concept/encounter.hospitalization.special.courtesy.csv',
        'Encounter_codeable_concept/encounter.hospitalization.special.arrangement.csv',
        'Encounter_codeable_concept/encounter.hospitalization.discharge.disposition.csv',
        'Encounter_codeable_concept/encounter.location.physical.type.csv',
        # 'Task_codeable_concept/task.code.csv',
        # 'Task_codeable_concept/task.performer.type.csv',
        'Endpoint_codeable_concept/endpoint.payload.type.csv',
        'Media_codeable_concept/media.type.csv',
        'Media_codeable_concept/media.modality.csv',
        'Media_codeable_concept/media.view.csv',
        'Media_codeable_concept/media.reason.code.csv',
        'Media_codeable_concept/media.body.site.csv',
        # 'DocumentReference_codeable_concept/document.reference.type.csv',
        # 'DocumentReference_codeable_concept/document.reference.category.csv',
        # 'DocumentReference_codeable_concept/document.reference.security.label.csv',
        # 'DocumentReference_codeable_concept/document.reference.context.event.csv',
        # 'DocumentReference_codeable_concept/document.reference.context.facility.type.csv',
        # 'DocumentReference_codeable_concept/document.reference.context.practice.setting.csv',
        # 'EpisodeOfCareType_codeable_type/episode.of.care.type.csv',
        # 'EpisodeOfCareType_codeable_type/episode.of.care.diagnosis.role.csv',
        # 'Procedure_codeable_concept/procedure.status.reason.csv',
        # 'Procedure_codeable_concept/procedure.category.csv',
        # 'Procedure_codeable_concept/procedure.code.csv',
        # 'Procedure_codeable_concept/procedure.performer.function.csv',
        # 'Procedure_codeable_concept/procedure.reason.code.csv',
        # 'Procedure_codeable_concept/procedure.body.site.csv',
        # 'Procedure_codeable_concept/procedure.outcome.csv',
        # 'Procedure_codeable_concept/procedure.complication.csv',
        # 'Procedure_codeable_concept/procedure.follow.up.csv',
        # 'Procedure_codeable_concept/procedure.focal.device.action.csv',
        # 'Procedure_codeable_concept/procedure.used.code.csv',
        'Observation_codeabale_concept/observation.category.csv',
        'Observation_codeabale_concept/observation.code.csv',
        'Observation_codeabale_concept/observation.data.absent.reason.csv',
        'Observation_codeabale_concept/observation.interpretation.csv',
        'Observation_codeabale_concept/observation.body.site.csv',
        'Observation_codeabale_concept/observation.method.csv',
        'Observation_codeabale_concept/observation.reference.range.type.csv',
        'Observation_codeabale_concept/observation.reference.range.appliesto.csv',
        'Observation_codeabale_concept/observation.component.code.csv',
        'Specimen_codeable_concept/specimen.type.csv',
        'Specimen_codeable_concept/specimen.collection.method.csv',
        'Specimen_codeable_concept/specimen.collection.body.site.csv',
        'Specimen_codeable_concept/specimen.collection.fasting.status.csv',
        'Specimen_codeable_concept/specimen.processing.procedure.csv',
        'Specimen_codeable_concept/specimen.container.type.csv',
        'Specimen_codeable_concept/specimen.container.additive.csv',
        'Specimen_codeable_concept/specimen.condition.csv',
        # 'ServiceRequest_codeable_concept/service.request.category.csv',
        # 'ServiceRequest_codeable_concept/service.request.code.csv',
        # 'ServiceRequest_codeable_concept/service.request.order.detail.csv',
        # 'ServiceRequest_codeable_concept/service.request.body.site.csv',
        # 'ServiceRequest_codeable_concept/service.request.reason.code.csv',
        # 'ServiceRequest_codeable_concept/service.request.location.code.csv',
        'ImagingStudy_codeable_concept/imaging.study.series.body.site.csv',
        'ImagingStudy_codeable_concept/imaging.study.series.laterality.csv',
        # # 'DeviceMetric_codeabale_cocept/device.metric.type.csv',
        # 'Medication_codeable_concept/medication.code.csv',
        # 'Substance_codebale_concept/substance.category.csv',
        # 'Substance_codebale_concept/substance.code.csv',

        # 'data/appointment.service.type.csv',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',`
        'views/organization_fhir.xml',
        # 'views/practitioner_fhir.xml',
        # 'views/practitioner_role_fhir.xml',
        # 'views/care_team_fhir.xml',
        # 'views/device_fhir.xml',
        # 'views/related_person.xml',
        # 'views/location_fhir.xml',
        # 'views/group_fhir.xml',
        # 'views/condition_fhir.xml',
        # 'views/appointment_fhir.xml',
        # 'views/slot_fhir.xml',
        # 'views/appointment_response_fhir.xml',
        # 'views/care_plan_fhir.xml',
        'views/encounter_fhir.xml',
        # 'views/task_fhir.xml',
        'views/endpoint_fhir.xml',
        'views/media_fhir.xml',
        # 'views/document_reference_fhir.xml',
        # 'views/episode_of_care_fhir.xml',
        'views/procedure_fhir.xml',
        'views/observation_fhir.xml',
        'views/specimen_fhir.xml',
        'views/diagnostic_report_fhir.xml',
        # 'views/service_request_fhir.xml',
        'views/imaging_study_fhir.xml',
        'views/annotation.xml',
        'views/identifier_fhir.xml',
        # 'views/device_metric_fhir.xml',
        # 'views/medication_fhir.xml',
        # 'views/substance_fhir.xml',
        # 'views/medication_request_fhir.xml',

        # 'views/human_name.xml',
        'views/attachment.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
}
