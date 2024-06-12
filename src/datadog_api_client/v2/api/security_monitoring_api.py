# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_findings_response import ListFindingsResponse
from datadog_api_client.v2.model.finding_evaluation import FindingEvaluation
from datadog_api_client.v2.model.finding_status import FindingStatus
from datadog_api_client.v2.model.finding import Finding
from datadog_api_client.v2.model.bulk_mute_findings_response import BulkMuteFindingsResponse
from datadog_api_client.v2.model.bulk_mute_findings_request import BulkMuteFindingsRequest
from datadog_api_client.v2.model.get_finding_response import GetFindingResponse
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
from datadog_api_client.v2.model.security_monitoring_rule_test_response import SecurityMonitoringRuleTestResponse
from datadog_api_client.v2.model.security_monitoring_rule_test_request import SecurityMonitoringRuleTestRequest
from datadog_api_client.v2.model.security_monitoring_rule_validate_payload import SecurityMonitoringRuleValidatePayload
from datadog_api_client.v2.model.security_monitoring_standard_rule_payload import SecurityMonitoringStandardRulePayload
from datadog_api_client.v2.model.security_monitoring_signal_rule_payload import SecurityMonitoringSignalRulePayload
from datadog_api_client.v2.model.cloud_configuration_rule_payload import CloudConfigurationRulePayload
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload
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


class SecurityMonitoringApi:
    """
    Create and manage your security rules, signals, filters, and more. See the `Datadog Security page <https://docs.datadoghq.com/security/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

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
    ) -> ListFindingsResponse:
        """List findings.

        Get a list of CSPM findings.

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
