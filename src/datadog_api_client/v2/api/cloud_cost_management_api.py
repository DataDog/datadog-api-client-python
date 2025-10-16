# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.arbitrary_rule_response_array import ArbitraryRuleResponseArray
from datadog_api_client.v2.model.arbitrary_rule_response import ArbitraryRuleResponse
from datadog_api_client.v2.model.arbitrary_cost_upsert_request import ArbitraryCostUpsertRequest
from datadog_api_client.v2.model.reorder_rule_resource_array import ReorderRuleResourceArray
from datadog_api_client.v2.model.aws_cur_configs_response import AwsCURConfigsResponse
from datadog_api_client.v2.model.aws_cur_config_response import AwsCurConfigResponse
from datadog_api_client.v2.model.aws_cur_config_post_request import AwsCURConfigPostRequest
from datadog_api_client.v2.model.aws_cur_config_patch_request import AwsCURConfigPatchRequest
from datadog_api_client.v2.model.azure_uc_configs_response import AzureUCConfigsResponse
from datadog_api_client.v2.model.azure_uc_config_pairs_response import AzureUCConfigPairsResponse
from datadog_api_client.v2.model.azure_uc_config_post_request import AzureUCConfigPostRequest
from datadog_api_client.v2.model.uc_config_pair import UCConfigPair
from datadog_api_client.v2.model.azure_uc_config_patch_request import AzureUCConfigPatchRequest
from datadog_api_client.v2.model.budget_with_entries import BudgetWithEntries
from datadog_api_client.v2.model.budget_array import BudgetArray
from datadog_api_client.v2.model.custom_costs_file_list_response import CustomCostsFileListResponse
from datadog_api_client.v2.model.custom_costs_file_upload_response import CustomCostsFileUploadResponse
from datadog_api_client.v2.model.custom_costs_file_line_item import CustomCostsFileLineItem
from datadog_api_client.v2.model.custom_costs_file_get_response import CustomCostsFileGetResponse
from datadog_api_client.v2.model.gcp_usage_cost_configs_response import GCPUsageCostConfigsResponse
from datadog_api_client.v2.model.gcp_usage_cost_config_response import GCPUsageCostConfigResponse
from datadog_api_client.v2.model.gcp_usage_cost_config_post_request import GCPUsageCostConfigPostRequest
from datadog_api_client.v2.model.gcp_uc_config_response import GcpUcConfigResponse
from datadog_api_client.v2.model.gcp_usage_cost_config_patch_request import GCPUsageCostConfigPatchRequest
from datadog_api_client.v2.model.ruleset_resp_array import RulesetRespArray
from datadog_api_client.v2.model.ruleset_resp import RulesetResp
from datadog_api_client.v2.model.create_ruleset_request import CreateRulesetRequest
from datadog_api_client.v2.model.reorder_ruleset_resource_array import ReorderRulesetResourceArray
from datadog_api_client.v2.model.rules_validate_query_response import RulesValidateQueryResponse
from datadog_api_client.v2.model.rules_validate_query_request import RulesValidateQueryRequest
from datadog_api_client.v2.model.update_ruleset_request import UpdateRulesetRequest


