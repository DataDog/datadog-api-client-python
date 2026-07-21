# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.incidents_response import IncidentsResponse
from datadog_api_client.v2.model.incident_related_object import IncidentRelatedObject
from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
from datadog_api_client.v2.model.incident_response import IncidentResponse
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequest
from datadog_api_client.v2.model.incident_handles_response import IncidentHandlesResponse
from datadog_api_client.v2.model.incident_handle_response import IncidentHandleResponse
from datadog_api_client.v2.model.incident_handle_request import IncidentHandleRequest
from datadog_api_client.v2.model.global_incident_settings_response import GlobalIncidentSettingsResponse
from datadog_api_client.v2.model.global_incident_settings_request import GlobalIncidentSettingsRequest
from datadog_api_client.v2.model.incident_google_chat_configuration_response import (
    IncidentGoogleChatConfigurationResponse,
)
from datadog_api_client.v2.model.incident_google_chat_configuration_request import (
    IncidentGoogleChatConfigurationRequest,
)
from datadog_api_client.v2.model.incident_google_chat_configuration_patch_request import (
    IncidentGoogleChatConfigurationPatchRequest,
)
from datadog_api_client.v2.model.incident_google_meet_configuration_response import (
    IncidentGoogleMeetConfigurationResponse,
)
from datadog_api_client.v2.model.incident_google_meet_configuration_request import (
    IncidentGoogleMeetConfigurationRequest,
)
from datadog_api_client.v2.model.incident_google_meet_configuration_patch_request import (
    IncidentGoogleMeetConfigurationPatchRequest,
)
from datadog_api_client.v2.model.incident_impact_fields_response import IncidentImpactFieldsResponse
from datadog_api_client.v2.model.incident_impact_field_response import IncidentImpactFieldResponse
from datadog_api_client.v2.model.incident_impact_field_request import IncidentImpactFieldRequest
from datadog_api_client.v2.model.incident_notification_rule_array import IncidentNotificationRuleArray
from datadog_api_client.v2.model.incident_notification_rule import IncidentNotificationRule
from datadog_api_client.v2.model.create_incident_notification_rule_request import CreateIncidentNotificationRuleRequest
from datadog_api_client.v2.model.put_incident_notification_rule_request import PutIncidentNotificationRuleRequest
from datadog_api_client.v2.model.incident_notification_template_array import IncidentNotificationTemplateArray
from datadog_api_client.v2.model.incident_notification_template import IncidentNotificationTemplate
from datadog_api_client.v2.model.create_incident_notification_template_request import (
    CreateIncidentNotificationTemplateRequest,
)
from datadog_api_client.v2.model.patch_incident_notification_template_request import (
    PatchIncidentNotificationTemplateRequest,
)
from datadog_api_client.v2.model.postmortem_templates_response import PostmortemTemplatesResponse
from datadog_api_client.v2.model.postmortem_template_response import PostmortemTemplateResponse
from datadog_api_client.v2.model.postmortem_template_request import PostmortemTemplateRequest
from datadog_api_client.v2.model.incident_rules_response import IncidentRulesResponse
from datadog_api_client.v2.model.incident_rule_response import IncidentRuleResponse
from datadog_api_client.v2.model.incident_rule_request import IncidentRuleRequest
from datadog_api_client.v2.model.incident_rule_patch_request import IncidentRulePatchRequest
from datadog_api_client.v2.model.incident_type_list_response import IncidentTypeListResponse
from datadog_api_client.v2.model.incident_type_response import IncidentTypeResponse
from datadog_api_client.v2.model.incident_type_create_request import IncidentTypeCreateRequest
from datadog_api_client.v2.model.incident_org_settings_list_response import IncidentOrgSettingsListResponse
from datadog_api_client.v2.model.incident_type_patch_request import IncidentTypePatchRequest
from datadog_api_client.v2.model.incident_org_settings_response import IncidentOrgSettingsResponse
from datadog_api_client.v2.model.incident_user_defined_field_list_response import IncidentUserDefinedFieldListResponse
from datadog_api_client.v2.model.incident_user_defined_field_response import IncidentUserDefinedFieldResponse
from datadog_api_client.v2.model.incident_user_defined_field_create_request import IncidentUserDefinedFieldCreateRequest
from datadog_api_client.v2.model.incident_user_defined_field_update_request import IncidentUserDefinedFieldUpdateRequest
from datadog_api_client.v2.model.incident_user_defined_roles_response import IncidentUserDefinedRolesResponse
from datadog_api_client.v2.model.incident_user_defined_role_response import IncidentUserDefinedRoleResponse
from datadog_api_client.v2.model.incident_user_defined_role_request import IncidentUserDefinedRoleRequest
from datadog_api_client.v2.model.incident_user_defined_role_patch_request import IncidentUserDefinedRolePatchRequest
from datadog_api_client.v2.model.incident_import_response import IncidentImportResponse
from datadog_api_client.v2.model.incident_import_related_object import IncidentImportRelatedObject
from datadog_api_client.v2.model.incident_import_request import IncidentImportRequest
from datadog_api_client.v2.model.incident_search_response import IncidentSearchResponse
from datadog_api_client.v2.model.incident_search_sort_order import IncidentSearchSortOrder
from datadog_api_client.v2.model.incident_search_response_incidents_data import IncidentSearchResponseIncidentsData
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.incident_ai_postmortem_response import IncidentAIPostmortemResponse
from datadog_api_client.v2.model.attachment_array import AttachmentArray
from datadog_api_client.v2.model.attachment import Attachment
from datadog_api_client.v2.model.create_attachment_request import CreateAttachmentRequest
from datadog_api_client.v2.model.postmortem_attachment_request import PostmortemAttachmentRequest
from datadog_api_client.v2.model.patch_attachment_request import PatchAttachmentRequest
from datadog_api_client.v2.model.incident_page_uuid_response import IncidentPageUUIDResponse
from datadog_api_client.v2.model.incident_create_page_from_incident_request import IncidentCreatePageFromIncidentRequest
from datadog_api_client.v2.model.incident_configuration_response import IncidentConfigurationResponse
from datadog_api_client.v2.model.incident_configuration_patch_request import IncidentConfigurationPatchRequest
from datadog_api_client.v2.model.incident_configuration_request import IncidentConfigurationRequest
from datadog_api_client.v2.model.incident_impacts_response import IncidentImpactsResponse
from datadog_api_client.v2.model.incident_impact_related_object import IncidentImpactRelatedObject
from datadog_api_client.v2.model.incident_impact_response import IncidentImpactResponse
from datadog_api_client.v2.model.incident_impact_create_request import IncidentImpactCreateRequest
from datadog_api_client.v2.model.incident_impact_patch_request import IncidentImpactPatchRequest
from datadog_api_client.v2.model.incident_create_on_call_page_request import IncidentCreateOnCallPageRequest
from datadog_api_client.v2.model.incident_integration_metadata_response import IncidentIntegrationMetadataResponse
from datadog_api_client.v2.model.incident_on_call_page_link_request import IncidentOnCallPageLinkRequest
from datadog_api_client.v2.model.incident_integration_metadata_list_response import (
    IncidentIntegrationMetadataListResponse,
)
from datadog_api_client.v2.model.incident_integration_metadata_create_request import (
    IncidentIntegrationMetadataCreateRequest,
)
from datadog_api_client.v2.model.incident_integration_metadata_patch_request import (
    IncidentIntegrationMetadataPatchRequest,
)
from datadog_api_client.v2.model.incident_todo_list_response import IncidentTodoListResponse
from datadog_api_client.v2.model.incident_todo_response import IncidentTodoResponse
from datadog_api_client.v2.model.incident_todo_create_request import IncidentTodoCreateRequest
from datadog_api_client.v2.model.incident_todo_patch_request import IncidentTodoPatchRequest
from datadog_api_client.v2.model.incident_responders_response import IncidentRespondersResponse
from datadog_api_client.v2.model.incident_responder_response import IncidentResponderResponse
from datadog_api_client.v2.model.incident_responder_request import IncidentResponderRequest
from datadog_api_client.v2.model.incident_service_now_record_request import IncidentServiceNowRecordRequest
from datadog_api_client.v2.model.incident_timestamp_overrides_response import IncidentTimestampOverridesResponse
from datadog_api_client.v2.model.incident_timestamp_override_response import IncidentTimestampOverrideResponse
from datadog_api_client.v2.model.incident_timestamp_override_request import IncidentTimestampOverrideRequest
from datadog_api_client.v2.model.incident_timestamp_override_patch_request import IncidentTimestampOverridePatchRequest


