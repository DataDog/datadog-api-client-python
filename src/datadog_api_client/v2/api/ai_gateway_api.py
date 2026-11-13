# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.ai_gateway_budget_list_response import AiGatewayBudgetListResponse
from datadog_api_client.v2.model.ai_gateway_budget_response import AiGatewayBudgetResponse
from datadog_api_client.v2.model.ai_gateway_budget_create_request import AiGatewayBudgetCreateRequest
from datadog_api_client.v2.model.ai_gateway_budget_update_request import AiGatewayBudgetUpdateRequest
from datadog_api_client.v2.model.ai_gateway_budget_period_response import AiGatewayBudgetPeriodResponse
from datadog_api_client.v2.model.ai_gateway_budget_instance_list_response import AiGatewayBudgetInstanceListResponse
from datadog_api_client.v2.model.ai_gateway_budget_instance_sort import AiGatewayBudgetInstanceSort
from datadog_api_client.v2.model.ai_gateway_budget_instance_response import AiGatewayBudgetInstanceResponse
from datadog_api_client.v2.model.ai_gateway_budget_instance_capacity_override_request import (
    AiGatewayBudgetInstanceCapacityOverrideRequest,
)
from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_list_response import (
    AiGatewayBudgetInstanceDimensionListResponse,
)
from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_request import AiGatewayBudgetInstanceResetRequest
from datadog_api_client.v2.model.ai_gateway_budget_instances_summary_response import (
    AiGatewayBudgetInstancesSummaryResponse,
)
from datadog_api_client.v2.model.ai_gateway_capture_configuration_response import AiGatewayCaptureConfigurationResponse
from datadog_api_client.v2.model.ai_gateway_capture_override_response import AiGatewayCaptureOverrideResponse
from datadog_api_client.v2.model.ai_gateway_capture_create_request import AiGatewayCaptureCreateRequest
from datadog_api_client.v2.model.ai_gateway_capture_delete_request import AiGatewayCaptureDeleteRequest
from datadog_api_client.v2.model.ai_gateway_capture_update_request import AiGatewayCaptureUpdateRequest
from datadog_api_client.v2.model.ai_gateway_governance_response import AiGatewayGovernanceResponse
from datadog_api_client.v2.model.ai_gateway_governance_replace_request import AiGatewayGovernanceReplaceRequest
from datadog_api_client.v2.model.ai_gateway_model_group_list_response import AiGatewayModelGroupListResponse
from datadog_api_client.v2.model.ai_gateway_model_group_response import AiGatewayModelGroupResponse
from datadog_api_client.v2.model.ai_gateway_model_group_create_request import AiGatewayModelGroupCreateRequest
from datadog_api_client.v2.model.ai_gateway_model_group_update_request import AiGatewayModelGroupUpdateRequest
from datadog_api_client.v2.model.ai_gateway_models_by_canonical_list_response import (
    AiGatewayModelsByCanonicalListResponse,
)
from datadog_api_client.v2.model.ai_gateway_policy_list_response import AiGatewayPolicyListResponse
from datadog_api_client.v2.model.ai_gateway_policy_response import AiGatewayPolicyResponse
from datadog_api_client.v2.model.ai_gateway_policy_request import AiGatewayPolicyRequest
from datadog_api_client.v2.model.ai_gateway_discovered_model_list_response import AiGatewayDiscoveredModelListResponse
from datadog_api_client.v2.model.ai_gateway_provider_list_response import AiGatewayProviderListResponse
from datadog_api_client.v2.model.ai_gateway_provider_response import AiGatewayProviderResponse
from datadog_api_client.v2.model.ai_gateway_provider_create_request import AiGatewayProviderCreateRequest
from datadog_api_client.v2.model.ai_gateway_provider_update_request import AiGatewayProviderUpdateRequest
from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_list_response import (
    AiGatewayModelCatalogEntryListResponse,
)
from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_response import AiGatewayModelCatalogEntryResponse
from datadog_api_client.v2.model.ai_gateway_model_create_request import AiGatewayModelCreateRequest
from datadog_api_client.v2.model.ai_gateway_models_bulk_create_request import AiGatewayModelsBulkCreateRequest
from datadog_api_client.v2.model.ai_gateway_model_update_request import AiGatewayModelUpdateRequest
from datadog_api_client.v2.model.ai_gateway_model_pricing_response import AiGatewayModelPricingResponse
from datadog_api_client.v2.model.ai_gateway_model_pricing_request import AiGatewayModelPricingRequest
from datadog_api_client.v2.model.ai_gateway_rate_limit_list_response import AiGatewayRateLimitListResponse
from datadog_api_client.v2.model.ai_gateway_rate_limit_response import AiGatewayRateLimitResponse
from datadog_api_client.v2.model.ai_gateway_rate_limit_create_request import AiGatewayRateLimitCreateRequest
from datadog_api_client.v2.model.ai_gateway_rate_limit_usage_list_response import AiGatewayRateLimitUsageListResponse
from datadog_api_client.v2.model.ai_gateway_rate_limit_update_request import AiGatewayRateLimitUpdateRequest
from datadog_api_client.v2.model.ai_gateway_rate_limit_instance_list_response import (
    AiGatewayRateLimitInstanceListResponse,
)
from datadog_api_client.v2.model.ai_gateway_rate_limit_instance_sort import AiGatewayRateLimitInstanceSort
from datadog_api_client.v2.model.ai_gateway_rate_limit_instances_summary_response import (
    AiGatewayRateLimitInstancesSummaryResponse,
)
from datadog_api_client.v2.model.ai_gateway_routing_rule_list_response import AiGatewayRoutingRuleListResponse
from datadog_api_client.v2.model.ai_gateway_routing_rule_response import AiGatewayRoutingRuleResponse
from datadog_api_client.v2.model.ai_gateway_routing_rule_create_request import AiGatewayRoutingRuleCreateRequest
from datadog_api_client.v2.model.ai_gateway_routing_rule_replace_request import AiGatewayRoutingRuleReplaceRequest