class CloudCostManagementApi:
    """
    The Cloud Cost Management API allows you to set up, edit, and delete Cloud Cost Management accounts for AWS, Azure, and Google Cloud. You can query your cost data by using the `Metrics endpoint <https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products>`_ and the ``cloud_cost`` data source. For more information, see the `Cloud Cost Management documentation <https://docs.datadoghq.com/cloud_cost_management/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCurConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config",
                "operation_id": "create_cost_awscur_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AwsCURConfigPostRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_cost_azure_uc_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AzureUCConfigPairsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config",
                "operation_id": "create_cost_azure_uc_configs",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AzureUCConfigPostRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_cost_gcp_usage_cost_config_endpoint = _Endpoint(
            settings={
                "response_type": (GCPUsageCostConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/gcp_uc_config",
                "operation_id": "create_cost_gcp_usage_cost_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GCPUsageCostConfigPostRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_custom_allocation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (ArbitraryRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/arbitrary_rule",
                "operation_id": "create_custom_allocation_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ArbitraryCostUpsertRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_tag_pipelines_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": (RulesetResp,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment",
                "operation_id": "create_tag_pipelines_ruleset",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateRulesetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_budget_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/budget/{budget_id}",
                "operation_id": "delete_budget",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "budget_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "budget_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config/{cloud_account_id}",
                "operation_id": "delete_cost_awscur_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_cost_azure_uc_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config/{cloud_account_id}",
                "operation_id": "delete_cost_azure_uc_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_cost_gcp_usage_cost_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/gcp_uc_config/{cloud_account_id}",
                "operation_id": "delete_cost_gcp_usage_cost_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_custom_allocation_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/arbitrary_rule/{rule_id}",
                "operation_id": "delete_custom_allocation_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_custom_costs_file_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/custom_costs/{file_id}",
                "operation_id": "delete_custom_costs_file",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "file_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "file_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_tag_pipelines_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment/{ruleset_id}",
                "operation_id": "delete_tag_pipelines_ruleset",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "ruleset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_budget_endpoint = _Endpoint(
            settings={
                "response_type": (BudgetWithEntries,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/budget/{budget_id}",
                "operation_id": "get_budget",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "budget_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "budget_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCurConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config/{cloud_account_id}",
                "operation_id": "get_cost_awscur_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_cost_azure_uc_config_endpoint = _Endpoint(
            settings={
                "response_type": (UCConfigPair,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config/{cloud_account_id}",
                "operation_id": "get_cost_azure_uc_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_cost_gcp_usage_cost_config_endpoint = _Endpoint(
            settings={
                "response_type": (GcpUcConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/gcp_uc_config/{cloud_account_id}",
                "operation_id": "get_cost_gcp_usage_cost_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_custom_allocation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (ArbitraryRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/arbitrary_rule/{rule_id}",
                "operation_id": "get_custom_allocation_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_custom_costs_file_endpoint = _Endpoint(
            settings={
                "response_type": (CustomCostsFileGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/custom_costs/{file_id}",
                "operation_id": "get_custom_costs_file",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "file_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "file_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_tag_pipelines_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": (RulesetResp,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment/{ruleset_id}",
                "operation_id": "get_tag_pipelines_ruleset",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "ruleset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_budgets_endpoint = _Endpoint(
            settings={
                "response_type": (BudgetArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/budgets",
                "operation_id": "list_budgets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_cost_awscur_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCURConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config",
                "operation_id": "list_cost_awscur_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_cost_azure_uc_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AzureUCConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config",
                "operation_id": "list_cost_azure_uc_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_cost_gcp_usage_cost_configs_endpoint = _Endpoint(
            settings={
                "response_type": (GCPUsageCostConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/gcp_uc_config",
                "operation_id": "list_cost_gcp_usage_cost_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_custom_allocation_rules_endpoint = _Endpoint(
            settings={
                "response_type": (ArbitraryRuleResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/arbitrary_rule",
                "operation_id": "list_custom_allocation_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_custom_costs_files_endpoint = _Endpoint(
            settings={
                "response_type": (CustomCostsFileListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/custom_costs",
                "operation_id": "list_custom_costs_files",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (str,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tag_pipelines_rulesets_endpoint = _Endpoint(
            settings={
                "response_type": (RulesetRespArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment",
                "operation_id": "list_tag_pipelines_rulesets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._reorder_custom_allocation_rules_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/arbitrary_rule/reorder",
                "operation_id": "reorder_custom_allocation_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ReorderRuleResourceArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._reorder_tag_pipelines_rulesets_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment/reorder",
                "operation_id": "reorder_tag_pipelines_rulesets",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ReorderRulesetResourceArray,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_cost_awscur_config_endpoint = _Endpoint(
            settings={
                "response_type": (AwsCURConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/aws_cur_config/{cloud_account_id}",
                "operation_id": "update_cost_awscur_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AwsCURConfigPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_cost_azure_uc_configs_endpoint = _Endpoint(
            settings={
                "response_type": (AzureUCConfigPairsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/azure_uc_config/{cloud_account_id}",
                "operation_id": "update_cost_azure_uc_configs",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AzureUCConfigPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_cost_gcp_usage_cost_config_endpoint = _Endpoint(
            settings={
                "response_type": (GCPUsageCostConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/gcp_uc_config/{cloud_account_id}",
                "operation_id": "update_cost_gcp_usage_cost_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "cloud_account_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "cloud_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GCPUsageCostConfigPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_custom_allocation_rule_endpoint = _Endpoint(
            settings={
                "response_type": (ArbitraryRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/arbitrary_rule/{rule_id}",
                "operation_id": "update_custom_allocation_rule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ArbitraryCostUpsertRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_tag_pipelines_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": (RulesetResp,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment/{ruleset_id}",
                "operation_id": "update_tag_pipelines_ruleset",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "ruleset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateRulesetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upload_custom_costs_file_endpoint = _Endpoint(
            settings={
                "response_type": (CustomCostsFileUploadResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/custom_costs",
                "operation_id": "upload_custom_costs_file",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": ([CustomCostsFileLineItem],),
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_budget_endpoint = _Endpoint(
            settings={
                "response_type": (BudgetWithEntries,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cost/budget",
                "operation_id": "upsert_budget",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (BudgetWithEntries,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._validate_query_endpoint = _Endpoint(
            settings={
                "response_type": (RulesValidateQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/tags/enrichment/validate-query",
                "operation_id": "validate_query",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RulesValidateQueryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_cost_awscur_config(
        self,
        body: AwsCURConfigPostRequest,
    ) -> AwsCurConfigResponse:
        """Create Cloud Cost Management AWS CUR config.

        Create a Cloud Cost Management account for an AWS CUR config.

        :type body: AwsCURConfigPostRequest
        :rtype: AwsCurConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def create_cost_azure_uc_configs(
        self,
        body: AzureUCConfigPostRequest,
    ) -> AzureUCConfigPairsResponse:
        """Create Cloud Cost Management Azure configs.

        Create a Cloud Cost Management account for an Azure config.

        :type body: AzureUCConfigPostRequest
        :rtype: AzureUCConfigPairsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cost_azure_uc_configs_endpoint.call_with_http_info(**kwargs)

    def create_cost_gcp_usage_cost_config(
        self,
        body: GCPUsageCostConfigPostRequest,
    ) -> GCPUsageCostConfigResponse:
        """Create Google Cloud Usage Cost config.

        Create a Cloud Cost Management account for an Google Cloud Usage Cost config.

        :type body: GCPUsageCostConfigPostRequest
        :rtype: GCPUsageCostConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_cost_gcp_usage_cost_config_endpoint.call_with_http_info(**kwargs)

    def create_custom_allocation_rule(
        self,
        body: ArbitraryCostUpsertRequest,
    ) -> ArbitraryRuleResponse:
        """Create custom allocation rule.

        Create a new custom allocation rule with the specified filters and allocation strategy.

        **Strategy Methods:**

        * **PROPORTIONAL/EVEN** : Allocates costs proportionally/evenly based on existing costs. Requires: granularity, allocated_by_tag_keys. Optional: based_on_costs, allocated_by_filters, evaluate_grouped_by_tag_keys, evaluate_grouped_by_filters.
        * **PROPORTIONAL_TIMESERIES/EVEN_TIMESERIES** : Allocates based on timeseries data. Requires: granularity, based_on_timeseries. Optional: evaluate_grouped_by_tag_keys.
        * **PERCENT** : Allocates fixed percentages to specific tags. Requires: allocated_by (array of percentage allocations).

        **Filter Conditions:**

        * Use **value** for single-value conditions: "is", "is not", "contains", "does not contain", "=", "!=", "like", "not like", "is all values", "is untagged"
        * Use **values** for multi-value conditions: "in", "not in"
        * Cannot use both value and values simultaneously.

        **Supported operators** : is, is not, is all values, is untagged, contains, does not contain, in, not in, =, !=, like, not like

        :type body: ArbitraryCostUpsertRequest
        :rtype: ArbitraryRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_custom_allocation_rule_endpoint.call_with_http_info(**kwargs)

    def create_tag_pipelines_ruleset(
        self,
        body: CreateRulesetRequest,
    ) -> RulesetResp:
        """Create tag pipeline ruleset.

        Create a new tag pipeline ruleset with the specified rules and configuration

        :type body: CreateRulesetRequest
        :rtype: RulesetResp
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_tag_pipelines_ruleset_endpoint.call_with_http_info(**kwargs)

    def delete_budget(
        self,
        budget_id: str,
    ) -> None:
        """Delete a budget.

        Delete a budget.

        :param budget_id: Budget id.
        :type budget_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["budget_id"] = budget_id

        return self._delete_budget_endpoint.call_with_http_info(**kwargs)

    def delete_cost_awscur_config(
        self,
        cloud_account_id: int,
    ) -> None:
        """Delete Cloud Cost Management AWS CUR config.

        Archive a Cloud Cost Management Account.

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._delete_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def delete_cost_azure_uc_config(
        self,
        cloud_account_id: int,
    ) -> None:
        """Delete Cloud Cost Management Azure config.

        Archive a Cloud Cost Management Account.

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._delete_cost_azure_uc_config_endpoint.call_with_http_info(**kwargs)

    def delete_cost_gcp_usage_cost_config(
        self,
        cloud_account_id: int,
    ) -> None:
        """Delete Google Cloud Usage Cost config.

        Archive a Cloud Cost Management account.

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._delete_cost_gcp_usage_cost_config_endpoint.call_with_http_info(**kwargs)

    def delete_custom_allocation_rule(
        self,
        rule_id: int,
    ) -> None:
        """Delete custom allocation rule.

        Delete a custom allocation rule - Delete an existing custom allocation rule by its ID

        :param rule_id: The unique identifier of the custom allocation rule
        :type rule_id: int
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_custom_allocation_rule_endpoint.call_with_http_info(**kwargs)

    def delete_custom_costs_file(
        self,
        file_id: str,
    ) -> None:
        """Delete Custom Costs file.

        Delete the specified Custom Costs file.

        :param file_id: File ID.
        :type file_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["file_id"] = file_id

        return self._delete_custom_costs_file_endpoint.call_with_http_info(**kwargs)

    def delete_tag_pipelines_ruleset(
        self,
        ruleset_id: str,
    ) -> None:
        """Delete tag pipeline ruleset.

        Delete a tag pipeline ruleset - Delete an existing tag pipeline ruleset by its ID

        :param ruleset_id: The unique identifier of the ruleset
        :type ruleset_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_id"] = ruleset_id

        return self._delete_tag_pipelines_ruleset_endpoint.call_with_http_info(**kwargs)

    def get_budget(
        self,
        budget_id: str,
    ) -> BudgetWithEntries:
        """Get a budget.

        Get a budget.

        :param budget_id: Budget id.
        :type budget_id: str
        :rtype: BudgetWithEntries
        """
        kwargs: Dict[str, Any] = {}
        kwargs["budget_id"] = budget_id

        return self._get_budget_endpoint.call_with_http_info(**kwargs)

    def get_cost_awscur_config(
        self,
        cloud_account_id: int,
    ) -> AwsCurConfigResponse:
        """Get cost AWS CUR config.

        Get a specific AWS CUR config.

        :param cloud_account_id: The unique identifier of the cloud account
        :type cloud_account_id: int
        :rtype: AwsCurConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._get_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def get_cost_azure_uc_config(
        self,
        cloud_account_id: int,
    ) -> UCConfigPair:
        """Get cost Azure UC config.

        Get a specific Azure config.

        :param cloud_account_id: The unique identifier of the cloud account
        :type cloud_account_id: int
        :rtype: UCConfigPair
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._get_cost_azure_uc_config_endpoint.call_with_http_info(**kwargs)

    def get_cost_gcp_usage_cost_config(
        self,
        cloud_account_id: int,
    ) -> GcpUcConfigResponse:
        """Get Google Cloud Usage Cost config.

        Get a specific Google Cloud Usage Cost config.

        :param cloud_account_id: The unique identifier of the cloud account
        :type cloud_account_id: int
        :rtype: GcpUcConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        return self._get_cost_gcp_usage_cost_config_endpoint.call_with_http_info(**kwargs)

    def get_custom_allocation_rule(
        self,
        rule_id: int,
    ) -> ArbitraryRuleResponse:
        """Get custom allocation rule.

        Get a specific custom allocation rule - Retrieve a specific custom allocation rule by its ID

        :param rule_id: The unique identifier of the custom allocation rule
        :type rule_id: int
        :rtype: ArbitraryRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._get_custom_allocation_rule_endpoint.call_with_http_info(**kwargs)

    def get_custom_costs_file(
        self,
        file_id: str,
    ) -> CustomCostsFileGetResponse:
        """Get Custom Costs file.

        Fetch the specified Custom Costs file.

        :param file_id: File ID.
        :type file_id: str
        :rtype: CustomCostsFileGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["file_id"] = file_id

        return self._get_custom_costs_file_endpoint.call_with_http_info(**kwargs)

    def get_tag_pipelines_ruleset(
        self,
        ruleset_id: str,
    ) -> RulesetResp:
        """Get a tag pipeline ruleset.

        Get a specific tag pipeline ruleset - Retrieve a specific tag pipeline ruleset by its ID

        :param ruleset_id: The unique identifier of the ruleset
        :type ruleset_id: str
        :rtype: RulesetResp
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_id"] = ruleset_id

        return self._get_tag_pipelines_ruleset_endpoint.call_with_http_info(**kwargs)

    def list_budgets(
        self,
    ) -> BudgetArray:
        """List budgets.

        List budgets.

        :rtype: BudgetArray
        """
        kwargs: Dict[str, Any] = {}
        return self._list_budgets_endpoint.call_with_http_info(**kwargs)

    def list_cost_awscur_configs(
        self,
    ) -> AwsCURConfigsResponse:
        """List Cloud Cost Management AWS CUR configs.

        List the AWS CUR configs.

        :rtype: AwsCURConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cost_awscur_configs_endpoint.call_with_http_info(**kwargs)

    def list_cost_azure_uc_configs(
        self,
    ) -> AzureUCConfigsResponse:
        """List Cloud Cost Management Azure configs.

        List the Azure configs.

        :rtype: AzureUCConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cost_azure_uc_configs_endpoint.call_with_http_info(**kwargs)

    def list_cost_gcp_usage_cost_configs(
        self,
    ) -> GCPUsageCostConfigsResponse:
        """List Google Cloud Usage Cost configs.

        List the Google Cloud Usage Cost configs.

        :rtype: GCPUsageCostConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_cost_gcp_usage_cost_configs_endpoint.call_with_http_info(**kwargs)

    def list_custom_allocation_rules(
        self,
    ) -> ArbitraryRuleResponseArray:
        """List custom allocation rules.

        List all custom allocation rules - Retrieve a list of all custom allocation rules for the organization

        :rtype: ArbitraryRuleResponseArray
        """
        kwargs: Dict[str, Any] = {}
        return self._list_custom_allocation_rules_endpoint.call_with_http_info(**kwargs)

    def list_custom_costs_files(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        filter_status: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> CustomCostsFileListResponse:
        """List Custom Costs files.

        List the Custom Costs files.

        :param page_number: Page number for pagination
        :type page_number: int, optional
        :param page_size: Page size for pagination
        :type page_size: int, optional
        :param filter_status: Filter by file status
        :type filter_status: str, optional
        :param sort: Sort key with optional descending prefix
        :type sort: str, optional
        :rtype: CustomCostsFileListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_custom_costs_files_endpoint.call_with_http_info(**kwargs)

    def list_tag_pipelines_rulesets(
        self,
    ) -> RulesetRespArray:
        """List tag pipeline rulesets.

        List all tag pipeline rulesets - Retrieve a list of all tag pipeline rulesets for the organization

        :rtype: RulesetRespArray
        """
        kwargs: Dict[str, Any] = {}
        return self._list_tag_pipelines_rulesets_endpoint.call_with_http_info(**kwargs)

    def reorder_custom_allocation_rules(
        self,
        body: ReorderRuleResourceArray,
    ) -> None:
        """Reorder custom allocation rules.

        Reorder custom allocation rules - Change the execution order of custom allocation rules.

        **Important** : You must provide the **complete list** of all rule IDs in the desired execution order. The API will reorder ALL rules according to the provided sequence.

        Rules are executed in the order specified, with lower indices (earlier in the array) having higher priority.

        **Example** : If you have rules with IDs [123, 456, 789] and want to change order from 123→456→789 to 456→123→789, send: [{"id": "456"}, {"id": "123"}, {"id": "789"}]

        :type body: ReorderRuleResourceArray
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._reorder_custom_allocation_rules_endpoint.call_with_http_info(**kwargs)

    def reorder_tag_pipelines_rulesets(
        self,
        body: ReorderRulesetResourceArray,
    ) -> None:
        """Reorder tag pipeline rulesets.

        Reorder tag pipeline rulesets - Change the execution order of tag pipeline rulesets

        :type body: ReorderRulesetResourceArray
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._reorder_tag_pipelines_rulesets_endpoint.call_with_http_info(**kwargs)

    def update_cost_awscur_config(
        self,
        cloud_account_id: int,
        body: AwsCURConfigPatchRequest,
    ) -> AwsCURConfigsResponse:
        """Update Cloud Cost Management AWS CUR config.

        Update the status (active/archived) and/or account filtering configuration of an AWS CUR config.

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: int
        :type body: AwsCURConfigPatchRequest
        :rtype: AwsCURConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        kwargs["body"] = body

        return self._update_cost_awscur_config_endpoint.call_with_http_info(**kwargs)

    def update_cost_azure_uc_configs(
        self,
        cloud_account_id: int,
        body: AzureUCConfigPatchRequest,
    ) -> AzureUCConfigPairsResponse:
        """Update Cloud Cost Management Azure config.

        Update the status of an  Azure config (active/archived).

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: int
        :type body: AzureUCConfigPatchRequest
        :rtype: AzureUCConfigPairsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        kwargs["body"] = body

        return self._update_cost_azure_uc_configs_endpoint.call_with_http_info(**kwargs)

    def update_cost_gcp_usage_cost_config(
        self,
        cloud_account_id: int,
        body: GCPUsageCostConfigPatchRequest,
    ) -> GCPUsageCostConfigResponse:
        """Update Google Cloud Usage Cost config.

        Update the status of an Google Cloud Usage Cost config (active/archived).

        :param cloud_account_id: Cloud Account id.
        :type cloud_account_id: int
        :type body: GCPUsageCostConfigPatchRequest
        :rtype: GCPUsageCostConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["cloud_account_id"] = cloud_account_id

        kwargs["body"] = body

        return self._update_cost_gcp_usage_cost_config_endpoint.call_with_http_info(**kwargs)

    def update_custom_allocation_rule(
        self,
        rule_id: int,
        body: ArbitraryCostUpsertRequest,
    ) -> ArbitraryRuleResponse:
        """Update custom allocation rule.

        Update an existing custom allocation rule with new filters and allocation strategy.

        **Strategy Methods:**

        * **PROPORTIONAL/EVEN** : Allocates costs proportionally/evenly based on existing costs. Requires: granularity, allocated_by_tag_keys. Optional: based_on_costs, allocated_by_filters, evaluate_grouped_by_tag_keys, evaluate_grouped_by_filters.
        * **PROPORTIONAL_TIMESERIES/EVEN_TIMESERIES** : Allocates based on timeseries data. Requires: granularity, based_on_timeseries. Optional: evaluate_grouped_by_tag_keys.
        * **PERCENT** : Allocates fixed percentages to specific tags. Requires: allocated_by (array of percentage allocations).
        * **USAGE_METRIC** : Allocates based on usage metrics (implementation varies).

        **Filter Conditions:**

        * Use **value** for single-value conditions: "is", "is not", "contains", "does not contain", "=", "!=", "like", "not like", "is all values", "is untagged"
        * Use **values** for multi-value conditions: "in", "not in"
        * Cannot use both value and values simultaneously.

        **Supported operators** : is, is not, is all values, is untagged, contains, does not contain, in, not in, =, !=, like, not like

        :param rule_id: The unique identifier of the custom allocation rule
        :type rule_id: int
        :type body: ArbitraryCostUpsertRequest
        :rtype: ArbitraryRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_custom_allocation_rule_endpoint.call_with_http_info(**kwargs)

    def update_tag_pipelines_ruleset(
        self,
        ruleset_id: str,
        body: UpdateRulesetRequest,
    ) -> RulesetResp:
        """Update tag pipeline ruleset.

        Update a tag pipeline ruleset - Update an existing tag pipeline ruleset with new rules and configuration

        :param ruleset_id: The unique identifier of the ruleset
        :type ruleset_id: str
        :type body: UpdateRulesetRequest
        :rtype: RulesetResp
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_id"] = ruleset_id

        kwargs["body"] = body

        return self._update_tag_pipelines_ruleset_endpoint.call_with_http_info(**kwargs)

    def upload_custom_costs_file(
        self,
        body: List[CustomCostsFileLineItem],
    ) -> CustomCostsFileUploadResponse:
        """Upload Custom Costs file.

        Upload a Custom Costs file.

        :type body: [CustomCostsFileLineItem]
        :rtype: CustomCostsFileUploadResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._upload_custom_costs_file_endpoint.call_with_http_info(**kwargs)

    def upsert_budget(
        self,
        body: BudgetWithEntries,
    ) -> BudgetWithEntries:
        """Create or update a budget.

        Create a new budget or update an existing one.

        :type body: BudgetWithEntries
        :rtype: BudgetWithEntries
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._upsert_budget_endpoint.call_with_http_info(**kwargs)

    def validate_query(
        self,
        body: RulesValidateQueryRequest,
    ) -> RulesValidateQueryResponse:
        """Validate query.

        Validate a tag pipeline query - Validate the syntax and structure of a tag pipeline query

        :type body: RulesValidateQueryRequest
        :rtype: RulesValidateQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._validate_query_endpoint.call_with_http_info(**kwargs)
