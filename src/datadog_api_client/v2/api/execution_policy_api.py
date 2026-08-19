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
from datadog_api_client.v2.model.execution_policy_list_response import ExecutionPolicyListResponse
from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration
from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
from datadog_api_client.v2.model.execution_policy_response import ExecutionPolicyResponse
from datadog_api_client.v2.model.execution_policy_create_request import ExecutionPolicyCreateRequest
from datadog_api_client.v2.model.execution_policy_update_request import ExecutionPolicyUpdateRequest


class ExecutionPolicyApi:
    """
    Execution policies control which actions Datadog Action Platform is allowed to run
    against your infrastructure, and where. Each policy pairs an effect (allow or deny)
    with a pattern of actions, and can scope that decision to specific Kubernetes
    namespaces, scripts, or remote shell paths.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_execution_policy_endpoint = _Endpoint(
            settings={
                "response_type": (ExecutionPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/execution-policies",
                "operation_id": "create_execution_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExecutionPolicyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_execution_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/execution-policies/{policy_id}",
                "operation_id": "delete_execution_policy",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_execution_policy_endpoint = _Endpoint(
            settings={
                "response_type": (ExecutionPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/execution-policies/{policy_id}",
                "operation_id": "get_execution_policy",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_execution_policies_endpoint = _Endpoint(
            settings={
                "response_type": (ExecutionPolicyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/execution-policies",
                "operation_id": "list_execution_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 0,
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
                "filter_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[ids]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_integration": {
                    "openapi_types": ([ExecutionPolicyIntegration],),
                    "attribute": "filter[integration]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_effects": {
                    "openapi_types": ([ExecutionPolicyEffect],),
                    "attribute": "filter[effects]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_creator_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[creator_ids]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "sort": {
                    "openapi_types": ([str],),
                    "attribute": "sort",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_execution_policy_endpoint = _Endpoint(
            settings={
                "response_type": (ExecutionPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/execution-policies/{policy_id}",
                "operation_id": "update_execution_policy",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "policy_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "policy_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExecutionPolicyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_execution_policy(
        self,
        body: ExecutionPolicyCreateRequest,
    ) -> ExecutionPolicyResponse:
        """Create an execution policy.

        Create a new execution policy.

        :param body: The execution policy to create.
        :type body: ExecutionPolicyCreateRequest
        :rtype: ExecutionPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_execution_policy_endpoint.call_with_http_info(**kwargs)

    def delete_execution_policy(
        self,
        policy_id: str,
    ) -> None:
        """Delete an execution policy.

        Delete a specific execution policy.

        :param policy_id: The ID of the execution policy.
        :type policy_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._delete_execution_policy_endpoint.call_with_http_info(**kwargs)

    def get_execution_policy(
        self,
        policy_id: str,
    ) -> ExecutionPolicyResponse:
        """Get an execution policy.

        Retrieve an existing execution policy by ID.

        :param policy_id: The ID of the execution policy.
        :type policy_id: str
        :rtype: ExecutionPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._get_execution_policy_endpoint.call_with_http_info(**kwargs)

    def list_execution_policies(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        filter_ids: Union[List[str], UnsetType] = unset,
        filter_integration: Union[List[ExecutionPolicyIntegration], UnsetType] = unset,
        filter_effects: Union[List[ExecutionPolicyEffect], UnsetType] = unset,
        filter_creator_ids: Union[List[str], UnsetType] = unset,
        sort: Union[List[str], UnsetType] = unset,
    ) -> ExecutionPolicyListResponse:
        """List execution policies.

        Retrieve a list of execution policies for the current organization.

        :param page_size: The number of execution policies to return per page.
        :type page_size: int, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :param filter_name: Filter execution policies by name.
        :type filter_name: str, optional
        :param filter_ids: Filter execution policies by a list of IDs.
        :type filter_ids: [str], optional
        :param filter_integration: Filter execution policies by a list of integrations.
        :type filter_integration: [ExecutionPolicyIntegration], optional
        :param filter_effects: Filter execution policies by a list of effects.
        :type filter_effects: [ExecutionPolicyEffect], optional
        :param filter_creator_ids: Filter execution policies by a list of creator IDs.
        :type filter_creator_ids: [str], optional
        :param sort: The sort order for the results. Prefix a field with ``-`` to sort in
            descending order. Valid fields are ``name`` , ``effect`` , ``integration`` ,
            ``created_at`` , and ``updated_at``.
        :type sort: [str], optional
        :rtype: ExecutionPolicyListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if filter_ids is not unset:
            kwargs["filter_ids"] = filter_ids

        if filter_integration is not unset:
            kwargs["filter_integration"] = filter_integration

        if filter_effects is not unset:
            kwargs["filter_effects"] = filter_effects

        if filter_creator_ids is not unset:
            kwargs["filter_creator_ids"] = filter_creator_ids

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_execution_policies_endpoint.call_with_http_info(**kwargs)

    def update_execution_policy(
        self,
        policy_id: str,
        body: ExecutionPolicyUpdateRequest,
    ) -> ExecutionPolicyResponse:
        """Update an execution policy.

        Update an existing execution policy.
        Returns the execution policy object when the request is successful.

        :param policy_id: The ID of the execution policy.
        :type policy_id: str
        :param body: The new execution policy.
        :type body: ExecutionPolicyUpdateRequest
        :rtype: ExecutionPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        kwargs["body"] = body

        return self._update_execution_policy_endpoint.call_with_http_info(**kwargs)
