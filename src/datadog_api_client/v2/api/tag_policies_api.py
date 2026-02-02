# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.tag_policies_response import TagPoliciesResponse
from datadog_api_client.v2.model.tag_policy_response import TagPolicyResponse
from datadog_api_client.v2.model.tag_policy_create_request import TagPolicyCreateRequest
from datadog_api_client.v2.model.tag_policy_update_request import TagPolicyUpdateRequest
from datadog_api_client.v2.model.tag_policy_score_response import TagPolicyScoreResponse


class TagPoliciesApi:
    """
    Manage tag policies to enforce tagging standards across your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_tag_policy_endpoint = _Endpoint(
            settings={
                "response_type": (TagPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies",
                "operation_id": "create_tag_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TagPolicyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_tag_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies/{policy_id}",
                "operation_id": "delete_tag_policy",
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

        self._get_tag_policy_endpoint = _Endpoint(
            settings={
                "response_type": (TagPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies/{policy_id}",
                "operation_id": "get_tag_policy",
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

        self._get_tag_policy_score_endpoint = _Endpoint(
            settings={
                "response_type": (TagPolicyScoreResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies/{policy_id}/score",
                "operation_id": "get_tag_policy_score",
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

        self._list_tag_policies_endpoint = _Endpoint(
            settings={
                "response_type": (TagPoliciesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies",
                "operation_id": "list_tag_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_source": {
                    "openapi_types": (str,),
                    "attribute": "filter[source]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_tag_policy_endpoint = _Endpoint(
            settings={
                "response_type": (TagPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies/{policy_id}",
                "operation_id": "update_tag_policy",
                "http_method": "PATCH",
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
                    "openapi_types": (TagPolicyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_tag_policy(
        self,
        body: TagPolicyCreateRequest,
    ) -> TagPolicyResponse:
        """Create a tag policy.

        Create a new tag policy for the organization.

        :type body: TagPolicyCreateRequest
        :rtype: TagPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_tag_policy_endpoint.call_with_http_info(**kwargs)

    def delete_tag_policy(
        self,
        policy_id: str,
    ) -> None:
        """Delete a tag policy.

        Delete a specific tag policy by its ID.

        :param policy_id: The ID of the tag policy.
        :type policy_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._delete_tag_policy_endpoint.call_with_http_info(**kwargs)

    def get_tag_policy(
        self,
        policy_id: str,
    ) -> TagPolicyResponse:
        """Get a tag policy.

        Retrieve a specific tag policy by its ID.

        :param policy_id: The ID of the tag policy.
        :type policy_id: str
        :rtype: TagPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._get_tag_policy_endpoint.call_with_http_info(**kwargs)

    def get_tag_policy_score(
        self,
        policy_id: str,
    ) -> TagPolicyScoreResponse:
        """Get tag policy score.

        Retrieve the compliance score for a specific tag policy.

        :param policy_id: The ID of the tag policy.
        :type policy_id: str
        :rtype: TagPolicyScoreResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        return self._get_tag_policy_score_endpoint.call_with_http_info(**kwargs)

    def list_tag_policies(
        self,
        *,
        filter_source: Union[str, UnsetType] = unset,
    ) -> TagPoliciesResponse:
        """List tag policies.

        Retrieve a list of all tag policies for the organization.

        :param filter_source: Filter policies by data source (e.g., logs, metrics).
        :type filter_source: str, optional
        :rtype: TagPoliciesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_source is not unset:
            kwargs["filter_source"] = filter_source

        return self._list_tag_policies_endpoint.call_with_http_info(**kwargs)

    def update_tag_policy(
        self,
        policy_id: str,
        body: TagPolicyUpdateRequest,
    ) -> TagPolicyResponse:
        """Update a tag policy.

        Update an existing tag policy by its ID.

        :param policy_id: The ID of the tag policy.
        :type policy_id: str
        :type body: TagPolicyUpdateRequest
        :rtype: TagPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        kwargs["body"] = body

        return self._update_tag_policy_endpoint.call_with_http_info(**kwargs)
