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
from datadog_api_client.v2.model.tag_policies_list_response import TagPoliciesListResponse
from datadog_api_client.v2.model.tag_policy_include import TagPolicyInclude
from datadog_api_client.v2.model.tag_policy_source import TagPolicySource
from datadog_api_client.v2.model.tag_policy_response import TagPolicyResponse
from datadog_api_client.v2.model.tag_policy_create_request import TagPolicyCreateRequest
from datadog_api_client.v2.model.tag_policy_update_request import TagPolicyUpdateRequest
from datadog_api_client.v2.model.tag_policy_score_response import TagPolicyScoreResponse


class TagPoliciesApi:
    """
    Tag Policies define rules that govern which tag values are accepted for a given tag key,
    scoped to a particular telemetry source (such as logs, spans, or metrics). Policies can be
    ``blocking`` (data not matching the policy is rejected) or ``surfacing`` (matching data is
    highlighted but not blocked). Each policy reports a compliance ``score`` derived from how
    much recent telemetry adheres to the policy.
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
                "hard_delete": {
                    "openapi_types": (bool,),
                    "attribute": "hard_delete",
                    "location": "query",
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
                "include": {
                    "openapi_types": (TagPolicyInclude,),
                    "attribute": "include",
                    "location": "query",
                },
                "ts_start": {
                    "openapi_types": (int,),
                    "attribute": "ts_start",
                    "location": "query",
                },
                "ts_end": {
                    "openapi_types": (int,),
                    "attribute": "ts_end",
                    "location": "query",
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
                "ts_start": {
                    "openapi_types": (int,),
                    "attribute": "ts_start",
                    "location": "query",
                },
                "ts_end": {
                    "openapi_types": (int,),
                    "attribute": "ts_end",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tag_policies_endpoint = _Endpoint(
            settings={
                "response_type": (TagPoliciesListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/tag-policies",
                "operation_id": "list_tag_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include_disabled": {
                    "openapi_types": (bool,),
                    "attribute": "include_disabled",
                    "location": "query",
                },
                "include_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "include_deleted",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (TagPolicyInclude,),
                    "attribute": "include",
                    "location": "query",
                },
                "filter_source": {
                    "openapi_types": (TagPolicySource,),
                    "attribute": "filter[source]",
                    "location": "query",
                },
                "ts_start": {
                    "openapi_types": (int,),
                    "attribute": "ts_start",
                    "location": "query",
                },
                "ts_end": {
                    "openapi_types": (int,),
                    "attribute": "ts_end",
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

        Create a new tag policy for the organization. The caller's organization is derived from
        the authenticated user; cross-organization creation is not supported. Fields such as
        ``policy_id`` , ``version`` , and the timestamp/audit fields are assigned by the server.

        :type body: TagPolicyCreateRequest
        :rtype: TagPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_tag_policy_endpoint.call_with_http_info(**kwargs)

    def delete_tag_policy(
        self,
        policy_id: str,
        *,
        hard_delete: Union[bool, UnsetType] = unset,
    ) -> None:
        """Delete a tag policy.

        Delete a tag policy. By default the policy is soft-deleted so it can be recovered later
        and so that historical score data remains queryable. Pass ``hard_delete=true`` to remove
        the policy permanently.

        :param policy_id: The unique identifier of the tag policy to delete.
        :type policy_id: str
        :param hard_delete: Whether to permanently delete the policy instead of performing a soft delete. Defaults to ``false``.
        :type hard_delete: bool, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        if hard_delete is not unset:
            kwargs["hard_delete"] = hard_delete

        return self._delete_tag_policy_endpoint.call_with_http_info(**kwargs)

    def get_tag_policy(
        self,
        policy_id: str,
        *,
        include: Union[TagPolicyInclude, UnsetType] = unset,
        ts_start: Union[int, UnsetType] = unset,
        ts_end: Union[int, UnsetType] = unset,
    ) -> TagPolicyResponse:
        """Get a tag policy.

        Retrieve a single tag policy by ID. Optionally include the policy's current compliance
        score via the ``include=score`` query parameter. Policies belonging to other organizations
        cannot be retrieved.

        :param policy_id: The unique identifier of the tag policy.
        :type policy_id: str
        :param include: Comma-separated list of related resources to include alongside the policy. Currently the only supported value is ``score``.
        :type include: TagPolicyInclude, optional
        :param ts_start: Start of the time window used for compliance score computation, as a Unix timestamp in milliseconds.
        :type ts_start: int, optional
        :param ts_end: End of the time window used for compliance score computation, as a Unix timestamp in milliseconds. Must be in the past and greater than ``ts_start``.
        :type ts_end: int, optional
        :rtype: TagPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        if include is not unset:
            kwargs["include"] = include

        if ts_start is not unset:
            kwargs["ts_start"] = ts_start

        if ts_end is not unset:
            kwargs["ts_end"] = ts_end

        return self._get_tag_policy_endpoint.call_with_http_info(**kwargs)

    def get_tag_policy_score(
        self,
        policy_id: str,
        *,
        ts_start: Union[int, UnsetType] = unset,
        ts_end: Union[int, UnsetType] = unset,
    ) -> TagPolicyScoreResponse:
        """Get a tag policy compliance score.

        Retrieve the compliance score for a single tag policy. The score is computed over the
        requested time window (or a source-appropriate default) and represents the percentage of
        telemetry within that window that conforms to the policy. A ``null`` score indicates that
        no relevant telemetry was found.

        :param policy_id: The unique identifier of the tag policy.
        :type policy_id: str
        :param ts_start: Start of the time window used for compliance score computation, as a Unix timestamp in milliseconds.
        :type ts_start: int, optional
        :param ts_end: End of the time window used for compliance score computation, as a Unix timestamp in milliseconds. Must be in the past and greater than ``ts_start``.
        :type ts_end: int, optional
        :rtype: TagPolicyScoreResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        if ts_start is not unset:
            kwargs["ts_start"] = ts_start

        if ts_end is not unset:
            kwargs["ts_end"] = ts_end

        return self._get_tag_policy_score_endpoint.call_with_http_info(**kwargs)

    def list_tag_policies(
        self,
        *,
        include_disabled: Union[bool, UnsetType] = unset,
        include_deleted: Union[bool, UnsetType] = unset,
        include: Union[TagPolicyInclude, UnsetType] = unset,
        filter_source: Union[TagPolicySource, UnsetType] = unset,
        ts_start: Union[int, UnsetType] = unset,
        ts_end: Union[int, UnsetType] = unset,
    ) -> TagPoliciesListResponse:
        """List tag policies.

        Retrieve all tag policies for the organization. Optionally include disabled or deleted
        policies, filter by telemetry source, and include each policy's current compliance score
        via the ``include=score`` query parameter.

        :param include_disabled: Whether to include policies that are currently disabled. Defaults to ``false``.
        :type include_disabled: bool, optional
        :param include_deleted: Whether to include policies that have been soft-deleted. Defaults to ``false``.
        :type include_deleted: bool, optional
        :param include: Comma-separated list of related resources to include alongside each policy in the response. Currently the only supported value is ``score``.
        :type include: TagPolicyInclude, optional
        :param filter_source: Restrict the result set to policies whose source matches the given value.
        :type filter_source: TagPolicySource, optional
        :param ts_start: Start of the time window used for compliance score computation, as a Unix timestamp in milliseconds. Defaults to a recent window appropriate for the source.
        :type ts_start: int, optional
        :param ts_end: End of the time window used for compliance score computation, as a Unix timestamp in milliseconds. Must be in the past and greater than ``ts_start``.
        :type ts_end: int, optional
        :rtype: TagPoliciesListResponse
        """
        kwargs: Dict[str, Any] = {}
        if include_disabled is not unset:
            kwargs["include_disabled"] = include_disabled

        if include_deleted is not unset:
            kwargs["include_deleted"] = include_deleted

        if include is not unset:
            kwargs["include"] = include

        if filter_source is not unset:
            kwargs["filter_source"] = filter_source

        if ts_start is not unset:
            kwargs["ts_start"] = ts_start

        if ts_end is not unset:
            kwargs["ts_end"] = ts_end

        return self._list_tag_policies_endpoint.call_with_http_info(**kwargs)

    def update_tag_policy(
        self,
        policy_id: str,
        body: TagPolicyUpdateRequest,
    ) -> TagPolicyResponse:
        """Update a tag policy.

        Update one or more attributes of an existing tag policy. Only the fields supplied in the
        request body are modified; omitted fields retain their current values. The policy's
        ``source`` cannot be changed after creation.

        :param policy_id: The unique identifier of the tag policy to update.
        :type policy_id: str
        :type body: TagPolicyUpdateRequest
        :rtype: TagPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["policy_id"] = policy_id

        kwargs["body"] = body

        return self._update_tag_policy_endpoint.call_with_http_info(**kwargs)
