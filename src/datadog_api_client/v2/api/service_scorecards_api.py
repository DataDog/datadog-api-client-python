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
from datadog_api_client.v2.model.outcomes_response import OutcomesResponse
from datadog_api_client.v2.model.outcomes_response_data_item import OutcomesResponseDataItem
from datadog_api_client.v2.model.outcomes_batch_response import OutcomesBatchResponse
from datadog_api_client.v2.model.outcomes_batch_request import OutcomesBatchRequest
from datadog_api_client.v2.model.list_rules_response import ListRulesResponse
from datadog_api_client.v2.model.list_rules_response_data_item import ListRulesResponseDataItem
from datadog_api_client.v2.model.create_rule_response import CreateRuleResponse
from datadog_api_client.v2.model.create_rule_request import CreateRuleRequest


class ServiceScorecardsApi:
    """
    API to create, update scorecard rules and outcomes. See `Service Scorecards <https://docs.datadoghq.com/service_catalog/scorecards>`_ for more information.

    This feature is currently in BETA. If you have any feedback, contact `Datadog support <https://docs.datadoghq.com/help/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_scorecard_outcomes_batch_endpoint = _Endpoint(
            settings={
                "response_type": (OutcomesBatchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/outcomes/batch",
                "operation_id": "create_scorecard_outcomes_batch",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OutcomesBatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_scorecard_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CreateRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules",
                "operation_id": "create_scorecard_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_scorecard_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules/{rule_id}",
                "operation_id": "delete_scorecard_rule",
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

        self._list_scorecard_outcomes_endpoint = _Endpoint(
            settings={
                "response_type": (OutcomesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/outcomes",
                "operation_id": "list_scorecard_outcomes",
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
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "fields_outcome": {
                    "openapi_types": (str,),
                    "attribute": "fields[outcome]",
                    "location": "query",
                },
                "fields_rule": {
                    "openapi_types": (str,),
                    "attribute": "fields[rule]",
                    "location": "query",
                },
                "filter_outcome_service_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[outcome][service_name]",
                    "location": "query",
                },
                "filter_outcome_state": {
                    "openapi_types": (str,),
                    "attribute": "filter[outcome][state]",
                    "location": "query",
                },
                "filter_rule_enabled": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][enabled]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][id]",
                    "location": "query",
                },
                "filter_rule_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][name]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_rules_endpoint = _Endpoint(
            settings={
                "response_type": (ListRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules",
                "operation_id": "list_scorecard_rules",
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
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][id]",
                    "location": "query",
                },
                "filter_rule_enabled": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][enabled]",
                    "location": "query",
                },
                "filter_rule_custom": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][custom]",
                    "location": "query",
                },
                "filter_rule_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][name]",
                    "location": "query",
                },
                "filter_rule_description": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][description]",
                    "location": "query",
                },
                "fields_rule": {
                    "openapi_types": (str,),
                    "attribute": "fields[rule]",
                    "location": "query",
                },
                "fields_scorecard": {
                    "openapi_types": (str,),
                    "attribute": "fields[scorecard]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_scorecard_outcomes_batch(
        self,
        body: OutcomesBatchRequest,
    ) -> OutcomesBatchResponse:
        """Create outcomes batch.

        Sets multiple service-rule outcomes in a single batched request.

        :param body: Set of scorecard outcomes.
        :type body: OutcomesBatchRequest
        :rtype: OutcomesBatchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_scorecard_outcomes_batch_endpoint.call_with_http_info(**kwargs)

    def create_scorecard_rule(
        self,
        body: CreateRuleRequest,
    ) -> CreateRuleResponse:
        """Create a new rule.

        Creates a new rule.

        :param body: Rule attributes.
        :type body: CreateRuleRequest
        :rtype: CreateRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_scorecard_rule_endpoint.call_with_http_info(**kwargs)

    def delete_scorecard_rule(
        self,
        rule_id: str,
    ) -> None:
        """Delete a rule.

        Deletes a single rule.

        :param rule_id: The ID of the rule/scorecard.
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_scorecard_rule_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_outcomes(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        fields_outcome: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        filter_outcome_service_name: Union[str, UnsetType] = unset,
        filter_outcome_state: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
    ) -> OutcomesResponse:
        """List all rule outcomes.

        Fetches all rule outcomes.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related rule details in the response.
        :type include: str, optional
        :param fields_outcome: Return only specified values in the outcome attributes.
        :type fields_outcome: str, optional
        :param fields_rule: Return only specified values in the included rule details.
        :type fields_rule: str, optional
        :param filter_outcome_service_name: Filter the outcomes on a specific service name.
        :type filter_outcome_service_name: str, optional
        :param filter_outcome_state: Filter the outcomes by a specific state.
        :type filter_outcome_state: str, optional
        :param filter_rule_enabled: Filter outcomes on whether a rule is enabled/disabled.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_id: Filter outcomes based on rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_name: Filter outcomes based on rule name.
        :type filter_rule_name: str, optional
        :rtype: OutcomesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if fields_outcome is not unset:
            kwargs["fields_outcome"] = fields_outcome

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if filter_outcome_service_name is not unset:
            kwargs["filter_outcome_service_name"] = filter_outcome_service_name

        if filter_outcome_state is not unset:
            kwargs["filter_outcome_state"] = filter_outcome_state

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        return self._list_scorecard_outcomes_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_outcomes_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        fields_outcome: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        filter_outcome_service_name: Union[str, UnsetType] = unset,
        filter_outcome_state: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[OutcomesResponseDataItem]:
        """List all rule outcomes.

        Provide a paginated version of :meth:`list_scorecard_outcomes`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related rule details in the response.
        :type include: str, optional
        :param fields_outcome: Return only specified values in the outcome attributes.
        :type fields_outcome: str, optional
        :param fields_rule: Return only specified values in the included rule details.
        :type fields_rule: str, optional
        :param filter_outcome_service_name: Filter the outcomes on a specific service name.
        :type filter_outcome_service_name: str, optional
        :param filter_outcome_state: Filter the outcomes by a specific state.
        :type filter_outcome_state: str, optional
        :param filter_rule_enabled: Filter outcomes on whether a rule is enabled/disabled.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_id: Filter outcomes based on rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_name: Filter outcomes based on rule name.
        :type filter_rule_name: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[OutcomesResponseDataItem]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if fields_outcome is not unset:
            kwargs["fields_outcome"] = fields_outcome

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if filter_outcome_service_name is not unset:
            kwargs["filter_outcome_service_name"] = filter_outcome_service_name

        if filter_outcome_state is not unset:
            kwargs["filter_outcome_state"] = filter_outcome_state

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_scorecard_outcomes_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_scorecard_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_custom: Union[bool, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
        filter_rule_description: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        fields_scorecard: Union[str, UnsetType] = unset,
    ) -> ListRulesResponse:
        """List all rules.

        Fetch all rules.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related scorecard details in the response.
        :type include: str, optional
        :param filter_rule_id: Filter the rules on a rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_enabled: Filter for enabled rules only.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_custom: Filter for custom rules only.
        :type filter_rule_custom: bool, optional
        :param filter_rule_name: Filter rules on the rule name.
        :type filter_rule_name: str, optional
        :param filter_rule_description: Filter rules on the rule description.
        :type filter_rule_description: str, optional
        :param fields_rule: Return only specific fields in the response for rule attributes.
        :type fields_rule: str, optional
        :param fields_scorecard: Return only specific fields in the included response for scorecard attributes.
        :type fields_scorecard: str, optional
        :rtype: ListRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_custom is not unset:
            kwargs["filter_rule_custom"] = filter_rule_custom

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        if filter_rule_description is not unset:
            kwargs["filter_rule_description"] = filter_rule_description

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if fields_scorecard is not unset:
            kwargs["fields_scorecard"] = fields_scorecard

        return self._list_scorecard_rules_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_rules_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_custom: Union[bool, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
        filter_rule_description: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        fields_scorecard: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[ListRulesResponseDataItem]:
        """List all rules.

        Provide a paginated version of :meth:`list_scorecard_rules`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related scorecard details in the response.
        :type include: str, optional
        :param filter_rule_id: Filter the rules on a rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_enabled: Filter for enabled rules only.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_custom: Filter for custom rules only.
        :type filter_rule_custom: bool, optional
        :param filter_rule_name: Filter rules on the rule name.
        :type filter_rule_name: str, optional
        :param filter_rule_description: Filter rules on the rule description.
        :type filter_rule_description: str, optional
        :param fields_rule: Return only specific fields in the response for rule attributes.
        :type fields_rule: str, optional
        :param fields_scorecard: Return only specific fields in the included response for scorecard attributes.
        :type fields_scorecard: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[ListRulesResponseDataItem]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_custom is not unset:
            kwargs["filter_rule_custom"] = filter_rule_custom

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        if filter_rule_description is not unset:
            kwargs["filter_rule_description"] = filter_rule_description

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if fields_scorecard is not unset:
            kwargs["fields_scorecard"] = fields_scorecard

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_scorecard_rules_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
