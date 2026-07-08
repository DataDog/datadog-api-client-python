# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union
import warnings

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
    file_type,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.create_custom_framework_response import CreateCustomFrameworkResponse
from datadog_api_client.v2.model.create_custom_framework_request import CreateCustomFrameworkRequest
from datadog_api_client.v2.model.delete_custom_framework_response import DeleteCustomFrameworkResponse
from datadog_api_client.v2.model.get_custom_framework_response import GetCustomFrameworkResponse
from datadog_api_client.v2.model.update_custom_framework_response import UpdateCustomFrameworkResponse
from datadog_api_client.v2.model.update_custom_framework_request import UpdateCustomFrameworkRequest
from datadog_api_client.v2.model.get_resource_evaluation_filters_response import GetResourceEvaluationFiltersResponse
from datadog_api_client.v2.model.update_resource_evaluation_filters_response import (
    UpdateResourceEvaluationFiltersResponse,
)
from datadog_api_client.v2.model.update_resource_evaluation_filters_request import (
    UpdateResourceEvaluationFiltersRequest,
)
from datadog_api_client.v2.model.list_findings_response import ListFindingsResponse
from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
from datadog_api_client.v2.model.finding_status import FindingStatus
from datadog_api_client.v2.model.finding_vulnerability_type import FindingVulnerabilityType
from datadog_api_client.v2.model.finding import Finding
from datadog_api_client.v2.model.get_finding_response import GetFindingResponse
from datadog_api_client.v2.model.list_security_findings_response import ListSecurityFindingsResponse
from datadog_api_client.v2.model.security_findings_sort import SecurityFindingsSort
from datadog_api_client.v2.model.security_findings_data import SecurityFindingsData
from datadog_api_client.v2.model.assignee_response import AssigneeResponse
from datadog_api_client.v2.model.assignee_request import AssigneeRequest
from datadog_api_client.v2.model.due_date_rules_response import DueDateRulesResponse
from datadog_api_client.v2.model.due_date_rule_response import DueDateRuleResponse
from datadog_api_client.v2.model.due_date_rule_create_request import DueDateRuleCreateRequest
from datadog_api_client.v2.model.due_date_rule_reorder_request import DueDateRuleReorderRequest
from datadog_api_client.v2.model.due_date_rule_update_request import DueDateRuleUpdateRequest
from datadog_api_client.v2.model.mute_rules_response import MuteRulesResponse
from datadog_api_client.v2.model.mute_rule_response import MuteRuleResponse
from datadog_api_client.v2.model.mute_rule_create_request import MuteRuleCreateRequest
from datadog_api_client.v2.model.mute_rule_reorder_request import MuteRuleReorderRequest
from datadog_api_client.v2.model.mute_rule_update_request import MuteRuleUpdateRequest
from datadog_api_client.v2.model.ticket_creation_rules_response import TicketCreationRulesResponse
from datadog_api_client.v2.model.ticket_creation_rule_response import TicketCreationRuleResponse
from datadog_api_client.v2.model.ticket_creation_rule_create_request import TicketCreationRuleCreateRequest
from datadog_api_client.v2.model.ticket_creation_rule_reorder_request import TicketCreationRuleReorderRequest
from datadog_api_client.v2.model.ticket_creation_rule_update_request import TicketCreationRuleUpdateRequest
from datadog_api_client.v2.model.detach_case_request import DetachCaseRequest
from datadog_api_client.v2.model.finding_case_response_array import FindingCaseResponseArray
from datadog_api_client.v2.model.create_case_request_array import CreateCaseRequestArray
from datadog_api_client.v2.model.finding_case_response import FindingCaseResponse
from datadog_api_client.v2.model.attach_case_request import AttachCaseRequest
from datadog_api_client.v2.model.attach_jira_issue_request import AttachJiraIssueRequest
from datadog_api_client.v2.model.create_jira_issue_request_array import CreateJiraIssueRequestArray
from datadog_api_client.v2.model.attach_linear_issue_request import AttachLinearIssueRequest
from datadog_api_client.v2.model.create_linear_issue_request_array import CreateLinearIssueRequestArray
from datadog_api_client.v2.model.mute_findings_response import MuteFindingsResponse
from datadog_api_client.v2.model.mute_findings_request import MuteFindingsRequest
from datadog_api_client.v2.model.security_findings_search_request import SecurityFindingsSearchRequest
from datadog_api_client.v2.model.attach_service_now_ticket_request import AttachServiceNowTicketRequest
from datadog_api_client.v2.model.create_service_now_ticket_request_array import CreateServiceNowTicketRequestArray
from datadog_api_client.v2.model.list_assets_sbo_ms_response import ListAssetsSBOMsResponse
from datadog_api_client.v2.model.asset_type import AssetType
from datadog_api_client.v2.model.sbom_component_license_type import SBOMComponentLicenseType
from datadog_api_client.v2.model.get_sbom_response import GetSBOMResponse
from datadog_api_client.v2.model.sbom_format import SBOMFormat
from datadog_api_client.v2.model.scanned_assets_metadata import ScannedAssetsMetadata
from datadog_api_client.v2.model.cloud_asset_type import CloudAssetType
from datadog_api_client.v2.model.io_c_explorer_list_response import IoCExplorerListResponse
from datadog_api_client.v2.model.io_c_triage_state import IoCTriageState
from datadog_api_client.v2.model.get_io_c_indicator_response import GetIoCIndicatorResponse
from datadog_api_client.v2.model.io_c_triage_write_response import IoCTriageWriteResponse
from datadog_api_client.v2.model.io_c_triage_write_request import IoCTriageWriteRequest
from datadog_api_client.v2.model.notification_rules_list_response import NotificationRulesListResponse
from datadog_api_client.v2.model.notification_rule_response import NotificationRuleResponse
from datadog_api_client.v2.model.create_notification_rule_parameters import CreateNotificationRuleParameters
from datadog_api_client.v2.model.patch_notification_rule_parameters import PatchNotificationRuleParameters
from datadog_api_client.v2.model.list_vulnerabilities_response import ListVulnerabilitiesResponse
from datadog_api_client.v2.model.vulnerability_type import VulnerabilityType
from datadog_api_client.v2.model.vulnerability_severity import VulnerabilitySeverity
from datadog_api_client.v2.model.vulnerability_status import VulnerabilityStatus
from datadog_api_client.v2.model.vulnerability_tool import VulnerabilityTool
from datadog_api_client.v2.model.vulnerability_ecosystem import VulnerabilityEcosystem
from datadog_api_client.v2.model.cyclone_dx_bom import CycloneDXBom
from datadog_api_client.v2.model.list_vulnerable_assets_response import ListVulnerableAssetsResponse
from datadog_api_client.v2.model.security_monitoring_critical_assets_response import (
    SecurityMonitoringCriticalAssetsResponse,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_response import (
    SecurityMonitoringCriticalAssetResponse,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_create_request import (
    SecurityMonitoringCriticalAssetCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_critical_asset_update_request import (
    SecurityMonitoringCriticalAssetUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_configs_response import (
    SecurityMonitoringIntegrationConfigsResponse,
)
from datadog_api_client.v2.model.security_monitoring_integration_type import SecurityMonitoringIntegrationType
from datadog_api_client.v2.model.security_monitoring_integration_config_response import (
    SecurityMonitoringIntegrationConfigResponse,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_create_request import (
    SecurityMonitoringIntegrationConfigCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_credentials_validate_request import (
    SecurityMonitoringIntegrationCredentialsValidateRequest,
)
from datadog_api_client.v2.model.security_monitoring_integration_config_update_request import (
    SecurityMonitoringIntegrationConfigUpdateRequest,
)
from datadog_api_client.v2.model.notification_rule_preview_response import NotificationRulePreviewResponse
from datadog_api_client.v2.model.security_filters_response import SecurityFiltersResponse
from datadog_api_client.v2.model.security_filter_response import SecurityFilterResponse
from datadog_api_client.v2.model.security_filter_create_request import SecurityFilterCreateRequest
from datadog_api_client.v2.model.security_filter_versions_response import SecurityFilterVersionsResponse
from datadog_api_client.v2.model.security_filter_update_request import SecurityFilterUpdateRequest
from datadog_api_client.v2.model.security_monitoring_paginated_suppressions_response import (
    SecurityMonitoringPaginatedSuppressionsResponse,
)
from datadog_api_client.v2.model.security_monitoring_suppression_sort import SecurityMonitoringSuppressionSort
from datadog_api_client.v2.model.security_monitoring_suppression_response import SecurityMonitoringSuppressionResponse
from datadog_api_client.v2.model.security_monitoring_suppression_create_request import (
    SecurityMonitoringSuppressionCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_suppressions_response import SecurityMonitoringSuppressionsResponse
from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_signal_rule_create_payload import (
    SecurityMonitoringSignalRuleCreatePayload,
)
from datadog_api_client.v2.model.cloud_configuration_rule_create_payload import CloudConfigurationRuleCreatePayload
from datadog_api_client.v2.model.security_monitoring_suppression_update_request import (
    SecurityMonitoringSuppressionUpdateRequest,
)
from datadog_api_client.v2.model.get_suppression_version_history_response import GetSuppressionVersionHistoryResponse
from datadog_api_client.v2.model.security_monitoring_content_pack_states_response import (
    SecurityMonitoringContentPackStatesResponse,
)
from datadog_api_client.v2.model.security_monitoring_datasets_list_response import (
    SecurityMonitoringDatasetsListResponse,
)
from datadog_api_client.v2.model.security_monitoring_dataset_create_response import (
    SecurityMonitoringDatasetCreateResponse,
)
from datadog_api_client.v2.model.security_monitoring_dataset_create_request import (
    SecurityMonitoringDatasetCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_response import (
    SecurityMonitoringDatasetDependenciesResponse,
)
from datadog_api_client.v2.model.security_monitoring_dataset_dependencies_request import (
    SecurityMonitoringDatasetDependenciesRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_response import SecurityMonitoringDatasetResponse
from datadog_api_client.v2.model.security_monitoring_dataset_update_request import (
    SecurityMonitoringDatasetUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_dataset_version_history_response import (
    SecurityMonitoringDatasetVersionHistoryResponse,
)
from datadog_api_client.v2.model.entity_context_response import EntityContextResponse
from datadog_api_client.v2.model.single_entity_context_response import SingleEntityContextResponse
from datadog_api_client.v2.model.security_monitoring_list_rules_response import SecurityMonitoringListRulesResponse
from datadog_api_client.v2.model.security_monitoring_rule_sort import SecurityMonitoringRuleSort
from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse
from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_response import (
    SecurityMonitoringRuleBulkDeleteResponse,
)
from datadog_api_client.v2.model.security_monitoring_rule_bulk_delete_payload import (
    SecurityMonitoringRuleBulkDeletePayload,
)
from datadog_api_client.v2.model.security_monitoring_rule_bulk_export_payload import (
    SecurityMonitoringRuleBulkExportPayload,
)
from datadog_api_client.v2.model.security_monitoring_rule_convert_response import SecurityMonitoringRuleConvertResponse
from datadog_api_client.v2.model.security_monitoring_rule_convert_payload import SecurityMonitoringRuleConvertPayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_payload import SecurityMonitoringStandardRulePayload
from datadog_api_client.v2.model.security_monitoring_signal_rule_payload import SecurityMonitoringSignalRulePayload
from datadog_api_client.v2.model.security_monitoring_rule_convert_bulk_payload import (
    SecurityMonitoringRuleConvertBulkPayload,
)
from datadog_api_client.v2.model.security_monitoring_rule_test_response import SecurityMonitoringRuleTestResponse
from datadog_api_client.v2.model.security_monitoring_rule_test_request import SecurityMonitoringRuleTestRequest
from datadog_api_client.v2.model.security_monitoring_rule_validate_payload import SecurityMonitoringRuleValidatePayload
from datadog_api_client.v2.model.cloud_configuration_rule_payload import CloudConfigurationRulePayload
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload
from datadog_api_client.v2.model.get_rule_version_history_response import GetRuleVersionHistoryResponse
from datadog_api_client.v2.model.sample_log_generation_subscriptions_response import (
    SampleLogGenerationSubscriptionsResponse,
)
from datadog_api_client.v2.model.sample_log_generation_subscriptions_status_filter import (
    SampleLogGenerationSubscriptionsStatusFilter,
)
from datadog_api_client.v2.model.sample_log_generation_subscription_response import (
    SampleLogGenerationSubscriptionResponse,
)
from datadog_api_client.v2.model.sample_log_generation_subscription_create_request import (
    SampleLogGenerationSubscriptionCreateRequest,
)
from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_response import (
    SampleLogGenerationBulkSubscriptionResponse,
)
from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_request import (
    SampleLogGenerationBulkSubscriptionRequest,
)
from datadog_api_client.v2.model.security_monitoring_signals_list_response import SecurityMonitoringSignalsListResponse
from datadog_api_client.v2.model.security_monitoring_signals_sort import SecurityMonitoringSignalsSort
from datadog_api_client.v2.model.security_monitoring_signal import SecurityMonitoringSignal
from datadog_api_client.v2.model.security_monitoring_signals_bulk_triage_update_response import (
    SecurityMonitoringSignalsBulkTriageUpdateResponse,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_assignee_update_request import (
    SecurityMonitoringSignalsBulkAssigneeUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_state_update_request import (
    SecurityMonitoringSignalsBulkStateUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signals_bulk_update_request import (
    SecurityMonitoringSignalsBulkUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_list_request import SecurityMonitoringSignalListRequest
from datadog_api_client.v2.model.security_monitoring_signal_response import SecurityMonitoringSignalResponse
from datadog_api_client.v2.model.security_monitoring_signal_triage_update_response import (
    SecurityMonitoringSignalTriageUpdateResponse,
)
from datadog_api_client.v2.model.security_monitoring_signal_assignee_update_request import (
    SecurityMonitoringSignalAssigneeUpdateRequest,
)
from datadog_api_client.v2.model.signal_entities_response import SignalEntitiesResponse
from datadog_api_client.v2.model.security_monitoring_signal_incidents_update_request import (
    SecurityMonitoringSignalIncidentsUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_suggested_actions_response import (
    SecurityMonitoringSignalSuggestedActionsResponse,
)
from datadog_api_client.v2.model.security_monitoring_signal_state_update_request import (
    SecurityMonitoringSignalStateUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_update_request import SecurityMonitoringSignalUpdateRequest
from datadog_api_client.v2.model.security_monitoring_terraform_resource_type import (
    SecurityMonitoringTerraformResourceType,
)
from datadog_api_client.v2.model.security_monitoring_terraform_bulk_export_request import (
    SecurityMonitoringTerraformBulkExportRequest,
)
from datadog_api_client.v2.model.security_monitoring_terraform_export_response import (
    SecurityMonitoringTerraformExportResponse,
)
from datadog_api_client.v2.model.security_monitoring_terraform_convert_request import (
    SecurityMonitoringTerraformConvertRequest,
)
from datadog_api_client.v2.model.list_historical_jobs_response import ListHistoricalJobsResponse
from datadog_api_client.v2.model.job_create_response import JobCreateResponse
from datadog_api_client.v2.model.run_historical_job_request import RunHistoricalJobRequest
from datadog_api_client.v2.model.convert_job_results_to_signals_request import ConvertJobResultsToSignalsRequest
from datadog_api_client.v2.model.historical_job_response import HistoricalJobResponse
from datadog_api_client.v2.model.sast_rulesets_response import SastRulesetsResponse
from datadog_api_client.v2.model.default_rulesets_per_language_response import DefaultRulesetsPerLanguageResponse
from datadog_api_client.v2.model.get_multiple_rulesets_response import GetMultipleRulesetsResponse
from datadog_api_client.v2.model.get_multiple_rulesets_request import GetMultipleRulesetsRequest
from datadog_api_client.v2.model.sast_ruleset_response import SastRulesetResponse
from datadog_api_client.v2.model.secret_rule_array import SecretRuleArray
from datadog_api_client.v2.model.analysis_response import AnalysisResponse
from datadog_api_client.v2.model.analysis_request import AnalysisRequest
from datadog_api_client.v2.model.get_ast_response import GetAstResponse
from datadog_api_client.v2.model.get_ast_request import GetAstRequest
from datadog_api_client.v2.model.node_types_response import NodeTypesResponse


class SecurityMonitoringApi:
    """
    Create and manage your security rules, signals, filters, and more. See the `Datadog Security page <https://docs.datadoghq.com/security/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._activate_content_pack_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/content_packs/{content_pack_id}/activate",
                "operation_id": "activate_content_pack",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "content_pack_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "content_pack_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._attach_case_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/cases/{case_id}",
                "operation_id": "attach_case",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "case_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AttachCaseRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._attach_jira_issue_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/jira_issues",
                "operation_id": "attach_jira_issue",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AttachJiraIssueRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._attach_linear_issue_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/linear_issues",
                "operation_id": "attach_linear_issue",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AttachLinearIssueRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._attach_service_now_ticket_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/servicenow_tickets",
                "operation_id": "attach_service_now_ticket",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AttachServiceNowTicketRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._batch_get_security_monitoring_dataset_dependencies_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringDatasetDependenciesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets/dependencies",
                "operation_id": "batch_get_security_monitoring_dataset_dependencies",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringDatasetDependenciesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_convert_existing_security_monitoring_rules_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/convert/bulk",
                "operation_id": "bulk_convert_existing_security_monitoring_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleConvertBulkPayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/zip", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_create_sample_log_generation_subscriptions_endpoint = _Endpoint(
            settings={
                "response_type": (SampleLogGenerationBulkSubscriptionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/sample_log_generation/subscriptions/bulk",
                "operation_id": "bulk_create_sample_log_generation_subscriptions",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SampleLogGenerationBulkSubscriptionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_delete_security_monitoring_rules_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleBulkDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/bulk_delete",
                "operation_id": "bulk_delete_security_monitoring_rules",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleBulkDeletePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_edit_security_monitoring_signals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsBulkTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/bulk/update",
                "operation_id": "bulk_edit_security_monitoring_signals",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalsBulkUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_edit_security_monitoring_signals_assignee_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsBulkTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/signals/bulk/assignee",
                "operation_id": "bulk_edit_security_monitoring_signals_assignee",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalsBulkAssigneeUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_edit_security_monitoring_signals_state_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsBulkTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/signals/bulk/state",
                "operation_id": "bulk_edit_security_monitoring_signals_state",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalsBulkStateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_export_security_monitoring_rules_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/bulk_export",
                "operation_id": "bulk_export_security_monitoring_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleBulkExportPayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/zip", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._bulk_export_security_monitoring_terraform_resources_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/terraform/{resource_type}/bulk",
                "operation_id": "bulk_export_security_monitoring_terraform_resources",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "resource_type": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringTerraformResourceType,),
                    "attribute": "resource_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringTerraformBulkExportRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/zip", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._cancel_historical_job_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs/{job_id}/cancel",
                "operation_id": "cancel_historical_job",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "job_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "job_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._convert_existing_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleConvertResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}/convert",
                "operation_id": "convert_existing_security_monitoring_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._convert_job_result_to_signal_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs/signal_convert",
                "operation_id": "convert_job_result_to_signal",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ConvertJobResultsToSignalsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._convert_security_monitoring_rule_from_json_to_terraform_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleConvertResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/convert",
                "operation_id": "convert_security_monitoring_rule_from_json_to_terraform",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleConvertPayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._convert_security_monitoring_terraform_resource_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringTerraformExportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/terraform/{resource_type}/convert",
                "operation_id": "convert_security_monitoring_terraform_resource",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "resource_type": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringTerraformResourceType,),
                    "attribute": "resource_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringTerraformConvertRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_cases_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/cases",
                "operation_id": "create_cases",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateCaseRequestArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_custom_framework_endpoint = _Endpoint(
            settings={
                "response_type": (CreateCustomFrameworkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_security_management/custom_frameworks",
                "operation_id": "create_custom_framework",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateCustomFrameworkRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_io_c_triage_state_endpoint = _Endpoint(
            settings={
                "response_type": (IoCTriageWriteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/siem/ioc-explorer/triage",
                "operation_id": "create_io_c_triage_state",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (IoCTriageWriteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_jira_issues_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/jira_issues",
                "operation_id": "create_jira_issues",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateJiraIssueRequestArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_linear_issues_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/linear_issues",
                "operation_id": "create_linear_issues",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateLinearIssueRequestArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_sample_log_generation_subscription_endpoint = _Endpoint(
            settings={
                "response_type": (SampleLogGenerationSubscriptionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/sample_log_generation/subscriptions",
                "operation_id": "create_sample_log_generation_subscription",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SampleLogGenerationSubscriptionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters",
                "operation_id": "create_security_filter",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_findings_automation_due_date_rule_endpoint = _Endpoint(
            settings={
                "response_type": (DueDateRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/due_date_rules",
                "operation_id": "create_security_findings_automation_due_date_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DueDateRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_findings_automation_mute_rule_endpoint = _Endpoint(
            settings={
                "response_type": (MuteRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/mute_rules",
                "operation_id": "create_security_findings_automation_mute_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MuteRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_findings_automation_ticket_creation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (TicketCreationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/ticket_creation_rules",
                "operation_id": "create_security_findings_automation_ticket_creation_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TicketCreationRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_monitoring_critical_asset_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringCriticalAssetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/critical_assets",
                "operation_id": "create_security_monitoring_critical_asset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringCriticalAssetCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_monitoring_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringDatasetCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets",
                "operation_id": "create_security_monitoring_dataset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringDatasetCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_monitoring_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringIntegrationConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config",
                "operation_id": "create_security_monitoring_integration_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringIntegrationConfigCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules",
                "operation_id": "create_security_monitoring_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleCreatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_monitoring_suppression_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSuppressionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions",
                "operation_id": "create_security_monitoring_suppression",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSuppressionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_service_now_tickets_endpoint = _Endpoint(
            settings={
                "response_type": (FindingCaseResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/servicenow_tickets",
                "operation_id": "create_service_now_tickets",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateServiceNowTicketRequestArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/signals/notification_rules",
                "operation_id": "create_signal_notification_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateNotificationRuleParameters,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_static_analysis_ast_endpoint = _Endpoint(
            settings={
                "response_type": (GetAstResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/static-analysis-server/get-ast",
                "operation_id": "create_static_analysis_ast",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GetAstRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_static_analysis_server_analysis_endpoint = _Endpoint(
            settings={
                "response_type": (AnalysisResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/static-analysis-server/analyze",
                "operation_id": "create_static_analysis_server_analysis",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AnalysisRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_vulnerability_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerabilities/notification_rules",
                "operation_id": "create_vulnerability_notification_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateNotificationRuleParameters,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._deactivate_content_pack_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/content_packs/{content_pack_id}/deactivate",
                "operation_id": "deactivate_content_pack",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "content_pack_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "content_pack_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_custom_framework_endpoint = _Endpoint(
            settings={
                "response_type": (DeleteCustomFrameworkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_security_management/custom_frameworks/{handle}/{version}",
                "operation_id": "delete_custom_framework",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "handle": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle",
                    "location": "path",
                },
                "version": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "version",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_historical_job_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs/{job_id}",
                "operation_id": "delete_historical_job",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "job_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "job_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_sample_log_generation_subscription_endpoint = _Endpoint(
            settings={
                "response_type": (SampleLogGenerationSubscriptionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/sample_log_generation/subscriptions/{content_pack_id}",
                "operation_id": "delete_sample_log_generation_subscription",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "content_pack_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "content_pack_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/{security_filter_id}",
                "operation_id": "delete_security_filter",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "security_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "security_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_security_findings_automation_due_date_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/due_date_rules/{rule_id}",
                "operation_id": "delete_security_findings_automation_due_date_rule",
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

        self._delete_security_findings_automation_mute_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/mute_rules/{rule_id}",
                "operation_id": "delete_security_findings_automation_mute_rule",
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

        self._delete_security_findings_automation_ticket_creation_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/ticket_creation_rules/{rule_id}",
                "operation_id": "delete_security_findings_automation_ticket_creation_rule",
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

        self._delete_security_monitoring_critical_asset_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/critical_assets/{critical_asset_id}",
                "operation_id": "delete_security_monitoring_critical_asset",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "critical_asset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "critical_asset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_security_monitoring_dataset_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets/{dataset_id}",
                "operation_id": "delete_security_monitoring_dataset",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_security_monitoring_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config/{integration_config_id}",
                "operation_id": "delete_security_monitoring_integration_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "integration_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_config_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}",
                "operation_id": "delete_security_monitoring_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_security_monitoring_suppression_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/{suppression_id}",
                "operation_id": "delete_security_monitoring_suppression",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "suppression_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "suppression_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/signals/notification_rules/{id}",
                "operation_id": "delete_signal_notification_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_vulnerability_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerabilities/notification_rules/{id}",
                "operation_id": "delete_vulnerability_notification_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._detach_case_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/cases",
                "operation_id": "detach_case",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DetachCaseRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_security_monitoring_signal_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/update",
                "operation_id": "edit_security_monitoring_signal",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_security_monitoring_signal_assignee_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/assignee",
                "operation_id": "edit_security_monitoring_signal_assignee",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalAssigneeUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_security_monitoring_signal_incidents_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/incidents",
                "operation_id": "edit_security_monitoring_signal_incidents",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalIncidentsUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_security_monitoring_signal_state_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/state",
                "operation_id": "edit_security_monitoring_signal_state",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSignalStateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._export_security_monitoring_terraform_resource_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringTerraformExportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/terraform/{resource_type}/{resource_id}",
                "operation_id": "export_security_monitoring_terraform_resource",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_type": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringTerraformResourceType,),
                    "attribute": "resource_type",
                    "location": "path",
                },
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_content_packs_states_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringContentPackStatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/content_packs/states",
                "operation_id": "get_content_packs_states",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_critical_assets_affecting_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringCriticalAssetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/critical_assets/rules/{rule_id}",
                "operation_id": "get_critical_assets_affecting_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_custom_framework_endpoint = _Endpoint(
            settings={
                "response_type": (GetCustomFrameworkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_security_management/custom_frameworks/{handle}/{version}",
                "operation_id": "get_custom_framework",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "handle": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle",
                    "location": "path",
                },
                "version": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "version",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_entity_context_endpoint = _Endpoint(
            settings={
                "response_type": (EntityContextResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/entity_context",
                "operation_id": "get_entity_context",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "_from": {
                    "openapi_types": (str,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (str,),
                    "attribute": "to",
                    "location": "query",
                },
                "as_of": {
                    "openapi_types": (str,),
                    "attribute": "as_of",
                    "location": "query",
                },
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "page_token": {
                    "openapi_types": (str,),
                    "attribute": "page_token",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_finding_endpoint = _Endpoint(
            settings={
                "response_type": (GetFindingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/posture_management/findings/{finding_id}",
                "operation_id": "get_finding",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "finding_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "finding_id",
                    "location": "path",
                },
                "snapshot_timestamp": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "snapshot_timestamp",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_historical_job_endpoint = _Endpoint(
            settings={
                "response_type": (HistoricalJobResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs/{job_id}",
                "operation_id": "get_historical_job",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "job_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "job_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_indicator_of_compromise_endpoint = _Endpoint(
            settings={
                "response_type": (GetIoCIndicatorResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/siem/ioc-explorer/indicator",
                "operation_id": "get_indicator_of_compromise",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "indicator": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "indicator",
                    "location": "query",
                },
                "ocsf": {
                    "openapi_types": (bool,),
                    "attribute": "ocsf",
                    "location": "query",
                },
                "include_triage_history": {
                    "openapi_types": (bool,),
                    "attribute": "include_triage_history",
                    "location": "query",
                },
                "triage_history_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "triage_history_limit",
                    "location": "query",
                },
                "triage_history_offset": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "triage_history_offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_investigation_log_queries_matching_signal_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalSuggestedActionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/investigation_queries",
                "operation_id": "get_investigation_log_queries_matching_signal",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_resource_evaluation_filters_endpoint = _Endpoint(
            settings={
                "response_type": (GetResourceEvaluationFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_security_management/resource_filters",
                "operation_id": "get_resource_evaluation_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "cloud_provider": {
                    "openapi_types": (str,),
                    "attribute": "cloud_provider",
                    "location": "query",
                },
                "account_id": {
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "query",
                },
                "skip_cache": {
                    "openapi_types": (bool,),
                    "attribute": "skip_cache",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_rule_version_history_endpoint = _Endpoint(
            settings={
                "response_type": (GetRuleVersionHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}/version_history",
                "operation_id": "get_rule_version_history",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_sbom_endpoint = _Endpoint(
            settings={
                "response_type": (GetSBOMResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/sboms/{asset_type}",
                "operation_id": "get_sbom",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "asset_type": {
                    "required": True,
                    "openapi_types": (AssetType,),
                    "attribute": "asset_type",
                    "location": "path",
                },
                "filter_asset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filter[asset_name]",
                    "location": "query",
                },
                "filter_repo_digest": {
                    "openapi_types": (str,),
                    "attribute": "filter[repo_digest]",
                    "location": "query",
                },
                "ext_format": {
                    "openapi_types": (SBOMFormat,),
                    "attribute": "ext:format",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_secrets_rules_endpoint = _Endpoint(
            settings={
                "response_type": (SecretRuleArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/secrets/rules",
                "operation_id": "get_secrets_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/{security_filter_id}",
                "operation_id": "get_security_filter",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "security_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "security_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_findings_automation_due_date_rule_endpoint = _Endpoint(
            settings={
                "response_type": (DueDateRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/due_date_rules/{rule_id}",
                "operation_id": "get_security_findings_automation_due_date_rule",
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

        self._get_security_findings_automation_mute_rule_endpoint = _Endpoint(
            settings={
                "response_type": (MuteRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/mute_rules/{rule_id}",
                "operation_id": "get_security_findings_automation_mute_rule",
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

        self._get_security_findings_automation_ticket_creation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (TicketCreationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/ticket_creation_rules/{rule_id}",
                "operation_id": "get_security_findings_automation_ticket_creation_rule",
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

        self._get_security_monitoring_critical_asset_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringCriticalAssetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/critical_assets/{critical_asset_id}",
                "operation_id": "get_security_monitoring_critical_asset",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "critical_asset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "critical_asset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_dataset_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringDatasetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets/{dataset_id}",
                "operation_id": "get_security_monitoring_dataset",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_dataset_by_version_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringDatasetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets/{dataset_id}/version/{version}",
                "operation_id": "get_security_monitoring_dataset_by_version",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "version": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "version",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_dataset_version_history_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringDatasetVersionHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets/{dataset_id}/version_history",
                "operation_id": "get_security_monitoring_dataset_version_history",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_histsignal_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/histsignals/{histsignal_id}",
                "operation_id": "get_security_monitoring_histsignal",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "histsignal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "histsignal_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_histsignals_by_job_id_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs/{job_id}/histsignals",
                "operation_id": "get_security_monitoring_histsignals_by_job_id",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "job_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "job_id",
                    "location": "path",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (SecurityMonitoringSignalsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringIntegrationConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config/{integration_config_id}",
                "operation_id": "get_security_monitoring_integration_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_config_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}",
                "operation_id": "get_security_monitoring_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_signal_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}",
                "operation_id": "get_security_monitoring_signal",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_suppression_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSuppressionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/{suppression_id}",
                "operation_id": "get_security_monitoring_suppression",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "suppression_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "suppression_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_signal_entities_endpoint = _Endpoint(
            settings={
                "response_type": (SignalEntitiesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/entities",
                "operation_id": "get_signal_entities",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/signals/notification_rules/{id}",
                "operation_id": "get_signal_notification_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_signal_notification_rules_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRulesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/signals/notification_rules",
                "operation_id": "get_signal_notification_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_single_entity_context_endpoint = _Endpoint(
            settings={
                "response_type": (SingleEntityContextResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/entity_context/{id}",
                "operation_id": "get_single_entity_context",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "_from": {
                    "openapi_types": (str,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (str,),
                    "attribute": "to",
                    "location": "query",
                },
                "as_of": {
                    "openapi_types": (str,),
                    "attribute": "as_of",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_static_analysis_default_rulesets_endpoint = _Endpoint(
            settings={
                "response_type": (DefaultRulesetsPerLanguageResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/default-rulesets/{language}",
                "operation_id": "get_static_analysis_default_rulesets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "language": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "language",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_static_analysis_node_types_endpoint = _Endpoint(
            settings={
                "response_type": (NodeTypesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/static-analysis-server/node-types/{language}",
                "operation_id": "get_static_analysis_node_types",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "language": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "language",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_static_analysis_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": (SastRulesetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/rulesets/{ruleset_name}",
                "operation_id": "get_static_analysis_ruleset",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
                "include_tests": {
                    "openapi_types": (bool,),
                    "attribute": "include_tests",
                    "location": "query",
                },
                "include_testing_rules": {
                    "openapi_types": (bool,),
                    "attribute": "include_testing_rules",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_static_analysis_tree_sitter_wasm_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/static-analysis-server/tree-sitter-wasm/{file}",
                "operation_id": "get_static_analysis_tree_sitter_wasm",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "file": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "file",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/octet-stream", "application/json"],
            },
            api_client=api_client,
        )

        self._get_suggested_actions_matching_signal_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalSuggestedActionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/{signal_id}/suggested_actions",
                "operation_id": "get_suggested_actions_matching_signal",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "signal_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "signal_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_suppressions_affecting_future_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSuppressionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/rules",
                "operation_id": "get_suppressions_affecting_future_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleCreatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_suppressions_affecting_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSuppressionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/rules/{rule_id}",
                "operation_id": "get_suppressions_affecting_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_suppression_version_history_endpoint = _Endpoint(
            settings={
                "response_type": (GetSuppressionVersionHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/{suppression_id}/version_history",
                "operation_id": "get_suppression_version_history",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "suppression_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "suppression_id",
                    "location": "path",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_vulnerability_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerabilities/notification_rules/{id}",
                "operation_id": "get_vulnerability_notification_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_vulnerability_notification_rules_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRulesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerabilities/notification_rules",
                "operation_id": "get_vulnerability_notification_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._import_security_vulnerabilities_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/vulnerabilities",
                "operation_id": "import_security_vulnerabilities",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CycloneDXBom,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_assets_sbo_ms_endpoint = _Endpoint(
            settings={
                "response_type": (ListAssetsSBOMsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/sboms",
                "operation_id": "list_assets_sbo_ms",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_token": {
                    "openapi_types": (str,),
                    "attribute": "page[token]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter_asset_type": {
                    "openapi_types": (AssetType,),
                    "attribute": "filter[asset_type]",
                    "location": "query",
                },
                "filter_asset_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset_name]",
                    "location": "query",
                },
                "filter_package_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[package_name]",
                    "location": "query",
                },
                "filter_package_version": {
                    "openapi_types": (str,),
                    "attribute": "filter[package_version]",
                    "location": "query",
                },
                "filter_license_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[license_name]",
                    "location": "query",
                },
                "filter_license_type": {
                    "openapi_types": (SBOMComponentLicenseType,),
                    "attribute": "filter[license_type]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_findings_endpoint = _Endpoint(
            settings={
                "response_type": (ListFindingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/posture_management/findings",
                "operation_id": "list_findings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "snapshot_timestamp": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "snapshot_timestamp",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "filter_evaluation_changed_at": {
                    "openapi_types": (str,),
                    "attribute": "filter[evaluation_changed_at]",
                    "location": "query",
                },
                "filter_muted": {
                    "openapi_types": (bool,),
                    "attribute": "filter[muted]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule_id]",
                    "location": "query",
                },
                "filter_rule_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule_name]",
                    "location": "query",
                },
                "filter_resource_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[resource_type]",
                    "location": "query",
                },
                "filter_resource_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[@resource_id]",
                    "location": "query",
                },
                "filter_discovery_timestamp": {
                    "openapi_types": (str,),
                    "attribute": "filter[discovery_timestamp]",
                    "location": "query",
                },
                "filter_evaluation": {
                    "openapi_types": (FindingEvaluation,),
                    "attribute": "filter[evaluation]",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (FindingStatus,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
                "filter_vulnerability_type": {
                    "openapi_types": ([FindingVulnerabilityType],),
                    "attribute": "filter[vulnerability_type]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "detailed_findings": {
                    "openapi_types": (bool,),
                    "attribute": "detailed_findings",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_historical_jobs_endpoint = _Endpoint(
            settings={
                "response_type": (ListHistoricalJobsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs",
                "operation_id": "list_historical_jobs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_indicators_of_compromise_endpoint = _Endpoint(
            settings={
                "response_type": (IoCExplorerListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/siem/ioc-explorer",
                "operation_id": "list_indicators_of_compromise",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "limit": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort_column": {
                    "openapi_types": (str,),
                    "attribute": "sort[column]",
                    "location": "query",
                },
                "sort_order": {
                    "openapi_types": (str,),
                    "attribute": "sort[order]",
                    "location": "query",
                },
                "ocsf": {
                    "openapi_types": (bool,),
                    "attribute": "ocsf",
                    "location": "query",
                },
                "worked_by": {
                    "openapi_types": (str,),
                    "attribute": "worked_by",
                    "location": "query",
                },
                "triage_state": {
                    "openapi_types": (IoCTriageState,),
                    "attribute": "triage_state",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_multiple_rulesets_endpoint = _Endpoint(
            settings={
                "response_type": (GetMultipleRulesetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/rulesets",
                "operation_id": "list_multiple_rulesets",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GetMultipleRulesetsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_sample_log_generation_subscriptions_endpoint = _Endpoint(
            settings={
                "response_type": (SampleLogGenerationSubscriptionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/sample_log_generation/subscriptions",
                "operation_id": "list_sample_log_generation_subscriptions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "status": {
                    "openapi_types": (SampleLogGenerationSubscriptionsStatusFilter,),
                    "attribute": "status",
                    "location": "query",
                },
                "start_timestamp": {
                    "openapi_types": (datetime,),
                    "attribute": "start_timestamp",
                    "location": "query",
                },
                "end_timestamp": {
                    "openapi_types": (datetime,),
                    "attribute": "end_timestamp",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scanned_assets_metadata_endpoint = _Endpoint(
            settings={
                "response_type": (ScannedAssetsMetadata,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/scanned-assets-metadata",
                "operation_id": "list_scanned_assets_metadata",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_token": {
                    "openapi_types": (str,),
                    "attribute": "page[token]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter_asset_type": {
                    "openapi_types": (CloudAssetType,),
                    "attribute": "filter[asset.type]",
                    "location": "query",
                },
                "filter_asset_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.name]",
                    "location": "query",
                },
                "filter_last_success_origin": {
                    "openapi_types": (str,),
                    "attribute": "filter[last_success.origin]",
                    "location": "query",
                },
                "filter_last_success_env": {
                    "openapi_types": (str,),
                    "attribute": "filter[last_success.env]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_filters_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters",
                "operation_id": "list_security_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_filter_versions_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterVersionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/versions",
                "operation_id": "list_security_filter_versions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_findings_endpoint = _Endpoint(
            settings={
                "response_type": (ListSecurityFindingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings",
                "operation_id": "list_security_findings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 150,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (SecurityFindingsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_findings_automation_due_date_rules_endpoint = _Endpoint(
            settings={
                "response_type": (DueDateRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/due_date_rules",
                "operation_id": "list_security_findings_automation_due_date_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_findings_automation_mute_rules_endpoint = _Endpoint(
            settings={
                "response_type": (MuteRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/mute_rules",
                "operation_id": "list_security_findings_automation_mute_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_findings_automation_ticket_creation_rules_endpoint = _Endpoint(
            settings={
                "response_type": (TicketCreationRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/ticket_creation_rules",
                "operation_id": "list_security_findings_automation_ticket_creation_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_critical_assets_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringCriticalAssetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/critical_assets",
                "operation_id": "list_security_monitoring_critical_assets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_datasets_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringDatasetsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets",
                "operation_id": "list_security_monitoring_datasets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_histsignals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/histsignals",
                "operation_id": "list_security_monitoring_histsignals",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (SecurityMonitoringSignalsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_integration_configs_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringIntegrationConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config",
                "operation_id": "list_security_monitoring_integration_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_integration_type": {
                    "openapi_types": (SecurityMonitoringIntegrationType,),
                    "attribute": "filter[integration_type]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_rules_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringListRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules",
                "operation_id": "list_security_monitoring_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (SecurityMonitoringRuleSort,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_signals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals",
                "operation_id": "list_security_monitoring_signals",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (SecurityMonitoringSignalsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_suppressions_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringPaginatedSuppressionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions",
                "operation_id": "list_security_monitoring_suppressions",
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
                    "openapi_types": (SecurityMonitoringSuppressionSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_static_analysis_codegen_rulesets_endpoint = _Endpoint(
            settings={
                "response_type": (SastRulesetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis/codegen/rulesets",
                "operation_id": "list_static_analysis_codegen_rulesets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_vulnerabilities_endpoint = _Endpoint(
            settings={
                "response_type": (ListVulnerabilitiesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerabilities",
                "operation_id": "list_vulnerabilities",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_token": {
                    "openapi_types": (str,),
                    "attribute": "page[token]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter_type": {
                    "openapi_types": (VulnerabilityType,),
                    "attribute": "filter[type]",
                    "location": "query",
                },
                "filter_cvss_base_score_op": {
                    "validation": {
                        "inclusive_maximum": 10,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (float,),
                    "attribute": "filter[cvss.base.score][`$op`]",
                    "location": "query",
                },
                "filter_cvss_base_severity": {
                    "openapi_types": (VulnerabilitySeverity,),
                    "attribute": "filter[cvss.base.severity]",
                    "location": "query",
                },
                "filter_cvss_base_vector": {
                    "openapi_types": (str,),
                    "attribute": "filter[cvss.base.vector]",
                    "location": "query",
                },
                "filter_cvss_datadog_score_op": {
                    "validation": {
                        "inclusive_maximum": 10,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (float,),
                    "attribute": "filter[cvss.datadog.score][`$op`]",
                    "location": "query",
                },
                "filter_cvss_datadog_severity": {
                    "openapi_types": (VulnerabilitySeverity,),
                    "attribute": "filter[cvss.datadog.severity]",
                    "location": "query",
                },
                "filter_cvss_datadog_vector": {
                    "openapi_types": (str,),
                    "attribute": "filter[cvss.datadog.vector]",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (VulnerabilityStatus,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
                "filter_tool": {
                    "openapi_types": (VulnerabilityTool,),
                    "attribute": "filter[tool]",
                    "location": "query",
                },
                "filter_library_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[library.name]",
                    "location": "query",
                },
                "filter_library_version": {
                    "openapi_types": (str,),
                    "attribute": "filter[library.version]",
                    "location": "query",
                },
                "filter_advisory_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[advisory.id]",
                    "location": "query",
                },
                "filter_risks_exploitation_probability": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.exploitation_probability]",
                    "location": "query",
                },
                "filter_risks_poc_exploit_available": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.poc_exploit_available]",
                    "location": "query",
                },
                "filter_risks_exploit_available": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.exploit_available]",
                    "location": "query",
                },
                "filter_risks_epss_score_op": {
                    "validation": {
                        "inclusive_maximum": 1,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (float,),
                    "attribute": "filter[risks.epss.score][`$op`]",
                    "location": "query",
                },
                "filter_risks_epss_severity": {
                    "openapi_types": (VulnerabilitySeverity,),
                    "attribute": "filter[risks.epss.severity]",
                    "location": "query",
                },
                "filter_language": {
                    "openapi_types": (str,),
                    "attribute": "filter[language]",
                    "location": "query",
                },
                "filter_ecosystem": {
                    "openapi_types": (VulnerabilityEcosystem,),
                    "attribute": "filter[ecosystem]",
                    "location": "query",
                },
                "filter_code_location_location": {
                    "openapi_types": (str,),
                    "attribute": "filter[code_location.location]",
                    "location": "query",
                },
                "filter_code_location_file_path": {
                    "openapi_types": (str,),
                    "attribute": "filter[code_location.file_path]",
                    "location": "query",
                },
                "filter_code_location_method": {
                    "openapi_types": (str,),
                    "attribute": "filter[code_location.method]",
                    "location": "query",
                },
                "filter_fix_available": {
                    "openapi_types": (bool,),
                    "attribute": "filter[fix_available]",
                    "location": "query",
                },
                "filter_repo_digests": {
                    "openapi_types": (str,),
                    "attribute": "filter[repo_digests]",
                    "location": "query",
                },
                "filter_origin": {
                    "openapi_types": (str,),
                    "attribute": "filter[origin]",
                    "location": "query",
                },
                "filter_running_kernel": {
                    "openapi_types": (bool,),
                    "attribute": "filter[running_kernel]",
                    "location": "query",
                },
                "filter_asset_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.name]",
                    "location": "query",
                },
                "filter_asset_type": {
                    "openapi_types": (AssetType,),
                    "attribute": "filter[asset.type]",
                    "location": "query",
                },
                "filter_asset_version_first": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.version.first]",
                    "location": "query",
                },
                "filter_asset_version_last": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.version.last]",
                    "location": "query",
                },
                "filter_asset_repository_url": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.repository_url]",
                    "location": "query",
                },
                "filter_asset_risks_in_production": {
                    "openapi_types": (bool,),
                    "attribute": "filter[asset.risks.in_production]",
                    "location": "query",
                },
                "filter_asset_risks_under_attack": {
                    "openapi_types": (bool,),
                    "attribute": "filter[asset.risks.under_attack]",
                    "location": "query",
                },
                "filter_asset_risks_is_publicly_accessible": {
                    "openapi_types": (bool,),
                    "attribute": "filter[asset.risks.is_publicly_accessible]",
                    "location": "query",
                },
                "filter_asset_risks_has_privileged_access": {
                    "openapi_types": (bool,),
                    "attribute": "filter[asset.risks.has_privileged_access]",
                    "location": "query",
                },
                "filter_asset_risks_has_access_to_sensitive_data": {
                    "openapi_types": (bool,),
                    "attribute": "filter[asset.risks.has_access_to_sensitive_data]",
                    "location": "query",
                },
                "filter_asset_environments": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.environments]",
                    "location": "query",
                },
                "filter_asset_teams": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.teams]",
                    "location": "query",
                },
                "filter_asset_arch": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.arch]",
                    "location": "query",
                },
                "filter_asset_operating_system_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.operating_system.name]",
                    "location": "query",
                },
                "filter_asset_operating_system_version": {
                    "openapi_types": (str,),
                    "attribute": "filter[asset.operating_system.version]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_vulnerable_assets_endpoint = _Endpoint(
            settings={
                "response_type": (ListVulnerableAssetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerable-assets",
                "operation_id": "list_vulnerable_assets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_token": {
                    "openapi_types": (str,),
                    "attribute": "page[token]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[name]",
                    "location": "query",
                },
                "filter_type": {
                    "openapi_types": (AssetType,),
                    "attribute": "filter[type]",
                    "location": "query",
                },
                "filter_version_first": {
                    "openapi_types": (str,),
                    "attribute": "filter[version.first]",
                    "location": "query",
                },
                "filter_version_last": {
                    "openapi_types": (str,),
                    "attribute": "filter[version.last]",
                    "location": "query",
                },
                "filter_repository_url": {
                    "openapi_types": (str,),
                    "attribute": "filter[repository_url]",
                    "location": "query",
                },
                "filter_risks_in_production": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.in_production]",
                    "location": "query",
                },
                "filter_risks_under_attack": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.under_attack]",
                    "location": "query",
                },
                "filter_risks_is_publicly_accessible": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.is_publicly_accessible]",
                    "location": "query",
                },
                "filter_risks_has_privileged_access": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.has_privileged_access]",
                    "location": "query",
                },
                "filter_risks_has_access_to_sensitive_data": {
                    "openapi_types": (bool,),
                    "attribute": "filter[risks.has_access_to_sensitive_data]",
                    "location": "query",
                },
                "filter_environments": {
                    "openapi_types": (str,),
                    "attribute": "filter[environments]",
                    "location": "query",
                },
                "filter_teams": {
                    "openapi_types": (str,),
                    "attribute": "filter[teams]",
                    "location": "query",
                },
                "filter_arch": {
                    "openapi_types": (str,),
                    "attribute": "filter[arch]",
                    "location": "query",
                },
                "filter_operating_system_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[operating_system.name]",
                    "location": "query",
                },
                "filter_operating_system_version": {
                    "openapi_types": (str,),
                    "attribute": "filter[operating_system.version]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._mute_security_findings_endpoint = _Endpoint(
            settings={
                "response_type": (MuteFindingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/mute",
                "operation_id": "mute_security_findings",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MuteFindingsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._patch_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/signals/notification_rules/{id}",
                "operation_id": "patch_signal_notification_rule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchNotificationRuleParameters,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._patch_vulnerability_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/vulnerabilities/notification_rules/{id}",
                "operation_id": "patch_vulnerability_notification_rule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchNotificationRuleParameters,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._reorder_security_findings_automation_due_date_rules_endpoint = _Endpoint(
            settings={
                "response_type": (DueDateRuleReorderRequest,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/due_date_rules/reorder",
                "operation_id": "reorder_security_findings_automation_due_date_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DueDateRuleReorderRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._reorder_security_findings_automation_mute_rules_endpoint = _Endpoint(
            settings={
                "response_type": (MuteRuleReorderRequest,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/mute_rules/reorder",
                "operation_id": "reorder_security_findings_automation_mute_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MuteRuleReorderRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._reorder_security_findings_automation_ticket_creation_rules_endpoint = _Endpoint(
            settings={
                "response_type": (TicketCreationRuleReorderRequest,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/ticket_creation_rules/reorder",
                "operation_id": "reorder_security_findings_automation_ticket_creation_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TicketCreationRuleReorderRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._restore_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}/restore/{version}",
                "operation_id": "restore_security_monitoring_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "version": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "version",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._run_historical_job_endpoint = _Endpoint(
            settings={
                "response_type": (JobCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/jobs",
                "operation_id": "run_historical_job",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RunHistoricalJobRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_security_findings_endpoint = _Endpoint(
            settings={
                "response_type": (ListSecurityFindingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/search",
                "operation_id": "search_security_findings",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityFindingsSearchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_security_monitoring_histsignals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/siem-historical-detections/histsignals/search",
                "operation_id": "search_security_monitoring_histsignals",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "openapi_types": (SecurityMonitoringSignalListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._search_security_monitoring_signals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/signals/search",
                "operation_id": "search_security_monitoring_signals",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "openapi_types": (SecurityMonitoringSignalListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._send_security_monitoring_notification_preview_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRulePreviewResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/notification_rules/send_notification_preview",
                "operation_id": "send_security_monitoring_notification_preview",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateNotificationRuleParameters,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._test_existing_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleTestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}/test",
                "operation_id": "test_existing_security_monitoring_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleTestRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._test_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleTestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/test",
                "operation_id": "test_security_monitoring_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleTestRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_custom_framework_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateCustomFrameworkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_security_management/custom_frameworks/{handle}/{version}",
                "operation_id": "update_custom_framework",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "handle": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "handle",
                    "location": "path",
                },
                "version": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "version",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateCustomFrameworkRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_findings_assignee_endpoint = _Endpoint(
            settings={
                "response_type": (AssigneeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/findings/assignee",
                "operation_id": "update_findings_assignee",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AssigneeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_resource_evaluation_filters_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateResourceEvaluationFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_security_management/resource_filters",
                "operation_id": "update_resource_evaluation_filters",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UpdateResourceEvaluationFiltersRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/{security_filter_id}",
                "operation_id": "update_security_filter",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "security_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "security_filter_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_findings_automation_due_date_rule_endpoint = _Endpoint(
            settings={
                "response_type": (DueDateRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/due_date_rules/{rule_id}",
                "operation_id": "update_security_findings_automation_due_date_rule",
                "http_method": "PUT",
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
                    "openapi_types": (DueDateRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_findings_automation_mute_rule_endpoint = _Endpoint(
            settings={
                "response_type": (MuteRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/mute_rules/{rule_id}",
                "operation_id": "update_security_findings_automation_mute_rule",
                "http_method": "PUT",
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
                    "openapi_types": (MuteRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_findings_automation_ticket_creation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (TicketCreationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security/findings/automation/ticket_creation_rules/{rule_id}",
                "operation_id": "update_security_findings_automation_ticket_creation_rule",
                "http_method": "PUT",
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
                    "openapi_types": (TicketCreationRuleUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_monitoring_critical_asset_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringCriticalAssetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/critical_assets/{critical_asset_id}",
                "operation_id": "update_security_monitoring_critical_asset",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "critical_asset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "critical_asset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringCriticalAssetUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_monitoring_dataset_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/datasets/{dataset_id}",
                "operation_id": "update_security_monitoring_dataset",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringDatasetUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_monitoring_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringIntegrationConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config/{integration_config_id}",
                "operation_id": "update_security_monitoring_integration_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "integration_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_config_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringIntegrationConfigUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}",
                "operation_id": "update_security_monitoring_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleUpdatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_monitoring_suppression_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSuppressionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/{suppression_id}",
                "operation_id": "update_security_monitoring_suppression",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "suppression_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "suppression_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSuppressionUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_security_monitoring_integration_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config/{integration_config_id}/validate",
                "operation_id": "validate_security_monitoring_integration_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "integration_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_config_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._validate_security_monitoring_integration_credentials_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/integration_config/validate",
                "operation_id": "validate_security_monitoring_integration_credentials",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringIntegrationCredentialsValidateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/rules/validation",
                "operation_id": "validate_security_monitoring_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleValidatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_security_monitoring_suppression_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions/validation",
                "operation_id": "validate_security_monitoring_suppression",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringSuppressionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def activate_content_pack(
        self,
        content_pack_id: str,
    ) -> None:
        """Activate content pack.

        Activate a Cloud SIEM content pack. This operation configures the necessary
        log filters or security filters depending on the pricing model and updates the content
        pack activation state.

        :param content_pack_id: The ID of the content pack to activate (for example, ``aws-cloudtrail`` ).
        :type content_pack_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["content_pack_id"] = content_pack_id

        return self._activate_content_pack_endpoint.call_with_http_info(**kwargs)

    def attach_case(
        self,
        case_id: str,
        body: AttachCaseRequest,
    ) -> FindingCaseResponse:
        """Attach security findings to a case.

        Attach security findings to a case.
        You can attach up to 50 security findings per case. Security findings that are already attached to another case will be detached from their previous case and attached to the specified case.

        :param case_id: Unique identifier of the case to attach security findings to
        :type case_id: str
        :type body: AttachCaseRequest
        :rtype: FindingCaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_id"] = case_id

        kwargs["body"] = body

        return self._attach_case_endpoint.call_with_http_info(**kwargs)

    def attach_jira_issue(
        self,
        body: AttachJiraIssueRequest,
    ) -> FindingCaseResponse:
        """Attach security findings to a Jira issue.

        Attach security findings to a Jira issue by providing the Jira issue URL.
        You can attach up to 50 security findings per Jira issue. If the Jira issue is not linked to any case, this operation will create a case for the security findings and link the Jira issue to the newly created case. To configure the Jira integration, see `Bidirectional ticket syncing with Jira <https://docs.datadoghq.com/security/ticketing_integrations/#bidirectional-ticket-syncing-with-jira>`_. Security findings that are already attached to another Jira issue will be detached from their previous Jira issue and attached to the specified Jira issue.

        :type body: AttachJiraIssueRequest
        :rtype: FindingCaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._attach_jira_issue_endpoint.call_with_http_info(**kwargs)

    def attach_linear_issue(
        self,
        body: AttachLinearIssueRequest,
    ) -> FindingCaseResponse:
        """Attach security findings to a Linear issue.

        Attach security findings to a Linear issue by providing the Linear issue URL.
        You can attach up to 50 security findings per Linear issue. If the Linear issue is not linked to any case, this operation will create a case for the security findings and link the Linear issue to the newly created case. Security findings that are already attached to another Linear issue will be detached from their previous Linear issue and attached to the specified Linear issue.

        :type body: AttachLinearIssueRequest
        :rtype: FindingCaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._attach_linear_issue_endpoint.call_with_http_info(**kwargs)

    def attach_service_now_ticket(
        self,
        body: AttachServiceNowTicketRequest,
    ) -> FindingCaseResponse:
        """Attach security findings to a ServiceNow ticket.

        Attach security findings to a ServiceNow ticket by providing the ServiceNow ticket URL.
        You can attach up to 50 security findings per ServiceNow ticket. If the ServiceNow ticket is not linked to any case, this operation will create a case for the security findings and link the ServiceNow ticket to the newly created case. Security findings that are already attached to another ServiceNow ticket will be detached from their previous ServiceNow ticket and attached to the specified ServiceNow ticket.

        :type body: AttachServiceNowTicketRequest
        :rtype: FindingCaseResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._attach_service_now_ticket_endpoint.call_with_http_info(**kwargs)

    def batch_get_security_monitoring_dataset_dependencies(
        self,
        body: SecurityMonitoringDatasetDependenciesRequest,
    ) -> SecurityMonitoringDatasetDependenciesResponse:
        """Get dataset dependencies.

        Return, for each of the requested datasets, the list of detection rules that depend
        on it. Useful for understanding the impact of updating or deleting a dataset.

        :type body: SecurityMonitoringDatasetDependenciesRequest
        :rtype: SecurityMonitoringDatasetDependenciesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._batch_get_security_monitoring_dataset_dependencies_endpoint.call_with_http_info(**kwargs)

    def bulk_convert_existing_security_monitoring_rules(
        self,
        body: SecurityMonitoringRuleConvertBulkPayload,
    ) -> file_type:
        """Bulk convert rules to Terraform.

        Convert a list of existing security monitoring rules to Terraform for the Datadog provider
        resource ``datadog_security_monitoring_rule``. Returns a ZIP archive containing one Terraform
        file per rule. You can convert rules for the following types:

        * App and API Protection
        * Cloud SIEM (log detection and signal correlation)
        * Workload Protection

        :type body: SecurityMonitoringRuleConvertBulkPayload
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_convert_existing_security_monitoring_rules_endpoint.call_with_http_info(**kwargs)

    def bulk_create_sample_log_generation_subscriptions(
        self,
        body: SampleLogGenerationBulkSubscriptionRequest,
    ) -> SampleLogGenerationBulkSubscriptionResponse:
        """Bulk subscribe to sample log generation.

        Subscribe to sample log generation for multiple Cloud SIEM content packs in a single call.
        Each requested content pack is processed independently; the response includes a per-item
        status so partial successes can be inspected.

        **Availability** : this endpoint is restricted to Cloud SIEM trial organizations on an
        eligible pricing model. Non-trial orgs receive ``403 Forbidden`` , the feature flag may also reject
        requests with ``400 Bad Request`` , and legacy pricing tiers receive per-item responses with ``status: not_available``.

        :param body: The content packs to subscribe to and the desired duration of the subscriptions.
        :type body: SampleLogGenerationBulkSubscriptionRequest
        :rtype: SampleLogGenerationBulkSubscriptionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_create_sample_log_generation_subscriptions_endpoint.call_with_http_info(**kwargs)

    def bulk_delete_security_monitoring_rules(
        self,
        body: SecurityMonitoringRuleBulkDeletePayload,
    ) -> SecurityMonitoringRuleBulkDeleteResponse:
        """Bulk delete security monitoring rules.

        Delete multiple security monitoring rules in a single request. Default rules cannot be deleted.

        :type body: SecurityMonitoringRuleBulkDeletePayload
        :rtype: SecurityMonitoringRuleBulkDeleteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_delete_security_monitoring_rules_endpoint.call_with_http_info(**kwargs)

    def bulk_edit_security_monitoring_signals(
        self,
        body: SecurityMonitoringSignalsBulkUpdateRequest,
    ) -> SecurityMonitoringSignalsBulkTriageUpdateResponse:
        """Bulk update security signals.

        Update the triage state or assignee of multiple security signals at once.
        The maximum number of signals that can be updated in a single request is 199.

        :param body: Attributes describing the signal updates.
        :type body: SecurityMonitoringSignalsBulkUpdateRequest
        :rtype: SecurityMonitoringSignalsBulkTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_edit_security_monitoring_signals_endpoint.call_with_http_info(**kwargs)

    def bulk_edit_security_monitoring_signals_assignee(
        self,
        body: SecurityMonitoringSignalsBulkAssigneeUpdateRequest,
    ) -> SecurityMonitoringSignalsBulkTriageUpdateResponse:
        """Bulk update triage assignee of security signals.

        Change the triage assignees of multiple security signals at once.
        The maximum number of signals that can be updated in a single request is 199.

        :param body: Attributes describing the signal assignee updates.
        :type body: SecurityMonitoringSignalsBulkAssigneeUpdateRequest
        :rtype: SecurityMonitoringSignalsBulkTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_edit_security_monitoring_signals_assignee_endpoint.call_with_http_info(**kwargs)

    def bulk_edit_security_monitoring_signals_state(
        self,
        body: SecurityMonitoringSignalsBulkStateUpdateRequest,
    ) -> SecurityMonitoringSignalsBulkTriageUpdateResponse:
        """Bulk update triage state of security signals.

        Change the triage states of multiple security signals at once.
        The maximum number of signals that can be updated in a single request is 199.

        :param body: Attributes describing the signal state updates.
        :type body: SecurityMonitoringSignalsBulkStateUpdateRequest
        :rtype: SecurityMonitoringSignalsBulkTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_edit_security_monitoring_signals_state_endpoint.call_with_http_info(**kwargs)

    def bulk_export_security_monitoring_rules(
        self,
        body: SecurityMonitoringRuleBulkExportPayload,
    ) -> file_type:
        """Bulk export security monitoring rules.

        Export a list of security monitoring rules as a ZIP file containing JSON rule definitions.
        The endpoint accepts a list of rule IDs and returns a ZIP archive where each rule is
        saved as a separate JSON file named after the rule.

        :type body: SecurityMonitoringRuleBulkExportPayload
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_export_security_monitoring_rules_endpoint.call_with_http_info(**kwargs)

    def bulk_export_security_monitoring_terraform_resources(
        self,
        resource_type: SecurityMonitoringTerraformResourceType,
        body: SecurityMonitoringTerraformBulkExportRequest,
    ) -> file_type:
        """Export security monitoring resources to Terraform.

        Export multiple security monitoring resources to Terraform, packaged as a zip archive.
        The ``resource_type`` path parameter specifies the type of resources to export
        and must be one of ``suppressions`` , ``critical_assets`` , ``security_filters`` , or ``rules``.
        A maximum of 1000 resources can be exported in a single request.
        For ``rules`` , partner rules cannot be exported and return a 400 error.

        :param resource_type: The type of security monitoring resource to export.
        :type resource_type: SecurityMonitoringTerraformResourceType
        :param body: The resource IDs to export.
        :type body: SecurityMonitoringTerraformBulkExportRequest
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_type"] = resource_type

        kwargs["body"] = body

        return self._bulk_export_security_monitoring_terraform_resources_endpoint.call_with_http_info(**kwargs)

    def cancel_historical_job(
        self,
        job_id: str,
    ) -> None:
        """Cancel a historical job.

        Cancel a historical job.

        :param job_id: The ID of the job.
        :type job_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["job_id"] = job_id

        return self._cancel_historical_job_endpoint.call_with_http_info(**kwargs)

    def convert_existing_security_monitoring_rule(
        self,
        rule_id: str,
    ) -> SecurityMonitoringRuleConvertResponse:
        """Convert an existing rule from JSON to Terraform.

        Convert an existing rule from JSON to Terraform for Datadog provider
        resource ``datadog_security_monitoring_rule``. You can do so for the following rule types:

        * App and API Protection
        * Cloud SIEM (log detection and signal correlation)
        * Workload Protection

        You can convert Cloud Security configuration rules using Terraform's `Datadog Cloud Configuration Rule resource <https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/cloud_configuration_rule>`_.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: SecurityMonitoringRuleConvertResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._convert_existing_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def convert_job_result_to_signal(
        self,
        body: ConvertJobResultsToSignalsRequest,
    ) -> None:
        """Convert a job result to a signal.

        Convert a job result to a signal.

        :type body: ConvertJobResultsToSignalsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._convert_job_result_to_signal_endpoint.call_with_http_info(**kwargs)

    def convert_security_monitoring_rule_from_json_to_terraform(
        self,
        body: Union[
            SecurityMonitoringRuleConvertPayload,
            SecurityMonitoringStandardRulePayload,
            SecurityMonitoringSignalRulePayload,
        ],
    ) -> SecurityMonitoringRuleConvertResponse:
        """Convert a rule from JSON to Terraform.

        Convert a rule that doesn't (yet) exist from JSON to Terraform for Datadog provider
        resource ``datadog_security_monitoring_rule``. You can do so for the following rule types:

        * App and API Protection
        * Cloud SIEM (log detection and signal correlation)
        * Workload Protection

        You can convert Cloud Security configuration rules using Terraform's `Datadog Cloud Configuration Rule resource <https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/cloud_configuration_rule>`_.

        :type body: SecurityMonitoringRuleConvertPayload
        :rtype: SecurityMonitoringRuleConvertResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._convert_security_monitoring_rule_from_json_to_terraform_endpoint.call_with_http_info(**kwargs)

    def convert_security_monitoring_terraform_resource(
        self,
        resource_type: SecurityMonitoringTerraformResourceType,
        body: SecurityMonitoringTerraformConvertRequest,
    ) -> SecurityMonitoringTerraformExportResponse:
        """Convert security monitoring resource to Terraform.

        Convert a security monitoring resource that doesn't (yet) exist from JSON to Terraform.
        The ``resource_type`` path parameter specifies the type of resource to convert
        and must be one of ``suppressions`` , ``critical_assets`` , ``security_filters`` , or ``rules``.

        :param resource_type: The type of security monitoring resource to export.
        :type resource_type: SecurityMonitoringTerraformResourceType
        :param body: The resource JSON to convert.
        :type body: SecurityMonitoringTerraformConvertRequest
        :rtype: SecurityMonitoringTerraformExportResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_type"] = resource_type

        kwargs["body"] = body

        return self._convert_security_monitoring_terraform_resource_endpoint.call_with_http_info(**kwargs)

    def create_cases(
        self,
        body: CreateCaseRequestArray,
    ) -> FindingCaseResponseArray:
        """Create cases for security findings.

        Create cases for security findings.
        You can create up to 50 cases per request and associate up to 50 security findings per case. Security findings that are already attached to another case will be detached from their previous case and attached to the newly created case.

        :type body: CreateCaseRequestArray
        :rtype: FindingCaseResponseArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cases_endpoint.call_with_http_info(**kwargs)

    def create_custom_framework(
        self,
        body: CreateCustomFrameworkRequest,
    ) -> CreateCustomFrameworkResponse:
        """Create a custom framework.

        Create a custom framework.

        :type body: CreateCustomFrameworkRequest
        :rtype: CreateCustomFrameworkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_custom_framework_endpoint.call_with_http_info(**kwargs)

    def create_io_c_triage_state(
        self,
        body: IoCTriageWriteRequest,
    ) -> IoCTriageWriteResponse:
        """Create or update an indicator triage state.

        Set the triage state of an indicator of compromise (IoC). This creates or
        updates the triage state for the indicator in your organization.

        :param body: The triage state to set for the indicator.
        :type body: IoCTriageWriteRequest
        :rtype: IoCTriageWriteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_io_c_triage_state_endpoint.call_with_http_info(**kwargs)

    def create_jira_issues(
        self,
        body: CreateJiraIssueRequestArray,
    ) -> FindingCaseResponseArray:
        """Create Jira issues for security findings.

        Create Jira issues for security findings.
        This operation creates a case in Datadog and a Jira issue linked to that case for bidirectional sync between Datadog and Jira. To configure the Jira integration, see `Bidirectional ticket syncing with Jira <https://docs.datadoghq.com/security/ticketing_integrations/#bidirectional-ticket-syncing-with-jira>`_. You can create up to 50 Jira issues per request and associate up to 50 security findings per Jira issue. Security findings that are already attached to another Jira issue will be detached from their previous Jira issue and attached to the newly created Jira issue.

        :type body: CreateJiraIssueRequestArray
        :rtype: FindingCaseResponseArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_jira_issues_endpoint.call_with_http_info(**kwargs)

    def create_linear_issues(
        self,
        body: CreateLinearIssueRequestArray,
    ) -> FindingCaseResponseArray:
        """Create Linear issues for security findings.

        Create Linear issues for security findings.
        This operation creates a case in Datadog and a Linear issue linked to that case for bidirectional sync between Datadog and Linear. You can create up to 50 Linear issues per request and associate up to 50 security findings per Linear issue. Security findings that are already attached to another Linear issue will be detached from their previous Linear issue and attached to the newly created Linear issue.

        :type body: CreateLinearIssueRequestArray
        :rtype: FindingCaseResponseArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_linear_issues_endpoint.call_with_http_info(**kwargs)

    def create_sample_log_generation_subscription(
        self,
        body: SampleLogGenerationSubscriptionCreateRequest,
    ) -> SampleLogGenerationSubscriptionResponse:
        """Subscribe to sample log generation.

        Subscribe to sample log generation for a Cloud SIEM content pack. Sample logs for the
        requested content pack are injected into the Logs platform for the duration of the subscription,
        so detection rules can be exercised without onboarding the underlying integration first.

        **Availability** : this endpoint is restricted to Cloud SIEM trial organizations on an
        eligible pricing model. Non-trial orgs receive ``403 Forbidden`` , the feature flag may also reject
        requests with ``400 Bad Request`` , and legacy pricing tiers receive a response with ``status: not_available``.

        :param body: The content pack to subscribe to and the desired duration of the subscription.
        :type body: SampleLogGenerationSubscriptionCreateRequest
        :rtype: SampleLogGenerationSubscriptionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_sample_log_generation_subscription_endpoint.call_with_http_info(**kwargs)

    def create_security_filter(
        self,
        body: SecurityFilterCreateRequest,
    ) -> SecurityFilterResponse:
        """Create a security filter.

        Create a security filter.

        See the `security filter guide <https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/>`_
        for more examples.

        :param body: The definition of the new security filter.
        :type body: SecurityFilterCreateRequest
        :rtype: SecurityFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_filter_endpoint.call_with_http_info(**kwargs)

    def create_security_findings_automation_due_date_rule(
        self,
        body: DueDateRuleCreateRequest,
    ) -> DueDateRuleResponse:
        """Create a due date rule.

        Create a new due date rule for the current organization.

        :type body: DueDateRuleCreateRequest
        :rtype: DueDateRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_findings_automation_due_date_rule_endpoint.call_with_http_info(**kwargs)

    def create_security_findings_automation_mute_rule(
        self,
        body: MuteRuleCreateRequest,
    ) -> MuteRuleResponse:
        """Create a mute rule.

        Create a new mute rule for the current organization.

        :type body: MuteRuleCreateRequest
        :rtype: MuteRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_findings_automation_mute_rule_endpoint.call_with_http_info(**kwargs)

    def create_security_findings_automation_ticket_creation_rule(
        self,
        body: TicketCreationRuleCreateRequest,
    ) -> TicketCreationRuleResponse:
        """Create a ticket creation rule.

        Create a new ticket creation rule for the current organization.

        :type body: TicketCreationRuleCreateRequest
        :rtype: TicketCreationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_findings_automation_ticket_creation_rule_endpoint.call_with_http_info(**kwargs)

    def create_security_monitoring_critical_asset(
        self,
        body: SecurityMonitoringCriticalAssetCreateRequest,
    ) -> SecurityMonitoringCriticalAssetResponse:
        """Create a critical asset.

        Create a new critical asset.

        :param body: The definition of the new critical asset.
        :type body: SecurityMonitoringCriticalAssetCreateRequest
        :rtype: SecurityMonitoringCriticalAssetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_monitoring_critical_asset_endpoint.call_with_http_info(**kwargs)

    def create_security_monitoring_dataset(
        self,
        body: SecurityMonitoringDatasetCreateRequest,
    ) -> SecurityMonitoringDatasetCreateResponse:
        """Create a dataset.

        Create a new Cloud SIEM dataset. A dataset bundles a data source, a set of
        indexes, and a search query that can be referenced from detection rules.

        :type body: SecurityMonitoringDatasetCreateRequest
        :rtype: SecurityMonitoringDatasetCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_monitoring_dataset_endpoint.call_with_http_info(**kwargs)

    def create_security_monitoring_integration_config(
        self,
        body: SecurityMonitoringIntegrationConfigCreateRequest,
    ) -> SecurityMonitoringIntegrationConfigResponse:
        """Create an entity context sync configuration.

        Create a new entity context sync configuration so Cloud SIEM can ingest entities from an external
        source. The credentials provided in ``secrets`` are validated against the source before the configuration
        is stored and never returned in subsequent responses.

        :param body: The definition of the new integration configuration.
        :type body: SecurityMonitoringIntegrationConfigCreateRequest
        :rtype: SecurityMonitoringIntegrationConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_monitoring_integration_config_endpoint.call_with_http_info(**kwargs)

    def create_security_monitoring_rule(
        self,
        body: Union[
            SecurityMonitoringRuleCreatePayload,
            SecurityMonitoringStandardRuleCreatePayload,
            SecurityMonitoringSignalRuleCreatePayload,
            CloudConfigurationRuleCreatePayload,
        ],
    ) -> SecurityMonitoringRuleResponse:
        """Create a detection rule.

        Create a detection rule.

        :type body: SecurityMonitoringRuleCreatePayload
        :rtype: SecurityMonitoringRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def create_security_monitoring_suppression(
        self,
        body: SecurityMonitoringSuppressionCreateRequest,
    ) -> SecurityMonitoringSuppressionResponse:
        """Create a suppression rule.

        Create a new suppression rule.

        :param body: The definition of the new suppression rule.
        :type body: SecurityMonitoringSuppressionCreateRequest
        :rtype: SecurityMonitoringSuppressionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_security_monitoring_suppression_endpoint.call_with_http_info(**kwargs)

    def create_service_now_tickets(
        self,
        body: CreateServiceNowTicketRequestArray,
    ) -> FindingCaseResponseArray:
        """Create ServiceNow tickets for security findings.

        Create ServiceNow tickets for security findings.
        This operation creates a case in Datadog and a ServiceNow ticket linked to that case for bidirectional sync between Datadog and ServiceNow. You can create up to 50 ServiceNow tickets per request and associate up to 50 security findings per ServiceNow ticket. Security findings that are already attached to another ServiceNow ticket will be detached from their previous ServiceNow ticket and attached to the newly created ServiceNow ticket.

        :type body: CreateServiceNowTicketRequestArray
        :rtype: FindingCaseResponseArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_service_now_tickets_endpoint.call_with_http_info(**kwargs)

    def create_signal_notification_rule(
        self,
        body: CreateNotificationRuleParameters,
    ) -> NotificationRuleResponse:
        """Create a new signal-based notification rule.

        Create a new notification rule for security signals and return the created rule.

        :param body: The body of the create notification rule request is composed of the rule type and the rule attributes:
            the rule name, the selectors, the notification targets, and the rule enabled status.
        :type body: CreateNotificationRuleParameters
        :rtype: NotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_signal_notification_rule_endpoint.call_with_http_info(**kwargs)

    def create_static_analysis_ast(
        self,
        body: GetAstRequest,
    ) -> GetAstResponse:
        """Get AST for source code.

        Parse source code into an abstract syntax tree (AST) for the specified language.

        :type body: GetAstRequest
        :rtype: GetAstResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_static_analysis_ast_endpoint.call_with_http_info(**kwargs)

    def create_static_analysis_server_analysis(
        self,
        body: AnalysisRequest,
    ) -> AnalysisResponse:
        """Analyze code.

        Run static analysis rules against a source code file and return violations found.

        :type body: AnalysisRequest
        :rtype: AnalysisResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_static_analysis_server_analysis_endpoint.call_with_http_info(**kwargs)

    def create_vulnerability_notification_rule(
        self,
        body: CreateNotificationRuleParameters,
    ) -> NotificationRuleResponse:
        """Create a new vulnerability-based notification rule.

        Create a new notification rule for security vulnerabilities and return the created rule.

        :param body: The body of the create notification rule request is composed of the rule type and the rule attributes:
            the rule name, the selectors, the notification targets, and the rule enabled status.
        :type body: CreateNotificationRuleParameters
        :rtype: NotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_vulnerability_notification_rule_endpoint.call_with_http_info(**kwargs)

    def deactivate_content_pack(
        self,
        content_pack_id: str,
    ) -> None:
        """Deactivate content pack.

        Deactivate a Cloud SIEM content pack. This operation removes the content pack's
        configuration from log filters or security filters and updates the content pack activation state.

        :param content_pack_id: The ID of the content pack to deactivate (for example, ``aws-cloudtrail`` ).
        :type content_pack_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["content_pack_id"] = content_pack_id

        return self._deactivate_content_pack_endpoint.call_with_http_info(**kwargs)

    def delete_custom_framework(
        self,
        handle: str,
        version: str,
    ) -> DeleteCustomFrameworkResponse:
        """Delete a custom framework.

        Delete a custom framework.

        :param handle: The framework handle
        :type handle: str
        :param version: The framework version
        :type version: str
        :rtype: DeleteCustomFrameworkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle"] = handle

        kwargs["version"] = version

        return self._delete_custom_framework_endpoint.call_with_http_info(**kwargs)

    def delete_historical_job(
        self,
        job_id: str,
    ) -> None:
        """Delete an existing job.

        Delete an existing job.

        :param job_id: The ID of the job.
        :type job_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["job_id"] = job_id

        return self._delete_historical_job_endpoint.call_with_http_info(**kwargs)

    def delete_sample_log_generation_subscription(
        self,
        content_pack_id: str,
    ) -> SampleLogGenerationSubscriptionResponse:
        """Unsubscribe from sample log generation.

        Unsubscribe from sample log generation for a Cloud SIEM content pack.
        After unsubscribing, no more sample logs are generated for the requested content pack.

        **Availability** : this endpoint is restricted to Cloud SIEM trial organizations on an
        eligible pricing model. Non-trial orgs receive ``403 Forbidden`` , the feature flag may also reject
        requests with ``400 Bad Request`` , and legacy pricing tiers receive a response with ``status: not_available``.

        :param content_pack_id: The identifier of the Cloud SIEM content pack to operate on (for example, ``aws-cloudtrail`` ).
        :type content_pack_id: str
        :rtype: SampleLogGenerationSubscriptionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["content_pack_id"] = content_pack_id

        return self._delete_sample_log_generation_subscription_endpoint.call_with_http_info(**kwargs)

    def delete_security_filter(
        self,
        security_filter_id: str,
    ) -> None:
        """Delete a security filter.

        Delete a specific security filter.

        :param security_filter_id: The ID of the security filter.
        :type security_filter_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["security_filter_id"] = security_filter_id

        return self._delete_security_filter_endpoint.call_with_http_info(**kwargs)

    def delete_security_findings_automation_due_date_rule(
        self,
        rule_id: UUID,
    ) -> None:
        """Delete a due date rule.

        Delete an existing due date rule by ID.

        :param rule_id: The ID of the due date rule.
        :type rule_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_security_findings_automation_due_date_rule_endpoint.call_with_http_info(**kwargs)

    def delete_security_findings_automation_mute_rule(
        self,
        rule_id: UUID,
    ) -> None:
        """Delete a mute rule.

        Delete an existing mute rule by ID.

        :param rule_id: The ID of the mute rule.
        :type rule_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_security_findings_automation_mute_rule_endpoint.call_with_http_info(**kwargs)

    def delete_security_findings_automation_ticket_creation_rule(
        self,
        rule_id: UUID,
    ) -> None:
        """Delete a ticket creation rule.

        Delete an existing ticket creation rule by ID.

        :param rule_id: The ID of the ticket creation rule.
        :type rule_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_security_findings_automation_ticket_creation_rule_endpoint.call_with_http_info(**kwargs)

    def delete_security_monitoring_critical_asset(
        self,
        critical_asset_id: str,
    ) -> None:
        """Delete a critical asset.

        Delete a specific critical asset.

        :param critical_asset_id: The ID of the critical asset.
        :type critical_asset_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["critical_asset_id"] = critical_asset_id

        return self._delete_security_monitoring_critical_asset_endpoint.call_with_http_info(**kwargs)

    def delete_security_monitoring_dataset(
        self,
        dataset_id: str,
    ) -> None:
        """Delete a dataset.

        Delete a Cloud SIEM dataset. Out-of-the-box datasets cannot be deleted and
        deleting a dataset that is referenced by a detection rule is rejected.

        :param dataset_id: The UUID of the dataset.
        :type dataset_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        return self._delete_security_monitoring_dataset_endpoint.call_with_http_info(**kwargs)

    def delete_security_monitoring_integration_config(
        self,
        integration_config_id: str,
    ) -> None:
        """Delete an entity context sync configuration.

        Delete an entity context sync configuration. Cloud SIEM stops ingesting entities from this source,
        and the credentials stored for the configuration are removed from the secrets store.

        :param integration_config_id: The ID of the entity context sync configuration.
        :type integration_config_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_config_id"] = integration_config_id

        return self._delete_security_monitoring_integration_config_endpoint.call_with_http_info(**kwargs)

    def delete_security_monitoring_rule(
        self,
        rule_id: str,
    ) -> None:
        """Delete an existing rule.

        Delete an existing rule. Default rules cannot be deleted.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def delete_security_monitoring_suppression(
        self,
        suppression_id: str,
    ) -> None:
        """Delete a suppression rule.

        Delete a specific suppression rule.

        :param suppression_id: The ID of the suppression rule
        :type suppression_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["suppression_id"] = suppression_id

        return self._delete_security_monitoring_suppression_endpoint.call_with_http_info(**kwargs)

    def delete_signal_notification_rule(
        self,
        id: str,
    ) -> None:
        """Delete a signal-based notification rule.

        Delete a notification rule for security signals.

        :param id: ID of the notification rule.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_signal_notification_rule_endpoint.call_with_http_info(**kwargs)

    def delete_vulnerability_notification_rule(
        self,
        id: str,
    ) -> None:
        """Delete a vulnerability-based notification rule.

        Delete a notification rule for security vulnerabilities.

        :param id: ID of the notification rule.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_vulnerability_notification_rule_endpoint.call_with_http_info(**kwargs)

    def detach_case(
        self,
        body: DetachCaseRequest,
    ) -> None:
        """Detach security findings from their case.

        Detach security findings from their case.
        This operation dissociates security findings from their associated cases without deleting the cases themselves. You can detach security findings from multiple different cases in a single request, with a limit of 50 security findings per request. Security findings that are not currently attached to any case will be ignored.

        :type body: DetachCaseRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._detach_case_endpoint.call_with_http_info(**kwargs)

    def edit_security_monitoring_signal(
        self,
        signal_id: str,
        body: SecurityMonitoringSignalUpdateRequest,
    ) -> SecurityMonitoringSignalTriageUpdateResponse:
        """Update security signal triage state or assignee.

        Update the triage state or assignee of a security signal.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal triage state or assignee update.
        :type body: SecurityMonitoringSignalUpdateRequest
        :rtype: SecurityMonitoringSignalTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._edit_security_monitoring_signal_endpoint.call_with_http_info(**kwargs)

    def edit_security_monitoring_signal_assignee(
        self,
        signal_id: str,
        body: SecurityMonitoringSignalAssigneeUpdateRequest,
    ) -> SecurityMonitoringSignalTriageUpdateResponse:
        """Modify the triage assignee of a security signal.

        Modify the triage assignee of a security signal.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal update.
        :type body: SecurityMonitoringSignalAssigneeUpdateRequest
        :rtype: SecurityMonitoringSignalTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._edit_security_monitoring_signal_assignee_endpoint.call_with_http_info(**kwargs)

    def edit_security_monitoring_signal_incidents(
        self,
        signal_id: str,
        body: SecurityMonitoringSignalIncidentsUpdateRequest,
    ) -> SecurityMonitoringSignalTriageUpdateResponse:
        """Change the related incidents of a security signal.

        Change the related incidents for a security signal.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal update.
        :type body: SecurityMonitoringSignalIncidentsUpdateRequest
        :rtype: SecurityMonitoringSignalTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._edit_security_monitoring_signal_incidents_endpoint.call_with_http_info(**kwargs)

    def edit_security_monitoring_signal_state(
        self,
        signal_id: str,
        body: SecurityMonitoringSignalStateUpdateRequest,
    ) -> SecurityMonitoringSignalTriageUpdateResponse:
        """Change the triage state of a security signal.

        Change the triage state of a security signal.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param body: Attributes describing the signal update.
        :type body: SecurityMonitoringSignalStateUpdateRequest
        :rtype: SecurityMonitoringSignalTriageUpdateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        kwargs["body"] = body

        return self._edit_security_monitoring_signal_state_endpoint.call_with_http_info(**kwargs)

    def export_security_monitoring_terraform_resource(
        self,
        resource_type: SecurityMonitoringTerraformResourceType,
        resource_id: str,
    ) -> SecurityMonitoringTerraformExportResponse:
        """Export security monitoring resource to Terraform.

        Export a security monitoring resource to a Terraform configuration.
        The ``resource_type`` path parameter specifies the type of resource to export
        and must be one of ``suppressions`` , ``critical_assets`` , ``security_filters`` , or ``rules``.
        For ``rules`` , partner rules cannot be exported and return a 400 error.

        :param resource_type: The type of security monitoring resource to export.
        :type resource_type: SecurityMonitoringTerraformResourceType
        :param resource_id: The ID of the security monitoring resource to export.
        :type resource_id: str
        :rtype: SecurityMonitoringTerraformExportResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_type"] = resource_type

        kwargs["resource_id"] = resource_id

        return self._export_security_monitoring_terraform_resource_endpoint.call_with_http_info(**kwargs)

    def get_content_packs_states(
        self,
    ) -> SecurityMonitoringContentPackStatesResponse:
        """Get content pack states.

        Get the activation state, integration status, and log collection status
        for all Cloud SIEM content packs.

        :rtype: SecurityMonitoringContentPackStatesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_content_packs_states_endpoint.call_with_http_info(**kwargs)

    def get_critical_assets_affecting_rule(
        self,
        rule_id: str,
    ) -> SecurityMonitoringCriticalAssetsResponse:
        """Get critical assets affecting a specific rule.

        Get the list of critical assets that affect a specific existing rule by the rule's ID.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: SecurityMonitoringCriticalAssetsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_critical_assets_affecting_rule_endpoint.call_with_http_info(**kwargs)

    def get_custom_framework(
        self,
        handle: str,
        version: str,
    ) -> GetCustomFrameworkResponse:
        """Get a custom framework.

        Get a custom framework.

        :param handle: The framework handle
        :type handle: str
        :param version: The framework version
        :type version: str
        :rtype: GetCustomFrameworkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle"] = handle

        kwargs["version"] = version

        return self._get_custom_framework_endpoint.call_with_http_info(**kwargs)

    def get_entity_context(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        _from: Union[str, UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
        as_of: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        page_token: Union[str, UnsetType] = unset,
    ) -> EntityContextResponse:
        """Get entity context.

        Search the Cloud SIEM entity context store for entities that match a query, and return the historical
        revisions of each entity in the requested time range. The endpoint can either return revisions across an
        interval ( ``from`` / ``to`` ) or the snapshot of each entity at a single point in time ( ``as_of`` ); the two modes
        are mutually exclusive.

        :param query: A free-text query (for example, an email address or principal ID) used to filter the entities returned.
        :type query: str, optional
        :param _from: The start of the time range to query, as an RFC3339 timestamp or a relative time (for example, ``now-7d`` ).
            Defaults to ``now-7d``. Ignored when ``as_of`` is set.
        :type _from: str, optional
        :param to: The end of the time range to query, as an RFC3339 timestamp or a relative time (for example, ``now`` ).
            Defaults to ``now``. Ignored when ``as_of`` is set.
        :type to: str, optional
        :param as_of: A point in time at which to query the entity revisions, as an RFC3339 timestamp, a Unix timestamp
            (in seconds), or a relative time (for example, ``now-1d`` ). When set, ``from`` and ``to`` are ignored.
            Cannot be combined with custom ``from`` / ``to`` values.
        :type as_of: str, optional
        :param limit: The maximum number of entities to return.
        :type limit: int, optional
        :param page_token: An opaque token used to fetch the next page of results, as returned in ``meta.page.next_token`` of a previous response.
        :type page_token: str, optional
        :rtype: EntityContextResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if _from is not unset:
            kwargs["_from"] = _from

        if to is not unset:
            kwargs["to"] = to

        if as_of is not unset:
            kwargs["as_of"] = as_of

        if limit is not unset:
            kwargs["limit"] = limit

        if page_token is not unset:
            kwargs["page_token"] = page_token

        return self._get_entity_context_endpoint.call_with_http_info(**kwargs)

    def get_finding(
        self,
        finding_id: str,
        *,
        snapshot_timestamp: Union[int, UnsetType] = unset,
    ) -> GetFindingResponse:
        """Get a finding.

        Returns a single finding with message and resource configuration.

        :param finding_id: The ID of the finding.
        :type finding_id: str
        :param snapshot_timestamp: Return the finding for a given snapshot of time (Unix ms).
        :type snapshot_timestamp: int, optional
        :rtype: GetFindingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["finding_id"] = finding_id

        if snapshot_timestamp is not unset:
            kwargs["snapshot_timestamp"] = snapshot_timestamp

        return self._get_finding_endpoint.call_with_http_info(**kwargs)

    def get_historical_job(
        self,
        job_id: str,
    ) -> HistoricalJobResponse:
        """Get a job's details.

        Get a job's details.

        :param job_id: The ID of the job.
        :type job_id: str
        :rtype: HistoricalJobResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["job_id"] = job_id

        return self._get_historical_job_endpoint.call_with_http_info(**kwargs)

    def get_indicator_of_compromise(
        self,
        indicator: str,
        *,
        ocsf: Union[bool, UnsetType] = unset,
        include_triage_history: Union[bool, UnsetType] = unset,
        triage_history_limit: Union[int, UnsetType] = unset,
        triage_history_offset: Union[int, UnsetType] = unset,
    ) -> GetIoCIndicatorResponse:
        """Get an indicator of compromise.

        Get detailed information about a specific indicator of compromise (IoC).

        :param indicator: The indicator value to look up (for example, an IP address or domain).
        :type indicator: str
        :param ocsf: When true, return only OCSF field-based matches. When false, return regex/message-based matches.
        :type ocsf: bool, optional
        :param include_triage_history: Include full triage history for the indicator.
        :type include_triage_history: bool, optional
        :param triage_history_limit: Maximum number of triage history events returned. Only applied when ``include_triage_history`` is true.
        :type triage_history_limit: int, optional
        :param triage_history_offset: Pagination offset into the triage history. Only applied when ``include_triage_history`` is true.
        :type triage_history_offset: int, optional
        :rtype: GetIoCIndicatorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["indicator"] = indicator

        if ocsf is not unset:
            kwargs["ocsf"] = ocsf

        if include_triage_history is not unset:
            kwargs["include_triage_history"] = include_triage_history

        if triage_history_limit is not unset:
            kwargs["triage_history_limit"] = triage_history_limit

        if triage_history_offset is not unset:
            kwargs["triage_history_offset"] = triage_history_offset

        return self._get_indicator_of_compromise_endpoint.call_with_http_info(**kwargs)

    def get_investigation_log_queries_matching_signal(
        self,
        signal_id: str,
    ) -> SecurityMonitoringSignalSuggestedActionsResponse:
        """Get investigation queries for a signal.

        Get the list of investigation log queries available for a given security signal.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :rtype: SecurityMonitoringSignalSuggestedActionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        return self._get_investigation_log_queries_matching_signal_endpoint.call_with_http_info(**kwargs)

    def get_resource_evaluation_filters(
        self,
        *,
        cloud_provider: Union[str, UnsetType] = unset,
        account_id: Union[str, UnsetType] = unset,
        skip_cache: Union[bool, UnsetType] = unset,
    ) -> GetResourceEvaluationFiltersResponse:
        """List resource filters.

        List resource filters.

        :param cloud_provider: Filter resource filters by cloud provider (e.g. aws, gcp, azure).
        :type cloud_provider: str, optional
        :param account_id: Filter resource filters by cloud provider account ID. This parameter is only valid when provider is specified.
        :type account_id: str, optional
        :param skip_cache: Skip cache for resource filters.
        :type skip_cache: bool, optional
        :rtype: GetResourceEvaluationFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        if cloud_provider is not unset:
            kwargs["cloud_provider"] = cloud_provider

        if account_id is not unset:
            kwargs["account_id"] = account_id

        if skip_cache is not unset:
            kwargs["skip_cache"] = skip_cache

        return self._get_resource_evaluation_filters_endpoint.call_with_http_info(**kwargs)

    def get_rule_version_history(
        self,
        rule_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> GetRuleVersionHistoryResponse:
        """Get a rule's version history.

        Get a rule's version history.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: GetRuleVersionHistoryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._get_rule_version_history_endpoint.call_with_http_info(**kwargs)

    def get_sbom(
        self,
        asset_type: AssetType,
        filter_asset_name: str,
        *,
        filter_repo_digest: Union[str, UnsetType] = unset,
        ext_format: Union[SBOMFormat, UnsetType] = unset,
    ) -> GetSBOMResponse:
        """Get SBOM.

        Get a single SBOM related to an asset by its type and name.

        :param asset_type: The type of the asset for the SBOM request.
        :type asset_type: AssetType
        :param filter_asset_name: The name of the asset for the SBOM request.
        :type filter_asset_name: str
        :param filter_repo_digest: The container image ``repo_digest`` for the SBOM request. When the requested asset type is 'Image', this filter is mandatory.
        :type filter_repo_digest: str, optional
        :param ext_format: The standard of the SBOM.
        :type ext_format: SBOMFormat, optional
        :rtype: GetSBOMResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["asset_type"] = asset_type

        kwargs["filter_asset_name"] = filter_asset_name

        if filter_repo_digest is not unset:
            kwargs["filter_repo_digest"] = filter_repo_digest

        if ext_format is not unset:
            kwargs["ext_format"] = ext_format

        return self._get_sbom_endpoint.call_with_http_info(**kwargs)

    def get_secrets_rules(
        self,
    ) -> SecretRuleArray:
        """Returns a list of Secrets rules.

        Returns a list of Secrets rules with ID, Pattern, Description, Priority, and SDS ID.

        :rtype: SecretRuleArray
        """
        kwargs: Dict[str, Any] = {}
        return self._get_secrets_rules_endpoint.call_with_http_info(**kwargs)

    def get_security_filter(
        self,
        security_filter_id: str,
    ) -> SecurityFilterResponse:
        """Get a security filter.

        Get the details of a specific security filter.

        See the `security filter guide <https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/>`_
        for more examples.

        :param security_filter_id: The ID of the security filter.
        :type security_filter_id: str
        :rtype: SecurityFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["security_filter_id"] = security_filter_id

        return self._get_security_filter_endpoint.call_with_http_info(**kwargs)

    def get_security_findings_automation_due_date_rule(
        self,
        rule_id: UUID,
    ) -> DueDateRuleResponse:
        """Get a due date rule.

        Get the details of a due date rule by ID.

        :param rule_id: The ID of the due date rule.
        :type rule_id: UUID
        :rtype: DueDateRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_security_findings_automation_due_date_rule_endpoint.call_with_http_info(**kwargs)

    def get_security_findings_automation_mute_rule(
        self,
        rule_id: UUID,
    ) -> MuteRuleResponse:
        """Get a mute rule.

        Get the details of a mute rule by ID.

        :param rule_id: The ID of the mute rule.
        :type rule_id: UUID
        :rtype: MuteRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_security_findings_automation_mute_rule_endpoint.call_with_http_info(**kwargs)

    def get_security_findings_automation_ticket_creation_rule(
        self,
        rule_id: UUID,
    ) -> TicketCreationRuleResponse:
        """Get a ticket creation rule.

        Get the details of a ticket creation rule by ID.

        :param rule_id: The ID of the ticket creation rule.
        :type rule_id: UUID
        :rtype: TicketCreationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_security_findings_automation_ticket_creation_rule_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_critical_asset(
        self,
        critical_asset_id: str,
    ) -> SecurityMonitoringCriticalAssetResponse:
        """Get a critical asset.

        Get the details of a specific critical asset.

        :param critical_asset_id: The ID of the critical asset.
        :type critical_asset_id: str
        :rtype: SecurityMonitoringCriticalAssetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["critical_asset_id"] = critical_asset_id

        return self._get_security_monitoring_critical_asset_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_dataset(
        self,
        dataset_id: str,
    ) -> SecurityMonitoringDatasetResponse:
        """Get a dataset.

        Get the current version of a Cloud SIEM dataset by ID.

        :param dataset_id: The UUID of the dataset.
        :type dataset_id: str
        :rtype: SecurityMonitoringDatasetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        return self._get_security_monitoring_dataset_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_dataset_by_version(
        self,
        dataset_id: str,
        version: int,
    ) -> SecurityMonitoringDatasetResponse:
        """Get a dataset at a specific version.

        Retrieve a specific historical version of a Cloud SIEM dataset.

        :param dataset_id: The UUID of the dataset.
        :type dataset_id: str
        :param version: The version number of the dataset to retrieve.
        :type version: int
        :rtype: SecurityMonitoringDatasetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        kwargs["version"] = version

        return self._get_security_monitoring_dataset_by_version_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_dataset_version_history(
        self,
        dataset_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> SecurityMonitoringDatasetVersionHistoryResponse:
        """Get the version history of a dataset.

        Retrieve the version history of a Cloud SIEM dataset, including the changes made at each version.

        :param dataset_id: The UUID of the dataset.
        :type dataset_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: SecurityMonitoringDatasetVersionHistoryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._get_security_monitoring_dataset_version_history_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_histsignal(
        self,
        histsignal_id: str,
    ) -> SecurityMonitoringSignalResponse:
        """Get a hist signal's details.

        Get a hist signal's details.

        :param histsignal_id: The ID of the historical signal.
        :type histsignal_id: str
        :rtype: SecurityMonitoringSignalResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["histsignal_id"] = histsignal_id

        return self._get_security_monitoring_histsignal_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_histsignals_by_job_id(
        self,
        job_id: str,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[SecurityMonitoringSignalsSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> SecurityMonitoringSignalsListResponse:
        """Get a job's hist signals.

        Get a job's hist signals.

        :param job_id: The ID of the job.
        :type job_id: str
        :param filter_query: The search query for security signals.
        :type filter_query: str, optional
        :param filter_from: The minimum timestamp for requested security signals.
        :type filter_from: datetime, optional
        :param filter_to: The maximum timestamp for requested security signals.
        :type filter_to: datetime, optional
        :param sort: The order of the security signals in results.
        :type sort: SecurityMonitoringSignalsSort, optional
        :param page_cursor: A list of results using the cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: The maximum number of security signals in the response.
        :type page_limit: int, optional
        :rtype: SecurityMonitoringSignalsListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["job_id"] = job_id

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._get_security_monitoring_histsignals_by_job_id_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_integration_config(
        self,
        integration_config_id: str,
    ) -> SecurityMonitoringIntegrationConfigResponse:
        """Get an entity context sync configuration.

        Get the details of a specific entity context sync configuration.

        :param integration_config_id: The ID of the entity context sync configuration.
        :type integration_config_id: str
        :rtype: SecurityMonitoringIntegrationConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_config_id"] = integration_config_id

        return self._get_security_monitoring_integration_config_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_rule(
        self,
        rule_id: str,
    ) -> SecurityMonitoringRuleResponse:
        """Get a rule's details.

        Get a rule's details.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: SecurityMonitoringRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_signal(
        self,
        signal_id: str,
    ) -> SecurityMonitoringSignalResponse:
        """Get a signal's details.

        Get a signal's details.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :rtype: SecurityMonitoringSignalResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        return self._get_security_monitoring_signal_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_suppression(
        self,
        suppression_id: str,
    ) -> SecurityMonitoringSuppressionResponse:
        """Get a suppression rule.

        Get the details of a specific suppression rule.

        :param suppression_id: The ID of the suppression rule
        :type suppression_id: str
        :rtype: SecurityMonitoringSuppressionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["suppression_id"] = suppression_id

        return self._get_security_monitoring_suppression_endpoint.call_with_http_info(**kwargs)

    def get_signal_entities(
        self,
        signal_id: str,
        *,
        limit: Union[int, UnsetType] = unset,
    ) -> SignalEntitiesResponse:
        """Get entities related to a signal.

        Get the list of entities related to a security signal, captured at the signal's timestamp.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :param limit: The maximum number of entities to return.
        :type limit: int, optional
        :rtype: SignalEntitiesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        if limit is not unset:
            kwargs["limit"] = limit

        return self._get_signal_entities_endpoint.call_with_http_info(**kwargs)

    def get_signal_notification_rule(
        self,
        id: str,
    ) -> NotificationRuleResponse:
        """Get details of a signal-based notification rule.

        Get the details of a notification rule for security signals.

        :param id: ID of the notification rule.
        :type id: str
        :rtype: NotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_signal_notification_rule_endpoint.call_with_http_info(**kwargs)

    def get_signal_notification_rules(
        self,
    ) -> NotificationRulesListResponse:
        """Get the list of signal-based notification rules.

        Returns the list of notification rules for security signals.

        :rtype: NotificationRulesListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_signal_notification_rules_endpoint.call_with_http_info(**kwargs)

    def get_single_entity_context(
        self,
        id: str,
        *,
        _from: Union[str, UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
        as_of: Union[str, UnsetType] = unset,
    ) -> SingleEntityContextResponse:
        """Get a single entity context.

        Get a single entity from the Cloud SIEM entity context store by its identifier, returning the historical
        revisions of the entity in the requested time range. The endpoint can either return revisions across an
        interval ( ``from`` / ``to`` ) or the snapshot of the entity at a single point in time ( ``as_of`` ); the two modes
        are mutually exclusive.

        :param id: The unique identifier of the entity to retrieve.
        :type id: str
        :param _from: The start of the time range to query, as an RFC3339 timestamp or a relative time (for example, ``now-7d`` ).
            Defaults to ``now-7d``. Ignored when ``as_of`` is set.
        :type _from: str, optional
        :param to: The end of the time range to query, as an RFC3339 timestamp or a relative time (for example, ``now`` ).
            Defaults to ``now``. Ignored when ``as_of`` is set.
        :type to: str, optional
        :param as_of: A point in time at which to query the entity revisions, as an RFC3339 timestamp, a Unix timestamp
            (in seconds), or a relative time (for example, ``now-1d`` ). When set, ``from`` and ``to`` are ignored.
            Cannot be combined with custom ``from`` / ``to`` values.
        :type as_of: str, optional
        :rtype: SingleEntityContextResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if _from is not unset:
            kwargs["_from"] = _from

        if to is not unset:
            kwargs["to"] = to

        if as_of is not unset:
            kwargs["as_of"] = as_of

        return self._get_single_entity_context_endpoint.call_with_http_info(**kwargs)

    def get_static_analysis_default_rulesets(
        self,
        language: str,
    ) -> DefaultRulesetsPerLanguageResponse:
        """Get default rulesets for a language.

        Get the default SAST ruleset names for a given programming language.

        :param language: The programming language for which to retrieve the default rulesets.
        :type language: str
        :rtype: DefaultRulesetsPerLanguageResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["language"] = language

        return self._get_static_analysis_default_rulesets_endpoint.call_with_http_info(**kwargs)

    def get_static_analysis_node_types(
        self,
        language: str,
    ) -> NodeTypesResponse:
        """Get node types for a language.

        Retrieve tree-sitter node type definitions for a given programming language.

        :param language: The programming language for which to retrieve node type definitions.
        :type language: str
        :rtype: NodeTypesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["language"] = language

        return self._get_static_analysis_node_types_endpoint.call_with_http_info(**kwargs)

    def get_static_analysis_ruleset(
        self,
        ruleset_name: str,
        *,
        include_tests: Union[bool, UnsetType] = unset,
        include_testing_rules: Union[bool, UnsetType] = unset,
    ) -> SastRulesetResponse:
        """Get a SAST ruleset.

        Get a SAST ruleset by name, including all its rules.

        :param ruleset_name: The name of the ruleset to retrieve.
        :type ruleset_name: str
        :param include_tests: When true, test cases for each rule are included in the response.
        :type include_tests: bool, optional
        :param include_testing_rules: When true, rules that are in testing mode are included in the response.
        :type include_testing_rules: bool, optional
        :rtype: SastRulesetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        if include_tests is not unset:
            kwargs["include_tests"] = include_tests

        if include_testing_rules is not unset:
            kwargs["include_testing_rules"] = include_testing_rules

        return self._get_static_analysis_ruleset_endpoint.call_with_http_info(**kwargs)

    def get_static_analysis_tree_sitter_wasm(
        self,
        file: str,
    ) -> file_type:
        """Get tree-sitter WASM file.

        Download the WebAssembly binary for a tree-sitter grammar by file name.

        :param file: The name of the WASM file to download.
        :type file: str
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["file"] = file

        return self._get_static_analysis_tree_sitter_wasm_endpoint.call_with_http_info(**kwargs)

    def get_suggested_actions_matching_signal(
        self,
        signal_id: str,
    ) -> SecurityMonitoringSignalSuggestedActionsResponse:
        """Get suggested actions for a signal.

        Get the list of suggested actions for a given security signal.

        :param signal_id: The ID of the signal.
        :type signal_id: str
        :rtype: SecurityMonitoringSignalSuggestedActionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["signal_id"] = signal_id

        return self._get_suggested_actions_matching_signal_endpoint.call_with_http_info(**kwargs)

    def get_suppressions_affecting_future_rule(
        self,
        body: Union[
            SecurityMonitoringRuleCreatePayload,
            SecurityMonitoringStandardRuleCreatePayload,
            SecurityMonitoringSignalRuleCreatePayload,
            CloudConfigurationRuleCreatePayload,
        ],
    ) -> SecurityMonitoringSuppressionsResponse:
        """Get suppressions affecting future rule.

        Get the list of suppressions that would affect a rule.

        :type body: SecurityMonitoringRuleCreatePayload
        :rtype: SecurityMonitoringSuppressionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_suppressions_affecting_future_rule_endpoint.call_with_http_info(**kwargs)

    def get_suppressions_affecting_rule(
        self,
        rule_id: str,
    ) -> SecurityMonitoringSuppressionsResponse:
        """Get suppressions affecting a specific rule.

        Get the list of suppressions that affect a specific existing rule by its ID.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: SecurityMonitoringSuppressionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_suppressions_affecting_rule_endpoint.call_with_http_info(**kwargs)

    def get_suppression_version_history(
        self,
        suppression_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> GetSuppressionVersionHistoryResponse:
        """Get a suppression's version history.

        Get a suppression's version history.

        :param suppression_id: The ID of the suppression rule
        :type suppression_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: GetSuppressionVersionHistoryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["suppression_id"] = suppression_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._get_suppression_version_history_endpoint.call_with_http_info(**kwargs)

    def get_vulnerability_notification_rule(
        self,
        id: str,
    ) -> NotificationRuleResponse:
        """Get details of a vulnerability notification rule.

        Get the details of a notification rule for security vulnerabilities.

        :param id: ID of the notification rule.
        :type id: str
        :rtype: NotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_vulnerability_notification_rule_endpoint.call_with_http_info(**kwargs)

    def get_vulnerability_notification_rules(
        self,
    ) -> NotificationRulesListResponse:
        """Get the list of vulnerability notification rules.

        Returns the list of notification rules for security vulnerabilities.

        :rtype: NotificationRulesListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_vulnerability_notification_rules_endpoint.call_with_http_info(**kwargs)

    def import_security_vulnerabilities(
        self,
        body: CycloneDXBom,
    ) -> None:
        """Import security vulnerabilities.

        Import security vulnerabilities from an external scanner in CycloneDX 1.5 format.

        The payload is validated against the CycloneDX 1.5 JSON schema and the following
        additional constraints:

        * ``metadata`` , ``metadata.component`` , and ``metadata.component.name`` are required.
        * ``metadata.tools.components`` must contain exactly one element with a ``name`` field.
        * ``components`` cannot be empty. Each component requires ``bom-ref`` , ``type`` , ``name`` , and ``version``.
        * When ``type`` is ``library`` , ``purl`` is required and must be a valid PURL.
        * When ``type`` is ``operating-system`` , ``name`` must be one of the supported OS values:
          ``alma`` , ``alpine`` , ``amazon`` , ``azurelinux`` , ``bottlerocket`` , ``cbl-mariner`` , ``chainguard`` ,
          ``centos`` , ``debian`` , ``fedora`` , ``opensuse`` , ``opensuse-leap`` , ``opensuse-tumbleweed`` ,
          ``oracle`` , ``photon`` , ``redhat`` , ``rocky`` , ``slem`` , ``sles`` , ``ubuntu`` , ``wolfi`` , ``windows`` , ``macos``.
        * ``vulnerabilities`` cannot be empty. Each vulnerability requires ``id`` , exactly one ``ratings`` entry,
          and at least one ``affects`` entry.
        * Each ``affects[].ref`` must match a ``bom-ref`` value in ``components``.

        :type body: CycloneDXBom
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._import_security_vulnerabilities_endpoint.call_with_http_info(**kwargs)

    def list_assets_sbo_ms(
        self,
        *,
        page_token: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_asset_type: Union[AssetType, UnsetType] = unset,
        filter_asset_name: Union[str, UnsetType] = unset,
        filter_package_name: Union[str, UnsetType] = unset,
        filter_package_version: Union[str, UnsetType] = unset,
        filter_license_name: Union[str, UnsetType] = unset,
        filter_license_type: Union[SBOMComponentLicenseType, UnsetType] = unset,
    ) -> ListAssetsSBOMsResponse:
        """List assets SBOMs.

        Get a list of assets SBOMs for an organization.

        The ``filter[asset_type]`` parameter is required for initial requests (when no ``page[token]`` is provided).
        Subsequent pages encode the asset type in the pagination token, so ``filter[asset_type]`` is not required
        for paginated requests. Mixing infrastructure asset types ( ``Host`` , ``HostImage`` , ``Image`` , ``ServerlessFunction`` )
        with code asset types ( ``Repository`` , ``Service`` ) in the same request is not supported and returns a 400 error.

        **Pagination**

        Please review the `Pagination section <#pagination>`_ for the "List Vulnerabilities" endpoint.

        **Filtering**

        Please review the `Filtering section <#filtering>`_ for the "List Vulnerabilities" endpoint.

        **Metadata**

        Please review the `Metadata section <#metadata>`_ for the "List Vulnerabilities" endpoint.

        :param page_token: Its value must come from the ``links`` section of the response of the first request. Do not manually edit it.
        :type page_token: str, optional
        :param page_number: The page number to be retrieved. It should be equal to or greater than 1.
        :type page_number: int, optional
        :param filter_asset_type: The type of the assets for the SBOM request. Required for initial requests (when no ``page[token]`` is provided). Infrastructure types ( ``Host`` , ``HostImage`` , ``Image`` , ``ServerlessFunction`` ) and code types ( ``Repository`` , ``Service`` ) cannot be mixed in the same request.
        :type filter_asset_type: AssetType, optional
        :param filter_asset_name: The name of the asset for the SBOM request.
        :type filter_asset_name: str, optional
        :param filter_package_name: The name of the component that is a dependency of an asset.
        :type filter_package_name: str, optional
        :param filter_package_version: The version of the component that is a dependency of an asset.
        :type filter_package_version: str, optional
        :param filter_license_name: The software license name of the component that is a dependency of an asset.
        :type filter_license_name: str, optional
        :param filter_license_type: The software license type of the component that is a dependency of an asset.
        :type filter_license_type: SBOMComponentLicenseType, optional
        :rtype: ListAssetsSBOMsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_token is not unset:
            kwargs["page_token"] = page_token

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_asset_type is not unset:
            kwargs["filter_asset_type"] = filter_asset_type

        if filter_asset_name is not unset:
            kwargs["filter_asset_name"] = filter_asset_name

        if filter_package_name is not unset:
            kwargs["filter_package_name"] = filter_package_name

        if filter_package_version is not unset:
            kwargs["filter_package_version"] = filter_package_version

        if filter_license_name is not unset:
            kwargs["filter_license_name"] = filter_license_name

        if filter_license_type is not unset:
            kwargs["filter_license_type"] = filter_license_type

        return self._list_assets_sbo_ms_endpoint.call_with_http_info(**kwargs)

    def list_findings(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        snapshot_timestamp: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_evaluation_changed_at: Union[str, UnsetType] = unset,
        filter_muted: Union[bool, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
        filter_resource_type: Union[str, UnsetType] = unset,
        filter_resource_id: Union[str, UnsetType] = unset,
        filter_discovery_timestamp: Union[str, UnsetType] = unset,
        filter_evaluation: Union[FindingEvaluation, UnsetType] = unset,
        filter_status: Union[FindingStatus, UnsetType] = unset,
        filter_vulnerability_type: Union[List[FindingVulnerabilityType], UnsetType] = unset,
        detailed_findings: Union[bool, UnsetType] = unset,
    ) -> ListFindingsResponse:
        """List findings.

        Get a list of findings. These include both misconfigurations and identity risks.

        **Note** : To filter and return only identity risks, add the following query parameter: ``?filter[tags]=dd_rule_type:ciem``

        **Filtering**

        Filters can be applied by appending query parameters to the URL.

        * Using a single filter: ``?filter[attribute_key]=attribute_value``
        * Chaining filters: ``?filter[attribute_key]=attribute_value&filter[attribute_key]=attribute_value...``
        * Filtering on tags: ``?filter[tags]=tag_key:tag_value&filter[tags]=tag_key_2:tag_value_2``

        Here, ``attribute_key`` can be any of the filter keys described further below.

        Query parameters of type ``integer`` support comparison operators ( ``>`` , ``>=`` , ``<`` , ``<=`` ). This is particularly useful when filtering by ``evaluation_changed_at`` or ``resource_discovery_timestamp``. For example: ``?filter[evaluation_changed_at]=>20123123121``.

        You can also use the negation operator on strings. For example, use ``filter[resource_type]=-aws*`` to filter for any non-AWS resources.

        The operator must come after the equal sign. For example, to filter with the ``>=`` operator, add the operator after the equal sign: ``filter[evaluation_changed_at]=>=1678809373257``.

        Query parameters must be only among the documented ones and with values of correct types. Duplicated query parameters (e.g. ``filter[status]=low&filter[status]=info`` ) are not allowed.

        **Additional extension fields**

        Additional extension fields are available for some findings.

        The data is available when you include the query parameter ``?detailed_findings=true`` in the request.

        The following fields are available for findings:

        * ``external_id`` : The resource external ID related to the finding.
        * ``description`` : The description and remediation steps for the finding.
        * ``datadog_link`` : The Datadog relative link for the finding.
        * ``ip_addresses`` : The list of private IP addresses for the resource related to the finding.

        **Response**

        The response includes an array of finding objects, pagination metadata, and a count of items that match the query.

        Each finding object contains the following:

        * The finding ID that can be used in a ``GetFinding`` request to retrieve the full finding details.
        * Core attributes, including status, evaluation, high-level resource details, muted state, and rule details.
        * ``evaluation_changed_at`` and ``resource_discovery_date`` time stamps.
        * An array of associated tags.

        :param page_limit: Limit the number of findings returned. Must be <= 1000.
        :type page_limit: int, optional
        :param snapshot_timestamp: Return findings for a given snapshot of time (Unix ms).
        :type snapshot_timestamp: int, optional
        :param page_cursor: Return the next page of findings pointed to by the cursor.
        :type page_cursor: str, optional
        :param filter_tags: Return findings that have these associated tags (repeatable).
        :type filter_tags: str, optional
        :param filter_evaluation_changed_at: Return findings that have changed from pass to fail or vice versa on a specified date (Unix ms) or date range (using comparison operators).
        :type filter_evaluation_changed_at: str, optional
        :param filter_muted: Set to ``true`` to return findings that are muted. Set to ``false`` to return unmuted findings.
        :type filter_muted: bool, optional
        :param filter_rule_id: Return findings for the specified rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_name: Return findings for the specified rule.
        :type filter_rule_name: str, optional
        :param filter_resource_type: Return only findings for the specified resource type.
        :type filter_resource_type: str, optional
        :param filter_resource_id: Return only findings for the specified resource id.
        :type filter_resource_id: str, optional
        :param filter_discovery_timestamp: Return findings that were found on a specified date (Unix ms) or date range (using comparison operators).
        :type filter_discovery_timestamp: str, optional
        :param filter_evaluation: Return only ``pass`` or ``fail`` findings.
        :type filter_evaluation: FindingEvaluation, optional
        :param filter_status: Return only findings with the specified status.
        :type filter_status: FindingStatus, optional
        :param filter_vulnerability_type: Return findings that match the selected vulnerability types (repeatable).
        :type filter_vulnerability_type: [FindingVulnerabilityType], optional
        :param detailed_findings: Return additional fields for some findings.
        :type detailed_findings: bool, optional
        :rtype: ListFindingsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if snapshot_timestamp is not unset:
            kwargs["snapshot_timestamp"] = snapshot_timestamp

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_evaluation_changed_at is not unset:
            kwargs["filter_evaluation_changed_at"] = filter_evaluation_changed_at

        if filter_muted is not unset:
            kwargs["filter_muted"] = filter_muted

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        if filter_resource_type is not unset:
            kwargs["filter_resource_type"] = filter_resource_type

        if filter_resource_id is not unset:
            kwargs["filter_resource_id"] = filter_resource_id

        if filter_discovery_timestamp is not unset:
            kwargs["filter_discovery_timestamp"] = filter_discovery_timestamp

        if filter_evaluation is not unset:
            kwargs["filter_evaluation"] = filter_evaluation

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_vulnerability_type is not unset:
            kwargs["filter_vulnerability_type"] = filter_vulnerability_type

        if detailed_findings is not unset:
            kwargs["detailed_findings"] = detailed_findings

        return self._list_findings_endpoint.call_with_http_info(**kwargs)

    def list_findings_with_pagination(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        snapshot_timestamp: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_evaluation_changed_at: Union[str, UnsetType] = unset,
        filter_muted: Union[bool, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
        filter_resource_type: Union[str, UnsetType] = unset,
        filter_resource_id: Union[str, UnsetType] = unset,
        filter_discovery_timestamp: Union[str, UnsetType] = unset,
        filter_evaluation: Union[FindingEvaluation, UnsetType] = unset,
        filter_status: Union[FindingStatus, UnsetType] = unset,
        filter_vulnerability_type: Union[List[FindingVulnerabilityType], UnsetType] = unset,
        detailed_findings: Union[bool, UnsetType] = unset,
    ) -> collections.abc.Iterable[Finding]:
        """List findings.

        Provide a paginated version of :meth:`list_findings`, returning all items.

        :param page_limit: Limit the number of findings returned. Must be <= 1000.
        :type page_limit: int, optional
        :param snapshot_timestamp: Return findings for a given snapshot of time (Unix ms).
        :type snapshot_timestamp: int, optional
        :param page_cursor: Return the next page of findings pointed to by the cursor.
        :type page_cursor: str, optional
        :param filter_tags: Return findings that have these associated tags (repeatable).
        :type filter_tags: str, optional
        :param filter_evaluation_changed_at: Return findings that have changed from pass to fail or vice versa on a specified date (Unix ms) or date range (using comparison operators).
        :type filter_evaluation_changed_at: str, optional
        :param filter_muted: Set to ``true`` to return findings that are muted. Set to ``false`` to return unmuted findings.
        :type filter_muted: bool, optional
        :param filter_rule_id: Return findings for the specified rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_name: Return findings for the specified rule.
        :type filter_rule_name: str, optional
        :param filter_resource_type: Return only findings for the specified resource type.
        :type filter_resource_type: str, optional
        :param filter_resource_id: Return only findings for the specified resource id.
        :type filter_resource_id: str, optional
        :param filter_discovery_timestamp: Return findings that were found on a specified date (Unix ms) or date range (using comparison operators).
        :type filter_discovery_timestamp: str, optional
        :param filter_evaluation: Return only ``pass`` or ``fail`` findings.
        :type filter_evaluation: FindingEvaluation, optional
        :param filter_status: Return only findings with the specified status.
        :type filter_status: FindingStatus, optional
        :param filter_vulnerability_type: Return findings that match the selected vulnerability types (repeatable).
        :type filter_vulnerability_type: [FindingVulnerabilityType], optional
        :param detailed_findings: Return additional fields for some findings.
        :type detailed_findings: bool, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Finding]
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if snapshot_timestamp is not unset:
            kwargs["snapshot_timestamp"] = snapshot_timestamp

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_evaluation_changed_at is not unset:
            kwargs["filter_evaluation_changed_at"] = filter_evaluation_changed_at

        if filter_muted is not unset:
            kwargs["filter_muted"] = filter_muted

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        if filter_resource_type is not unset:
            kwargs["filter_resource_type"] = filter_resource_type

        if filter_resource_id is not unset:
            kwargs["filter_resource_id"] = filter_resource_id

        if filter_discovery_timestamp is not unset:
            kwargs["filter_discovery_timestamp"] = filter_discovery_timestamp

        if filter_evaluation is not unset:
            kwargs["filter_evaluation"] = filter_evaluation

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_vulnerability_type is not unset:
            kwargs["filter_vulnerability_type"] = filter_vulnerability_type

        if detailed_findings is not unset:
            kwargs["detailed_findings"] = detailed_findings

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 100)
        endpoint = self._list_findings_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.cursor",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_historical_jobs(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
    ) -> ListHistoricalJobsResponse:
        """List historical jobs.

        List historical jobs.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: The order of the jobs in results.
        :type sort: str, optional
        :param filter_query: Query used to filter items from the fetched list.
        :type filter_query: str, optional
        :rtype: ListHistoricalJobsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        return self._list_historical_jobs_endpoint.call_with_http_info(**kwargs)

    def list_indicators_of_compromise(
        self,
        *,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sort_column: Union[str, UnsetType] = unset,
        sort_order: Union[str, UnsetType] = unset,
        ocsf: Union[bool, UnsetType] = unset,
        worked_by: Union[str, UnsetType] = unset,
        triage_state: Union[IoCTriageState, UnsetType] = unset,
    ) -> IoCExplorerListResponse:
        """List indicators of compromise.

        Get a list of indicators of compromise (IoCs) matching the specified filters.

        :param limit: Number of results per page.
        :type limit: int, optional
        :param offset: Pagination offset.
        :type offset: int, optional
        :param query: Search/filter query (supports field:value syntax).
        :type query: str, optional
        :param sort_column: Sort column: score, first_seen_ts_epoch, last_seen_ts_epoch, indicator, indicator_type, signal_count, log_count, category, as_type.
        :type sort_column: str, optional
        :param sort_order: Sort order: asc or desc.
        :type sort_order: str, optional
        :param ocsf: When true, return only OCSF field-based matches. When false, return regex/message-based matches.
        :type ocsf: bool, optional
        :param worked_by: Filter indicators whose triage state was updated by a specific user identified by their handle.
        :type worked_by: str, optional
        :param triage_state: Filter by triage state.
        :type triage_state: IoCTriageState, optional
        :rtype: IoCExplorerListResponse
        """
        kwargs: Dict[str, Any] = {}
        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        if query is not unset:
            kwargs["query"] = query

        if sort_column is not unset:
            kwargs["sort_column"] = sort_column

        if sort_order is not unset:
            kwargs["sort_order"] = sort_order

        if ocsf is not unset:
            kwargs["ocsf"] = ocsf

        if worked_by is not unset:
            kwargs["worked_by"] = worked_by

        if triage_state is not unset:
            kwargs["triage_state"] = triage_state

        return self._list_indicators_of_compromise_endpoint.call_with_http_info(**kwargs)

    def list_multiple_rulesets(
        self,
        body: GetMultipleRulesetsRequest,
    ) -> GetMultipleRulesetsResponse:
        """Ruleset get multiple.

        Get rules for multiple rulesets in batch.

        :type body: GetMultipleRulesetsRequest
        :rtype: GetMultipleRulesetsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._list_multiple_rulesets_endpoint.call_with_http_info(**kwargs)

    def list_sample_log_generation_subscriptions(
        self,
        *,
        status: Union[SampleLogGenerationSubscriptionsStatusFilter, UnsetType] = unset,
        start_timestamp: Union[datetime, UnsetType] = unset,
        end_timestamp: Union[datetime, UnsetType] = unset,
    ) -> SampleLogGenerationSubscriptionsResponse:
        """Get sample log generation subscriptions.

        Get the sample log generation subscriptions for the organization.
        Sample log generation injects representative example logs for a given Cloud SIEM content pack into the Logs platform,
        which can be used to test detection rules without onboarding the underlying integration first.

        **Availability** : this endpoint is restricted to Cloud SIEM trial organizations on an eligible
        pricing model. Other organizations receive a ``403 Forbidden`` (non-trial orgs) or a ``400 Bad Request``
        (feature disabled), and legacy pricing tiers receive a response with ``status: not_available``.

        :param status: Filter the subscriptions by status. Use ``active`` to return only currently active
            subscriptions, or ``all`` to return every subscription including expired ones.
            Ignored when ``start_timestamp`` is provided. Defaults to ``active``.
        :type status: SampleLogGenerationSubscriptionsStatusFilter, optional
        :param start_timestamp: The start of the time range, as an RFC3339 timestamp. When provided, the response includes
            every subscription that was active at any point in ``[start_timestamp, end_timestamp]`` ,
            and the ``status`` filter is ignored.
        :type start_timestamp: datetime, optional
        :param end_timestamp: The end of the time range, as an RFC3339 timestamp. Ignored unless ``start_timestamp`` is set.
            Defaults to the current time when ``start_timestamp`` is provided.
        :type end_timestamp: datetime, optional
        :rtype: SampleLogGenerationSubscriptionsResponse
        """
        kwargs: Dict[str, Any] = {}
        if status is not unset:
            kwargs["status"] = status

        if start_timestamp is not unset:
            kwargs["start_timestamp"] = start_timestamp

        if end_timestamp is not unset:
            kwargs["end_timestamp"] = end_timestamp

        return self._list_sample_log_generation_subscriptions_endpoint.call_with_http_info(**kwargs)

    def list_scanned_assets_metadata(
        self,
        *,
        page_token: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_asset_type: Union[CloudAssetType, UnsetType] = unset,
        filter_asset_name: Union[str, UnsetType] = unset,
        filter_last_success_origin: Union[str, UnsetType] = unset,
        filter_last_success_env: Union[str, UnsetType] = unset,
    ) -> ScannedAssetsMetadata:
        """List scanned assets metadata.

        Get a list of security scanned assets metadata for an organization.

        **Pagination**

        For the "List Vulnerabilities" endpoint, see the `Pagination section <#pagination>`_.

        **Filtering**

        For the "List Vulnerabilities" endpoint, see the `Filtering section <#filtering>`_.

        **Metadata**

         For the "List Vulnerabilities" endpoint, see the `Metadata section <#metadata>`_.

        **Related endpoints**

        This endpoint returns additional metadata for cloud resources that is not available from the standard resource endpoints. To access a richer dataset, call this endpoint together with the relevant resource endpoint(s) and merge (join) their results using the resource identifier.

        **Hosts**

        To enrich host data, join the response from the `Hosts <https://docs.datadoghq.com/api/latest/hosts/>`_ endpoint with the response from the scanned-assets-metadata endpoint on the following key fields:

        .. list-table::
           :header-rows: 1

           * - ENDPOINT
             - JOIN KEY
             - TYPE
           * - `/api/v1/hosts <https://docs.datadoghq.com/api/latest/hosts/>`_
             - host_list.host_name
             - string
           * - /api/v2/security/scanned-assets-metadata
             - data.attributes.asset.name
             - string

        **Host Images**

        To enrich host image data, join the response from the `Hosts <https://docs.datadoghq.com/api/latest/hosts/>`_ endpoint with the response from the scanned-assets-metadata endpoint on the following key fields:

        .. list-table::
           :header-rows: 1

           * - ENDPOINT
             - JOIN KEY
             - TYPE
           * - `/api/v1/hosts <https://docs.datadoghq.com/api/latest/hosts/>`_
             - host_list.tags_by_source["Amazon Web Services"]["image"]
             - string
           * - /api/v2/security/scanned-assets-metadata
             - data.attributes.asset.name
             - string

        **Container Images**

        To enrich container image data, join the response from the `Container Images <https://docs.datadoghq.com/api/latest/container-images/>`_ endpoint with the response from the scanned-assets-metadata endpoint on the following key fields:

        .. list-table::
           :header-rows: 1

           * - ENDPOINT
             - JOIN KEY
             - TYPE
           * - `/api/v2/container_images <https://docs.datadoghq.com/api/latest/container-images/>`_
             - ``data.attributes.name`` @ ``data.attributes.repo_digest``
             - string
           * - /api/v2/security/scanned-assets-metadata
             - data.attributes.asset.name
             - string


        :param page_token: Its value must come from the ``links`` section of the response of the first request. Do not manually edit it.
        :type page_token: str, optional
        :param page_number: The page number to be retrieved. It should be equal to or greater than 1.
        :type page_number: int, optional
        :param filter_asset_type: The type of the scanned asset.
        :type filter_asset_type: CloudAssetType, optional
        :param filter_asset_name: The name of the scanned asset.
        :type filter_asset_name: str, optional
        :param filter_last_success_origin: The origin of last success scan.
        :type filter_last_success_origin: str, optional
        :param filter_last_success_env: The environment of last success scan.
        :type filter_last_success_env: str, optional
        :rtype: ScannedAssetsMetadata
        """
        kwargs: Dict[str, Any] = {}
        if page_token is not unset:
            kwargs["page_token"] = page_token

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_asset_type is not unset:
            kwargs["filter_asset_type"] = filter_asset_type

        if filter_asset_name is not unset:
            kwargs["filter_asset_name"] = filter_asset_name

        if filter_last_success_origin is not unset:
            kwargs["filter_last_success_origin"] = filter_last_success_origin

        if filter_last_success_env is not unset:
            kwargs["filter_last_success_env"] = filter_last_success_env

        return self._list_scanned_assets_metadata_endpoint.call_with_http_info(**kwargs)

    def list_security_filters(
        self,
    ) -> SecurityFiltersResponse:
        """Get all security filters.

        Get the list of configured security filters with their definitions.

        :rtype: SecurityFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_security_filters_endpoint.call_with_http_info(**kwargs)

    def list_security_filter_versions(
        self,
    ) -> SecurityFilterVersionsResponse:
        """Get the version history of security filters.

        Get the configured security filters at each historical version of the configuration.
        Each entry in the response represents the set of all security filters at a given version,
        ordered from the most recent version to the oldest.

        :rtype: SecurityFilterVersionsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_security_filter_versions_endpoint.call_with_http_info(**kwargs)

    def list_security_findings(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        sort: Union[SecurityFindingsSort, UnsetType] = unset,
    ) -> ListSecurityFindingsResponse:
        """List security findings.

        Get a list of security findings that match a search query. `See the schema for security findings <https://docs.datadoghq.com/security/guide/findings-schema/>`_.

        **Query Syntax**

        This endpoint uses the logs query syntax. Findings attributes (living in the attributes.attributes. namespace) are prefixed by @ when queried. Tags are queried without a prefix.

        Example: ``@severity:(critical OR high) @status:open team:platform``

        :param filter_query: The search query following log search syntax.
        :type filter_query: str, optional
        :param page_cursor: Get the next page of results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: The maximum number of findings in the response.
        :type page_limit: int, optional
        :param sort: Sorts by @detection_changed_at.
        :type sort: SecurityFindingsSort, optional
        :rtype: ListSecurityFindingsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_security_findings_endpoint.call_with_http_info(**kwargs)

    def list_security_findings_with_pagination(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        sort: Union[SecurityFindingsSort, UnsetType] = unset,
    ) -> collections.abc.Iterable[SecurityFindingsData]:
        """List security findings.

        Provide a paginated version of :meth:`list_security_findings`, returning all items.

        :param filter_query: The search query following log search syntax.
        :type filter_query: str, optional
        :param page_cursor: Get the next page of results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: The maximum number of findings in the response.
        :type page_limit: int, optional
        :param sort: Sorts by @detection_changed_at.
        :type sort: SecurityFindingsSort, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[SecurityFindingsData]
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if sort is not unset:
            kwargs["sort"] = sort

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 10)
        endpoint = self._list_security_findings_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_security_findings_automation_due_date_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> DueDateRulesResponse:
        """Get all due date rules.

        Get all due date rules for the current organization.

        :param page_size: The number of rules per page. Maximum is 1000.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :rtype: DueDateRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_security_findings_automation_due_date_rules_endpoint.call_with_http_info(**kwargs)

    def list_security_findings_automation_mute_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> MuteRulesResponse:
        """Get all mute rules.

        Get all mute rules for the current organization.

        :param page_size: The number of rules per page. Maximum is 1000.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :rtype: MuteRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_security_findings_automation_mute_rules_endpoint.call_with_http_info(**kwargs)

    def list_security_findings_automation_ticket_creation_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> TicketCreationRulesResponse:
        """Get all ticket creation rules.

        Get all ticket creation rules for the current organization.

        :param page_size: The number of rules per page. Maximum is 1000.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :rtype: TicketCreationRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_security_findings_automation_ticket_creation_rules_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_critical_assets(
        self,
    ) -> SecurityMonitoringCriticalAssetsResponse:
        """Get all critical assets.

        Get the list of all critical assets.

        :rtype: SecurityMonitoringCriticalAssetsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_security_monitoring_critical_assets_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_datasets(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
    ) -> SecurityMonitoringDatasetsListResponse:
        """List datasets.

        List all Cloud SIEM datasets available to the organization, including both
        customer-defined datasets and Datadog out-of-the-box datasets.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Attribute used to sort datasets. Prefix with ``-`` to sort in descending order.
        :type sort: str, optional
        :param filter_query: A search query to filter datasets by name or description.
        :type filter_query: str, optional
        :rtype: SecurityMonitoringDatasetsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        return self._list_security_monitoring_datasets_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_histsignals(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[SecurityMonitoringSignalsSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> SecurityMonitoringSignalsListResponse:
        """List hist signals.

        List hist signals.

        :param filter_query: The search query for security signals.
        :type filter_query: str, optional
        :param filter_from: The minimum timestamp for requested security signals.
        :type filter_from: datetime, optional
        :param filter_to: The maximum timestamp for requested security signals.
        :type filter_to: datetime, optional
        :param sort: The order of the security signals in results.
        :type sort: SecurityMonitoringSignalsSort, optional
        :param page_cursor: A list of results using the cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: The maximum number of security signals in the response.
        :type page_limit: int, optional
        :rtype: SecurityMonitoringSignalsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_security_monitoring_histsignals_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_integration_configs(
        self,
        *,
        filter_integration_type: Union[SecurityMonitoringIntegrationType, UnsetType] = unset,
    ) -> SecurityMonitoringIntegrationConfigsResponse:
        """List entity context sync configurations.

        List the entity context sync configurations for Cloud SIEM. Each configuration connects Cloud SIEM
        to an external source that provides entities (for example, users from an identity provider) for use
        in signals and the entity explorer.

        :param filter_integration_type: Filter the entity context sync configurations by source type.
        :type filter_integration_type: SecurityMonitoringIntegrationType, optional
        :rtype: SecurityMonitoringIntegrationConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_integration_type is not unset:
            kwargs["filter_integration_type"] = filter_integration_type

        return self._list_security_monitoring_integration_configs_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sort: Union[SecurityMonitoringRuleSort, UnsetType] = unset,
    ) -> SecurityMonitoringListRulesResponse:
        """List rules.

        List rules.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param query: A search query to filter security rules. You can filter by attributes such as ``type`` , ``source`` , ``tags``.
        :type query: str, optional
        :param sort: Attribute used to sort rules. Prefix with ``-`` to sort in descending order.
        :type sort: SecurityMonitoringRuleSort, optional
        :rtype: SecurityMonitoringListRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if query is not unset:
            kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_security_monitoring_rules_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_signals(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[SecurityMonitoringSignalsSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> SecurityMonitoringSignalsListResponse:
        """Get a quick list of security signals.

        The list endpoint returns security signals that match a search query.
        Both this endpoint and the POST endpoint can be used interchangeably when listing
        security signals.

        :param filter_query: The search query for security signals.
        :type filter_query: str, optional
        :param filter_from: The minimum timestamp for requested security signals.
        :type filter_from: datetime, optional
        :param filter_to: The maximum timestamp for requested security signals.
        :type filter_to: datetime, optional
        :param sort: The order of the security signals in results.
        :type sort: SecurityMonitoringSignalsSort, optional
        :param page_cursor: A list of results using the cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: The maximum number of security signals in the response.
        :type page_limit: int, optional
        :rtype: SecurityMonitoringSignalsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_security_monitoring_signals_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_signals_with_pagination(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[SecurityMonitoringSignalsSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[SecurityMonitoringSignal]:
        """Get a quick list of security signals.

        Provide a paginated version of :meth:`list_security_monitoring_signals`, returning all items.

        :param filter_query: The search query for security signals.
        :type filter_query: str, optional
        :param filter_from: The minimum timestamp for requested security signals.
        :type filter_from: datetime, optional
        :param filter_to: The maximum timestamp for requested security signals.
        :type filter_to: datetime, optional
        :param sort: The order of the security signals in results.
        :type sort: SecurityMonitoringSignalsSort, optional
        :param page_cursor: A list of results using the cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: The maximum number of security signals in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[SecurityMonitoringSignal]
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 10)
        endpoint = self._list_security_monitoring_signals_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_security_monitoring_suppressions(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        sort: Union[SecurityMonitoringSuppressionSort, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> SecurityMonitoringPaginatedSuppressionsResponse:
        """Get all suppression rules.

        Get the list of all suppression rules.

        :param query: Query string.
        :type query: str, optional
        :param sort: Attribute used to sort the list of suppression rules. Prefix with ``-`` to sort in descending order.
        :type sort: SecurityMonitoringSuppressionSort, optional
        :param page_size: Size for a given page. Use ``-1`` to return all items.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: SecurityMonitoringPaginatedSuppressionsResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_security_monitoring_suppressions_endpoint.call_with_http_info(**kwargs)

    def list_static_analysis_codegen_rulesets(
        self,
    ) -> SastRulesetsResponse:
        """List codegen rulesets.

        Get the rulesets relevant for code generation for the authenticated user.

        :rtype: SastRulesetsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_static_analysis_codegen_rulesets_endpoint.call_with_http_info(**kwargs)

    def list_vulnerabilities(
        self,
        *,
        page_token: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_type: Union[VulnerabilityType, UnsetType] = unset,
        filter_cvss_base_score_op: Union[float, UnsetType] = unset,
        filter_cvss_base_severity: Union[VulnerabilitySeverity, UnsetType] = unset,
        filter_cvss_base_vector: Union[str, UnsetType] = unset,
        filter_cvss_datadog_score_op: Union[float, UnsetType] = unset,
        filter_cvss_datadog_severity: Union[VulnerabilitySeverity, UnsetType] = unset,
        filter_cvss_datadog_vector: Union[str, UnsetType] = unset,
        filter_status: Union[VulnerabilityStatus, UnsetType] = unset,
        filter_tool: Union[VulnerabilityTool, UnsetType] = unset,
        filter_library_name: Union[str, UnsetType] = unset,
        filter_library_version: Union[str, UnsetType] = unset,
        filter_advisory_id: Union[str, UnsetType] = unset,
        filter_risks_exploitation_probability: Union[bool, UnsetType] = unset,
        filter_risks_poc_exploit_available: Union[bool, UnsetType] = unset,
        filter_risks_exploit_available: Union[bool, UnsetType] = unset,
        filter_risks_epss_score_op: Union[float, UnsetType] = unset,
        filter_risks_epss_severity: Union[VulnerabilitySeverity, UnsetType] = unset,
        filter_language: Union[str, UnsetType] = unset,
        filter_ecosystem: Union[VulnerabilityEcosystem, UnsetType] = unset,
        filter_code_location_location: Union[str, UnsetType] = unset,
        filter_code_location_file_path: Union[str, UnsetType] = unset,
        filter_code_location_method: Union[str, UnsetType] = unset,
        filter_fix_available: Union[bool, UnsetType] = unset,
        filter_repo_digests: Union[str, UnsetType] = unset,
        filter_origin: Union[str, UnsetType] = unset,
        filter_running_kernel: Union[bool, UnsetType] = unset,
        filter_asset_name: Union[str, UnsetType] = unset,
        filter_asset_type: Union[AssetType, UnsetType] = unset,
        filter_asset_version_first: Union[str, UnsetType] = unset,
        filter_asset_version_last: Union[str, UnsetType] = unset,
        filter_asset_repository_url: Union[str, UnsetType] = unset,
        filter_asset_risks_in_production: Union[bool, UnsetType] = unset,
        filter_asset_risks_under_attack: Union[bool, UnsetType] = unset,
        filter_asset_risks_is_publicly_accessible: Union[bool, UnsetType] = unset,
        filter_asset_risks_has_privileged_access: Union[bool, UnsetType] = unset,
        filter_asset_risks_has_access_to_sensitive_data: Union[bool, UnsetType] = unset,
        filter_asset_environments: Union[str, UnsetType] = unset,
        filter_asset_teams: Union[str, UnsetType] = unset,
        filter_asset_arch: Union[str, UnsetType] = unset,
        filter_asset_operating_system_name: Union[str, UnsetType] = unset,
        filter_asset_operating_system_version: Union[str, UnsetType] = unset,
    ) -> ListVulnerabilitiesResponse:
        """List vulnerabilities. **Deprecated**.

        Get a list of vulnerabilities.

        **Pagination**

        Pagination is enabled by default in both ``vulnerabilities`` and ``assets``. The size of the page varies depending on the endpoint and cannot be modified. To automate the request of the next page, you can use the links section in the response.

        This endpoint will return paginated responses. The pages are stored in the links section of the response:

        .. code-block:: JSON

           {
             "data": [...],
             "meta": {...},
             "links": {
               "self": "https://.../api/v2/security/vulnerabilities",
               "first": "https://.../api/v2/security/vulnerabilities?page[number]=1&page[token]=abc",
               "last": "https://.../api/v2/security/vulnerabilities?page[number]=43&page[token]=abc",
               "next": "https://.../api/v2/security/vulnerabilities?page[number]=2&page[token]=abc"
             }
           }

        * ``links.previous`` is empty if the first page is requested.
        * ``links.next`` is empty if the last page is requested.

        **Token**

        Vulnerabilities can be created, updated or deleted at any point in time.

        Upon the first request, a token is created to ensure consistency across subsequent paginated requests.

        A token is valid only for 24 hours.

        **First request**

        We consider a request to be the first request when there is no ``page[token]`` parameter.

        The response of this first request contains the newly created token in the ``links`` section.

        This token can then be used in the subsequent paginated requests.

        *Note: The first request may take longer to complete than subsequent requests.*

        **Subsequent requests**

        Any request containing valid ``page[token]`` and ``page[number]`` parameters will be considered a subsequent request.

        If the ``token`` is invalid, a ``404`` response will be returned.

        If the page ``number`` is invalid, a ``400`` response will be returned.

        The returned ``token`` is valid for all requests in the pagination sequence. To send paginated requests in parallel, reuse the same ``token`` and change only the ``page[number]`` parameter.

        **Filtering**

        The request can include some filter parameters to filter the data to be retrieved. The format of the filter parameters follows the `JSON:API format <https://jsonapi.org/format/#fetching-filtering>`_ : ``filter[$prop_name]`` , where ``prop_name`` is the property name in the entity being filtered by.

        All filters can include multiple values, where data will be filtered with an OR clause: ``filter[title]=Title1,Title2`` will filter all vulnerabilities where title is equal to ``Title1`` OR ``Title2``.

        String filters are case sensitive.

        Boolean filters accept ``true`` or ``false`` as values.

        Number filters must include an operator as a second filter input: ``filter[$prop_name][$operator]``. For example, for the vulnerabilities endpoint: ``filter[cvss.base.score][lte]=8``.

        Available operators are: ``eq`` (==), ``lt`` (<), ``lte`` (<=), ``gt`` (>) and ``gte`` (>=).

        **Metadata**

        Following `JSON:API format <https://jsonapi.org/format/#document-meta>`_ , object including non-standard meta-information.

        This endpoint includes the meta member in the response. For more details on each of the properties included in this section, check the endpoints response tables.

        .. code-block:: JSON

           {
             "data": [...],
             "meta": {
               "total": 1500,
               "count": 18732,
               "token": "some_token"
             },
             "links": {...}
           }

        **Extensions**

        Requests may include extensions to modify the behavior of the requested endpoint. The filter parameters follow the `JSON:API format <https://jsonapi.org/extensions/#extensions>`_ format: ``ext:$extension_name`` , where ``extension_name`` is the name of the modifier that is being applied.

        Extensions can only include one value: ``ext:modifier=value``.

        :param page_token: Its value must come from the ``links`` section of the response of the first request. Do not manually edit it.
        :type page_token: str, optional
        :param page_number: The page number to be retrieved. It should be equal or greater than ``1``
        :type page_number: int, optional
        :param filter_type: Filter by vulnerability type.
        :type filter_type: VulnerabilityType, optional
        :param filter_cvss_base_score_op: Filter by vulnerability base (i.e. from the original advisory) severity score.
        :type filter_cvss_base_score_op: float, optional
        :param filter_cvss_base_severity: Filter by vulnerability base severity.
        :type filter_cvss_base_severity: VulnerabilitySeverity, optional
        :param filter_cvss_base_vector: Filter by vulnerability base CVSS vector.
        :type filter_cvss_base_vector: str, optional
        :param filter_cvss_datadog_score_op: Filter by vulnerability Datadog severity score.
        :type filter_cvss_datadog_score_op: float, optional
        :param filter_cvss_datadog_severity: Filter by vulnerability Datadog severity.
        :type filter_cvss_datadog_severity: VulnerabilitySeverity, optional
        :param filter_cvss_datadog_vector: Filter by vulnerability Datadog CVSS vector.
        :type filter_cvss_datadog_vector: str, optional
        :param filter_status: Filter by the status of the vulnerability.
        :type filter_status: VulnerabilityStatus, optional
        :param filter_tool: Filter by the tool of the vulnerability.
        :type filter_tool: VulnerabilityTool, optional
        :param filter_library_name: Filter by library name.
        :type filter_library_name: str, optional
        :param filter_library_version: Filter by library version.
        :type filter_library_version: str, optional
        :param filter_advisory_id: Filter by advisory ID.
        :type filter_advisory_id: str, optional
        :param filter_risks_exploitation_probability: Filter by exploitation probability.
        :type filter_risks_exploitation_probability: bool, optional
        :param filter_risks_poc_exploit_available: Filter by POC exploit availability.
        :type filter_risks_poc_exploit_available: bool, optional
        :param filter_risks_exploit_available: Filter by public exploit availability.
        :type filter_risks_exploit_available: bool, optional
        :param filter_risks_epss_score_op: Filter by vulnerability `EPSS <https://www.first.org/epss/>`_ severity score.
        :type filter_risks_epss_score_op: float, optional
        :param filter_risks_epss_severity: Filter by vulnerability `EPSS <https://www.first.org/epss/>`_ severity.
        :type filter_risks_epss_severity: VulnerabilitySeverity, optional
        :param filter_language: Filter by language.
        :type filter_language: str, optional
        :param filter_ecosystem: Filter by ecosystem.
        :type filter_ecosystem: VulnerabilityEcosystem, optional
        :param filter_code_location_location: Filter by vulnerability location.
        :type filter_code_location_location: str, optional
        :param filter_code_location_file_path: Filter by vulnerability file path.
        :type filter_code_location_file_path: str, optional
        :param filter_code_location_method: Filter by method.
        :type filter_code_location_method: str, optional
        :param filter_fix_available: Filter by fix availability.
        :type filter_fix_available: bool, optional
        :param filter_repo_digests: Filter by vulnerability ``repo_digest`` (when the vulnerability is related to ``Image`` asset).
        :type filter_repo_digests: str, optional
        :param filter_origin: Filter by origin.
        :type filter_origin: str, optional
        :param filter_running_kernel: Filter for whether the vulnerability affects a running kernel (for vulnerabilities related to a ``Host`` asset).
        :type filter_running_kernel: bool, optional
        :param filter_asset_name: Filter by asset name. This field supports the usage of wildcards (*).
        :type filter_asset_name: str, optional
        :param filter_asset_type: Filter by asset type.
        :type filter_asset_type: AssetType, optional
        :param filter_asset_version_first: Filter by the first version of the asset this vulnerability has been detected on.
        :type filter_asset_version_first: str, optional
        :param filter_asset_version_last: Filter by the last version of the asset this vulnerability has been detected on.
        :type filter_asset_version_last: str, optional
        :param filter_asset_repository_url: Filter by the repository url associated to the asset.
        :type filter_asset_repository_url: str, optional
        :param filter_asset_risks_in_production: Filter whether the asset is in production or not.
        :type filter_asset_risks_in_production: bool, optional
        :param filter_asset_risks_under_attack: Filter whether the asset is under attack or not.
        :type filter_asset_risks_under_attack: bool, optional
        :param filter_asset_risks_is_publicly_accessible: Filter whether the asset is publicly accessible or not.
        :type filter_asset_risks_is_publicly_accessible: bool, optional
        :param filter_asset_risks_has_privileged_access: Filter whether the asset is publicly accessible or not.
        :type filter_asset_risks_has_privileged_access: bool, optional
        :param filter_asset_risks_has_access_to_sensitive_data: Filter whether the asset  has access to sensitive data or not.
        :type filter_asset_risks_has_access_to_sensitive_data: bool, optional
        :param filter_asset_environments: Filter by asset environments.
        :type filter_asset_environments: str, optional
        :param filter_asset_teams: Filter by asset teams.
        :type filter_asset_teams: str, optional
        :param filter_asset_arch: Filter by asset architecture.
        :type filter_asset_arch: str, optional
        :param filter_asset_operating_system_name: Filter by asset operating system name.
        :type filter_asset_operating_system_name: str, optional
        :param filter_asset_operating_system_version: Filter by asset operating system version.
        :type filter_asset_operating_system_version: str, optional
        :rtype: ListVulnerabilitiesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_token is not unset:
            kwargs["page_token"] = page_token

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_type is not unset:
            kwargs["filter_type"] = filter_type

        if filter_cvss_base_score_op is not unset:
            kwargs["filter_cvss_base_score_op"] = filter_cvss_base_score_op

        if filter_cvss_base_severity is not unset:
            kwargs["filter_cvss_base_severity"] = filter_cvss_base_severity

        if filter_cvss_base_vector is not unset:
            kwargs["filter_cvss_base_vector"] = filter_cvss_base_vector

        if filter_cvss_datadog_score_op is not unset:
            kwargs["filter_cvss_datadog_score_op"] = filter_cvss_datadog_score_op

        if filter_cvss_datadog_severity is not unset:
            kwargs["filter_cvss_datadog_severity"] = filter_cvss_datadog_severity

        if filter_cvss_datadog_vector is not unset:
            kwargs["filter_cvss_datadog_vector"] = filter_cvss_datadog_vector

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_tool is not unset:
            kwargs["filter_tool"] = filter_tool

        if filter_library_name is not unset:
            kwargs["filter_library_name"] = filter_library_name

        if filter_library_version is not unset:
            kwargs["filter_library_version"] = filter_library_version

        if filter_advisory_id is not unset:
            kwargs["filter_advisory_id"] = filter_advisory_id

        if filter_risks_exploitation_probability is not unset:
            kwargs["filter_risks_exploitation_probability"] = filter_risks_exploitation_probability

        if filter_risks_poc_exploit_available is not unset:
            kwargs["filter_risks_poc_exploit_available"] = filter_risks_poc_exploit_available

        if filter_risks_exploit_available is not unset:
            kwargs["filter_risks_exploit_available"] = filter_risks_exploit_available

        if filter_risks_epss_score_op is not unset:
            kwargs["filter_risks_epss_score_op"] = filter_risks_epss_score_op

        if filter_risks_epss_severity is not unset:
            kwargs["filter_risks_epss_severity"] = filter_risks_epss_severity

        if filter_language is not unset:
            kwargs["filter_language"] = filter_language

        if filter_ecosystem is not unset:
            kwargs["filter_ecosystem"] = filter_ecosystem

        if filter_code_location_location is not unset:
            kwargs["filter_code_location_location"] = filter_code_location_location

        if filter_code_location_file_path is not unset:
            kwargs["filter_code_location_file_path"] = filter_code_location_file_path

        if filter_code_location_method is not unset:
            kwargs["filter_code_location_method"] = filter_code_location_method

        if filter_fix_available is not unset:
            kwargs["filter_fix_available"] = filter_fix_available

        if filter_repo_digests is not unset:
            kwargs["filter_repo_digests"] = filter_repo_digests

        if filter_origin is not unset:
            kwargs["filter_origin"] = filter_origin

        if filter_running_kernel is not unset:
            kwargs["filter_running_kernel"] = filter_running_kernel

        if filter_asset_name is not unset:
            kwargs["filter_asset_name"] = filter_asset_name

        if filter_asset_type is not unset:
            kwargs["filter_asset_type"] = filter_asset_type

        if filter_asset_version_first is not unset:
            kwargs["filter_asset_version_first"] = filter_asset_version_first

        if filter_asset_version_last is not unset:
            kwargs["filter_asset_version_last"] = filter_asset_version_last

        if filter_asset_repository_url is not unset:
            kwargs["filter_asset_repository_url"] = filter_asset_repository_url

        if filter_asset_risks_in_production is not unset:
            kwargs["filter_asset_risks_in_production"] = filter_asset_risks_in_production

        if filter_asset_risks_under_attack is not unset:
            kwargs["filter_asset_risks_under_attack"] = filter_asset_risks_under_attack

        if filter_asset_risks_is_publicly_accessible is not unset:
            kwargs["filter_asset_risks_is_publicly_accessible"] = filter_asset_risks_is_publicly_accessible

        if filter_asset_risks_has_privileged_access is not unset:
            kwargs["filter_asset_risks_has_privileged_access"] = filter_asset_risks_has_privileged_access

        if filter_asset_risks_has_access_to_sensitive_data is not unset:
            kwargs["filter_asset_risks_has_access_to_sensitive_data"] = filter_asset_risks_has_access_to_sensitive_data

        if filter_asset_environments is not unset:
            kwargs["filter_asset_environments"] = filter_asset_environments

        if filter_asset_teams is not unset:
            kwargs["filter_asset_teams"] = filter_asset_teams

        if filter_asset_arch is not unset:
            kwargs["filter_asset_arch"] = filter_asset_arch

        if filter_asset_operating_system_name is not unset:
            kwargs["filter_asset_operating_system_name"] = filter_asset_operating_system_name

        if filter_asset_operating_system_version is not unset:
            kwargs["filter_asset_operating_system_version"] = filter_asset_operating_system_version

        warnings.warn("list_vulnerabilities is deprecated", DeprecationWarning, stacklevel=2)
        return self._list_vulnerabilities_endpoint.call_with_http_info(**kwargs)

    def list_vulnerable_assets(
        self,
        *,
        page_token: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        filter_type: Union[AssetType, UnsetType] = unset,
        filter_version_first: Union[str, UnsetType] = unset,
        filter_version_last: Union[str, UnsetType] = unset,
        filter_repository_url: Union[str, UnsetType] = unset,
        filter_risks_in_production: Union[bool, UnsetType] = unset,
        filter_risks_under_attack: Union[bool, UnsetType] = unset,
        filter_risks_is_publicly_accessible: Union[bool, UnsetType] = unset,
        filter_risks_has_privileged_access: Union[bool, UnsetType] = unset,
        filter_risks_has_access_to_sensitive_data: Union[bool, UnsetType] = unset,
        filter_environments: Union[str, UnsetType] = unset,
        filter_teams: Union[str, UnsetType] = unset,
        filter_arch: Union[str, UnsetType] = unset,
        filter_operating_system_name: Union[str, UnsetType] = unset,
        filter_operating_system_version: Union[str, UnsetType] = unset,
    ) -> ListVulnerableAssetsResponse:
        """List vulnerable assets.

        Get a list of vulnerable assets.

        **Pagination**

        Please review the `Pagination section for the "List Vulnerabilities" <#pagination>`_ endpoint.

        **Filtering**

        Please review the `Filtering section for the "List Vulnerabilities" <#filtering>`_ endpoint.

        **Metadata**

        Please review the `Metadata section for the "List Vulnerabilities" <#metadata>`_ endpoint.

        :param page_token: Its value must come from the ``links`` section of the response of the first request. Do not manually edit it.
        :type page_token: str, optional
        :param page_number: The page number to be retrieved. It should be equal or greater than ``1``
        :type page_number: int, optional
        :param filter_name: Filter by name. This field supports the usage of wildcards (*).
        :type filter_name: str, optional
        :param filter_type: Filter by type.
        :type filter_type: AssetType, optional
        :param filter_version_first: Filter by the first version of the asset since it has been vulnerable.
        :type filter_version_first: str, optional
        :param filter_version_last: Filter by the last detected version of the asset.
        :type filter_version_last: str, optional
        :param filter_repository_url: Filter by the repository url associated to the asset.
        :type filter_repository_url: str, optional
        :param filter_risks_in_production: Filter whether the asset is in production or not.
        :type filter_risks_in_production: bool, optional
        :param filter_risks_under_attack: Filter whether the asset (Service) is under attack or not.
        :type filter_risks_under_attack: bool, optional
        :param filter_risks_is_publicly_accessible: Filter whether the asset (Host) is publicly accessible or not.
        :type filter_risks_is_publicly_accessible: bool, optional
        :param filter_risks_has_privileged_access: Filter whether the asset (Host) has privileged access or not.
        :type filter_risks_has_privileged_access: bool, optional
        :param filter_risks_has_access_to_sensitive_data: Filter whether the asset (Host)  has access to sensitive data or not.
        :type filter_risks_has_access_to_sensitive_data: bool, optional
        :param filter_environments: Filter by environment.
        :type filter_environments: str, optional
        :param filter_teams: Filter by teams.
        :type filter_teams: str, optional
        :param filter_arch: Filter by architecture.
        :type filter_arch: str, optional
        :param filter_operating_system_name: Filter by operating system name.
        :type filter_operating_system_name: str, optional
        :param filter_operating_system_version: Filter by operating system version.
        :type filter_operating_system_version: str, optional
        :rtype: ListVulnerableAssetsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_token is not unset:
            kwargs["page_token"] = page_token

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if filter_type is not unset:
            kwargs["filter_type"] = filter_type

        if filter_version_first is not unset:
            kwargs["filter_version_first"] = filter_version_first

        if filter_version_last is not unset:
            kwargs["filter_version_last"] = filter_version_last

        if filter_repository_url is not unset:
            kwargs["filter_repository_url"] = filter_repository_url

        if filter_risks_in_production is not unset:
            kwargs["filter_risks_in_production"] = filter_risks_in_production

        if filter_risks_under_attack is not unset:
            kwargs["filter_risks_under_attack"] = filter_risks_under_attack

        if filter_risks_is_publicly_accessible is not unset:
            kwargs["filter_risks_is_publicly_accessible"] = filter_risks_is_publicly_accessible

        if filter_risks_has_privileged_access is not unset:
            kwargs["filter_risks_has_privileged_access"] = filter_risks_has_privileged_access

        if filter_risks_has_access_to_sensitive_data is not unset:
            kwargs["filter_risks_has_access_to_sensitive_data"] = filter_risks_has_access_to_sensitive_data

        if filter_environments is not unset:
            kwargs["filter_environments"] = filter_environments

        if filter_teams is not unset:
            kwargs["filter_teams"] = filter_teams

        if filter_arch is not unset:
            kwargs["filter_arch"] = filter_arch

        if filter_operating_system_name is not unset:
            kwargs["filter_operating_system_name"] = filter_operating_system_name

        if filter_operating_system_version is not unset:
            kwargs["filter_operating_system_version"] = filter_operating_system_version

        return self._list_vulnerable_assets_endpoint.call_with_http_info(**kwargs)

    def mute_security_findings(
        self,
        body: MuteFindingsRequest,
    ) -> MuteFindingsResponse:
        """Mute or unmute security findings.

        Mute or unmute security findings.
        You can mute or unmute up to 100 security findings per request. The request body must include ``is_muted`` and ``reason`` attributes. The allowed reasons depend on whether the finding is being muted or unmuted:

        * To mute a finding: ``PENDING_FIX`` , ``FALSE_POSITIVE`` , ``OTHER`` , ``NO_FIX`` , ``DUPLICATE`` , ``RISK_ACCEPTED``.
        * To unmute a finding: ``NO_PENDING_FIX`` , ``HUMAN_ERROR`` , ``NO_LONGER_ACCEPTED_RISK`` , ``OTHER``.

        :type body: MuteFindingsRequest
        :rtype: MuteFindingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._mute_security_findings_endpoint.call_with_http_info(**kwargs)

    def patch_signal_notification_rule(
        self,
        id: str,
        body: PatchNotificationRuleParameters,
    ) -> NotificationRuleResponse:
        """Patch a signal-based notification rule.

        Partially update the notification rule. All fields are optional; if a field is not provided, it is not updated.

        :param id: ID of the notification rule.
        :type id: str
        :type body: PatchNotificationRuleParameters
        :rtype: NotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._patch_signal_notification_rule_endpoint.call_with_http_info(**kwargs)

    def patch_vulnerability_notification_rule(
        self,
        id: str,
        body: PatchNotificationRuleParameters,
    ) -> NotificationRuleResponse:
        """Patch a vulnerability-based notification rule.

        Partially update the notification rule. All fields are optional; if a field is not provided, it is not updated.

        :param id: ID of the notification rule.
        :type id: str
        :type body: PatchNotificationRuleParameters
        :rtype: NotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._patch_vulnerability_notification_rule_endpoint.call_with_http_info(**kwargs)

    def reorder_security_findings_automation_due_date_rules(
        self,
        body: DueDateRuleReorderRequest,
    ) -> DueDateRuleReorderRequest:
        """Reorder due date rules.

        Reorder the list of due date rules for the current organization.

        :type body: DueDateRuleReorderRequest
        :rtype: DueDateRuleReorderRequest
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._reorder_security_findings_automation_due_date_rules_endpoint.call_with_http_info(**kwargs)

    def reorder_security_findings_automation_mute_rules(
        self,
        body: MuteRuleReorderRequest,
    ) -> MuteRuleReorderRequest:
        """Reorder mute rules.

        Reorder the list of mute rules for the current organization.

        :type body: MuteRuleReorderRequest
        :rtype: MuteRuleReorderRequest
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._reorder_security_findings_automation_mute_rules_endpoint.call_with_http_info(**kwargs)

    def reorder_security_findings_automation_ticket_creation_rules(
        self,
        body: TicketCreationRuleReorderRequest,
    ) -> TicketCreationRuleReorderRequest:
        """Reorder ticket creation rules.

        Reorder the list of ticket creation rules for the current organization.

        :type body: TicketCreationRuleReorderRequest
        :rtype: TicketCreationRuleReorderRequest
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._reorder_security_findings_automation_ticket_creation_rules_endpoint.call_with_http_info(**kwargs)

    def restore_security_monitoring_rule(
        self,
        rule_id: str,
        version: int,
    ) -> SecurityMonitoringRuleResponse:
        """Restore a rule to a historical version.

        Restores a custom detection rule to a previously saved historical version.
        Only custom rules can be restored. Default and partner rules return 400.
        The restore creates a new version entry; it does not overwrite history.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :param version: The historical version number of the rule.
        :type version: int
        :rtype: SecurityMonitoringRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["version"] = version

        return self._restore_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def run_historical_job(
        self,
        body: RunHistoricalJobRequest,
    ) -> JobCreateResponse:
        """Run a historical job.

        Run a historical job.

        :type body: RunHistoricalJobRequest
        :rtype: JobCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._run_historical_job_endpoint.call_with_http_info(**kwargs)

    def search_security_findings(
        self,
        body: SecurityFindingsSearchRequest,
    ) -> ListSecurityFindingsResponse:
        """Search security findings.

        Get a list of security findings that match a search query. `See the schema for security findings <https://docs.datadoghq.com/security/guide/findings-schema/>`_.

        **Query Syntax**

        The API uses the logs query syntax. Findings attributes (living in the attributes.attributes. namespace) are prefixed by @ when queried. Tags are queried without a prefix.

        Example: ``@severity:(critical OR high) @status:open team:platform``

        :type body: SecurityFindingsSearchRequest
        :rtype: ListSecurityFindingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._search_security_findings_endpoint.call_with_http_info(**kwargs)

    def search_security_findings_with_pagination(
        self,
        body: SecurityFindingsSearchRequest,
    ) -> collections.abc.Iterable[SecurityFindingsData]:
        """Search security findings.

        Provide a paginated version of :meth:`search_security_findings`, returning all items.

        :type body: SecurityFindingsSearchRequest

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[SecurityFindingsData]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.data.attributes.page.limit", 10)
        endpoint = self._search_security_findings_endpoint
        set_attribute_from_path(kwargs, "body.data.attributes.page.limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "body.data.attributes.page.cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def search_security_monitoring_histsignals(
        self,
        *,
        body: Union[SecurityMonitoringSignalListRequest, UnsetType] = unset,
    ) -> SecurityMonitoringSignalsListResponse:
        """Search hist signals.

        Search hist signals.

        :type body: SecurityMonitoringSignalListRequest, optional
        :rtype: SecurityMonitoringSignalsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._search_security_monitoring_histsignals_endpoint.call_with_http_info(**kwargs)

    def search_security_monitoring_signals(
        self,
        *,
        body: Union[SecurityMonitoringSignalListRequest, UnsetType] = unset,
    ) -> SecurityMonitoringSignalsListResponse:
        """Get a list of security signals.

        Returns security signals that match a search query.
        Both this endpoint and the GET endpoint can be used interchangeably for listing
        security signals.

        :type body: SecurityMonitoringSignalListRequest, optional
        :rtype: SecurityMonitoringSignalsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._search_security_monitoring_signals_endpoint.call_with_http_info(**kwargs)

    def search_security_monitoring_signals_with_pagination(
        self,
        *,
        body: Union[SecurityMonitoringSignalListRequest, UnsetType] = unset,
    ) -> collections.abc.Iterable[SecurityMonitoringSignal]:
        """Get a list of security signals.

        Provide a paginated version of :meth:`search_security_monitoring_signals`, returning all items.

        :type body: SecurityMonitoringSignalListRequest, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[SecurityMonitoringSignal]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.page.limit", 10)
        endpoint = self._search_security_monitoring_signals_endpoint
        set_attribute_from_path(kwargs, "body.page.limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "body.page.cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def send_security_monitoring_notification_preview(
        self,
        body: CreateNotificationRuleParameters,
    ) -> NotificationRulePreviewResponse:
        """Test a notification rule.

        Send a notification preview to test that a notification rule's targets are properly configured.

        :type body: CreateNotificationRuleParameters
        :rtype: NotificationRulePreviewResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._send_security_monitoring_notification_preview_endpoint.call_with_http_info(**kwargs)

    def test_existing_security_monitoring_rule(
        self,
        rule_id: str,
        body: SecurityMonitoringRuleTestRequest,
    ) -> SecurityMonitoringRuleTestResponse:
        """Test an existing rule.

        Test an existing rule.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :type body: SecurityMonitoringRuleTestRequest
        :rtype: SecurityMonitoringRuleTestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._test_existing_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def test_security_monitoring_rule(
        self,
        body: SecurityMonitoringRuleTestRequest,
    ) -> SecurityMonitoringRuleTestResponse:
        """Test a rule.

        Test a rule.

        :type body: SecurityMonitoringRuleTestRequest
        :rtype: SecurityMonitoringRuleTestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._test_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def update_custom_framework(
        self,
        handle: str,
        version: str,
        body: UpdateCustomFrameworkRequest,
    ) -> UpdateCustomFrameworkResponse:
        """Update a custom framework.

        Update a custom framework.

        :param handle: The framework handle
        :type handle: str
        :param version: The framework version
        :type version: str
        :type body: UpdateCustomFrameworkRequest
        :rtype: UpdateCustomFrameworkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["handle"] = handle

        kwargs["version"] = version

        kwargs["body"] = body

        return self._update_custom_framework_endpoint.call_with_http_info(**kwargs)

    def update_findings_assignee(
        self,
        body: AssigneeRequest,
    ) -> AssigneeResponse:
        """Assign or unassign security findings.

        Assign or unassign security findings.
        You can assign up to 100 security findings per request. Set ``assignee_id`` to the unique identifier of the Datadog user you want to assign the findings to. Omit ``assignee_id`` (or set it to ``null`` ) to unassign the findings. Per-finding warnings and failures are returned in the response ``meta`` object.

        :type body: AssigneeRequest
        :rtype: AssigneeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_findings_assignee_endpoint.call_with_http_info(**kwargs)

    def update_resource_evaluation_filters(
        self,
        body: UpdateResourceEvaluationFiltersRequest,
    ) -> UpdateResourceEvaluationFiltersResponse:
        """Update resource filters.

        Update resource filters.

        :type body: UpdateResourceEvaluationFiltersRequest
        :rtype: UpdateResourceEvaluationFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_resource_evaluation_filters_endpoint.call_with_http_info(**kwargs)

    def update_security_filter(
        self,
        security_filter_id: str,
        body: SecurityFilterUpdateRequest,
    ) -> SecurityFilterResponse:
        """Update a security filter.

        Update a specific security filter.
        Returns the security filter object when the request is successful.

        :param security_filter_id: The ID of the security filter.
        :type security_filter_id: str
        :param body: New definition of the security filter.
        :type body: SecurityFilterUpdateRequest
        :rtype: SecurityFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["security_filter_id"] = security_filter_id

        kwargs["body"] = body

        return self._update_security_filter_endpoint.call_with_http_info(**kwargs)

    def update_security_findings_automation_due_date_rule(
        self,
        rule_id: UUID,
        body: DueDateRuleUpdateRequest,
    ) -> DueDateRuleResponse:
        """Update a due date rule.

        Update an existing due date rule by ID.

        :param rule_id: The ID of the due date rule.
        :type rule_id: UUID
        :type body: DueDateRuleUpdateRequest
        :rtype: DueDateRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_security_findings_automation_due_date_rule_endpoint.call_with_http_info(**kwargs)

    def update_security_findings_automation_mute_rule(
        self,
        rule_id: UUID,
        body: MuteRuleUpdateRequest,
    ) -> MuteRuleResponse:
        """Update a mute rule.

        Update an existing mute rule by ID.

        :param rule_id: The ID of the mute rule.
        :type rule_id: UUID
        :type body: MuteRuleUpdateRequest
        :rtype: MuteRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_security_findings_automation_mute_rule_endpoint.call_with_http_info(**kwargs)

    def update_security_findings_automation_ticket_creation_rule(
        self,
        rule_id: UUID,
        body: TicketCreationRuleUpdateRequest,
    ) -> TicketCreationRuleResponse:
        """Update a ticket creation rule.

        Update an existing ticket creation rule by ID.

        :param rule_id: The ID of the ticket creation rule.
        :type rule_id: UUID
        :type body: TicketCreationRuleUpdateRequest
        :rtype: TicketCreationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_security_findings_automation_ticket_creation_rule_endpoint.call_with_http_info(**kwargs)

    def update_security_monitoring_critical_asset(
        self,
        critical_asset_id: str,
        body: SecurityMonitoringCriticalAssetUpdateRequest,
    ) -> SecurityMonitoringCriticalAssetResponse:
        """Update a critical asset.

        Update a specific critical asset.

        :param critical_asset_id: The ID of the critical asset.
        :type critical_asset_id: str
        :param body: New definition of the critical asset. Supports partial updates.
        :type body: SecurityMonitoringCriticalAssetUpdateRequest
        :rtype: SecurityMonitoringCriticalAssetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["critical_asset_id"] = critical_asset_id

        kwargs["body"] = body

        return self._update_security_monitoring_critical_asset_endpoint.call_with_http_info(**kwargs)

    def update_security_monitoring_dataset(
        self,
        dataset_id: str,
        body: SecurityMonitoringDatasetUpdateRequest,
    ) -> None:
        """Update a dataset.

        Update an existing Cloud SIEM dataset. The current version of the dataset can be
        provided to detect concurrent modifications.

        :param dataset_id: The UUID of the dataset.
        :type dataset_id: str
        :type body: SecurityMonitoringDatasetUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        kwargs["body"] = body

        return self._update_security_monitoring_dataset_endpoint.call_with_http_info(**kwargs)

    def update_security_monitoring_integration_config(
        self,
        integration_config_id: str,
        body: SecurityMonitoringIntegrationConfigUpdateRequest,
    ) -> SecurityMonitoringIntegrationConfigResponse:
        """Update an entity context sync configuration.

        Update an existing entity context sync configuration. Supports partial updates; only the fields provided in the request body are modified.

        :param integration_config_id: The ID of the entity context sync configuration.
        :type integration_config_id: str
        :param body: The fields to update on the integration configuration.
        :type body: SecurityMonitoringIntegrationConfigUpdateRequest
        :rtype: SecurityMonitoringIntegrationConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_config_id"] = integration_config_id

        kwargs["body"] = body

        return self._update_security_monitoring_integration_config_endpoint.call_with_http_info(**kwargs)

    def update_security_monitoring_rule(
        self,
        rule_id: str,
        body: SecurityMonitoringRuleUpdatePayload,
    ) -> SecurityMonitoringRuleResponse:
        """Update an existing rule.

        Update an existing rule. When updating ``cases`` , ``queries`` or ``options`` , the whole field
        must be included. For example, when modifying a query all queries must be included.
        Default rules can only be updated to be enabled, to change notifications, or to update
        the tags (default tags cannot be removed).

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :type body: SecurityMonitoringRuleUpdatePayload
        :rtype: SecurityMonitoringRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def update_security_monitoring_suppression(
        self,
        suppression_id: str,
        body: SecurityMonitoringSuppressionUpdateRequest,
    ) -> SecurityMonitoringSuppressionResponse:
        """Update a suppression rule.

        Update a specific suppression rule.

        :param suppression_id: The ID of the suppression rule
        :type suppression_id: str
        :param body: New definition of the suppression rule. Supports partial updates.
        :type body: SecurityMonitoringSuppressionUpdateRequest
        :rtype: SecurityMonitoringSuppressionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["suppression_id"] = suppression_id

        kwargs["body"] = body

        return self._update_security_monitoring_suppression_endpoint.call_with_http_info(**kwargs)

    def validate_security_monitoring_integration_config(
        self,
        integration_config_id: str,
    ) -> None:
        """Validate an entity context sync configuration.

        Validate the credentials currently stored on an existing entity context sync configuration.
        Returns a 200 status code if the credentials are still valid against the external entity source.

        :param integration_config_id: The ID of the entity context sync configuration.
        :type integration_config_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_config_id"] = integration_config_id

        return self._validate_security_monitoring_integration_config_endpoint.call_with_http_info(**kwargs)

    def validate_security_monitoring_integration_credentials(
        self,
        body: SecurityMonitoringIntegrationCredentialsValidateRequest,
    ) -> None:
        """Validate entity context sync credentials.

        Validate a set of credentials against the external entity source before creating a sync configuration.
        Returns a 200 status code if the credentials are valid.

        :param body: The credentials to validate.
        :type body: SecurityMonitoringIntegrationCredentialsValidateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._validate_security_monitoring_integration_credentials_endpoint.call_with_http_info(**kwargs)

    def validate_security_monitoring_rule(
        self,
        body: Union[
            SecurityMonitoringRuleValidatePayload,
            SecurityMonitoringStandardRulePayload,
            SecurityMonitoringSignalRulePayload,
            CloudConfigurationRulePayload,
        ],
    ) -> None:
        """Validate a detection rule.

        Validate a detection rule.

        :type body: SecurityMonitoringRuleValidatePayload
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._validate_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def validate_security_monitoring_suppression(
        self,
        body: SecurityMonitoringSuppressionCreateRequest,
    ) -> None:
        """Validate a suppression rule.

        Validate a suppression rule.

        :type body: SecurityMonitoringSuppressionCreateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._validate_security_monitoring_suppression_endpoint.call_with_http_info(**kwargs)
