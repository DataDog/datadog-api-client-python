# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.sca_request import ScaRequest
from datadog_api_client.v2.model.resolve_vulnerable_symbols_response import ResolveVulnerableSymbolsResponse
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request import ResolveVulnerableSymbolsRequest
from datadog_api_client.v2.model.custom_ruleset_response import CustomRulesetResponse
from datadog_api_client.v2.model.custom_ruleset_request import CustomRulesetRequest
from datadog_api_client.v2.model.custom_rule_response import CustomRuleResponse
from datadog_api_client.v2.model.custom_rule_request import CustomRuleRequest
from datadog_api_client.v2.model.custom_rule_revisions_response import CustomRuleRevisionsResponse
from datadog_api_client.v2.model.custom_rule_revision import CustomRuleRevision
from datadog_api_client.v2.model.custom_rule_revision_request import CustomRuleRevisionRequest
from datadog_api_client.v2.model.revert_custom_rule_revision_request import RevertCustomRuleRevisionRequest
from datadog_api_client.v2.model.custom_rule_revision_response import CustomRuleRevisionResponse


class StaticAnalysisApi:
    """
    API for static analysis
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CustomRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules",
                "operation_id": "create_custom_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CustomRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_custom_rule_revision_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions",
                "operation_id": "create_custom_rule_revision",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
                "rule_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CustomRuleRevisionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_sca_resolve_vulnerable_symbols_endpoint = _Endpoint(
            settings={
                "response_type": (ResolveVulnerableSymbolsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols",
                "operation_id": "create_sca_resolve_vulnerable_symbols",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ResolveVulnerableSymbolsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_sca_result_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis-sca/dependencies",
                "operation_id": "create_sca_result",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ScaRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}",
                "operation_id": "delete_custom_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
                "rule_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_custom_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}",
                "operation_id": "delete_custom_ruleset",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_custom_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CustomRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}",
                "operation_id": "get_custom_rule",
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
                "rule_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_custom_rule_revision_endpoint = _Endpoint(
            settings={
                "response_type": (CustomRuleRevisionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/{id}",
                "operation_id": "get_custom_rule_revision",
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
                "rule_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_name",
                    "location": "path",
                },
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

        self._get_custom_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": (CustomRulesetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}",
                "operation_id": "get_custom_ruleset",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_custom_rule_revisions_endpoint = _Endpoint(
            settings={
                "response_type": (CustomRuleRevisionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions",
                "operation_id": "list_custom_rule_revisions",
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
                "rule_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_name",
                    "location": "path",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
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

        self._revert_custom_rule_revision_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}/rules/{rule_name}/revisions/revert",
                "operation_id": "revert_custom_rule_revision",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
                "rule_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RevertCustomRuleRevisionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_custom_ruleset_endpoint = _Endpoint(
            settings={
                "response_type": (CustomRulesetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/static-analysis/custom/rulesets/{ruleset_name}",
                "operation_id": "update_custom_ruleset",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "ruleset_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ruleset_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CustomRulesetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_custom_rule(
        self,
        ruleset_name: str,
        body: CustomRuleRequest,
    ) -> CustomRuleResponse:
        """Create Custom Rule.

        Create a new custom rule within a ruleset

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :type body: CustomRuleRequest
        :rtype: CustomRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["body"] = body

        return self._create_custom_rule_endpoint.call_with_http_info(**kwargs)

    def create_custom_rule_revision(
        self,
        ruleset_name: str,
        rule_name: str,
        body: CustomRuleRevisionRequest,
    ) -> None:
        """Create Custom Rule Revision.

        Create a new revision for a custom rule

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :type body: CustomRuleRevisionRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        kwargs["body"] = body

        return self._create_custom_rule_revision_endpoint.call_with_http_info(**kwargs)

    def create_sca_resolve_vulnerable_symbols(
        self,
        body: ResolveVulnerableSymbolsRequest,
    ) -> ResolveVulnerableSymbolsResponse:
        """POST request to resolve vulnerable symbols.

        :type body: ResolveVulnerableSymbolsRequest
        :rtype: ResolveVulnerableSymbolsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_sca_resolve_vulnerable_symbols_endpoint.call_with_http_info(**kwargs)

    def create_sca_result(
        self,
        body: ScaRequest,
    ) -> None:
        """Post dependencies for analysis.

        :type body: ScaRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_sca_result_endpoint.call_with_http_info(**kwargs)

    def delete_custom_rule(
        self,
        ruleset_name: str,
        rule_name: str,
    ) -> None:
        """Delete Custom Rule.

        Delete a custom rule

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        return self._delete_custom_rule_endpoint.call_with_http_info(**kwargs)

    def delete_custom_ruleset(
        self,
        ruleset_name: str,
    ) -> None:
        """Delete Custom Ruleset.

        Delete a custom ruleset

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        return self._delete_custom_ruleset_endpoint.call_with_http_info(**kwargs)

    def get_custom_rule(
        self,
        ruleset_name: str,
        rule_name: str,
    ) -> CustomRuleResponse:
        """Show Custom Rule.

        Get a custom rule by name

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :rtype: CustomRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        return self._get_custom_rule_endpoint.call_with_http_info(**kwargs)

    def get_custom_rule_revision(
        self,
        ruleset_name: str,
        rule_name: str,
        id: str,
    ) -> CustomRuleRevisionResponse:
        """Show Custom Rule Revision.

        Get a specific revision of a custom rule

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :param id: The revision ID
        :type id: str
        :rtype: CustomRuleRevisionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        kwargs["id"] = id

        return self._get_custom_rule_revision_endpoint.call_with_http_info(**kwargs)

    def get_custom_ruleset(
        self,
        ruleset_name: str,
    ) -> CustomRulesetResponse:
        """Show Custom Ruleset.

        Get a custom ruleset by name

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :rtype: CustomRulesetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        return self._get_custom_ruleset_endpoint.call_with_http_info(**kwargs)

    def list_custom_rule_revisions(
        self,
        ruleset_name: str,
        rule_name: str,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> CustomRuleRevisionsResponse:
        """List Custom Rule Revisions.

        Get all revisions for a custom rule

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :param page_offset: Pagination offset
        :type page_offset: int, optional
        :param page_limit: Pagination limit
        :type page_limit: int, optional
        :rtype: CustomRuleRevisionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_custom_rule_revisions_endpoint.call_with_http_info(**kwargs)

    def list_custom_rule_revisions_with_pagination(
        self,
        ruleset_name: str,
        rule_name: str,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[CustomRuleRevision]:
        """List Custom Rule Revisions.

        Provide a paginated version of :meth:`list_custom_rule_revisions`, returning all items.

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :param page_offset: Pagination offset
        :type page_offset: int, optional
        :param page_limit: Pagination limit
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[CustomRuleRevision]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 10)
        endpoint = self._list_custom_rule_revisions_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def revert_custom_rule_revision(
        self,
        ruleset_name: str,
        rule_name: str,
        body: RevertCustomRuleRevisionRequest,
    ) -> None:
        """Revert Custom Rule Revision.

        Revert a custom rule to a previous revision

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :param rule_name: The rule name
        :type rule_name: str
        :type body: RevertCustomRuleRevisionRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["rule_name"] = rule_name

        kwargs["body"] = body

        return self._revert_custom_rule_revision_endpoint.call_with_http_info(**kwargs)

    def update_custom_ruleset(
        self,
        ruleset_name: str,
        body: CustomRulesetRequest,
    ) -> CustomRulesetResponse:
        """Update Custom Ruleset.

        Update an existing custom ruleset

        :param ruleset_name: The ruleset name
        :type ruleset_name: str
        :type body: CustomRulesetRequest
        :rtype: CustomRulesetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["ruleset_name"] = ruleset_name

        kwargs["body"] = body

        return self._update_custom_ruleset_endpoint.call_with_http_info(**kwargs)
