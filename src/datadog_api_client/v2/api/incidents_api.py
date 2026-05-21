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
    file_type,
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
from datadog_api_client.v2.model.incident_jira_templates_response import IncidentJiraTemplatesResponse
from datadog_api_client.v2.model.incident_jira_template_response import IncidentJiraTemplateResponse
from datadog_api_client.v2.model.incident_jira_template_request import IncidentJiraTemplateRequest
from datadog_api_client.v2.model.incident_microsoft_teams_configuration_response import (
    IncidentMicrosoftTeamsConfigurationResponse,
)
from datadog_api_client.v2.model.incident_microsoft_teams_configuration_request import (
    IncidentMicrosoftTeamsConfigurationRequest,
)
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
from datadog_api_client.v2.model.incident_reserved_roles_response import IncidentReservedRolesResponse
from datadog_api_client.v2.model.incident_reserved_role_response import IncidentReservedRoleResponse
from datadog_api_client.v2.model.incident_template_variables_response import IncidentTemplateVariablesResponse
from datadog_api_client.v2.model.incident_type_list_response import IncidentTypeListResponse
from datadog_api_client.v2.model.incident_type_response import IncidentTypeResponse
from datadog_api_client.v2.model.incident_type_create_request import IncidentTypeCreateRequest
from datadog_api_client.v2.model.incident_type_patch_request import IncidentTypePatchRequest
from datadog_api_client.v2.model.incident_user_defined_field_list_response import IncidentUserDefinedFieldListResponse
from datadog_api_client.v2.model.incident_user_defined_field_response import IncidentUserDefinedFieldResponse
from datadog_api_client.v2.model.incident_user_defined_field_create_request import IncidentUserDefinedFieldCreateRequest
from datadog_api_client.v2.model.incident_user_defined_field_update_request import IncidentUserDefinedFieldUpdateRequest
from datadog_api_client.v2.model.incident_zoom_configuration_response import IncidentZoomConfigurationResponse
from datadog_api_client.v2.model.incident_zoom_configuration_request import IncidentZoomConfigurationRequest
from datadog_api_client.v2.model.incident_import_response import IncidentImportResponse
from datadog_api_client.v2.model.incident_import_related_object import IncidentImportRelatedObject
from datadog_api_client.v2.model.incident_import_request import IncidentImportRequest
from datadog_api_client.v2.model.incident_pagerduty_services_response import IncidentPagerdutyServicesResponse
from datadog_api_client.v2.model.incident_pagerduty_related_incidents_response import (
    IncidentPagerdutyRelatedIncidentsResponse,
)
from datadog_api_client.v2.model.incident_role_assignment_response import IncidentRoleAssignmentResponse
from datadog_api_client.v2.model.incident_role_assignment_request import IncidentRoleAssignmentRequest
from datadog_api_client.v2.model.incident_search_response import IncidentSearchResponse
from datadog_api_client.v2.model.incident_search_sort_order import IncidentSearchSortOrder
from datadog_api_client.v2.model.incident_search_response_incidents_data import IncidentSearchResponseIncidentsData
from datadog_api_client.v2.model.incident_search_incidents_sort_order import IncidentSearchIncidentsSortOrder
from datadog_api_client.v2.model.incident_search_incidents_include_type import IncidentSearchIncidentsIncludeType
from datadog_api_client.v2.model.incident_search_incidents_export_request import IncidentSearchIncidentsExportRequest
from datadog_api_client.v2.model.incident_statuspage_incident_response import IncidentStatuspageIncidentResponse
from datadog_api_client.v2.model.incident_statuspage_incident_request import IncidentStatuspageIncidentRequest
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest
from datadog_api_client.v2.model.attachment_array import AttachmentArray
from datadog_api_client.v2.model.attachment import Attachment
from datadog_api_client.v2.model.create_attachment_request import CreateAttachmentRequest
from datadog_api_client.v2.model.postmortem_attachment_request import PostmortemAttachmentRequest
from datadog_api_client.v2.model.patch_attachment_request import PatchAttachmentRequest
from datadog_api_client.v2.model.incident_automation_data_response import IncidentAutomationDataResponse
from datadog_api_client.v2.model.incident_automation_data_request import IncidentAutomationDataRequest
from datadog_api_client.v2.model.incident_case_link_response import IncidentCaseLinkResponse
from datadog_api_client.v2.model.incident_communications_response import IncidentCommunicationsResponse
from datadog_api_client.v2.model.incident_communication_response import IncidentCommunicationResponse
from datadog_api_client.v2.model.incident_communication_request import IncidentCommunicationRequest
from datadog_api_client.v2.model.incident_google_meet_integration_response import IncidentGoogleMeetIntegrationResponse
from datadog_api_client.v2.model.incident_impacts_response import IncidentImpactsResponse
from datadog_api_client.v2.model.incident_impact_related_object import IncidentImpactRelatedObject
from datadog_api_client.v2.model.incident_impact_response import IncidentImpactResponse
from datadog_api_client.v2.model.incident_impact_create_request import IncidentImpactCreateRequest
from datadog_api_client.v2.model.incident_jira_issue_integration_response import IncidentJiraIssueIntegrationResponse
from datadog_api_client.v2.model.incident_jira_issue_request import IncidentJiraIssueRequest
from datadog_api_client.v2.model.incident_ms_teams_integration_response import IncidentMSTeamsIntegrationResponse
from datadog_api_client.v2.model.incident_integration_metadata_list_response import (
    IncidentIntegrationMetadataListResponse,
)
from datadog_api_client.v2.model.incident_integration_metadata_response import IncidentIntegrationMetadataResponse
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
from datadog_api_client.v2.model.incident_rendered_template_response import IncidentRenderedTemplateResponse
from datadog_api_client.v2.model.incident_render_template_request import IncidentRenderTemplateRequest
from datadog_api_client.v2.model.incident_rule_execution_states_response import IncidentRuleExecutionStatesResponse
from datadog_api_client.v2.model.incident_batch_create_rule_execution_states_request import (
    IncidentBatchCreateRuleExecutionStatesRequest,
)
from datadog_api_client.v2.model.incident_batch_update_rule_execution_states_request import (
    IncidentBatchUpdateRuleExecutionStatesRequest,
)
from datadog_api_client.v2.model.incident_status_pages_suggestion_response import IncidentStatusPagesSuggestionResponse
from datadog_api_client.v2.model.incident_status_page_notice_integration_response import (
    IncidentStatusPageNoticeIntegrationResponse,
)
from datadog_api_client.v2.model.incident_status_page_notice_create_request import IncidentStatusPageNoticeCreateRequest
from datadog_api_client.v2.model.incident_status_page_notice_update_request import IncidentStatusPageNoticeUpdateRequest
from datadog_api_client.v2.model.incident_timeline_entries_response import IncidentTimelineEntriesResponse
from datadog_api_client.v2.model.incident_timeline_entry_response import IncidentTimelineEntryResponse
from datadog_api_client.v2.model.incident_timeline_entry_request import IncidentTimelineEntryRequest
from datadog_api_client.v2.model.incident_timeline_thread_response import IncidentTimelineThreadResponse
from datadog_api_client.v2.model.incident_zoom_integration_response import IncidentZoomIntegrationResponse
from datadog_api_client.v2.model.incident_create_zoom_meeting_request import IncidentCreateZoomMeetingRequest
from datadog_api_client.v2.model.incident_statuspage_preferences_response import IncidentStatuspagePreferencesResponse
from datadog_api_client.v2.model.incident_statuspage_subscriptions_response import (
    IncidentStatuspageSubscriptionsResponse,
)
from datadog_api_client.v2.model.incident_statuspage_subscription_response import IncidentStatuspageSubscriptionResponse
from datadog_api_client.v2.model.incident_statuspage_subscription_request import IncidentStatuspageSubscriptionRequest