class IncidentsApi:
    """
    Manage incident response, as well as associated attachments, metadata, and todos. See the `Incident Management page <https://docs.datadoghq.com/service_management/incident_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_global_incident_handle_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/global/incident-handles",
                "operation_id": "create_global_incident_handle",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents",
                "operation_id": "create_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_attachment_endpoint = _Endpoint(
            settings={
                "response_type": (Attachment,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments",
                "operation_id": "create_incident_attachment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateAttachmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/configurations",
                "operation_id": "create_incident_configuration",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentConfigurationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_google_chat_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentGoogleChatConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/google-chat-configurations",
                "operation_id": "create_incident_google_chat_configuration",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentGoogleChatConfigurationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_google_meet_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentGoogleMeetConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/google-meet-configurations",
                "operation_id": "create_incident_google_meet_configuration",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentGoogleMeetConfigurationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_impact_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImpactResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/impacts",
                "operation_id": "create_incident_impact",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentImpactRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentImpactCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_impact_field_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImpactFieldResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/impact-fields",
                "operation_id": "create_incident_impact_field",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentImpactFieldRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_integration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentIntegrationMetadataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/integrations",
                "operation_id": "create_incident_integration",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentIntegrationMetadataCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationRule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-rules",
                "operation_id": "create_incident_notification_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateIncidentNotificationRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_notification_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationTemplate,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-templates",
                "operation_id": "create_incident_notification_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateIncidentNotificationTemplateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_postmortem_attachment_endpoint = _Endpoint(
            settings={
                "response_type": (Attachment,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments/postmortems",
                "operation_id": "create_incident_postmortem_attachment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PostmortemAttachmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_postmortem_template_endpoint = _Endpoint(
            settings={
                "response_type": (PostmortemTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/postmortem-templates",
                "operation_id": "create_incident_postmortem_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (PostmortemTemplateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_responder_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/responders",
                "operation_id": "create_incident_responder",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentResponderRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/rules",
                "operation_id": "create_incident_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_service_now_record_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentIntegrationMetadataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/servicenow-records",
                "operation_id": "create_incident_service_now_record",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentServiceNowRecordRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_todo_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTodoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/todos",
                "operation_id": "create_incident_todo",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTodoCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_type_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTypeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types",
                "operation_id": "create_incident_type",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTypeCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_user_defined_field_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedFieldResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-fields",
                "operation_id": "create_incident_user_defined_field",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUserDefinedFieldCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_user_defined_role_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedRoleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-roles",
                "operation_id": "create_incident_user_defined_role",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUserDefinedRoleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_on_call_page_from_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentPageUUIDResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/page",
                "operation_id": "create_on_call_page_from_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentCreateOnCallPageRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_page_from_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentPageUUIDResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/cases/page",
                "operation_id": "create_page_from_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentCreatePageFromIncidentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_timestamp_override_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimestampOverrideResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timestamp-overrides",
                "operation_id": "create_timestamp_override",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTimestampOverrideRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_global_incident_handle_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/global/incident-handles",
                "operation_id": "delete_global_incident_handle",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "delete_incident",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_attachment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments/{attachment_id}",
                "operation_id": "delete_incident_attachment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "attachment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "attachment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_impact_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/impacts/{impact_id}",
                "operation_id": "delete_incident_impact",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "impact_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "impact_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_impact_field_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/impact-fields/{field_id}",
                "operation_id": "delete_incident_impact_field",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "field_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "field_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_integration_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}",
                "operation_id": "delete_incident_integration",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "integration_metadata_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_metadata_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-rules/{id}",
                "operation_id": "delete_incident_notification_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_notification_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-templates/{id}",
                "operation_id": "delete_incident_notification_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_postmortem_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/postmortem-templates/{template_id}",
                "operation_id": "delete_incident_postmortem_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_responder_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/responders/{responder_id}",
                "operation_id": "delete_incident_responder",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "responder_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "responder_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/rules/{rule_id}",
                "operation_id": "delete_incident_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_todo_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}",
                "operation_id": "delete_incident_todo",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "todo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "todo_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_type_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types/{incident_type_id}",
                "operation_id": "delete_incident_type",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_user_defined_field_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-fields/{field_id}",
                "operation_id": "delete_incident_user_defined_field",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "field_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "field_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_user_defined_role_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-roles/{role_id}",
                "operation_id": "delete_incident_user_defined_role",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "role_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_timestamp_override_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timestamp-overrides/{id}",
                "operation_id": "delete_timestamp_override",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_global_incident_settings_endpoint = _Endpoint(
            settings={
                "response_type": (GlobalIncidentSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/global/settings",
                "operation_id": "get_global_incident_settings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "get_incident",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_ai_postmortem_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentAIPostmortemResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/ai/postmortem",
                "operation_id": "get_incident_ai_postmortem",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_integration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentIntegrationMetadataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}",
                "operation_id": "get_incident_integration",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "integration_metadata_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_metadata_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationRule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-rules/{id}",
                "operation_id": "get_incident_notification_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_notification_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationTemplate,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-templates/{id}",
                "operation_id": "get_incident_notification_template",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_postmortem_template_endpoint = _Endpoint(
            settings={
                "response_type": (PostmortemTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/postmortem-templates/{template_id}",
                "operation_id": "get_incident_postmortem_template",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_responder_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/responders/{responder_id}",
                "operation_id": "get_incident_responder",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "responder_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "responder_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/rules/{rule_id}",
                "operation_id": "get_incident_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_todo_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTodoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}",
                "operation_id": "get_incident_todo",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "todo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "todo_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_type_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTypeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types/{incident_type_id}",
                "operation_id": "get_incident_type",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_user_defined_field_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedFieldResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-fields/{field_id}",
                "operation_id": "get_incident_user_defined_field",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "field_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "field_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_user_defined_role_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedRoleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-roles/{role_id}",
                "operation_id": "get_incident_user_defined_role",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_org_settings_by_incident_type_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentOrgSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types/{incident_type_id}/org-settings",
                "operation_id": "get_org_settings_by_incident_type",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_type_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "incident_type_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._import_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/import",
                "operation_id": "import_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([IncidentImportRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentImportRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._link_page_to_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentIntegrationMetadataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/pages/link",
                "operation_id": "link_page_to_incident",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentOnCallPageLinkRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_global_incident_handles_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentHandlesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/global/incident-handles",
                "operation_id": "list_global_incident_handles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_attachments_endpoint = _Endpoint(
            settings={
                "response_type": (AttachmentArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments",
                "operation_id": "list_incident_attachments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "filter_attachment_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[attachment_type]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_impact_fields_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImpactFieldsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/impact-fields",
                "operation_id": "list_incident_impact_fields",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_impacts_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImpactsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/impacts",
                "operation_id": "list_incident_impacts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentImpactRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_integrations_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentIntegrationMetadataListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/integrations",
                "operation_id": "list_incident_integrations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_notification_rules_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationRuleArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-rules",
                "operation_id": "list_incident_notification_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_notification_templates_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationTemplateArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-templates",
                "operation_id": "list_incident_notification_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_incident_type": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[incident-type]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_postmortem_templates_endpoint = _Endpoint(
            settings={
                "response_type": (PostmortemTemplatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/postmortem-templates",
                "operation_id": "list_incident_postmortem_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_responders_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRespondersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/responders",
                "operation_id": "list_incident_responders",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_rules_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/rules",
                "operation_id": "list_incident_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_task_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[task_id]",
                    "location": "query",
                },
                "filter_trigger": {
                    "openapi_types": (str,),
                    "attribute": "filter[trigger]",
                    "location": "query",
                },
                "incident_type_uuid": {
                    "openapi_types": (UUID,),
                    "attribute": "incidentTypeUUID",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents",
                "operation_id": "list_incidents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_todos_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTodoListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/todos",
                "operation_id": "list_incident_todos",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_types_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTypeListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types",
                "operation_id": "list_incident_types",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "include_deleted",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_user_defined_fields_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedFieldListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-fields",
                "operation_id": "list_incident_user_defined_fields",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "include_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "include-deleted",
                    "location": "query",
                },
                "filter_incident_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[incident-type]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_user_defined_roles_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedRolesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-roles",
                "operation_id": "list_incident_user_defined_roles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_incident_type": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[incident-type]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_settings_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentOrgSettingsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types/org-settings",
                "operation_id": "list_org_settings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "include_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "include-deleted",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_timestamp_overrides_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimestampOverridesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timestamp-overrides",
                "operation_id": "list_timestamp_overrides",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._patch_incident_impact_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImpactResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/impacts/{impact_id}",
                "operation_id": "patch_incident_impact",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "impact_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "impact_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentImpactRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentImpactPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/search",
                "operation_id": "search_incidents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (IncidentRelatedObject,),
                    "attribute": "include",
                    "location": "query",
                },
                "query": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (IncidentSearchSortOrder,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_global_incident_handle_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentHandleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/global/incident-handles",
                "operation_id": "update_global_incident_handle",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentHandleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_global_incident_settings_endpoint = _Endpoint(
            settings={
                "response_type": (GlobalIncidentSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/global/settings",
                "operation_id": "update_global_incident_settings",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GlobalIncidentSettingsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}",
                "operation_id": "update_incident",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([IncidentRelatedObject],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_attachment_endpoint = _Endpoint(
            settings={
                "response_type": (Attachment,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/attachments/{attachment_id}",
                "operation_id": "update_incident_attachment",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "attachment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "attachment_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchAttachmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/configurations",
                "operation_id": "update_incident_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentConfigurationPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_google_chat_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentGoogleChatConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/google-chat-configurations/{id}",
                "operation_id": "update_incident_google_chat_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentGoogleChatConfigurationPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_google_meet_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentGoogleMeetConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/google-meet-configurations/{id}",
                "operation_id": "update_incident_google_meet_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentGoogleMeetConfigurationPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_impact_field_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentImpactFieldResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/impact-fields/{field_id}",
                "operation_id": "update_incident_impact_field",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "field_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "field_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentImpactFieldRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_integration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentIntegrationMetadataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/integrations/{integration_metadata_id}",
                "operation_id": "update_incident_integration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "integration_metadata_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_metadata_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentIntegrationMetadataPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationRule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-rules/{id}",
                "operation_id": "update_incident_notification_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PutIncidentNotificationRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_notification_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationTemplate,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-templates/{id}",
                "operation_id": "update_incident_notification_template",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchIncidentNotificationTemplateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_postmortem_template_endpoint = _Endpoint(
            settings={
                "response_type": (PostmortemTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/incidents/config/postmortem-templates/{template_id}",
                "operation_id": "update_incident_postmortem_template",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PostmortemTemplateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/rules/{rule_id}",
                "operation_id": "update_incident_rule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentRulePatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_todo_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTodoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/relationships/todos/{todo_id}",
                "operation_id": "update_incident_todo",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "todo_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "todo_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTodoPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_type_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTypeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/types/{incident_type_id}",
                "operation_id": "update_incident_type",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_type_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTypePatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_user_defined_field_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedFieldResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-fields/{field_id}",
                "operation_id": "update_incident_user_defined_field",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "field_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "field_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUserDefinedFieldUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_user_defined_role_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentUserDefinedRoleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/user-defined-roles/{role_id}",
                "operation_id": "update_incident_user_defined_role",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "role_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentUserDefinedRolePatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_timestamp_override_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimestampOverrideResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timestamp-overrides/{id}",
                "operation_id": "update_timestamp_override",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTimestampOverridePatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_global_incident_handle(
        self,
        body: IncidentHandleRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentHandleResponse:
        """Create global incident handle.

        Create a new global incident handle.

        :type body: IncidentHandleRequest
        :param include: Comma-separated list of related resources to include in the response
        :type include: str, optional
        :rtype: IncidentHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_global_incident_handle_endpoint.call_with_http_info(**kwargs)

    def create_incident(
        self,
        body: IncidentCreateRequest,
    ) -> IncidentResponse:
        """Create an incident.

        Create an incident.

        :param body: Incident payload.
        :type body: IncidentCreateRequest
        :rtype: IncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_endpoint.call_with_http_info(**kwargs)

    def create_incident_attachment(
        self,
        incident_id: str,
        body: CreateAttachmentRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Attachment:
        """Create incident attachment.

        Create an incident attachment.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: CreateAttachmentRequest
        :param include: Resource to include in the response. Supported value: ``last_modified_by_user``.
        :type include: str, optional
        :rtype: Attachment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_incident_attachment_endpoint.call_with_http_info(**kwargs)

    def create_incident_configuration(
        self,
        incident_id: str,
        body: IncidentConfigurationRequest,
    ) -> IncidentConfigurationResponse:
        """Create an incident configuration.

        Create a configuration for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident configuration payload.
        :type body: IncidentConfigurationRequest
        :rtype: IncidentConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_configuration_endpoint.call_with_http_info(**kwargs)

    def create_incident_google_chat_configuration(
        self,
        body: IncidentGoogleChatConfigurationRequest,
    ) -> IncidentGoogleChatConfigurationResponse:
        """Create an incident Google Chat configuration.

        Create a Google Chat configuration for incidents.

        :param body: Google Chat configuration payload.
        :type body: IncidentGoogleChatConfigurationRequest
        :rtype: IncidentGoogleChatConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_google_chat_configuration_endpoint.call_with_http_info(**kwargs)

    def create_incident_google_meet_configuration(
        self,
        body: IncidentGoogleMeetConfigurationRequest,
    ) -> IncidentGoogleMeetConfigurationResponse:
        """Create an incident Google Meet configuration.

        Create a Google Meet configuration for incidents.

        :param body: Google Meet configuration payload.
        :type body: IncidentGoogleMeetConfigurationRequest
        :rtype: IncidentGoogleMeetConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_google_meet_configuration_endpoint.call_with_http_info(**kwargs)

    def create_incident_impact(
        self,
        incident_id: str,
        body: IncidentImpactCreateRequest,
        *,
        include: Union[List[IncidentImpactRelatedObject], UnsetType] = unset,
    ) -> IncidentImpactResponse:
        """Create an incident impact.

        Create an impact for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident impact payload.
        :type body: IncidentImpactCreateRequest
        :param include: Specifies which related resources should be included in the response.
        :type include: [IncidentImpactRelatedObject], optional
        :rtype: IncidentImpactResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_incident_impact_endpoint.call_with_http_info(**kwargs)

    def create_incident_impact_field(
        self,
        body: IncidentImpactFieldRequest,
    ) -> IncidentImpactFieldResponse:
        """Create an incident impact field.

        Create an impact field for incidents.

        :param body: Impact field payload.
        :type body: IncidentImpactFieldRequest
        :rtype: IncidentImpactFieldResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_impact_field_endpoint.call_with_http_info(**kwargs)

    def create_incident_integration(
        self,
        incident_id: str,
        body: IncidentIntegrationMetadataCreateRequest,
    ) -> IncidentIntegrationMetadataResponse:
        """Create an incident integration metadata.

        Create an incident integration metadata.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident integration metadata payload.
        :type body: IncidentIntegrationMetadataCreateRequest
        :rtype: IncidentIntegrationMetadataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_integration_endpoint.call_with_http_info(**kwargs)

    def create_incident_notification_rule(
        self,
        body: CreateIncidentNotificationRuleRequest,
    ) -> IncidentNotificationRule:
        """Create an incident notification rule.

        Creates a new notification rule.

        :type body: CreateIncidentNotificationRuleRequest
        :rtype: IncidentNotificationRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_notification_rule_endpoint.call_with_http_info(**kwargs)

    def create_incident_notification_template(
        self,
        body: CreateIncidentNotificationTemplateRequest,
    ) -> IncidentNotificationTemplate:
        """Create incident notification template.

        Creates a new notification template.

        :type body: CreateIncidentNotificationTemplateRequest
        :rtype: IncidentNotificationTemplate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_notification_template_endpoint.call_with_http_info(**kwargs)

    def create_incident_postmortem_attachment(
        self,
        incident_id: str,
        body: PostmortemAttachmentRequest,
    ) -> Attachment:
        """Create postmortem attachment.

        Create a postmortem attachment for an incident.

        The endpoint accepts markdown for notebooks created in Confluence or Google Docs.
        Postmortems created from notebooks need to be formatted using frontend notebook cells,
        in addition to markdown format.

        :param incident_id: The ID of the incident
        :type incident_id: str
        :type body: PostmortemAttachmentRequest
        :rtype: Attachment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_postmortem_attachment_endpoint.call_with_http_info(**kwargs)

    def create_incident_postmortem_template(
        self,
        body: PostmortemTemplateRequest,
    ) -> PostmortemTemplateResponse:
        """Create postmortem template.

        Create a new postmortem template for incidents.

        :type body: PostmortemTemplateRequest
        :rtype: PostmortemTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_postmortem_template_endpoint.call_with_http_info(**kwargs)

    def create_incident_responder(
        self,
        incident_id: str,
        body: IncidentResponderRequest,
    ) -> IncidentResponderResponse:
        """Create an incident responder.

        Add a responder to an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident responder payload.
        :type body: IncidentResponderRequest
        :rtype: IncidentResponderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_responder_endpoint.call_with_http_info(**kwargs)

    def create_incident_rule(
        self,
        body: IncidentRuleRequest,
    ) -> IncidentRuleResponse:
        """Create an incident rule.

        Create an incident rule.

        :param body: Incident rule payload.
        :type body: IncidentRuleRequest
        :rtype: IncidentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_rule_endpoint.call_with_http_info(**kwargs)

    def create_incident_service_now_record(
        self,
        incident_id: str,
        body: IncidentServiceNowRecordRequest,
    ) -> IncidentIntegrationMetadataResponse:
        """Create an incident ServiceNow record.

        Create a ServiceNow record for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: ServiceNow record payload.
        :type body: IncidentServiceNowRecordRequest
        :rtype: IncidentIntegrationMetadataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_service_now_record_endpoint.call_with_http_info(**kwargs)

    def create_incident_todo(
        self,
        incident_id: str,
        body: IncidentTodoCreateRequest,
    ) -> IncidentTodoResponse:
        """Create an incident todo.

        Create an incident todo.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident todo payload.
        :type body: IncidentTodoCreateRequest
        :rtype: IncidentTodoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_todo_endpoint.call_with_http_info(**kwargs)

    def create_incident_type(
        self,
        body: IncidentTypeCreateRequest,
    ) -> IncidentTypeResponse:
        """Create an incident type.

        Create an incident type.

        :param body: Incident type payload.
        :type body: IncidentTypeCreateRequest
        :rtype: IncidentTypeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_type_endpoint.call_with_http_info(**kwargs)

    def create_incident_user_defined_field(
        self,
        body: IncidentUserDefinedFieldCreateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedFieldResponse:
        """Create an incident user-defined field.

        Create an incident user-defined field.

        :param body: Incident user-defined field payload.
        :type body: IncidentUserDefinedFieldCreateRequest
        :param include: Comma-separated list of related resources to include. Supported values are "last_modified_by_user", "created_by_user", and "incident_type".
        :type include: str, optional
        :rtype: IncidentUserDefinedFieldResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_incident_user_defined_field_endpoint.call_with_http_info(**kwargs)

    def create_incident_user_defined_role(
        self,
        body: IncidentUserDefinedRoleRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedRoleResponse:
        """Create an incident user-defined role.

        Create a new user-defined role for incidents.

        :type body: IncidentUserDefinedRoleRequest
        :param include: Comma-separated list of related resources to include in the response.
        :type include: str, optional
        :rtype: IncidentUserDefinedRoleResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_incident_user_defined_role_endpoint.call_with_http_info(**kwargs)

    def create_on_call_page_from_incident(
        self,
        incident_id: str,
        body: IncidentCreateOnCallPageRequest,
    ) -> IncidentPageUUIDResponse:
        """Create an on-call page from an incident.

        Create an on-call page directly from an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: On-call page creation payload.
        :type body: IncidentCreateOnCallPageRequest
        :rtype: IncidentPageUUIDResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_on_call_page_from_incident_endpoint.call_with_http_info(**kwargs)

    def create_page_from_incident(
        self,
        incident_id: str,
        body: IncidentCreatePageFromIncidentRequest,
    ) -> IncidentPageUUIDResponse:
        """Create a page from an incident.

        Create a page from an incident using the Cases service.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Page creation payload.
        :type body: IncidentCreatePageFromIncidentRequest
        :rtype: IncidentPageUUIDResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_page_from_incident_endpoint.call_with_http_info(**kwargs)

    def create_timestamp_override(
        self,
        incident_id: str,
        body: IncidentTimestampOverrideRequest,
    ) -> IncidentTimestampOverrideResponse:
        """Create an incident timestamp override.

        Create a timestamp override for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Timestamp override payload.
        :type body: IncidentTimestampOverrideRequest
        :rtype: IncidentTimestampOverrideResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_timestamp_override_endpoint.call_with_http_info(**kwargs)

    def delete_global_incident_handle(
        self,
    ) -> None:
        """Delete global incident handle.

        Delete a global incident handle.

        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        return self._delete_global_incident_handle_endpoint.call_with_http_info(**kwargs)

    def delete_incident(
        self,
        incident_id: str,
    ) -> None:
        """Delete an existing incident.

        Deletes an existing incident from the users organization.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._delete_incident_endpoint.call_with_http_info(**kwargs)

    def delete_incident_attachment(
        self,
        incident_id: str,
        attachment_id: str,
    ) -> None:
        """Delete incident attachment.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param attachment_id: The ID of the attachment.
        :type attachment_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["attachment_id"] = attachment_id

        return self._delete_incident_attachment_endpoint.call_with_http_info(**kwargs)

    def delete_incident_impact(
        self,
        incident_id: str,
        impact_id: str,
    ) -> None:
        """Delete an incident impact.

        Delete an incident impact.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param impact_id: The UUID of the incident impact.
        :type impact_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["impact_id"] = impact_id

        return self._delete_incident_impact_endpoint.call_with_http_info(**kwargs)

    def delete_incident_impact_field(
        self,
        field_id: UUID,
    ) -> None:
        """Delete an incident impact field.

        Delete an impact field for incidents.

        :param field_id: The UUID of the impact field.
        :type field_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["field_id"] = field_id

        return self._delete_incident_impact_field_endpoint.call_with_http_info(**kwargs)

    def delete_incident_integration(
        self,
        incident_id: str,
        integration_metadata_id: str,
    ) -> None:
        """Delete an incident integration metadata.

        Delete an incident integration metadata.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param integration_metadata_id: The UUID of the incident integration metadata.
        :type integration_metadata_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["integration_metadata_id"] = integration_metadata_id

        return self._delete_incident_integration_endpoint.call_with_http_info(**kwargs)

    def delete_incident_notification_rule(
        self,
        id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> None:
        """Delete an incident notification rule.

        Deletes a notification rule by its ID.

        :param id: The ID of the notification rule.
        :type id: UUID
        :param include: Comma-separated list of resources to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type`` , ``notification_template``
        :type include: str, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if include is not unset:
            kwargs["include"] = include

        return self._delete_incident_notification_rule_endpoint.call_with_http_info(**kwargs)

    def delete_incident_notification_template(
        self,
        id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> None:
        """Delete a notification template.

        Deletes a notification template by its ID.

        :param id: The ID of the notification template.
        :type id: UUID
        :param include: Comma-separated list of relationships to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type``
        :type include: str, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if include is not unset:
            kwargs["include"] = include

        return self._delete_incident_notification_template_endpoint.call_with_http_info(**kwargs)

    def delete_incident_postmortem_template(
        self,
        template_id: str,
    ) -> None:
        """Delete postmortem template.

        Delete a postmortem template.

        :param template_id: The ID of the postmortem template
        :type template_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._delete_incident_postmortem_template_endpoint.call_with_http_info(**kwargs)

    def delete_incident_responder(
        self,
        incident_id: str,
        responder_id: UUID,
    ) -> None:
        """Delete an incident responder.

        Remove a responder from an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param responder_id: The UUID of the incident responder.
        :type responder_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["responder_id"] = responder_id

        return self._delete_incident_responder_endpoint.call_with_http_info(**kwargs)

    def delete_incident_rule(
        self,
        rule_id: UUID,
    ) -> None:
        """Delete an incident rule.

        Delete an incident rule.

        :param rule_id: The UUID of the incident rule.
        :type rule_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_incident_rule_endpoint.call_with_http_info(**kwargs)

    def delete_incident_todo(
        self,
        incident_id: str,
        todo_id: str,
    ) -> None:
        """Delete an incident todo.

        Delete an incident todo.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param todo_id: The UUID of the incident todo.
        :type todo_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["todo_id"] = todo_id

        return self._delete_incident_todo_endpoint.call_with_http_info(**kwargs)

    def delete_incident_type(
        self,
        incident_type_id: str,
    ) -> None:
        """Delete an incident type.

        Delete an incident type.

        :param incident_type_id: The UUID of the incident type.
        :type incident_type_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_type_id"] = incident_type_id

        return self._delete_incident_type_endpoint.call_with_http_info(**kwargs)

    def delete_incident_user_defined_field(
        self,
        field_id: str,
    ) -> None:
        """Delete an incident user-defined field.

        Delete an incident user-defined field.

        :param field_id: The ID of the incident user-defined field.
        :type field_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["field_id"] = field_id

        return self._delete_incident_user_defined_field_endpoint.call_with_http_info(**kwargs)

    def delete_incident_user_defined_role(
        self,
        role_id: UUID,
    ) -> None:
        """Delete an incident user-defined role.

        Delete an existing user-defined role for incidents.

        :param role_id: The UUID of the incident user-defined role.
        :type role_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_id"] = role_id

        return self._delete_incident_user_defined_role_endpoint.call_with_http_info(**kwargs)

    def delete_timestamp_override(
        self,
        incident_id: str,
        id: UUID,
    ) -> None:
        """Delete an incident timestamp override.

        Delete a timestamp override for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param id: The UUID of the timestamp override.
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["id"] = id

        return self._delete_timestamp_override_endpoint.call_with_http_info(**kwargs)

    def get_global_incident_settings(
        self,
    ) -> GlobalIncidentSettingsResponse:
        """Get global incident settings.

        Retrieve global incident settings for the organization.

        :rtype: GlobalIncidentSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_global_incident_settings_endpoint.call_with_http_info(**kwargs)

    def get_incident(
        self,
        incident_id: str,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
    ) -> IncidentResponse:
        """Get the details of an incident.

        Get the details of an incident by ``incident_id``.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :rtype: IncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_endpoint.call_with_http_info(**kwargs)

    def get_incident_ai_postmortem(
        self,
        incident_id: str,
    ) -> IncidentAIPostmortemResponse:
        """Get an AI-generated incident postmortem.

        Generate an AI postmortem for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentAIPostmortemResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._get_incident_ai_postmortem_endpoint.call_with_http_info(**kwargs)

    def get_incident_integration(
        self,
        incident_id: str,
        integration_metadata_id: str,
    ) -> IncidentIntegrationMetadataResponse:
        """Get incident integration metadata details.

        Get incident integration metadata details.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param integration_metadata_id: The UUID of the incident integration metadata.
        :type integration_metadata_id: str
        :rtype: IncidentIntegrationMetadataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["integration_metadata_id"] = integration_metadata_id

        return self._get_incident_integration_endpoint.call_with_http_info(**kwargs)

    def get_incident_notification_rule(
        self,
        id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationRule:
        """Get an incident notification rule.

        Retrieves a specific notification rule by its ID.

        :param id: The ID of the notification rule.
        :type id: UUID
        :param include: Comma-separated list of resources to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type`` , ``notification_template``
        :type include: str, optional
        :rtype: IncidentNotificationRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_notification_rule_endpoint.call_with_http_info(**kwargs)

    def get_incident_notification_template(
        self,
        id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationTemplate:
        """Get incident notification template.

        Retrieves a specific notification template by its ID.

        :param id: The ID of the notification template.
        :type id: UUID
        :param include: Comma-separated list of relationships to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type``
        :type include: str, optional
        :rtype: IncidentNotificationTemplate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_notification_template_endpoint.call_with_http_info(**kwargs)

    def get_incident_postmortem_template(
        self,
        template_id: str,
    ) -> PostmortemTemplateResponse:
        """Get postmortem template.

        Retrieve details of a specific postmortem template.

        :param template_id: The ID of the postmortem template
        :type template_id: str
        :rtype: PostmortemTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._get_incident_postmortem_template_endpoint.call_with_http_info(**kwargs)

    def get_incident_responder(
        self,
        incident_id: str,
        responder_id: UUID,
    ) -> IncidentResponderResponse:
        """Get an incident responder.

        Get a single responder for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param responder_id: The UUID of the incident responder.
        :type responder_id: UUID
        :rtype: IncidentResponderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["responder_id"] = responder_id

        return self._get_incident_responder_endpoint.call_with_http_info(**kwargs)

    def get_incident_rule(
        self,
        rule_id: UUID,
    ) -> IncidentRuleResponse:
        """Get an incident rule.

        Get a single incident rule by ID.

        :param rule_id: The UUID of the incident rule.
        :type rule_id: UUID
        :rtype: IncidentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_incident_rule_endpoint.call_with_http_info(**kwargs)

    def get_incident_todo(
        self,
        incident_id: str,
        todo_id: str,
    ) -> IncidentTodoResponse:
        """Get incident todo details.

        Get incident todo details.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param todo_id: The UUID of the incident todo.
        :type todo_id: str
        :rtype: IncidentTodoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["todo_id"] = todo_id

        return self._get_incident_todo_endpoint.call_with_http_info(**kwargs)

    def get_incident_type(
        self,
        incident_type_id: str,
    ) -> IncidentTypeResponse:
        """Get incident type details.

        Get incident type details.

        :param incident_type_id: The UUID of the incident type.
        :type incident_type_id: str
        :rtype: IncidentTypeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_type_id"] = incident_type_id

        return self._get_incident_type_endpoint.call_with_http_info(**kwargs)

    def get_incident_user_defined_field(
        self,
        field_id: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedFieldResponse:
        """Get an incident user-defined field.

        Get details of an incident user-defined field.

        :param field_id: The ID of the incident user-defined field.
        :type field_id: str
        :param include: Comma-separated list of related resources to include. Supported values are "last_modified_by_user", "created_by_user", and "incident_type".
        :type include: str, optional
        :rtype: IncidentUserDefinedFieldResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["field_id"] = field_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_user_defined_field_endpoint.call_with_http_info(**kwargs)

    def get_incident_user_defined_role(
        self,
        role_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedRoleResponse:
        """Get an incident user-defined role.

        Retrieve a single user-defined role for incidents.

        :param role_id: The UUID of the incident user-defined role.
        :type role_id: UUID
        :param include: Comma-separated list of related resources to include in the response.
        :type include: str, optional
        :rtype: IncidentUserDefinedRoleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_id"] = role_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_user_defined_role_endpoint.call_with_http_info(**kwargs)

    def get_org_settings_by_incident_type(
        self,
        incident_type_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentOrgSettingsResponse:
        """Get org settings by incident type.

        Get the org settings for a specific incident type.

        :param incident_type_id: The UUID of the incident type.
        :type incident_type_id: UUID
        :param include: Comma-separated list of related resources to include in the response.
        :type include: str, optional
        :rtype: IncidentOrgSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_type_id"] = incident_type_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_org_settings_by_incident_type_endpoint.call_with_http_info(**kwargs)

    def import_incident(
        self,
        body: IncidentImportRequest,
        *,
        include: Union[List[IncidentImportRelatedObject], UnsetType] = unset,
    ) -> IncidentImportResponse:
        """Import an incident.

        Import an incident from an external system. This endpoint allows you to create incidents with
        historical data such as custom timestamps for detection, declaration, and resolution.
        Imported incidents do not execute integrations or notification rules.

        :param body: Incident import payload.
        :type body: IncidentImportRequest
        :param include: Specifies which related object types to include in the response when importing an incident.
        :type include: [IncidentImportRelatedObject], optional
        :rtype: IncidentImportResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._import_incident_endpoint.call_with_http_info(**kwargs)

    def link_page_to_incident(
        self,
        incident_id: str,
        body: IncidentOnCallPageLinkRequest,
    ) -> IncidentIntegrationMetadataResponse:
        """Link a page to an incident.

        Link an existing on-call page to an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: On-call page link payload.
        :type body: IncidentOnCallPageLinkRequest
        :rtype: IncidentIntegrationMetadataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._link_page_to_incident_endpoint.call_with_http_info(**kwargs)

    def list_global_incident_handles(
        self,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentHandlesResponse:
        """List global incident handles.

        Retrieve a list of global incident handles.

        :param include: Comma-separated list of related resources to include in the response
        :type include: str, optional
        :rtype: IncidentHandlesResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        return self._list_global_incident_handles_endpoint.call_with_http_info(**kwargs)

    def list_incident_attachments(
        self,
        incident_id: str,
        *,
        filter_attachment_type: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> AttachmentArray:
        """List incident attachments.

        List incident attachments.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param filter_attachment_type: Filter attachments by type. Supported values are ``1`` ( ``postmortem`` ) and ``2`` ( ``link`` ).
        :type filter_attachment_type: str, optional
        :param include: Resource to include in the response. Supported value: ``last_modified_by_user``.
        :type include: str, optional
        :rtype: AttachmentArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if filter_attachment_type is not unset:
            kwargs["filter_attachment_type"] = filter_attachment_type

        if include is not unset:
            kwargs["include"] = include

        return self._list_incident_attachments_endpoint.call_with_http_info(**kwargs)

    def list_incident_impact_fields(
        self,
    ) -> IncidentImpactFieldsResponse:
        """List incident impact fields.

        List all impact fields for incidents.

        :rtype: IncidentImpactFieldsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_incident_impact_fields_endpoint.call_with_http_info(**kwargs)

    def list_incident_impacts(
        self,
        incident_id: str,
        *,
        include: Union[List[IncidentImpactRelatedObject], UnsetType] = unset,
    ) -> IncidentImpactsResponse:
        """List an incident's impacts.

        Get all impacts for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param include: Specifies which related resources should be included in the response.
        :type include: [IncidentImpactRelatedObject], optional
        :rtype: IncidentImpactsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        return self._list_incident_impacts_endpoint.call_with_http_info(**kwargs)

    def list_incident_integrations(
        self,
        incident_id: str,
    ) -> IncidentIntegrationMetadataListResponse:
        """Get a list of an incident's integration metadata.

        Get all integration metadata for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentIntegrationMetadataListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._list_incident_integrations_endpoint.call_with_http_info(**kwargs)

    def list_incident_notification_rules(
        self,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationRuleArray:
        """List incident notification rules.

        Lists all notification rules for the organization. Optionally filter by incident type.

        :param include: Comma-separated list of resources to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type`` , ``notification_template``
        :type include: str, optional
        :rtype: IncidentNotificationRuleArray
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        return self._list_incident_notification_rules_endpoint.call_with_http_info(**kwargs)

    def list_incident_notification_templates(
        self,
        *,
        filter_incident_type: Union[UUID, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationTemplateArray:
        """List incident notification templates.

        Lists all notification templates. Optionally filter by incident type.

        :param filter_incident_type: Optional incident type ID filter.
        :type filter_incident_type: UUID, optional
        :param include: Comma-separated list of relationships to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type``
        :type include: str, optional
        :rtype: IncidentNotificationTemplateArray
        """
        kwargs: Dict[str, Any] = {}
        if filter_incident_type is not unset:
            kwargs["filter_incident_type"] = filter_incident_type

        if include is not unset:
            kwargs["include"] = include

        return self._list_incident_notification_templates_endpoint.call_with_http_info(**kwargs)

    def list_incident_postmortem_templates(
        self,
    ) -> PostmortemTemplatesResponse:
        """List postmortem templates.

        Retrieve a list of all postmortem templates for incidents.

        :rtype: PostmortemTemplatesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_incident_postmortem_templates_endpoint.call_with_http_info(**kwargs)

    def list_incident_responders(
        self,
        incident_id: str,
    ) -> IncidentRespondersResponse:
        """List incident responders.

        List all responders for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentRespondersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._list_incident_responders_endpoint.call_with_http_info(**kwargs)

    def list_incident_rules(
        self,
        *,
        filter_task_id: Union[str, UnsetType] = unset,
        filter_trigger: Union[str, UnsetType] = unset,
        incident_type_uuid: Union[UUID, UnsetType] = unset,
    ) -> IncidentRulesResponse:
        """List incident rules.

        List all incident rules.

        :param filter_task_id: Filter rules by task ID.
        :type filter_task_id: str, optional
        :param filter_trigger: Filter rules by trigger.
        :type filter_trigger: str, optional
        :param incident_type_uuid: Filter rules by incident type UUID.
        :type incident_type_uuid: UUID, optional
        :rtype: IncidentRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_task_id is not unset:
            kwargs["filter_task_id"] = filter_task_id

        if filter_trigger is not unset:
            kwargs["filter_trigger"] = filter_trigger

        if incident_type_uuid is not unset:
            kwargs["incident_type_uuid"] = incident_type_uuid

        return self._list_incident_rules_endpoint.call_with_http_info(**kwargs)

    def list_incidents(
        self,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> IncidentsResponse:
        """Get a list of incidents.

        Get all incidents for the user's organization.

        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :rtype: IncidentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_incidents_endpoint.call_with_http_info(**kwargs)

    def list_incidents_with_pagination(
        self,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[IncidentResponseData]:
        """Get a list of incidents.

        Provide a paginated version of :meth:`list_incidents`, returning all items.

        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[IncidentResponseData]
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_incidents_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_incident_todos(
        self,
        incident_id: str,
    ) -> IncidentTodoListResponse:
        """Get a list of an incident's todos.

        Get all todos for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentTodoListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._list_incident_todos_endpoint.call_with_http_info(**kwargs)

    def list_incident_types(
        self,
        *,
        include_deleted: Union[bool, UnsetType] = unset,
    ) -> IncidentTypeListResponse:
        """Get a list of incident types.

        Get all incident types.

        :param include_deleted: Include deleted incident types in the response.
        :type include_deleted: bool, optional
        :rtype: IncidentTypeListResponse
        """
        kwargs: Dict[str, Any] = {}
        if include_deleted is not unset:
            kwargs["include_deleted"] = include_deleted

        return self._list_incident_types_endpoint.call_with_http_info(**kwargs)

    def list_incident_user_defined_fields(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        include_deleted: Union[bool, UnsetType] = unset,
        filter_incident_type: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedFieldListResponse:
        """Get a list of incident user-defined fields.

        Get a list of all incident user-defined fields.

        :param page_size: The number of results to return per page. Must be between 0 and 1000.
        :type page_size: int, optional
        :param page_number: The page number to retrieve, starting at 0.
        :type page_number: int, optional
        :param include_deleted: When true, include soft-deleted fields in the response.
        :type include_deleted: bool, optional
        :param filter_incident_type: Filter results to fields associated with the given incident type UUID.
        :type filter_incident_type: str, optional
        :param include: Comma-separated list of related resources to include. Supported values are "last_modified_by_user", "created_by_user", and "incident_type".
        :type include: str, optional
        :rtype: IncidentUserDefinedFieldListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if include_deleted is not unset:
            kwargs["include_deleted"] = include_deleted

        if filter_incident_type is not unset:
            kwargs["filter_incident_type"] = filter_incident_type

        if include is not unset:
            kwargs["include"] = include

        return self._list_incident_user_defined_fields_endpoint.call_with_http_info(**kwargs)

    def list_incident_user_defined_roles(
        self,
        *,
        filter_incident_type: Union[UUID, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedRolesResponse:
        """List incident user-defined roles.

        List all user-defined roles for incidents.

        :param filter_incident_type: Filter roles by incident type UUID.
        :type filter_incident_type: UUID, optional
        :param include: Comma-separated list of related resources to include in the response.
        :type include: str, optional
        :rtype: IncidentUserDefinedRolesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_incident_type is not unset:
            kwargs["filter_incident_type"] = filter_incident_type

        if include is not unset:
            kwargs["include"] = include

        return self._list_incident_user_defined_roles_endpoint.call_with_http_info(**kwargs)

    def list_org_settings(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include_deleted: Union[bool, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentOrgSettingsListResponse:
        """List incident type org settings.

        List org settings for all incident types.

        :param page_size: Maximum number of results to return.
        :type page_size: int, optional
        :param page_offset: The offset for pagination.
        :type page_offset: int, optional
        :param include_deleted: Whether to include deleted records.
        :type include_deleted: bool, optional
        :param include: Comma-separated list of related resources to include in the response.
        :type include: str, optional
        :rtype: IncidentOrgSettingsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include_deleted is not unset:
            kwargs["include_deleted"] = include_deleted

        if include is not unset:
            kwargs["include"] = include

        return self._list_org_settings_endpoint.call_with_http_info(**kwargs)

    def list_timestamp_overrides(
        self,
        incident_id: str,
    ) -> IncidentTimestampOverridesResponse:
        """List incident timestamp overrides.

        List all timestamp overrides for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentTimestampOverridesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._list_timestamp_overrides_endpoint.call_with_http_info(**kwargs)

    def patch_incident_impact(
        self,
        incident_id: str,
        impact_id: str,
        body: IncidentImpactPatchRequest,
        *,
        include: Union[List[IncidentImpactRelatedObject], UnsetType] = unset,
    ) -> IncidentImpactResponse:
        """Update an incident impact.

        Update an incident impact.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param impact_id: The UUID of the incident impact.
        :type impact_id: str
        :param body: Incident impact patch payload.
        :type body: IncidentImpactPatchRequest
        :param include: Specifies which related resources should be included in the response.
        :type include: [IncidentImpactRelatedObject], optional
        :rtype: IncidentImpactResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["impact_id"] = impact_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._patch_incident_impact_endpoint.call_with_http_info(**kwargs)

    def search_incidents(
        self,
        query: str,
        *,
        include: Union[IncidentRelatedObject, UnsetType] = unset,
        sort: Union[IncidentSearchSortOrder, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> IncidentSearchResponse:
        """Search for incidents.

        Search for incidents matching a certain query.

        :param query: Specifies which incidents should be returned. The query can contain any number of incident facets
            joined by ``ANDs`` , along with multiple values for each of those facets joined by ``OR`` s. For
            example: ``state:active AND severity:(SEV-2 OR SEV-1)``.
        :type query: str
        :param include: Specifies which types of related objects should be included in the response.
        :type include: IncidentRelatedObject, optional
        :param sort: Specifies the order of returned incidents.
        :type sort: IncidentSearchSortOrder, optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :rtype: IncidentSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._search_incidents_endpoint.call_with_http_info(**kwargs)

    def search_incidents_with_pagination(
        self,
        query: str,
        *,
        include: Union[IncidentRelatedObject, UnsetType] = unset,
        sort: Union[IncidentSearchSortOrder, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[IncidentSearchResponseIncidentsData]:
        """Search for incidents.

        Provide a paginated version of :meth:`search_incidents`, returning all items.

        :param query: Specifies which incidents should be returned. The query can contain any number of incident facets
            joined by ``ANDs`` , along with multiple values for each of those facets joined by ``OR`` s. For
            example: ``state:active AND severity:(SEV-2 OR SEV-1)``.
        :type query: str
        :param include: Specifies which types of related objects should be included in the response.
        :type include: IncidentRelatedObject, optional
        :param sort: Specifies the order of returned incidents.
        :type sort: IncidentSearchSortOrder, optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[IncidentSearchResponseIncidentsData]
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._search_incidents_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data.attributes.incidents",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def update_global_incident_handle(
        self,
        body: IncidentHandleRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentHandleResponse:
        """Update global incident handle.

        Update an existing global incident handle.

        :type body: IncidentHandleRequest
        :param include: Comma-separated list of related resources to include in the response
        :type include: str, optional
        :rtype: IncidentHandleResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_global_incident_handle_endpoint.call_with_http_info(**kwargs)

    def update_global_incident_settings(
        self,
        body: GlobalIncidentSettingsRequest,
    ) -> GlobalIncidentSettingsResponse:
        """Update global incident settings.

        Update global incident settings for the organization.

        :type body: GlobalIncidentSettingsRequest
        :rtype: GlobalIncidentSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_global_incident_settings_endpoint.call_with_http_info(**kwargs)

    def update_incident(
        self,
        incident_id: str,
        body: IncidentUpdateRequest,
        *,
        include: Union[List[IncidentRelatedObject], UnsetType] = unset,
    ) -> IncidentResponse:
        """Update an existing incident.

        Updates an incident. Provide only the attributes that should be updated as this request is a partial update.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident Payload.
        :type body: IncidentUpdateRequest
        :param include: Specifies which types of related objects should be included in the response.
        :type include: [IncidentRelatedObject], optional
        :rtype: IncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_endpoint.call_with_http_info(**kwargs)

    def update_incident_attachment(
        self,
        incident_id: str,
        attachment_id: str,
        body: PatchAttachmentRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> Attachment:
        """Update incident attachment.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param attachment_id: The ID of the attachment.
        :type attachment_id: str
        :type body: PatchAttachmentRequest
        :param include: Resource to include in the response. Supported value: ``last_modified_by_user``.
        :type include: str, optional
        :rtype: Attachment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["attachment_id"] = attachment_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_attachment_endpoint.call_with_http_info(**kwargs)

    def update_incident_configuration(
        self,
        incident_id: str,
        body: IncidentConfigurationPatchRequest,
    ) -> IncidentConfigurationResponse:
        """Update an incident configuration.

        Update a configuration for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param body: Incident configuration patch payload.
        :type body: IncidentConfigurationPatchRequest
        :rtype: IncidentConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._update_incident_configuration_endpoint.call_with_http_info(**kwargs)

    def update_incident_google_chat_configuration(
        self,
        id: UUID,
        body: IncidentGoogleChatConfigurationPatchRequest,
    ) -> IncidentGoogleChatConfigurationResponse:
        """Update an incident Google Chat configuration.

        Update a Google Chat configuration for incidents.

        :param id: The UUID of the Google Chat configuration.
        :type id: UUID
        :param body: Google Chat configuration patch payload.
        :type body: IncidentGoogleChatConfigurationPatchRequest
        :rtype: IncidentGoogleChatConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_incident_google_chat_configuration_endpoint.call_with_http_info(**kwargs)

    def update_incident_google_meet_configuration(
        self,
        id: UUID,
        body: IncidentGoogleMeetConfigurationPatchRequest,
    ) -> IncidentGoogleMeetConfigurationResponse:
        """Update an incident Google Meet configuration.

        Update a Google Meet configuration for incidents.

        :param id: The UUID of the Google Meet configuration.
        :type id: UUID
        :param body: Google Meet configuration patch payload.
        :type body: IncidentGoogleMeetConfigurationPatchRequest
        :rtype: IncidentGoogleMeetConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_incident_google_meet_configuration_endpoint.call_with_http_info(**kwargs)

    def update_incident_impact_field(
        self,
        field_id: UUID,
        body: IncidentImpactFieldRequest,
    ) -> IncidentImpactFieldResponse:
        """Update an incident impact field.

        Update an impact field for incidents.

        :param field_id: The UUID of the impact field.
        :type field_id: UUID
        :param body: Impact field update payload.
        :type body: IncidentImpactFieldRequest
        :rtype: IncidentImpactFieldResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["field_id"] = field_id

        kwargs["body"] = body

        return self._update_incident_impact_field_endpoint.call_with_http_info(**kwargs)

    def update_incident_integration(
        self,
        incident_id: str,
        integration_metadata_id: str,
        body: IncidentIntegrationMetadataPatchRequest,
    ) -> IncidentIntegrationMetadataResponse:
        """Update an existing incident integration metadata.

        Update an existing incident integration metadata.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param integration_metadata_id: The UUID of the incident integration metadata.
        :type integration_metadata_id: str
        :param body: Incident integration metadata payload.
        :type body: IncidentIntegrationMetadataPatchRequest
        :rtype: IncidentIntegrationMetadataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["integration_metadata_id"] = integration_metadata_id

        kwargs["body"] = body

        return self._update_incident_integration_endpoint.call_with_http_info(**kwargs)

    def update_incident_notification_rule(
        self,
        id: UUID,
        body: PutIncidentNotificationRuleRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationRule:
        """Update an incident notification rule.

        Updates an existing notification rule with a complete replacement.

        :param id: The ID of the notification rule.
        :type id: UUID
        :type body: PutIncidentNotificationRuleRequest
        :param include: Comma-separated list of resources to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type`` , ``notification_template``
        :type include: str, optional
        :rtype: IncidentNotificationRule
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_notification_rule_endpoint.call_with_http_info(**kwargs)

    def update_incident_notification_template(
        self,
        id: UUID,
        body: PatchIncidentNotificationTemplateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationTemplate:
        """Update incident notification template.

        Updates an existing notification template's attributes.

        :param id: The ID of the notification template.
        :type id: UUID
        :type body: PatchIncidentNotificationTemplateRequest
        :param include: Comma-separated list of relationships to include. Supported values: ``created_by_user`` , ``last_modified_by_user`` , ``incident_type``
        :type include: str, optional
        :rtype: IncidentNotificationTemplate
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_notification_template_endpoint.call_with_http_info(**kwargs)

    def update_incident_postmortem_template(
        self,
        template_id: str,
        body: PostmortemTemplateRequest,
    ) -> PostmortemTemplateResponse:
        """Update postmortem template.

        Update an existing postmortem template.

        :param template_id: The ID of the postmortem template
        :type template_id: str
        :type body: PostmortemTemplateRequest
        :rtype: PostmortemTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        kwargs["body"] = body

        return self._update_incident_postmortem_template_endpoint.call_with_http_info(**kwargs)

    def update_incident_rule(
        self,
        rule_id: UUID,
        body: IncidentRulePatchRequest,
    ) -> IncidentRuleResponse:
        """Update an incident rule.

        Update an incident rule.

        :param rule_id: The UUID of the incident rule.
        :type rule_id: UUID
        :param body: Incident rule patch payload.
        :type body: IncidentRulePatchRequest
        :rtype: IncidentRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_incident_rule_endpoint.call_with_http_info(**kwargs)

    def update_incident_todo(
        self,
        incident_id: str,
        todo_id: str,
        body: IncidentTodoPatchRequest,
    ) -> IncidentTodoResponse:
        """Update an incident todo.

        Update an incident todo.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param todo_id: The UUID of the incident todo.
        :type todo_id: str
        :param body: Incident todo payload.
        :type body: IncidentTodoPatchRequest
        :rtype: IncidentTodoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["todo_id"] = todo_id

        kwargs["body"] = body

        return self._update_incident_todo_endpoint.call_with_http_info(**kwargs)

    def update_incident_type(
        self,
        incident_type_id: str,
        body: IncidentTypePatchRequest,
    ) -> IncidentTypeResponse:
        """Update an incident type.

        Update an incident type.

        :param incident_type_id: The UUID of the incident type.
        :type incident_type_id: str
        :param body: Incident type payload.
        :type body: IncidentTypePatchRequest
        :rtype: IncidentTypeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_type_id"] = incident_type_id

        kwargs["body"] = body

        return self._update_incident_type_endpoint.call_with_http_info(**kwargs)

    def update_incident_user_defined_field(
        self,
        field_id: str,
        body: IncidentUserDefinedFieldUpdateRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedFieldResponse:
        """Update an incident user-defined field.

        Update an incident user-defined field.

        :param field_id: The ID of the incident user-defined field.
        :type field_id: str
        :param body: Incident user-defined field update payload.
        :type body: IncidentUserDefinedFieldUpdateRequest
        :param include: Comma-separated list of related resources to include. Supported values are "last_modified_by_user", "created_by_user", and "incident_type".
        :type include: str, optional
        :rtype: IncidentUserDefinedFieldResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["field_id"] = field_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_user_defined_field_endpoint.call_with_http_info(**kwargs)

    def update_incident_user_defined_role(
        self,
        role_id: UUID,
        body: IncidentUserDefinedRolePatchRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentUserDefinedRoleResponse:
        """Update an incident user-defined role.

        Update an existing user-defined role for incidents.

        :param role_id: The UUID of the incident user-defined role.
        :type role_id: UUID
        :type body: IncidentUserDefinedRolePatchRequest
        :param include: Comma-separated list of related resources to include in the response.
        :type include: str, optional
        :rtype: IncidentUserDefinedRoleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_id"] = role_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_user_defined_role_endpoint.call_with_http_info(**kwargs)

    def update_timestamp_override(
        self,
        incident_id: str,
        id: UUID,
        body: IncidentTimestampOverridePatchRequest,
    ) -> IncidentTimestampOverrideResponse:
        """Update an incident timestamp override.

        Update a timestamp override for an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param id: The UUID of the timestamp override.
        :type id: UUID
        :param body: Timestamp override patch payload.
        :type body: IncidentTimestampOverridePatchRequest
        :rtype: IncidentTimestampOverrideResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_timestamp_override_endpoint.call_with_http_info(**kwargs)
