# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
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
from datadog_api_client.v2.model.bulk_mute_findings_response import BulkMuteFindingsResponse
from datadog_api_client.v2.model.bulk_mute_findings_request import BulkMuteFindingsRequest
from datadog_api_client.v2.model.get_finding_response import GetFindingResponse
from datadog_api_client.v2.model.list_vulnerable_assets_response import ListVulnerableAssetsResponse
from datadog_api_client.v2.model.asset_type import AssetType
from datadog_api_client.v2.model.list_assets_sbo_ms_response import ListAssetsSBOMsResponse
from datadog_api_client.v2.model.sbom_component_license_type import SBOMComponentLicenseType
from datadog_api_client.v2.model.get_sbom_response import GetSBOMResponse
from datadog_api_client.v2.model.notification_rule_response import NotificationRuleResponse
from datadog_api_client.v2.model.create_notification_rule_parameters import CreateNotificationRuleParameters
from datadog_api_client.v2.model.patch_notification_rule_parameters import PatchNotificationRuleParameters
from datadog_api_client.v2.model.list_vulnerabilities_response import ListVulnerabilitiesResponse
from datadog_api_client.v2.model.vulnerability_type import VulnerabilityType
from datadog_api_client.v2.model.vulnerability_severity import VulnerabilitySeverity
from datadog_api_client.v2.model.vulnerability_status import VulnerabilityStatus
from datadog_api_client.v2.model.vulnerability_tool import VulnerabilityTool
from datadog_api_client.v2.model.vulnerability_ecosystem import VulnerabilityEcosystem
from datadog_api_client.v2.model.security_filters_response import SecurityFiltersResponse
from datadog_api_client.v2.model.security_filter_response import SecurityFilterResponse
from datadog_api_client.v2.model.security_filter_create_request import SecurityFilterCreateRequest
from datadog_api_client.v2.model.security_filter_update_request import SecurityFilterUpdateRequest
from datadog_api_client.v2.model.security_monitoring_suppressions_response import SecurityMonitoringSuppressionsResponse
from datadog_api_client.v2.model.security_monitoring_suppression_response import SecurityMonitoringSuppressionResponse
from datadog_api_client.v2.model.security_monitoring_suppression_create_request import (
    SecurityMonitoringSuppressionCreateRequest,
)
from datadog_api_client.v2.model.security_monitoring_suppression_update_request import (
    SecurityMonitoringSuppressionUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_list_rules_response import SecurityMonitoringListRulesResponse
from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse
from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_create_payload import (
    SecurityMonitoringStandardRuleCreatePayload,
)
from datadog_api_client.v2.model.security_monitoring_signal_rule_create_payload import (
    SecurityMonitoringSignalRuleCreatePayload,
)
from datadog_api_client.v2.model.cloud_configuration_rule_create_payload import CloudConfigurationRuleCreatePayload
from datadog_api_client.v2.model.security_monitoring_rule_convert_response import SecurityMonitoringRuleConvertResponse
from datadog_api_client.v2.model.security_monitoring_rule_convert_payload import SecurityMonitoringRuleConvertPayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_payload import SecurityMonitoringStandardRulePayload
from datadog_api_client.v2.model.security_monitoring_signal_rule_payload import SecurityMonitoringSignalRulePayload
from datadog_api_client.v2.model.security_monitoring_rule_test_response import SecurityMonitoringRuleTestResponse
from datadog_api_client.v2.model.security_monitoring_rule_test_request import SecurityMonitoringRuleTestRequest
from datadog_api_client.v2.model.security_monitoring_rule_validate_payload import SecurityMonitoringRuleValidatePayload
from datadog_api_client.v2.model.cloud_configuration_rule_payload import CloudConfigurationRulePayload
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload
from datadog_api_client.v2.model.get_rule_version_history_response import GetRuleVersionHistoryResponse
from datadog_api_client.v2.model.security_monitoring_signals_list_response import SecurityMonitoringSignalsListResponse
from datadog_api_client.v2.model.security_monitoring_signals_sort import SecurityMonitoringSignalsSort
from datadog_api_client.v2.model.security_monitoring_signal import SecurityMonitoringSignal
from datadog_api_client.v2.model.security_monitoring_signal_list_request import SecurityMonitoringSignalListRequest
from datadog_api_client.v2.model.security_monitoring_signal_response import SecurityMonitoringSignalResponse
from datadog_api_client.v2.model.security_monitoring_signal_triage_update_response import (
    SecurityMonitoringSignalTriageUpdateResponse,
)
from datadog_api_client.v2.model.security_monitoring_signal_assignee_update_request import (
    SecurityMonitoringSignalAssigneeUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_incidents_update_request import (
    SecurityMonitoringSignalIncidentsUpdateRequest,
)
from datadog_api_client.v2.model.security_monitoring_signal_state_update_request import (
    SecurityMonitoringSignalStateUpdateRequest,
)
from datadog_api_client.v2.model.list_historical_jobs_response import ListHistoricalJobsResponse
from datadog_api_client.v2.model.job_create_response import JobCreateResponse
from datadog_api_client.v2.model.run_historical_job_request import RunHistoricalJobRequest
from datadog_api_client.v2.model.convert_job_results_to_signals_request import ConvertJobResultsToSignalsRequest
from datadog_api_client.v2.model.historical_job_response import HistoricalJobResponse


class SecurityMonitoringApi:
    """
    Create and manage your security rules, signals, filters, and more. See the `Datadog Security page <https://docs.datadoghq.com/security/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

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

        self._create_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._create_vulnerability_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._edit_security_monitoring_signal_assignee_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalTriageUpdateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
            },
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

        self._get_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._get_vulnerability_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "response_type": (dict,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._list_assets_sbo_ms_endpoint = _Endpoint(
            settings={
                "response_type": (ListAssetsSBOMsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "response_type": (SecurityMonitoringSuppressionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/suppressions",
                "operation_id": "list_security_monitoring_suppressions",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                    "attribute": "filter[advisory_id]",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security/assets",
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

        self._mute_findings_endpoint = _Endpoint(
            settings={
                "response_type": (BulkMuteFindingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/posture_management/findings",
                "operation_id": "mute_findings",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (BulkMuteFindingsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._patch_signal_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (NotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        Convert an existing rule from JSON to Terraform for datadog provider
        resource datadog_security_monitoring_rule.

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

        Convert a rule that doesn't (yet) exist from JSON to Terraform for datadog provider
        resource datadog_security_monitoring_rule.

        :type body: SecurityMonitoringRuleConvertPayload
        :rtype: SecurityMonitoringRuleConvertResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._convert_security_monitoring_rule_from_json_to_terraform_endpoint.call_with_http_info(**kwargs)

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
    ) -> GetSBOMResponse:
        """Get SBOM.

        Get a single SBOM related to an asset by its type and name.

        :param asset_type: The type of the asset for the SBOM request.
        :type asset_type: AssetType
        :param filter_asset_name: The name of the asset for the SBOM request.
        :type filter_asset_name: str
        :param filter_repo_digest: The container image ``repo_digest`` for the SBOM request. When the requested asset type is 'Image', this filter is mandatory.
        :type filter_repo_digest: str, optional
        :rtype: GetSBOMResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["asset_type"] = asset_type

        kwargs["filter_asset_name"] = filter_asset_name

        if filter_repo_digest is not unset:
            kwargs["filter_repo_digest"] = filter_repo_digest

        return self._get_sbom_endpoint.call_with_http_info(**kwargs)

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
    ) -> dict:
        """Get the list of signal-based notification rules.

        Returns the list of notification rules for security signals.

        :rtype: dict
        """
        kwargs: Dict[str, Any] = {}
        return self._get_signal_notification_rules_endpoint.call_with_http_info(**kwargs)

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
    ) -> dict:
        """Get the list of vulnerability notification rules.

        Returns the list of notification rules for security vulnerabilities.

        :rtype: dict
        """
        kwargs: Dict[str, Any] = {}
        return self._get_vulnerability_notification_rules_endpoint.call_with_http_info(**kwargs)

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
        :param filter_asset_type: The type of the assets for the SBOM request.
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

    def list_security_filters(
        self,
    ) -> SecurityFiltersResponse:
        """Get all security filters.

        Get the list of configured security filters with their definitions.

        :rtype: SecurityFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_security_filters_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> SecurityMonitoringListRulesResponse:
        """List rules.

        List rules.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: SecurityMonitoringListRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

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
    ) -> SecurityMonitoringSuppressionsResponse:
        """Get all suppression rules.

        Get the list of all suppression rules.

        :rtype: SecurityMonitoringSuppressionsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_security_monitoring_suppressions_endpoint.call_with_http_info(**kwargs)

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
        """List vulnerabilities.

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

        **Subsequent requests**

        Any request containing valid ``page[token]`` and ``page[number]`` parameters will be considered a subsequent request.

        If the ``token`` is invalid, a ``404`` response will be returned.

        If the page ``number`` is invalid, a ``400`` response will be returned.

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
        :param filter_asset_name: Filter by asset name.
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
        :param filter_name: Filter by name.
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

    def mute_findings(
        self,
        body: BulkMuteFindingsRequest,
    ) -> BulkMuteFindingsResponse:
        """Mute or unmute a batch of findings.

        Mute or unmute findings.

        :param body: **Attributes**

            All findings are updated with the same attributes. The request body must include at least two attributes: ``muted`` and ``reason``.
            The allowed reasons depend on whether the finding is being muted or unmuted:

            * To mute a finding: ``PENDING_FIX`` , ``FALSE_POSITIVE`` , ``ACCEPTED_RISK`` , ``OTHER``.
            * To unmute a finding : ``NO_PENDING_FIX`` , ``HUMAN_ERROR`` , ``NO_LONGER_ACCEPTED_RISK`` , ``OTHER``.

            **Meta**

            The request body must include a list of the finding IDs to be updated.
        :type body: BulkMuteFindingsRequest
        :rtype: BulkMuteFindingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._mute_findings_endpoint.call_with_http_info(**kwargs)

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