class AIGatewayApi:
    """
    AI Gateway routes your applications' LLM requests to the model providers you connect, and
    applies your organization's routing, access, spending, rate limit, and data capture rules.

    These endpoints allow you to configure:

    * Providers: the model providers your organization connects, and the models and pricing each offers.
    * Routing rules: the named routes your applications call, and the models that serve each one.
    * Access: inbound routing policies and model groups that decide who can use which models.
    * Budgets and rate limits: spending caps and request limits, and their current usage.
    * Data capture and governance: what request data is recorded, and organization-wide controls.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._bulk_create_ai_gateway_models_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelCatalogEntryListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models/bulk",
                "operation_id": "bulk_create_ai_gateway_models",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayModelsBulkCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_budget_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets",
                "operation_id": "create_ai_gateway_budget",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayBudgetCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_data_capture_override_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayCaptureOverrideResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/data-capture/overrides",
                "operation_id": "create_ai_gateway_data_capture_override",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayCaptureCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_model_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelCatalogEntryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models",
                "operation_id": "create_ai_gateway_model",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayModelCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_model_group_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/model-groups",
                "operation_id": "create_ai_gateway_model_group",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayModelGroupCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_provider_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayProviderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers",
                "operation_id": "create_ai_gateway_provider",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayProviderCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_rate_limit_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits",
                "operation_id": "create_ai_gateway_rate_limit",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayRateLimitCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ai_gateway_routing_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRoutingRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/routing-rules",
                "operation_id": "create_ai_gateway_routing_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayRoutingRuleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_ai_gateway_budget_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}",
                "operation_id": "delete_ai_gateway_budget",
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
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_ai_gateway_data_capture_override_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/data-capture/overrides/{id}",
                "operation_id": "delete_ai_gateway_data_capture_override",
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
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayCaptureDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_ai_gateway_model_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models/{canonical}",
                "operation_id": "delete_ai_gateway_model",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "canonical": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "canonical",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_ai_gateway_model_group_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/model-groups/{id}",
                "operation_id": "delete_ai_gateway_model_group",
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

        self._delete_ai_gateway_model_pricing_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models/{canonical}/pricing",
                "operation_id": "delete_ai_gateway_model_pricing",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "canonical": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "canonical",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_ai_gateway_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/policies/{inbound}",
                "operation_id": "delete_ai_gateway_policy",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "inbound": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "inbound",
                    "location": "path",
                },
                "user_id": {
                    "openapi_types": (UUID,),
                    "attribute": "user_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_ai_gateway_provider_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{id}",
                "operation_id": "delete_ai_gateway_provider",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "id",
                    "location": "path",
                },
                "force": {
                    "openapi_types": (bool,),
                    "attribute": "force",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_ai_gateway_rate_limit_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits/{id}",
                "operation_id": "delete_ai_gateway_rate_limit",
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
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_ai_gateway_routing_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/routing-rules",
                "operation_id": "delete_ai_gateway_routing_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "slug": {
                    "required": True,
                    "validation": {
                        "max_length": 128,
                    },
                    "openapi_types": (str,),
                    "attribute": "slug",
                    "location": "query",
                },
                "force": {
                    "openapi_types": (bool,),
                    "attribute": "force",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_budget_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}",
                "operation_id": "get_ai_gateway_budget",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_budget_current_period_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetPeriodResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}/current-period",
                "operation_id": "get_ai_gateway_budget_current_period",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_budget_instances_summary_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetInstancesSummaryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}/instances/summary",
                "operation_id": "get_ai_gateway_budget_instances_summary",
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
                "window": {
                    "openapi_types": (datetime,),
                    "attribute": "window",
                    "location": "query",
                },
                "split_dim": {
                    "openapi_types": ([str],),
                    "attribute": "split_dim",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_data_capture_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayCaptureConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/data-capture/configuration",
                "operation_id": "get_ai_gateway_data_capture_configuration",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_governance_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayGovernanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance",
                "operation_id": "get_ai_gateway_governance",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_model_group_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/model-groups/{id}",
                "operation_id": "get_ai_gateway_model_group",
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

        self._get_ai_gateway_model_pricing_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelPricingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models/{canonical}/pricing",
                "operation_id": "get_ai_gateway_model_pricing",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "canonical": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "canonical",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_policy_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/policies/{inbound}",
                "operation_id": "get_ai_gateway_policy",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "inbound": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "inbound",
                    "location": "path",
                },
                "user_id": {
                    "openapi_types": (UUID,),
                    "attribute": "user_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_provider_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayProviderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{id}",
                "operation_id": "get_ai_gateway_provider",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_rate_limit_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits/{id}",
                "operation_id": "get_ai_gateway_rate_limit",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_rate_limit_instances_summary_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitInstancesSummaryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits/{id}/instances/summary",
                "operation_id": "get_ai_gateway_rate_limit_instances_summary",
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
                "split_dim": {
                    "openapi_types": ([str],),
                    "attribute": "split_dim",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_rate_limit_usage_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitUsageListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits/usage",
                "operation_id": "get_ai_gateway_rate_limit_usage",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_ai_gateway_routing_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRoutingRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/routing-rules/get",
                "operation_id": "get_ai_gateway_routing_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "slug": {
                    "required": True,
                    "validation": {
                        "max_length": 128,
                    },
                    "openapi_types": (str,),
                    "attribute": "slug",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_budget_instance_dimensions_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetInstanceDimensionListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}/instances/dimensions",
                "operation_id": "list_ai_gateway_budget_instance_dimensions",
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
                "window": {
                    "openapi_types": (datetime,),
                    "attribute": "window",
                    "location": "query",
                },
                "split_dim": {
                    "openapi_types": ([str],),
                    "attribute": "split_dim",
                    "location": "query",
                    "collection_format": "multi",
                },
                "dim": {
                    "openapi_types": ([str],),
                    "attribute": "dim",
                    "location": "query",
                    "collection_format": "multi",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "value": {
                    "openapi_types": ([str],),
                    "attribute": "value",
                    "location": "query",
                    "collection_format": "multi",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 500,
                        "inclusive_minimum": 1,
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

        self._list_ai_gateway_budget_instances_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetInstanceListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}/instances",
                "operation_id": "list_ai_gateway_budget_instances",
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
                "window": {
                    "openapi_types": (datetime,),
                    "attribute": "window",
                    "location": "query",
                },
                "split_dim": {
                    "openapi_types": ([str],),
                    "attribute": "split_dim",
                    "location": "query",
                    "collection_format": "multi",
                },
                "sort": {
                    "openapi_types": (AiGatewayBudgetInstanceSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 500,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_budgets_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets",
                "operation_id": "list_ai_gateway_budgets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_model_groups_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelGroupListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/model-groups",
                "operation_id": "list_ai_gateway_model_groups",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_models_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelCatalogEntryListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models",
                "operation_id": "list_ai_gateway_models",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_models_by_canonical_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelsByCanonicalListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/models",
                "operation_id": "list_ai_gateway_models_by_canonical",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_policies_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayPolicyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/policies",
                "operation_id": "list_ai_gateway_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "user_id": {
                    "openapi_types": (UUID,),
                    "attribute": "user_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_provider_models_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayDiscoveredModelListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/provider-models",
                "operation_id": "list_ai_gateway_provider_models",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_type",
                    "location": "query",
                },
                "integration_account_id": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "integration_account_id",
                    "location": "query",
                },
                "project_id": {
                    "openapi_types": (str,),
                    "attribute": "project_id",
                    "location": "query",
                },
                "location": {
                    "openapi_types": (str,),
                    "attribute": "location",
                    "location": "query",
                },
                "bedrock_region": {
                    "openapi_types": (str,),
                    "attribute": "bedrock_region",
                    "location": "query",
                },
                "foundry_resource_id": {
                    "openapi_types": (str,),
                    "attribute": "foundry_resource_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_providers_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayProviderListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers",
                "operation_id": "list_ai_gateway_providers",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_rate_limit_instances_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitInstanceListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits/{id}/instances",
                "operation_id": "list_ai_gateway_rate_limit_instances",
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
                "split_dim": {
                    "openapi_types": ([str],),
                    "attribute": "split_dim",
                    "location": "query",
                    "collection_format": "multi",
                },
                "sort": {
                    "openapi_types": (AiGatewayRateLimitInstanceSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 500,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_rate_limits_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits",
                "operation_id": "list_ai_gateway_rate_limits",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_gateway_routing_rules_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRoutingRuleListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/routing-rules",
                "operation_id": "list_ai_gateway_routing_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._override_ai_gateway_budget_instance_capacity_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetInstanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}/instances/capacity",
                "operation_id": "override_ai_gateway_budget_instance_capacity",
                "http_method": "POST",
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
                    "openapi_types": (AiGatewayBudgetInstanceCapacityOverrideRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._reset_ai_gateway_budget_instance_spend_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetInstanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}/instances/reset",
                "operation_id": "reset_ai_gateway_budget_instance_spend",
                "http_method": "POST",
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
                    "openapi_types": (AiGatewayBudgetInstanceResetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_budget_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayBudgetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/budgets/{id}",
                "operation_id": "update_ai_gateway_budget",
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
                    "openapi_types": (AiGatewayBudgetUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_data_capture_override_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayCaptureOverrideResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/data-capture/overrides/{id}",
                "operation_id": "update_ai_gateway_data_capture_override",
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
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayCaptureUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_governance_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayGovernanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance",
                "operation_id": "update_ai_gateway_governance",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayGovernanceReplaceRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_model_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelCatalogEntryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models/{canonical}",
                "operation_id": "update_ai_gateway_model",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "canonical": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "canonical",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayModelUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_model_group_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/model-groups/{id}",
                "operation_id": "update_ai_gateway_model_group",
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
                    "openapi_types": (AiGatewayModelGroupUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_model_pricing_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayModelPricingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{provider_id}/models/{canonical}/pricing",
                "operation_id": "update_ai_gateway_model_pricing",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "provider_id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "provider_id",
                    "location": "path",
                },
                "canonical": {
                    "required": True,
                    "validation": {
                        "max_length": 256,
                    },
                    "openapi_types": (str,),
                    "attribute": "canonical",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayModelPricingRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_provider_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayProviderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/providers/{id}",
                "operation_id": "update_ai_gateway_provider",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayProviderUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_rate_limit_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRateLimitResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rate-limits/{id}",
                "operation_id": "update_ai_gateway_rate_limit",
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
                    "openapi_types": (AiGatewayRateLimitUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_ai_gateway_routing_rule_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayRoutingRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/routing-rules",
                "operation_id": "update_ai_gateway_routing_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "slug": {
                    "required": True,
                    "validation": {
                        "max_length": 128,
                    },
                    "openapi_types": (str,),
                    "attribute": "slug",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayRoutingRuleReplaceRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_ai_gateway_policy_endpoint = _Endpoint(
            settings={
                "response_type": (AiGatewayPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/policies",
                "operation_id": "upsert_ai_gateway_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "user_id": {
                    "openapi_types": (UUID,),
                    "attribute": "user_id",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AiGatewayPolicyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def bulk_create_ai_gateway_models(
        self,
        provider_id: int,
        body: AiGatewayModelsBulkCreateRequest,
    ) -> AiGatewayModelCatalogEntryListResponse:
        """Add multiple models to an AI Gateway provider.

        Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.
        Add multiple manually managed model catalog entries to a provider in a single request. Manually managed
        entries are not modified by automatic catalog synchronization.

        :param provider_id: Provider ID.
        :type provider_id: int
        :type body: AiGatewayModelsBulkCreateRequest
        :rtype: AiGatewayModelCatalogEntryListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["body"] = body

        return self._bulk_create_ai_gateway_models_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_budget(
        self,
        body: AiGatewayBudgetCreateRequest,
    ) -> AiGatewayBudgetResponse:
        """Create an AI Gateway budget.

        Create a spend budget. Scope tags may include provider, model, and custom dimensions.
        Reserved metadata keys are rejected.

        :type body: AiGatewayBudgetCreateRequest
        :rtype: AiGatewayBudgetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_gateway_budget_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_data_capture_override(
        self,
        body: AiGatewayCaptureCreateRequest,
    ) -> AiGatewayCaptureOverrideResponse:
        """Create an AI Gateway data capture override.

        Create a scoped override with a client-generated UUID and the current ``configuration_revision``. If the override can enable full capture for more traffic, set ``confirm_full_capture`` to ``true``. Returns HTTP 409 when ``configuration_revision`` is stale, the UUID already exists, or the organization has 100 overrides. Missing ``configuration_revision`` or required full-capture confirmation returns HTTP 400. Retrying an accepted create with the same UUID returns HTTP 409. To undo a create, read the current configuration revision and delete the override using its returned override revision.

        :type body: AiGatewayCaptureCreateRequest
        :rtype: AiGatewayCaptureOverrideResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_gateway_data_capture_override_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_model(
        self,
        provider_id: int,
        body: AiGatewayModelCreateRequest,
    ) -> AiGatewayModelCatalogEntryResponse:
        """Add a model to an AI Gateway provider.

        Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.
        Add a manually managed model catalog entry to a provider. Manually managed entries are not modified by
        automatic catalog synchronization.

        :param provider_id: Provider ID.
        :type provider_id: int
        :type body: AiGatewayModelCreateRequest
        :rtype: AiGatewayModelCatalogEntryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["body"] = body

        return self._create_ai_gateway_model_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_model_group(
        self,
        body: AiGatewayModelGroupCreateRequest,
    ) -> AiGatewayModelGroupResponse:
        """Create an AI Gateway model group.

        Create an AI Gateway model group from a name and any combination of model catalog entries and routing rules, with optional fast-mode and reasoning limits and initial access bindings.

        :type body: AiGatewayModelGroupCreateRequest
        :rtype: AiGatewayModelGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_gateway_model_group_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_provider(
        self,
        body: AiGatewayProviderCreateRequest,
    ) -> AiGatewayProviderResponse:
        """Create an AI Gateway provider.

        Creating a provider requires ``ai_gateway_config_write``. No provider View check applies before creation.
        Create a provider and its initial model catalog. All discovered models are enabled; optional models are
        added as manually managed entries. The slug is the immutable routing identifier.
        Provider and initial catalog rows are saved in one transaction. Initial sharing is unavailable:
        supplying initial_bindings returns 503 with stage initial_permissions and outcome not_saved.
        A failed database commit can return 503 with stage database_commit and outcome unknown; check the
        provider list before retrying. Creation without initial_bindings keeps normal unrestricted defaults.

        :type body: AiGatewayProviderCreateRequest
        :rtype: AiGatewayProviderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_gateway_provider_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_rate_limit(
        self,
        body: AiGatewayRateLimitCreateRequest,
    ) -> AiGatewayRateLimitResponse:
        """Create an AI Gateway rate limit.

        Create a rate limit. All requests matching its scope share one allowance, unless a selector makes it a template, which gives each matched user, Team, or value its own allowance. Every matching rate limit applies. Returns 409 when another active rate limit has the same user, Team, tags, and selector, or when the organization already has the maximum number of rate limits.

        :type body: AiGatewayRateLimitCreateRequest
        :rtype: AiGatewayRateLimitResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_gateway_rate_limit_endpoint.call_with_http_info(**kwargs)

    def create_ai_gateway_routing_rule(
        self,
        body: AiGatewayRoutingRuleCreateRequest,
    ) -> AiGatewayRoutingRuleResponse:
        """Create an AI Gateway routing rule.

        Create an organization-owned route with ``ai_gateway_config_write``. New provider/model and route references require View. New routes use standard unrestricted defaults. To restrict configuration access, create the route and then apply a restriction policy using its numeric route_id. Sharing follows standard restriction-policy propagation and does not grant or revoke policy-authorized inference. Data capture overrides are managed independently. Each tier has an ordering, which defaults to configured. A weighted_affinity tier distributes first-choice assignments by relative target weights (1 to 10000, default 1) and accepts only distinct model targets with an explicit provider. Weights need not total 100. Configured tiers must omit weights or set them to null.

        :type body: AiGatewayRoutingRuleCreateRequest
        :rtype: AiGatewayRoutingRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_gateway_routing_rule_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_budget(
        self,
        id: UUID,
    ) -> None:
        """Archive an AI Gateway budget.

        Archive a spend budget by ID while retaining its accounting history.

        :param id: Budget UUID.
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_ai_gateway_budget_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_data_capture_override(
        self,
        id: UUID,
        body: AiGatewayCaptureDeleteRequest,
    ) -> None:
        """Delete an AI Gateway data capture override.

        Delete an override using its ``revision`` and the current ``configuration_revision``. If deleting the override can enable full capture for affected traffic, set ``confirm_full_capture`` to ``true``. Returns HTTP 409 when ``configuration_revision`` or the override ``revision`` is stale, including a concurrent change during deletion. Missing revisions or required full-capture confirmation returns HTTP 400.

        :param id: Data capture override ID.
        :type id: UUID
        :type body: AiGatewayCaptureDeleteRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._delete_ai_gateway_data_capture_override_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_model(
        self,
        provider_id: int,
        canonical: str,
    ) -> None:
        """Delete a model from an AI Gateway provider.

        Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.
        Delete a manually managed model catalog entry by its canonical model ID. Discovered entries are read-only.

        :param provider_id: Provider ID.
        :type provider_id: int
        :param canonical: Canonical model identifier.
        :type canonical: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["canonical"] = canonical

        return self._delete_ai_gateway_model_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_model_group(
        self,
        id: str,
    ) -> None:
        """Delete an AI Gateway model group.

        Delete a named model group. The organization-wide policy cannot be deleted. Requires configuration write permission and edit access to the group.

        :param id: Model group ID, or "default" for the explicit organization-wide access policy.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_ai_gateway_model_group_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_model_pricing(
        self,
        provider_id: int,
        canonical: str,
    ) -> None:
        """Delete a model pricing override.

        Clear a custom provider model's pricing override. Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.

        :param provider_id: Provider ID.
        :type provider_id: int
        :param canonical: Canonical model identifier.
        :type canonical: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["canonical"] = canonical

        return self._delete_ai_gateway_model_pricing_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_policy(
        self,
        inbound: str,
        *,
        user_id: Union[UUID, UnsetType] = unset,
    ) -> None:
        """Delete an AI Gateway routing policy.

        Delete the routing policy document for a specific inbound pattern.

        :param inbound: Inbound routing pattern.
        :type inbound: str
        :param user_id: Filter or scope policies to a specific user. Omit for organization-wide policies.
        :type user_id: UUID, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["inbound"] = inbound

        if user_id is not unset:
            kwargs["user_id"] = user_id

        return self._delete_ai_gateway_policy_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_provider(
        self,
        id: int,
        *,
        force: Union[bool, UnsetType] = unset,
    ) -> None:
        """Delete an AI Gateway provider.

        Requires ``ai_gateway_config_write`` and provider View/Edit. Models and pricing inherit provider access. Every affected route and policy membership requires the corresponding Edit permission; force=true never bypasses authorization. Providers used by routing rules return provider_in_use with HTTP 409. Each JSON:API error item's ``meta`` contains blocked, restricted_dependencies, policies, rules_to_delete, and rules_to_update. Visible policy entries contain id, name, and editable; visible route entries contain id, slug, and editable. Hidden dependencies are omitted from every collection and reported only by restricted_dependencies. A blocked response changes no configuration; an authorized editor must first remove the blocking references. Retry with force=true to confirm an authorized cascade that removes provider targets and deletes rules left without targets. Surviving tiers keep their ordering and weights. A deletion that would rewrite a surviving tier with an unknown ordering_issue fails with HTTP 409 and code routing_rule_unknown_ordering until that rule is replaced or deleted.

        :param id: Provider ID.
        :type id: int
        :param force: Apply the routing rule changes returned by provider_in_use. Defaults to false.
        :type force: bool, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if force is not unset:
            kwargs["force"] = force

        return self._delete_ai_gateway_provider_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_rate_limit(
        self,
        id: UUID,
    ) -> None:
        """Archive an AI Gateway rate limit.

        Archive a rate limit by ID. An archived rate limit no longer appears in lists or lookups, and its alert monitor is deleted.

        :param id: Rate limit UUID.
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_ai_gateway_rate_limit_endpoint.call_with_http_info(**kwargs)

    def delete_ai_gateway_routing_rule(
        self,
        slug: str,
        *,
        force: Union[bool, UnsetType] = unset,
    ) -> None:
        """Delete an AI Gateway routing rule.

        Delete a route with ``ai_gateway_config_write`` and route View/Edit. Every affected route and policy membership requires the corresponding Edit permission. The force=true parameter confirms impact and never bypasses authorization. A denied or unavailable check changes no configuration. Visible dependencies include editable; hidden dependencies are omitted and reported only by restricted_dependencies. A blocked response means an authorized editor must first remove blocking references. Each JSON:API error item's ``meta`` contains blocked, restricted_dependencies, policies, rules_to_delete, and rules_to_update. Visible policy entries contain id, name, and editable. Route deletion entries contain rule, reason, and editable; update entries contain rule, removed_tiers, and editable. Each rule contains route_id, slug, tiers, created_at, and updated_at with hidden nested selections redacted. The removed_tiers array identifies original tier numbers removed entirely by the cascade. Already-authorized in-flight operations may finish. Referenced rules require force=true. Surviving tiers keep their ordering and weights. A deletion that would rewrite a surviving tier with an unknown ordering_issue fails with HTTP 409 and code routing_rule_unknown_ordering until that rule is replaced or deleted. Restriction cleanup occurs only after confirmed deletion. Cleanup failure returns 500 with configuration_deleted=true and permissions_cleanup_failed=true; refresh instead of assuming the route still exists.

        :param slug: Organization-unique routing rule slug.
        :type slug: str
        :param force: Delete referencing tiers and recursively delete parent rules left without tiers.
        :type force: bool, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["slug"] = slug

        if force is not unset:
            kwargs["force"] = force

        return self._delete_ai_gateway_routing_rule_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_budget(
        self,
        id: UUID,
    ) -> AiGatewayBudgetResponse:
        """Get an AI Gateway budget.

        Get a spend budget by ID, including its capacity, scope, reset window, warning threshold, and enforcement mode.

        :param id: Budget UUID.
        :type id: UUID
        :rtype: AiGatewayBudgetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ai_gateway_budget_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_budget_current_period(
        self,
        id: UUID,
    ) -> AiGatewayBudgetPeriodResponse:
        """Get an AI Gateway budget's current period.

        Get the active accounting window, enforced capacity, and current spend.

        :param id: Budget UUID.
        :type id: UUID
        :rtype: AiGatewayBudgetPeriodResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ai_gateway_budget_current_period_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_budget_instances_summary(
        self,
        id: UUID,
        *,
        window: Union[datetime, UnsetType] = unset,
        split_dim: Union[List[str], UnsetType] = unset,
    ) -> AiGatewayBudgetInstancesSummaryResponse:
        """Get an AI Gateway budget instance summary.

        Aggregate counters for an accounting window, including total spend and the numbers of instances at or above the warning threshold and capacity. Use split_dim to aggregate only counters that match every given dimension value.

        :param id: Budget UUID.
        :type id: UUID
        :param window: RFC3339 timestamp inside the desired accounting window. Omit to use the current window.
        :type window: datetime, optional
        :param split_dim: Keep only instance counters whose split dimension equals a value, written as ``<dim>=<value>`` , such as ``split_dim=user_id=<uuid>&split_dim=tag:env=prod``. Dimensions use the ``split_dims`` names ``user_id`` , ``team_id`` , ``model`` , ``provider`` , and ``tag:<key>``. Repeat the parameter to filter on several dimensions; a counter must match all of them. Each dimension may appear once and must be a per-value dimension of the budget.
        :type split_dim: [str], optional
        :rtype: AiGatewayBudgetInstancesSummaryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if window is not unset:
            kwargs["window"] = window

        if split_dim is not unset:
            kwargs["split_dim"] = split_dim

        return self._get_ai_gateway_budget_instances_summary_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_data_capture_configuration(
        self,
    ) -> AiGatewayCaptureConfigurationResponse:
        """Get the AI Gateway data capture configuration.

        Get the organization default mode, scoped capture overrides, and configuration revision.

        :rtype: AiGatewayCaptureConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_ai_gateway_data_capture_configuration_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_governance(
        self,
    ) -> AiGatewayGovernanceResponse:
        """Get AI Gateway governance controls.

        Get the organization-wide AI Gateway governance settings, which are the default data capture mode and whether requests must reach providers covered by a zero data retention agreement.

        :rtype: AiGatewayGovernanceResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_ai_gateway_governance_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_model_group(
        self,
        id: str,
    ) -> AiGatewayModelGroupResponse:
        """Get an AI Gateway model group.

        Get a named policy or the explicit organization-wide policy by id "default". Requires configuration read permission; named policies also require view access. Provider selections cover current and future models and are returned separately from individual model selections.

        :param id: Model group ID, or "default" for the explicit organization-wide access policy.
        :type id: str
        :rtype: AiGatewayModelGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ai_gateway_model_group_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_model_pricing(
        self,
        provider_id: int,
        canonical: str,
    ) -> AiGatewayModelPricingResponse:
        """Get a model pricing override.

        Get a custom provider model's pricing override and effective pricing source. Requires ``ai_gateway_config_read`` and provider View. Catalog and pricing metadata inherit provider access. Lists omit hidden entries; direct reads of hidden resources return 404.

        :param provider_id: Provider ID.
        :type provider_id: int
        :param canonical: Canonical model identifier.
        :type canonical: str
        :rtype: AiGatewayModelPricingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["canonical"] = canonical

        return self._get_ai_gateway_model_pricing_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_policy(
        self,
        inbound: str,
        *,
        user_id: Union[UUID, UnsetType] = unset,
    ) -> AiGatewayPolicyResponse:
        """Get an AI Gateway routing policy.

        Get the routing policy document for a specific inbound pattern.

        :param inbound: Inbound routing pattern.
        :type inbound: str
        :param user_id: Filter or scope policies to a specific user. Omit for organization-wide policies.
        :type user_id: UUID, optional
        :rtype: AiGatewayPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["inbound"] = inbound

        if user_id is not unset:
            kwargs["user_id"] = user_id

        return self._get_ai_gateway_policy_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_provider(
        self,
        id: int,
    ) -> AiGatewayProviderResponse:
        """Get an AI Gateway provider.

        Get a provider by ID, including its routing slug, integration account, and cost multiplier. Credentials stay in the integration account and are never returned. Requires ``ai_gateway_config_read`` and provider View. Catalog and pricing metadata inherit provider access. Lists omit hidden entries; direct reads of hidden resources return 404.

        :param id: Provider ID.
        :type id: int
        :rtype: AiGatewayProviderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ai_gateway_provider_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_rate_limit(
        self,
        id: UUID,
    ) -> AiGatewayRateLimitResponse:
        """Get an AI Gateway rate limit.

        Get a rate limit by ID, including its scope, per-minute request and token limits, and whether it is enabled.

        :param id: Rate limit UUID.
        :type id: UUID
        :rtype: AiGatewayRateLimitResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ai_gateway_rate_limit_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_rate_limit_instances_summary(
        self,
        id: UUID,
        *,
        split_dim: Union[List[str], UnsetType] = unset,
    ) -> AiGatewayRateLimitInstancesSummaryResponse:
        """Get an AI Gateway rate limit counter summary.

        Aggregate a template rate limit's counters, including how many there are, how many are near or at their limit, and the fullest counter's utilization. Use split_dim to aggregate only counters that match every given dimension value. When the caller can't see the template's selector, every count is zero and scope_restricted is true. Summaries are cached for up to 15 seconds. Returns 503 when counter usage can't be read.

        :param id: Rate limit UUID.
        :type id: UUID
        :param split_dim: Keep only counters whose split dimension equals a value, written as ``<dim>=<value>`` , such as ``split_dim=user_id=<uuid>&split_dim=model=gpt-4o``. Dimensions use the ``split_dims`` names ``user_id`` , ``team_id`` , ``model`` , ``provider`` , and ``tag:<key>``. Repeat the parameter to filter on several dimensions; a counter must match all of them. Each dimension may appear once and must be a per-value dimension of the rate limit.
        :type split_dim: [str], optional
        :rtype: AiGatewayRateLimitInstancesSummaryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if split_dim is not unset:
            kwargs["split_dim"] = split_dim

        return self._get_ai_gateway_rate_limit_instances_summary_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_rate_limit_usage(
        self,
    ) -> AiGatewayRateLimitUsageListResponse:
        """Get AI Gateway rate limit usage.

        Get live usage for the organization's rate limits. Returns requests and tokens counted in the rolling one-minute window and requests limited in the last 15 minutes for each enabled rate limit, plus ``untracked`` (traffic no enforced rate limit covers) and ``total`` (all gateway traffic).

        :rtype: AiGatewayRateLimitUsageListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_ai_gateway_rate_limit_usage_endpoint.call_with_http_info(**kwargs)

    def get_ai_gateway_routing_rule(
        self,
        slug: str,
    ) -> AiGatewayRoutingRuleResponse:
        """Get an AI Gateway routing rule.

        Get a routing rule by slug with ``ai_gateway_config_read`` and route View. Hidden and missing routes both return 404. Hidden target identities are omitted; parent-local target IDs remain available for retention.

        :param slug: Organization-unique routing rule slug.
        :type slug: str
        :rtype: AiGatewayRoutingRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["slug"] = slug

        return self._get_ai_gateway_routing_rule_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_budget_instance_dimensions(
        self,
        id: UUID,
        *,
        window: Union[datetime, UnsetType] = unset,
        split_dim: Union[List[str], UnsetType] = unset,
        dim: Union[List[str], UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        value: Union[List[str], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> AiGatewayBudgetInstanceDimensionListResponse:
        """List AI Gateway budget instance dimension values.

        Search the values that a template budget's split dimensions take across its instance counters in an accounting window. Each dimension returns its top values by spend, with counter counts. Use query or value to narrow results and limit to cap them. The truncated field reports whether more values matched. Each dimension's values are counted under the other dimensions' split_dim filters, so a dimension's own filter does not hide its alternatives. Legacy fixed-scope budgets return an empty list.

        :param id: Budget UUID.
        :type id: UUID
        :param window: RFC3339 timestamp inside the desired accounting window. Omit to use the current window.
        :type window: datetime, optional
        :param split_dim: Keep only instance counters whose split dimension equals a value, written as ``<dim>=<value>`` , such as ``split_dim=user_id=<uuid>&split_dim=tag:env=prod``. Dimensions use the ``split_dims`` names ``user_id`` , ``team_id`` , ``model`` , ``provider`` , and ``tag:<key>``. Repeat the parameter to filter on several dimensions; a counter must match all of them. Each dimension may appear once and must be a per-value dimension of the budget.
        :type split_dim: [str], optional
        :param dim: Return only these split dimensions, such as ``dim=user_id``. Repeat the parameter for several dimensions. Omit it to return every split dimension of the budget.
        :type dim: [str], optional
        :param query: Keep only values that contain this text, case-insensitively. It matches raw values, so User and Team values match their UUIDs; search their names elsewhere and pass the IDs as ``value``.
        :type query: str, optional
        :param value: Keep only these values. Repeat the parameter to check several candidates, such as User IDs found by name, and learn which of them have instance counters.
        :type value: [str], optional
        :param limit: Maximum number of values to return per dimension.
        :type limit: int, optional
        :rtype: AiGatewayBudgetInstanceDimensionListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if window is not unset:
            kwargs["window"] = window

        if split_dim is not unset:
            kwargs["split_dim"] = split_dim

        if dim is not unset:
            kwargs["dim"] = dim

        if query is not unset:
            kwargs["query"] = query

        if value is not unset:
            kwargs["value"] = value

        if limit is not unset:
            kwargs["limit"] = limit

        return self._list_ai_gateway_budget_instance_dimensions_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_budget_instances(
        self,
        id: UUID,
        *,
        window: Union[datetime, UnsetType] = unset,
        split_dim: Union[List[str], UnsetType] = unset,
        sort: Union[AiGatewayBudgetInstanceSort, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> AiGatewayBudgetInstanceListResponse:
        """List AI Gateway budget instances.

        List instance counters for an accounting window. Legacy fixed-scope budgets return one pooled row with an empty instance_key. Omit window to use the current window. Use split_dim to keep only counters that match every given dimension value.

        :param id: Budget UUID.
        :type id: UUID
        :param window: RFC3339 timestamp inside the desired accounting window. Omit to use the current window.
        :type window: datetime, optional
        :param split_dim: Keep only instance counters whose split dimension equals a value, written as ``<dim>=<value>`` , such as ``split_dim=user_id=<uuid>&split_dim=tag:env=prod``. Dimensions use the ``split_dims`` names ``user_id`` , ``team_id`` , ``model`` , ``provider`` , and ``tag:<key>``. Repeat the parameter to filter on several dimensions; a counter must match all of them. Each dimension may appear once and must be a per-value dimension of the budget.
        :type split_dim: [str], optional
        :param sort: Sort order for budget instance counters.
        :type sort: AiGatewayBudgetInstanceSort, optional
        :param limit: Maximum number of budget instance counters to return.
        :type limit: int, optional
        :param offset: Number of budget instance counters to skip.
        :type offset: int, optional
        :rtype: AiGatewayBudgetInstanceListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if window is not unset:
            kwargs["window"] = window

        if split_dim is not unset:
            kwargs["split_dim"] = split_dim

        if sort is not unset:
            kwargs["sort"] = sort

        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        return self._list_ai_gateway_budget_instances_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_budgets(
        self,
    ) -> AiGatewayBudgetListResponse:
        """List AI Gateway budgets.

        List spend budgets for the organization, including active-window spend and effective capacity.

        :rtype: AiGatewayBudgetListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ai_gateway_budgets_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_model_groups(
        self,
    ) -> AiGatewayModelGroupListResponse:
        """List AI Gateway model groups.

        List model groups the user can view. The organization-wide policy has id "default" and explicit model, provider, and route selections. Missing or empty selections grant no organization-wide access. Its audience is fixed to the organization; it cannot be renamed or deleted. Named policies retain their access bindings. Requires configuration read permission; named policies also require view access.

        :rtype: AiGatewayModelGroupListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ai_gateway_model_groups_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_models(
        self,
        provider_id: int,
    ) -> AiGatewayModelCatalogEntryListResponse:
        """List models for an AI Gateway provider.

        List all model catalog entries for a provider. Requires ``ai_gateway_config_read`` and provider View. Catalog and pricing metadata inherit provider access. Lists omit hidden entries; direct reads of hidden resources return 404.

        :param provider_id: Provider ID.
        :type provider_id: int
        :rtype: AiGatewayModelCatalogEntryListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        return self._list_ai_gateway_models_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_models_by_canonical(
        self,
    ) -> AiGatewayModelsByCanonicalListResponse:
        """List AI Gateway models by canonical ID.

        List all model catalog entries grouped by canonical model ID. Requires ``ai_gateway_config_read`` and provider View. Catalog and pricing metadata inherit provider access. Lists omit hidden entries; direct reads of hidden resources return 404.

        :rtype: AiGatewayModelsByCanonicalListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ai_gateway_models_by_canonical_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_policies(
        self,
        *,
        user_id: Union[UUID, UnsetType] = unset,
    ) -> AiGatewayPolicyListResponse:
        """List AI Gateway routing policies.

        List all routing policy documents for the organization. Pass user_id to filter by user scope.

        :param user_id: Filter or scope policies to a specific user. Omit for organization-wide policies.
        :type user_id: UUID, optional
        :rtype: AiGatewayPolicyListResponse
        """
        kwargs: Dict[str, Any] = {}
        if user_id is not unset:
            kwargs["user_id"] = user_id

        return self._list_ai_gateway_policies_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_provider_models(
        self,
        integration_type: str,
        integration_account_id: str,
        *,
        project_id: Union[str, UnsetType] = unset,
        location: Union[str, UnsetType] = unset,
        bedrock_region: Union[str, UnsetType] = unset,
        foundry_resource_id: Union[str, UnsetType] = unset,
    ) -> AiGatewayDiscoveredModelListResponse:
        """List models available from a provider integration.

        List live models available to a provider integration account that supports model discovery.

        :param integration_type: Provider integration type.
        :type integration_type: str
        :param integration_account_id: Provider integration account ID.
        :type integration_account_id: str
        :param project_id: GCP project ID used for Gemini model discovery. Required for Gemini integrations.
        :type project_id: str, optional
        :param location: Optional GCP location used for Gemini model discovery. Defaults to global.
        :type location: str, optional
        :param bedrock_region: AWS region used for Bedrock model discovery. Required for Amazon Bedrock integrations.
        :type bedrock_region: str, optional
        :param foundry_resource_id: ARM resource ID of the Azure AI Foundry resource used for model discovery. Required for Azure AI Foundry integrations.
        :type foundry_resource_id: str, optional
        :rtype: AiGatewayDiscoveredModelListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_type"] = integration_type

        kwargs["integration_account_id"] = integration_account_id

        if project_id is not unset:
            kwargs["project_id"] = project_id

        if location is not unset:
            kwargs["location"] = location

        if bedrock_region is not unset:
            kwargs["bedrock_region"] = bedrock_region

        if foundry_resource_id is not unset:
            kwargs["foundry_resource_id"] = foundry_resource_id

        return self._list_ai_gateway_provider_models_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_providers(
        self,
    ) -> AiGatewayProviderListResponse:
        """List AI Gateway providers.

        List the model providers connected to the organization. Credentials stay in each provider's integration account and are never returned. Requires ``ai_gateway_config_read`` and provider View. Catalog and pricing metadata inherit provider access. Lists omit hidden entries; direct reads of hidden resources return 404.

        :rtype: AiGatewayProviderListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ai_gateway_providers_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_rate_limit_instances(
        self,
        id: UUID,
        *,
        split_dim: Union[List[str], UnsetType] = unset,
        sort: Union[AiGatewayRateLimitInstanceSort, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> AiGatewayRateLimitInstanceListResponse:
        """List AI Gateway rate limit counters.

        List the counters of a template rate limit, one per matched user, Team, or value, with their live usage. Counters appear within a few minutes of their first request and are dropped after 30 days without one. Usage is read for counters seen in the last 20 minutes, at most 200 per request; past that, rows carry usage_known false. Counters for a provider or model the caller can't see are left out, and when the caller can't see the template's selector, the list is empty. A rate limit with one shared allowance, including one whose selector has no per_value entry, returns an empty list. Returns 503 when counter usage can't be read.

        :param id: Rate limit UUID.
        :type id: UUID
        :param split_dim: Keep only counters whose split dimension equals a value, written as ``<dim>=<value>`` , such as ``split_dim=user_id=<uuid>&split_dim=model=gpt-4o``. Dimensions use the ``split_dims`` names ``user_id`` , ``team_id`` , ``model`` , ``provider`` , and ``tag:<key>``. Repeat the parameter to filter on several dimensions; a counter must match all of them. Each dimension may appear once and must be a per-value dimension of the rate limit.
        :type split_dim: [str], optional
        :param sort: Sort order for rate limit counters.
        :type sort: AiGatewayRateLimitInstanceSort, optional
        :param limit: Maximum number of rate limit counters to return.
        :type limit: int, optional
        :param offset: Number of rate limit counters to skip.
        :type offset: int, optional
        :rtype: AiGatewayRateLimitInstanceListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if split_dim is not unset:
            kwargs["split_dim"] = split_dim

        if sort is not unset:
            kwargs["sort"] = sort

        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        return self._list_ai_gateway_rate_limit_instances_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_rate_limits(
        self,
    ) -> AiGatewayRateLimitListResponse:
        """List AI Gateway rate limits.

        List the organization's AI Gateway rate limits.

        :rtype: AiGatewayRateLimitListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ai_gateway_rate_limits_endpoint.call_with_http_info(**kwargs)

    def list_ai_gateway_routing_rules(
        self,
    ) -> AiGatewayRoutingRuleListResponse:
        """List AI Gateway routing rules.

        List the organization's routing rules that the caller has View access to. Requires ``ai_gateway_config_read``. Hidden route references are omitted from nested targets.

        :rtype: AiGatewayRoutingRuleListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_ai_gateway_routing_rules_endpoint.call_with_http_info(**kwargs)

    def override_ai_gateway_budget_instance_capacity(
        self,
        id: UUID,
        body: AiGatewayBudgetInstanceCapacityOverrideRequest,
    ) -> AiGatewayBudgetInstanceResponse:
        """Override a budget instance's capacity.

        Override active-period capacity for one instance of a template budget, identified by its instance_key. Other instances and the budget's default capacity are unchanged. The override is retained in the budget adjustment audit history. Returns 404 when the instance has no counter in the active period. Not supported for legacy fixed-scope budgets.

        :param id: Budget UUID.
        :type id: UUID
        :type body: AiGatewayBudgetInstanceCapacityOverrideRequest
        :rtype: AiGatewayBudgetInstanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._override_ai_gateway_budget_instance_capacity_endpoint.call_with_http_info(**kwargs)

    def reset_ai_gateway_budget_instance_spend(
        self,
        id: UUID,
        body: AiGatewayBudgetInstanceResetRequest,
    ) -> AiGatewayBudgetInstanceResponse:
        """Reset a budget instance's spend.

        Reset active-period spend for one instance of a template budget, identified by its instance_key. The reset is retained in the budget adjustment audit history. Returns 404 when the instance has no counter in the active period. Not supported for legacy fixed-scope budgets.

        :param id: Budget UUID.
        :type id: UUID
        :type body: AiGatewayBudgetInstanceResetRequest
        :rtype: AiGatewayBudgetInstanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._reset_ai_gateway_budget_instance_spend_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_budget(
        self,
        id: UUID,
        body: AiGatewayBudgetUpdateRequest,
    ) -> AiGatewayBudgetResponse:
        """Update an AI Gateway budget.

        Update a budget's mutable definition. Capacity changes apply to future accounting periods
        unless ``apply_to_current_period`` is true.

        :param id: Budget UUID.
        :type id: UUID
        :type body: AiGatewayBudgetUpdateRequest
        :rtype: AiGatewayBudgetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_ai_gateway_budget_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_data_capture_override(
        self,
        id: UUID,
        body: AiGatewayCaptureUpdateRequest,
    ) -> AiGatewayCaptureOverrideResponse:
        """Replace an AI Gateway data capture override.

        Replace an override using its ``revision`` and the current ``configuration_revision``. Changes to capture overrides don't affect routing rules. Returns HTTP 409 when ``configuration_revision`` or the override ``revision`` is stale, including a concurrent change during replacement. Missing revisions or required full-capture confirmation returns HTTP 400.

        :param id: Data capture override ID.
        :type id: UUID
        :type body: AiGatewayCaptureUpdateRequest
        :rtype: AiGatewayCaptureOverrideResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_ai_gateway_data_capture_override_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_governance(
        self,
        body: AiGatewayGovernanceReplaceRequest,
    ) -> AiGatewayGovernanceResponse:
        """Replace AI Gateway governance controls.

        Replace the organization-wide AI Gateway governance settings, which are the default data capture mode and whether requests must reach providers covered by a zero data retention agreement.

        :type body: AiGatewayGovernanceReplaceRequest
        :rtype: AiGatewayGovernanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_ai_gateway_governance_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_model(
        self,
        provider_id: int,
        canonical: str,
        body: AiGatewayModelUpdateRequest,
    ) -> AiGatewayModelCatalogEntryResponse:
        """Update a model for an AI Gateway provider.

        Update a manually managed model catalog entry. Discovered entries are read-only. Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.

        :param provider_id: Provider ID.
        :type provider_id: int
        :param canonical: Canonical model identifier.
        :type canonical: str
        :type body: AiGatewayModelUpdateRequest
        :rtype: AiGatewayModelCatalogEntryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["canonical"] = canonical

        kwargs["body"] = body

        return self._update_ai_gateway_model_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_model_group(
        self,
        id: str,
        body: AiGatewayModelGroupUpdateRequest,
    ) -> AiGatewayModelGroupResponse:
        """Update an AI Gateway model group.

        Update a model group. For id "default", save membership and request options atomically with expected_revision. Empty selections grant no organization-wide access. Applicable authorized named policies override organization-wide request options; a rejected named-policy request cannot fall back to organization-wide options. The organization-wide audience is fixed and grants resource use only. Requires configuration write permission; named policies also require edit access.

        :param id: Model group ID, or "default" for the explicit organization-wide access policy.
        :type id: str
        :type body: AiGatewayModelGroupUpdateRequest
        :rtype: AiGatewayModelGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_ai_gateway_model_group_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_model_pricing(
        self,
        provider_id: int,
        canonical: str,
        body: AiGatewayModelPricingRequest,
    ) -> AiGatewayModelPricingResponse:
        """Set a model pricing override.

        Set a custom provider model's pricing override. Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.

        :param provider_id: Provider ID.
        :type provider_id: int
        :param canonical: Canonical model identifier.
        :type canonical: str
        :type body: AiGatewayModelPricingRequest
        :rtype: AiGatewayModelPricingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["provider_id"] = provider_id

        kwargs["canonical"] = canonical

        kwargs["body"] = body

        return self._update_ai_gateway_model_pricing_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_provider(
        self,
        id: int,
        body: AiGatewayProviderUpdateRequest,
    ) -> AiGatewayProviderResponse:
        """Update an AI Gateway provider.

        Update a provider's display name or cost multiplier. Provider type, integration settings, and slug are immutable. Requires ``ai_gateway_config_write`` and provider Edit. Models and pricing inherit provider access.

        :param id: Provider ID.
        :type id: int
        :type body: AiGatewayProviderUpdateRequest
        :rtype: AiGatewayProviderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_ai_gateway_provider_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_rate_limit(
        self,
        id: UUID,
        body: AiGatewayRateLimitUpdateRequest,
    ) -> AiGatewayRateLimitResponse:
        """Update an AI Gateway rate limit.

        Update a rate limit. Only the attributes sent are changed, and changes never reset current usage. Scope stays editable, except on a template rate limit, whose user_id, team_id, and tags are rejected with 400. Returns 409 when the rule was changed concurrently or the new scope duplicates another rule.

        :param id: Rate limit UUID.
        :type id: UUID
        :type body: AiGatewayRateLimitUpdateRequest
        :rtype: AiGatewayRateLimitResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_ai_gateway_rate_limit_endpoint.call_with_http_info(**kwargs)

    def update_ai_gateway_routing_rule(
        self,
        slug: str,
        body: AiGatewayRoutingRuleReplaceRequest,
    ) -> AiGatewayRoutingRuleResponse:
        """Update an AI Gateway routing rule.

        Update a route with ``ai_gateway_config_write`` and route View/Edit. The slug is immutable; data capture is managed independently. Omitting tiers preserves the entire graph. When tiers are supplied, saved parent-local target IDs retain omitted destination and reasoning, weight, rubric, and default settings. Omitted ordering/classifier settings preserve the saved same-position tier. Explicit null resets nullable settings. New references require View on their resources. A hidden target omitted from tiers must be explicitly listed in removed_target_ids, otherwise the update fails without changes. expected_updated_at rejects stale updates with 409. Sharing-only saves do not replace target rows. Hidden and missing routes return the same 404; visible non-editors receive 403. Inference authorization is unchanged.

        :param slug: Organization-unique routing rule slug.
        :type slug: str
        :type body: AiGatewayRoutingRuleReplaceRequest
        :rtype: AiGatewayRoutingRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["slug"] = slug

        kwargs["body"] = body

        return self._update_ai_gateway_routing_rule_endpoint.call_with_http_info(**kwargs)

    def upsert_ai_gateway_policy(
        self,
        body: AiGatewayPolicyRequest,
        *,
        user_id: Union[UUID, UnsetType] = unset,
    ) -> AiGatewayPolicyResponse:
        """Create or replace an AI Gateway routing policy.

        Create or replace the routing policy document for an inbound pattern. Pass user_id to scope the policy to a user.

        :type body: AiGatewayPolicyRequest
        :param user_id: Filter or scope policies to a specific user. Omit for organization-wide policies.
        :type user_id: UUID, optional
        :rtype: AiGatewayPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        if user_id is not unset:
            kwargs["user_id"] = user_id

        kwargs["body"] = body

        return self._upsert_ai_gateway_policy_endpoint.call_with_http_info(**kwargs)