class IncidentsApi:
    """
    Manage incident response, as well as associated attachments, metadata, and todos. See the `Incident Management page <https://docs.datadoghq.com/service_management/incident_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._batch_create_incident_rule_execution_states_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRuleExecutionStatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/rule-execution-states/batch",
                "operation_id": "batch_create_incident_rule_execution_states",
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
                    "openapi_types": (IncidentBatchCreateRuleExecutionStatesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._batch_update_incident_rule_execution_states_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRuleExecutionStatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/rule-execution-states/batch",
                "operation_id": "batch_update_incident_rule_execution_states",
                "http_method": "PUT",
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
                    "openapi_types": (IncidentBatchUpdateRuleExecutionStatesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

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

        self._create_incident_communication_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentCommunicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/communications",
                "operation_id": "create_incident_communication",
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
                    "openapi_types": (IncidentCommunicationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_google_meet_space_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentGoogleMeetIntegrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/google-meet/space",
                "operation_id": "create_incident_google_meet_space",
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

        self._create_incident_jira_issue_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentJiraIssueIntegrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/jira-issues",
                "operation_id": "create_incident_jira_issue",
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
                    "openapi_types": (IncidentJiraIssueRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_jira_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentJiraTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/jira-templates",
                "operation_id": "create_incident_jira_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentJiraTemplateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_microsoft_teams_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentMicrosoftTeamsConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/microsoft-teams-configurations",
                "operation_id": "create_incident_microsoft_teams_configuration",
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
                    "openapi_types": (IncidentMicrosoftTeamsConfigurationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_ms_teams_online_meeting_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentMSTeamsIntegrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/microsoft-teams-integration/online-meeting",
                "operation_id": "create_incident_ms_teams_online_meeting",
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

        self._create_incident_role_assignment_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRoleAssignmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/role_assignments",
                "operation_id": "create_incident_role_assignment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentRoleAssignmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_statuspage_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatuspageIncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/statuspage/{incident_id}/statuspage-incidents",
                "operation_id": "create_incident_statuspage_incident",
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
                    "openapi_types": (IncidentStatuspageIncidentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_status_page_notice_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatusPageNoticeIntegrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/statuspages/{statuspage_id}/notices",
                "operation_id": "create_incident_status_page_notice",
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
                "statuspage_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "statuspage_id",
                    "location": "path",
                },
                "notify_subscribers": {
                    "openapi_types": (bool,),
                    "attribute": "notify_subscribers",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentStatusPageNoticeCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_timeline_entry_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimelineEntryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timeline",
                "operation_id": "create_incident_timeline_entry",
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
                    "openapi_types": (IncidentTimelineEntryRequest,),
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

        self._create_incident_zoom_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentZoomConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/zoom-configurations",
                "operation_id": "create_incident_zoom_configuration",
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
                    "openapi_types": (IncidentZoomConfigurationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_incident_zoom_meeting_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentZoomIntegrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/zoom/meeting",
                "operation_id": "create_incident_zoom_meeting",
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
                    "openapi_types": (IncidentCreateZoomMeetingRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_statuspage_email_subscription_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatuspageSubscriptionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/subscriptions/email",
                "operation_id": "create_statuspage_email_subscription",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentStatuspageSubscriptionRequest,),
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

        self._delete_incident_communication_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/communications/{communication_id}",
                "operation_id": "delete_incident_communication",
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
                "communication_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "communication_id",
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

        self._delete_incident_jira_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/jira-templates/{template_id}",
                "operation_id": "delete_incident_jira_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "template_id",
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

        self._delete_incident_role_assignment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/role_assignments/{role_assignment_id}",
                "operation_id": "delete_incident_role_assignment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "role_assignment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "role_assignment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_incident_timeline_entry_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timeline/{timeline_entry_id}",
                "operation_id": "delete_incident_timeline_entry",
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
                "timeline_entry_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "timeline_entry_id",
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

        self._export_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/search-incidents/export",
                "operation_id": "export_incidents",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IncidentSearchIncidentsExportRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["text/csv", "application/json"], "content_type": ["application/json"]},
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

        self._get_incident_automation_data_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentAutomationDataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/automation-data/{key}",
                "operation_id": "get_incident_automation_data",
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
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
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

        self._get_incident_case_source_link_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentCaseLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/cases/source-link",
                "operation_id": "get_incident_case_source_link",
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

        self._get_incident_communication_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentCommunicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/communications/{communication_id}",
                "operation_id": "get_incident_communication",
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
                "communication_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "communication_id",
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

        self._get_incident_jira_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentJiraTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/jira-templates/{template_id}",
                "operation_id": "get_incident_jira_template",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "template_id",
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

        self._get_incident_pagerduty_related_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentPagerdutyRelatedIncidentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/pagerduty/{pagerduty_incident_id}/relationships/incidents",
                "operation_id": "get_incident_pagerduty_related_incidents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "pagerduty_incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pagerduty_incident_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_page_source_link_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentCaseLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/pages/source-link",
                "operation_id": "get_incident_page_source_link",
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

        self._get_incident_reserved_role_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentReservedRoleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/reserved-roles/{role_id}",
                "operation_id": "get_incident_reserved_role",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_role_assignment_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRoleAssignmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/role_assignments/{role_assignment_id}",
                "operation_id": "get_incident_role_assignment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "role_assignment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "role_assignment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_incident_status_pages_suggestion_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatusPagesSuggestionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/statuspages-suggestion",
                "operation_id": "get_incident_status_pages_suggestion",
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

        self._get_incident_timeline_entry_thread_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimelineThreadResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timeline/{timeline_entry_id}/thread",
                "operation_id": "get_incident_timeline_entry_thread",
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
                "timeline_entry_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "timeline_entry_id",
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

        self._get_statuspage_subscription_preferences_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatuspagePreferencesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/statuspages/subscription/preferences",
                "operation_id": "get_statuspage_subscription_preferences",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
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

        self._list_incident_communications_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentCommunicationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/communications",
                "operation_id": "list_incident_communications",
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
                "filter_communication_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[communication_type]",
                    "location": "query",
                },
            },
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

        self._list_incident_jira_templates_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentJiraTemplatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/jira-templates",
                "operation_id": "list_incident_jira_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "is_default": {
                    "openapi_types": (bool,),
                    "attribute": "isDefault",
                    "location": "query",
                },
                "incident_type_id": {
                    "openapi_types": (UUID,),
                    "attribute": "incidentTypeId",
                    "location": "query",
                },
                "template_type": {
                    "openapi_types": (str,),
                    "attribute": "templateType",
                    "location": "query",
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

        self._list_incident_pagerduty_services_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentPagerdutyServicesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/pagerduty/services",
                "operation_id": "list_incident_pagerduty_services",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include_unresolved": {
                    "openapi_types": (bool,),
                    "attribute": "include_unresolved",
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

        self._list_incident_reserved_roles_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentReservedRolesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/reserved-roles",
                "operation_id": "list_incident_reserved_roles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_rule_execution_states_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRuleExecutionStatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/rule-execution-states",
                "operation_id": "list_incident_rule_execution_states",
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

        self._list_incident_template_variables_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTemplateVariablesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/template-variables",
                "operation_id": "list_incident_template_variables",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_incident_type": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[incident-type]",
                    "location": "query",
                },
                "include_follow_ups": {
                    "openapi_types": (bool,),
                    "attribute": "includeFollowUps",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_incident_timeline_entries_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimelineEntriesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timeline",
                "operation_id": "list_incident_timeline_entries",
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

        self._list_statuspage_email_subscriptions_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatuspageSubscriptionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/statuspages/{page_id}/subscriptions/email",
                "operation_id": "list_statuspage_email_subscriptions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "page_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._patch_incident_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentNotificationRule,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/notification-rules/{id}",
                "operation_id": "patch_incident_notification_rule",
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
                    "openapi_types": (PutIncidentNotificationRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._render_incident_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentRenderedTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/render-template",
                "operation_id": "render_incident_template",
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
                    "openapi_types": (IncidentRenderTemplateRequest,),
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

        self._search_incidents_v2_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/search-incidents",
                "operation_id": "search_incidents_v2",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (IncidentSearchIncidentsSortOrder,),
                    "attribute": "sort",
                    "location": "query",
                },
                "with_facets": {
                    "openapi_types": (bool,),
                    "attribute": "with_facets",
                    "location": "query",
                },
                "filter_with_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "filter[with_deleted]",
                    "location": "query",
                },
                "semantic_query": {
                    "openapi_types": (str,),
                    "attribute": "semantic_query",
                    "location": "query",
                },
                "time_zone": {
                    "openapi_types": (str,),
                    "attribute": "timeZone",
                    "location": "query",
                },
                "include": {
                    "openapi_types": ([IncidentSearchIncidentsIncludeType],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
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

        self._update_incident_communication_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentCommunicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/communications/{communication_id}",
                "operation_id": "update_incident_communication",
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
                "communication_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "communication_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentCommunicationRequest,),
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

        self._update_incident_jira_template_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentJiraTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/jira-templates/{template_id}",
                "operation_id": "update_incident_jira_template",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "template_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentJiraTemplateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_microsoft_teams_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentMicrosoftTeamsConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/microsoft-teams-configurations/{configuration_id}",
                "operation_id": "update_incident_microsoft_teams_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "configuration_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "configuration_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentMicrosoftTeamsConfigurationRequest,),
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

        self._update_incident_statuspage_incident_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatuspageIncidentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/statuspage/{incident_id}/statuspage-incidents/pages/{page_id}/incidents/{statuspage_incident_id}",
                "operation_id": "update_incident_statuspage_incident",
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
                "page_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "statuspage_incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "statuspage_incident_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentStatuspageIncidentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_status_page_notice_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentStatusPageNoticeIntegrationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/statuspages/{statuspage_id}/notices/{notice_id}",
                "operation_id": "update_incident_status_page_notice",
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
                "statuspage_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "statuspage_id",
                    "location": "path",
                },
                "notice_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "notice_id",
                    "location": "path",
                },
                "notify_subscribers": {
                    "openapi_types": (bool,),
                    "attribute": "notify_subscribers",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentStatusPageNoticeUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_incident_timeline_entry_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentTimelineEntryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/timeline/{timeline_entry_id}",
                "operation_id": "update_incident_timeline_entry",
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
                "timeline_entry_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "timeline_entry_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentTimelineEntryRequest,),
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

        self._update_incident_zoom_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentZoomConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/config/zoom-configurations/{configuration_id}",
                "operation_id": "update_incident_zoom_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "configuration_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "configuration_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentZoomConfigurationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_incident_automation_data_endpoint = _Endpoint(
            settings={
                "response_type": (IncidentAutomationDataResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/incidents/{incident_id}/automation-data/{key}",
                "operation_id": "upsert_incident_automation_data",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "incident_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_id",
                    "location": "path",
                },
                "key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IncidentAutomationDataRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def batch_create_incident_rule_execution_states(
        self,
        incident_id: str,
        body: IncidentBatchCreateRuleExecutionStatesRequest,
    ) -> IncidentRuleExecutionStatesResponse:
        """Batch create incident rule execution states.

        Batch create rule execution states for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentBatchCreateRuleExecutionStatesRequest
        :rtype: IncidentRuleExecutionStatesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._batch_create_incident_rule_execution_states_endpoint.call_with_http_info(**kwargs)

    def batch_update_incident_rule_execution_states(
        self,
        incident_id: str,
        body: IncidentBatchUpdateRuleExecutionStatesRequest,
    ) -> IncidentRuleExecutionStatesResponse:
        """Batch update incident rule execution states.

        Batch update rule execution states for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentBatchUpdateRuleExecutionStatesRequest
        :rtype: IncidentRuleExecutionStatesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._batch_update_incident_rule_execution_states_endpoint.call_with_http_info(**kwargs)

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

    def create_incident_communication(
        self,
        incident_id: str,
        body: IncidentCommunicationRequest,
    ) -> IncidentCommunicationResponse:
        """Create an incident communication.

        Create a new communication for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentCommunicationRequest
        :rtype: IncidentCommunicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_communication_endpoint.call_with_http_info(**kwargs)

    def create_incident_google_meet_space(
        self,
        incident_id: str,
    ) -> IncidentGoogleMeetIntegrationResponse:
        """Create an incident Google Meet space.

        Create a Google Meet space for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentGoogleMeetIntegrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._create_incident_google_meet_space_endpoint.call_with_http_info(**kwargs)

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

    def create_incident_jira_issue(
        self,
        incident_id: str,
        body: IncidentJiraIssueRequest,
    ) -> IncidentJiraIssueIntegrationResponse:
        """Create an incident Jira issue.

        Create a Jira issue linked to a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentJiraIssueRequest
        :rtype: IncidentJiraIssueIntegrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_jira_issue_endpoint.call_with_http_info(**kwargs)

    def create_incident_jira_template(
        self,
        body: IncidentJiraTemplateRequest,
    ) -> IncidentJiraTemplateResponse:
        """Create an incident Jira template.

        Create a new incident Jira template for the organization.

        :type body: IncidentJiraTemplateRequest
        :rtype: IncidentJiraTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_jira_template_endpoint.call_with_http_info(**kwargs)

    def create_incident_microsoft_teams_configuration(
        self,
        body: IncidentMicrosoftTeamsConfigurationRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentMicrosoftTeamsConfigurationResponse:
        """Create an incident Microsoft Teams configuration.

        Create a Microsoft Teams configuration for incidents.

        :type body: IncidentMicrosoftTeamsConfigurationRequest
        :param include: Specifies which related objects to include in the response.
        :type include: str, optional
        :rtype: IncidentMicrosoftTeamsConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_incident_microsoft_teams_configuration_endpoint.call_with_http_info(**kwargs)

    def create_incident_ms_teams_online_meeting(
        self,
        incident_id: str,
    ) -> IncidentMSTeamsIntegrationResponse:
        """Create an incident Microsoft Teams online meeting.

        Create a Microsoft Teams online meeting for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentMSTeamsIntegrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._create_incident_ms_teams_online_meeting_endpoint.call_with_http_info(**kwargs)

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

    def create_incident_role_assignment(
        self,
        body: IncidentRoleAssignmentRequest,
    ) -> IncidentRoleAssignmentResponse:
        """Create an incident role assignment.

        Create a new role assignment for an incident.

        :type body: IncidentRoleAssignmentRequest
        :rtype: IncidentRoleAssignmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_role_assignment_endpoint.call_with_http_info(**kwargs)

    def create_incident_statuspage_incident(
        self,
        incident_id: str,
        body: IncidentStatuspageIncidentRequest,
    ) -> IncidentStatuspageIncidentResponse:
        """Create a Statuspage incident for an incident.

        Create a Statuspage incident linked to a Datadog incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentStatuspageIncidentRequest
        :rtype: IncidentStatuspageIncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_statuspage_incident_endpoint.call_with_http_info(**kwargs)

    def create_incident_status_page_notice(
        self,
        incident_id: str,
        statuspage_id: UUID,
        body: IncidentStatusPageNoticeCreateRequest,
        *,
        notify_subscribers: Union[bool, UnsetType] = unset,
    ) -> IncidentStatusPageNoticeIntegrationResponse:
        """Publish an incident status page notice.

        Publish a status page notice for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param statuspage_id: The ID of the status page.
        :type statuspage_id: UUID
        :type body: IncidentStatusPageNoticeCreateRequest
        :param notify_subscribers: Whether to notify subscribers about this notice.
        :type notify_subscribers: bool, optional
        :rtype: IncidentStatusPageNoticeIntegrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["statuspage_id"] = statuspage_id

        if notify_subscribers is not unset:
            kwargs["notify_subscribers"] = notify_subscribers

        kwargs["body"] = body

        return self._create_incident_status_page_notice_endpoint.call_with_http_info(**kwargs)

    def create_incident_timeline_entry(
        self,
        incident_id: str,
        body: IncidentTimelineEntryRequest,
    ) -> IncidentTimelineEntryResponse:
        """Create an incident timeline entry.

        Create a new timeline entry for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentTimelineEntryRequest
        :rtype: IncidentTimelineEntryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_timeline_entry_endpoint.call_with_http_info(**kwargs)

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

    def create_incident_zoom_configuration(
        self,
        body: IncidentZoomConfigurationRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentZoomConfigurationResponse:
        """Create an incident Zoom configuration.

        Create a Zoom configuration for incidents.

        :type body: IncidentZoomConfigurationRequest
        :param include: Specifies which related objects to include in the response.
        :type include: str, optional
        :rtype: IncidentZoomConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._create_incident_zoom_configuration_endpoint.call_with_http_info(**kwargs)

    def create_incident_zoom_meeting(
        self,
        incident_id: str,
        body: IncidentCreateZoomMeetingRequest,
    ) -> IncidentZoomIntegrationResponse:
        """Create an incident Zoom meeting.

        Create a Zoom meeting for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentCreateZoomMeetingRequest
        :rtype: IncidentZoomIntegrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._create_incident_zoom_meeting_endpoint.call_with_http_info(**kwargs)

    def create_statuspage_email_subscription(
        self,
        page_id: str,
        body: IncidentStatuspageSubscriptionRequest,
    ) -> IncidentStatuspageSubscriptionResponse:
        """Create a status page email subscription.

        Create an email subscription for a status page.

        :param page_id: The ID of the status page.
        :type page_id: str
        :type body: IncidentStatuspageSubscriptionRequest
        :rtype: IncidentStatuspageSubscriptionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["body"] = body

        return self._create_statuspage_email_subscription_endpoint.call_with_http_info(**kwargs)

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

    def delete_incident_communication(
        self,
        incident_id: str,
        communication_id: UUID,
    ) -> None:
        """Delete an incident communication.

        Delete a communication for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param communication_id: The ID of the communication.
        :type communication_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["communication_id"] = communication_id

        return self._delete_incident_communication_endpoint.call_with_http_info(**kwargs)

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

    def delete_incident_jira_template(
        self,
        template_id: UUID,
    ) -> None:
        """Delete an incident Jira template.

        Delete an incident Jira template by its identifier.

        :param template_id: The ID of the Jira template.
        :type template_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._delete_incident_jira_template_endpoint.call_with_http_info(**kwargs)

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

    def delete_incident_role_assignment(
        self,
        role_assignment_id: UUID,
    ) -> None:
        """Delete an incident role assignment.

        Delete a role assignment by its identifier.

        :param role_assignment_id: The ID of the role assignment.
        :type role_assignment_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_assignment_id"] = role_assignment_id

        return self._delete_incident_role_assignment_endpoint.call_with_http_info(**kwargs)

    def delete_incident_timeline_entry(
        self,
        incident_id: str,
        timeline_entry_id: UUID,
    ) -> None:
        """Delete an incident timeline entry.

        Delete a timeline entry for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param timeline_entry_id: The ID of the timeline entry.
        :type timeline_entry_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["timeline_entry_id"] = timeline_entry_id

        return self._delete_incident_timeline_entry_endpoint.call_with_http_info(**kwargs)

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

    def export_incidents(
        self,
        body: IncidentSearchIncidentsExportRequest,
    ) -> file_type:
        """Export incidents.

        Export incidents matching a search query as a CSV file.

        :type body: IncidentSearchIncidentsExportRequest
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._export_incidents_endpoint.call_with_http_info(**kwargs)

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

    def get_incident_automation_data(
        self,
        incident_id: str,
        key: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentAutomationDataResponse:
        """Get incident automation data.

        Get automation data for a given incident and key.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param key: The automation data key.
        :type key: str
        :param include: Specifies which related objects to include in the response.
        :type include: str, optional
        :rtype: IncidentAutomationDataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["key"] = key

        if include is not unset:
            kwargs["include"] = include

        return self._get_incident_automation_data_endpoint.call_with_http_info(**kwargs)

    def get_incident_case_source_link(
        self,
        incident_id: str,
    ) -> IncidentCaseLinkResponse:
        """Get incident case source link.

        Get the source link for a case associated with an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentCaseLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._get_incident_case_source_link_endpoint.call_with_http_info(**kwargs)

    def get_incident_communication(
        self,
        incident_id: str,
        communication_id: UUID,
    ) -> IncidentCommunicationResponse:
        """Get an incident communication.

        Get the details of a communication for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param communication_id: The ID of the communication.
        :type communication_id: UUID
        :rtype: IncidentCommunicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["communication_id"] = communication_id

        return self._get_incident_communication_endpoint.call_with_http_info(**kwargs)

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

    def get_incident_jira_template(
        self,
        template_id: UUID,
    ) -> IncidentJiraTemplateResponse:
        """Get an incident Jira template.

        Get the details of an incident Jira template by its identifier.

        :param template_id: The ID of the Jira template.
        :type template_id: UUID
        :rtype: IncidentJiraTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        return self._get_incident_jira_template_endpoint.call_with_http_info(**kwargs)

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

    def get_incident_pagerduty_related_incidents(
        self,
        pagerduty_incident_id: str,
    ) -> IncidentPagerdutyRelatedIncidentsResponse:
        """Get PagerDuty related incidents.

        Get the list of Datadog incidents attached to a PagerDuty incident.

        :param pagerduty_incident_id: The PagerDuty incident identifier.
        :type pagerduty_incident_id: str
        :rtype: IncidentPagerdutyRelatedIncidentsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["pagerduty_incident_id"] = pagerduty_incident_id

        return self._get_incident_pagerduty_related_incidents_endpoint.call_with_http_info(**kwargs)

    def get_incident_page_source_link(
        self,
        incident_id: str,
    ) -> IncidentCaseLinkResponse:
        """Get incident page source link.

        Get the source link for a page associated with an incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentCaseLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._get_incident_page_source_link_endpoint.call_with_http_info(**kwargs)

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

    def get_incident_reserved_role(
        self,
        role_id: UUID,
    ) -> IncidentReservedRoleResponse:
        """Get an incident reserved role.

        Get the details of a reserved role by its identifier.

        :param role_id: The ID of the reserved role.
        :type role_id: UUID
        :rtype: IncidentReservedRoleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_id"] = role_id

        return self._get_incident_reserved_role_endpoint.call_with_http_info(**kwargs)

    def get_incident_role_assignment(
        self,
        role_assignment_id: UUID,
    ) -> IncidentRoleAssignmentResponse:
        """Get an incident role assignment.

        Get the details of a role assignment by its identifier.

        :param role_assignment_id: The ID of the role assignment.
        :type role_assignment_id: UUID
        :rtype: IncidentRoleAssignmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_assignment_id"] = role_assignment_id

        return self._get_incident_role_assignment_endpoint.call_with_http_info(**kwargs)

    def get_incident_status_pages_suggestion(
        self,
        incident_id: str,
    ) -> IncidentStatusPagesSuggestionResponse:
        """Get incident status page suggestion.

        Get an AI-generated suggestion for a status page notice for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentStatusPagesSuggestionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._get_incident_status_pages_suggestion_endpoint.call_with_http_info(**kwargs)

    def get_incident_timeline_entry_thread(
        self,
        incident_id: str,
        timeline_entry_id: UUID,
    ) -> IncidentTimelineThreadResponse:
        """Get incident timeline entry thread.

        Get the thread entries for a given timeline entry.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param timeline_entry_id: The ID of the timeline entry.
        :type timeline_entry_id: UUID
        :rtype: IncidentTimelineThreadResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["timeline_entry_id"] = timeline_entry_id

        return self._get_incident_timeline_entry_thread_endpoint.call_with_http_info(**kwargs)

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

    def get_statuspage_subscription_preferences(
        self,
    ) -> IncidentStatuspagePreferencesResponse:
        """Get status page subscription preferences.

        Get the subscription preferences for the current user.

        :rtype: IncidentStatuspagePreferencesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_statuspage_subscription_preferences_endpoint.call_with_http_info(**kwargs)

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

    def list_incident_communications(
        self,
        incident_id: str,
        *,
        filter_communication_type: Union[str, UnsetType] = unset,
    ) -> IncidentCommunicationsResponse:
        """List incident communications.

        List all communications for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param filter_communication_type: Filter by communication type.
        :type filter_communication_type: str, optional
        :rtype: IncidentCommunicationsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        if filter_communication_type is not unset:
            kwargs["filter_communication_type"] = filter_communication_type

        return self._list_incident_communications_endpoint.call_with_http_info(**kwargs)

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

    def list_incident_jira_templates(
        self,
        *,
        is_default: Union[bool, UnsetType] = unset,
        incident_type_id: Union[UUID, UnsetType] = unset,
        template_type: Union[str, UnsetType] = unset,
    ) -> IncidentJiraTemplatesResponse:
        """List incident Jira templates.

        List all incident Jira templates for the organization.

        :param is_default: Filter templates by default status.
        :type is_default: bool, optional
        :param incident_type_id: Filter templates by incident type identifier.
        :type incident_type_id: UUID, optional
        :param template_type: Filter templates by type.
        :type template_type: str, optional
        :rtype: IncidentJiraTemplatesResponse
        """
        kwargs: Dict[str, Any] = {}
        if is_default is not unset:
            kwargs["is_default"] = is_default

        if incident_type_id is not unset:
            kwargs["incident_type_id"] = incident_type_id

        if template_type is not unset:
            kwargs["template_type"] = template_type

        return self._list_incident_jira_templates_endpoint.call_with_http_info(**kwargs)

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

    def list_incident_pagerduty_services(
        self,
        *,
        include_unresolved: Union[bool, UnsetType] = unset,
    ) -> IncidentPagerdutyServicesResponse:
        """List PagerDuty services.

        List all PagerDuty services configured for the organization.

        :param include_unresolved: Whether to include unresolved PagerDuty services.
        :type include_unresolved: bool, optional
        :rtype: IncidentPagerdutyServicesResponse
        """
        kwargs: Dict[str, Any] = {}
        if include_unresolved is not unset:
            kwargs["include_unresolved"] = include_unresolved

        return self._list_incident_pagerduty_services_endpoint.call_with_http_info(**kwargs)

    def list_incident_postmortem_templates(
        self,
    ) -> PostmortemTemplatesResponse:
        """List postmortem templates.

        Retrieve a list of all postmortem templates for incidents.

        :rtype: PostmortemTemplatesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_incident_postmortem_templates_endpoint.call_with_http_info(**kwargs)

    def list_incident_reserved_roles(
        self,
    ) -> IncidentReservedRolesResponse:
        """List incident reserved roles.

        List all reserved roles for incidents.

        :rtype: IncidentReservedRolesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_incident_reserved_roles_endpoint.call_with_http_info(**kwargs)

    def list_incident_rule_execution_states(
        self,
        incident_id: str,
    ) -> IncidentRuleExecutionStatesResponse:
        """List incident rule execution states.

        List all rule execution states for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentRuleExecutionStatesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._list_incident_rule_execution_states_endpoint.call_with_http_info(**kwargs)

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

    def list_incident_template_variables(
        self,
        *,
        filter_incident_type: Union[UUID, UnsetType] = unset,
        include_follow_ups: Union[bool, UnsetType] = unset,
    ) -> IncidentTemplateVariablesResponse:
        """List incident template variables.

        List all available template variables for incident templates.

        :param filter_incident_type: Filter template variables by incident type.
        :type filter_incident_type: UUID, optional
        :param include_follow_ups: Whether to include follow-up template variables.
        :type include_follow_ups: bool, optional
        :rtype: IncidentTemplateVariablesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_incident_type is not unset:
            kwargs["filter_incident_type"] = filter_incident_type

        if include_follow_ups is not unset:
            kwargs["include_follow_ups"] = include_follow_ups

        return self._list_incident_template_variables_endpoint.call_with_http_info(**kwargs)

    def list_incident_timeline_entries(
        self,
        incident_id: str,
    ) -> IncidentTimelineEntriesResponse:
        """List incident timeline entries.

        Get the timeline for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :rtype: IncidentTimelineEntriesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        return self._list_incident_timeline_entries_endpoint.call_with_http_info(**kwargs)

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

    def list_statuspage_email_subscriptions(
        self,
        page_id: str,
    ) -> IncidentStatuspageSubscriptionsResponse:
        """List status page email subscriptions.

        List all email subscriptions for a status page.

        :param page_id: The ID of the status page.
        :type page_id: str
        :rtype: IncidentStatuspageSubscriptionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        return self._list_statuspage_email_subscriptions_endpoint.call_with_http_info(**kwargs)

    def patch_incident_notification_rule(
        self,
        id: UUID,
        body: PutIncidentNotificationRuleRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentNotificationRule:
        """Partially update an incident notification rule.

        Partially updates an existing notification rule.

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

        return self._patch_incident_notification_rule_endpoint.call_with_http_info(**kwargs)

    def render_incident_template(
        self,
        incident_id: str,
        body: IncidentRenderTemplateRequest,
    ) -> IncidentRenderedTemplateResponse:
        """Render an incident template.

        Render a template with incident-specific data.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :type body: IncidentRenderTemplateRequest
        :rtype: IncidentRenderedTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["body"] = body

        return self._render_incident_template_endpoint.call_with_http_info(**kwargs)

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

    def search_incidents_v2(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        sort: Union[IncidentSearchIncidentsSortOrder, UnsetType] = unset,
        with_facets: Union[bool, UnsetType] = unset,
        filter_with_deleted: Union[bool, UnsetType] = unset,
        semantic_query: Union[str, UnsetType] = unset,
        time_zone: Union[str, UnsetType] = unset,
        include: Union[List[IncidentSearchIncidentsIncludeType], UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> IncidentSearchResponse:
        """Search incidents.

        Search for incidents using advanced filtering and pagination.

        :param query: Specifies which incidents should be returned by the search.
        :type query: str, optional
        :param sort: Specifies the order of returned incidents.
        :type sort: IncidentSearchIncidentsSortOrder, optional
        :param with_facets: Whether to include facet data in the response.
        :type with_facets: bool, optional
        :param filter_with_deleted: Whether to include deleted incidents in the response.
        :type filter_with_deleted: bool, optional
        :param semantic_query: A semantic search query.
        :type semantic_query: str, optional
        :param time_zone: The timezone for date-based operations.
        :type time_zone: str, optional
        :param include: Specifies which types of related objects to include.
        :type include: [IncidentSearchIncidentsIncludeType], optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :rtype: IncidentSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if with_facets is not unset:
            kwargs["with_facets"] = with_facets

        if filter_with_deleted is not unset:
            kwargs["filter_with_deleted"] = filter_with_deleted

        if semantic_query is not unset:
            kwargs["semantic_query"] = semantic_query

        if time_zone is not unset:
            kwargs["time_zone"] = time_zone

        if include is not unset:
            kwargs["include"] = include

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._search_incidents_v2_endpoint.call_with_http_info(**kwargs)

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

    def update_incident_communication(
        self,
        incident_id: str,
        communication_id: UUID,
        body: IncidentCommunicationRequest,
    ) -> IncidentCommunicationResponse:
        """Update an incident communication.

        Update a communication for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param communication_id: The ID of the communication.
        :type communication_id: UUID
        :type body: IncidentCommunicationRequest
        :rtype: IncidentCommunicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["communication_id"] = communication_id

        kwargs["body"] = body

        return self._update_incident_communication_endpoint.call_with_http_info(**kwargs)

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

    def update_incident_jira_template(
        self,
        template_id: UUID,
        body: IncidentJiraTemplateRequest,
    ) -> IncidentJiraTemplateResponse:
        """Update an incident Jira template.

        Update an existing incident Jira template.

        :param template_id: The ID of the Jira template.
        :type template_id: UUID
        :type body: IncidentJiraTemplateRequest
        :rtype: IncidentJiraTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["template_id"] = template_id

        kwargs["body"] = body

        return self._update_incident_jira_template_endpoint.call_with_http_info(**kwargs)

    def update_incident_microsoft_teams_configuration(
        self,
        configuration_id: UUID,
        body: IncidentMicrosoftTeamsConfigurationRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentMicrosoftTeamsConfigurationResponse:
        """Update an incident Microsoft Teams configuration.

        Update a Microsoft Teams configuration for incidents.

        :param configuration_id: The ID of the Microsoft Teams configuration.
        :type configuration_id: UUID
        :type body: IncidentMicrosoftTeamsConfigurationRequest
        :param include: Specifies which related objects to include in the response.
        :type include: str, optional
        :rtype: IncidentMicrosoftTeamsConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["configuration_id"] = configuration_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_microsoft_teams_configuration_endpoint.call_with_http_info(**kwargs)

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

    def update_incident_statuspage_incident(
        self,
        incident_id: str,
        page_id: str,
        statuspage_incident_id: str,
        body: IncidentStatuspageIncidentRequest,
    ) -> IncidentStatuspageIncidentResponse:
        """Update a Statuspage incident for an incident.

        Update a Statuspage incident linked to a Datadog incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param page_id: The ID of the Statuspage page.
        :type page_id: str
        :param statuspage_incident_id: The ID of the Statuspage incident.
        :type statuspage_incident_id: str
        :type body: IncidentStatuspageIncidentRequest
        :rtype: IncidentStatuspageIncidentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["page_id"] = page_id

        kwargs["statuspage_incident_id"] = statuspage_incident_id

        kwargs["body"] = body

        return self._update_incident_statuspage_incident_endpoint.call_with_http_info(**kwargs)

    def update_incident_status_page_notice(
        self,
        incident_id: str,
        statuspage_id: UUID,
        notice_id: UUID,
        body: IncidentStatusPageNoticeUpdateRequest,
        *,
        notify_subscribers: Union[bool, UnsetType] = unset,
    ) -> IncidentStatusPageNoticeIntegrationResponse:
        """Update an incident status page notice.

        Update a status page notice for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param statuspage_id: The ID of the status page.
        :type statuspage_id: UUID
        :param notice_id: The ID of the status page notice.
        :type notice_id: UUID
        :type body: IncidentStatusPageNoticeUpdateRequest
        :param notify_subscribers: Whether to notify subscribers about this notice.
        :type notify_subscribers: bool, optional
        :rtype: IncidentStatusPageNoticeIntegrationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["statuspage_id"] = statuspage_id

        kwargs["notice_id"] = notice_id

        if notify_subscribers is not unset:
            kwargs["notify_subscribers"] = notify_subscribers

        kwargs["body"] = body

        return self._update_incident_status_page_notice_endpoint.call_with_http_info(**kwargs)

    def update_incident_timeline_entry(
        self,
        incident_id: str,
        timeline_entry_id: UUID,
        body: IncidentTimelineEntryRequest,
    ) -> IncidentTimelineEntryResponse:
        """Update an incident timeline entry.

        Update a timeline entry for a given incident.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param timeline_entry_id: The ID of the timeline entry.
        :type timeline_entry_id: UUID
        :type body: IncidentTimelineEntryRequest
        :rtype: IncidentTimelineEntryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["timeline_entry_id"] = timeline_entry_id

        kwargs["body"] = body

        return self._update_incident_timeline_entry_endpoint.call_with_http_info(**kwargs)

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

    def update_incident_zoom_configuration(
        self,
        configuration_id: UUID,
        body: IncidentZoomConfigurationRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentZoomConfigurationResponse:
        """Update an incident Zoom configuration.

        Update a Zoom configuration for incidents.

        :param configuration_id: The ID of the Zoom configuration.
        :type configuration_id: UUID
        :type body: IncidentZoomConfigurationRequest
        :param include: Specifies which related objects to include in the response.
        :type include: str, optional
        :rtype: IncidentZoomConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["configuration_id"] = configuration_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_incident_zoom_configuration_endpoint.call_with_http_info(**kwargs)

    def upsert_incident_automation_data(
        self,
        incident_id: str,
        key: str,
        body: IncidentAutomationDataRequest,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> IncidentAutomationDataResponse:
        """Create or update incident automation data.

        Create or update automation data for a given incident and key.

        :param incident_id: The UUID of the incident.
        :type incident_id: str
        :param key: The automation data key.
        :type key: str
        :type body: IncidentAutomationDataRequest
        :param include: Specifies which related objects to include in the response.
        :type include: str, optional
        :rtype: IncidentAutomationDataResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_id"] = incident_id

        kwargs["key"] = key

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._upsert_incident_automation_data_endpoint.call_with_http_info(**kwargs)
