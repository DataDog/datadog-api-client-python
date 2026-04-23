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
    UUID,
)
from datadog_api_client.v2.model.org_group_membership_list_response import OrgGroupMembershipListResponse
from datadog_api_client.v2.model.org_group_membership_sort_option import OrgGroupMembershipSortOption
from datadog_api_client.v2.model.org_group_membership_bulk_update_request import OrgGroupMembershipBulkUpdateRequest
from datadog_api_client.v2.model.org_group_membership_response import OrgGroupMembershipResponse
from datadog_api_client.v2.model.org_group_membership_update_request import OrgGroupMembershipUpdateRequest
from datadog_api_client.v2.model.org_group_policy_list_response import OrgGroupPolicyListResponse
from datadog_api_client.v2.model.org_group_policy_sort_option import OrgGroupPolicySortOption
from datadog_api_client.v2.model.org_group_policy_response import OrgGroupPolicyResponse
from datadog_api_client.v2.model.org_group_policy_create_request import OrgGroupPolicyCreateRequest
from datadog_api_client.v2.model.org_group_policy_update_request import OrgGroupPolicyUpdateRequest
from datadog_api_client.v2.model.org_group_policy_config_list_response import OrgGroupPolicyConfigListResponse
from datadog_api_client.v2.model.org_group_policy_override_list_response import OrgGroupPolicyOverrideListResponse
from datadog_api_client.v2.model.org_group_policy_override_sort_option import OrgGroupPolicyOverrideSortOption
from datadog_api_client.v2.model.org_group_policy_override_response import OrgGroupPolicyOverrideResponse
from datadog_api_client.v2.model.org_group_policy_override_create_request import OrgGroupPolicyOverrideCreateRequest
from datadog_api_client.v2.model.org_group_policy_override_update_request import OrgGroupPolicyOverrideUpdateRequest
from datadog_api_client.v2.model.org_group_list_response import OrgGroupListResponse
from datadog_api_client.v2.model.org_group_sort_option import OrgGroupSortOption
from datadog_api_client.v2.model.org_group_include_option import OrgGroupIncludeOption
from datadog_api_client.v2.model.org_group_response import OrgGroupResponse
from datadog_api_client.v2.model.org_group_create_request import OrgGroupCreateRequest
from datadog_api_client.v2.model.org_group_update_request import OrgGroupUpdateRequest


class OrgGroupsApi:
    """
    Manage organization groups, memberships, policies, policy overrides, and policy configurations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._bulk_update_org_group_memberships_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupMembershipListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_memberships/bulk",
                "operation_id": "bulk_update_org_group_memberships",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupMembershipBulkUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_org_group_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_groups",
                "operation_id": "create_org_group",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_org_group_policy_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policies",
                "operation_id": "create_org_group_policy",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupPolicyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_org_group_policy_override_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyOverrideResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policy_overrides",
                "operation_id": "create_org_group_policy_override",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupPolicyOverrideCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_org_group_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_groups/{org_group_id}",
                "operation_id": "delete_org_group",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "org_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_org_group_policy_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policies/{org_group_policy_id}",
                "operation_id": "delete_org_group_policy",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "org_group_policy_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_policy_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_org_group_policy_override_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policy_overrides/{org_group_policy_override_id}",
                "operation_id": "delete_org_group_policy_override",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "org_group_policy_override_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_policy_override_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_org_group_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_groups/{org_group_id}",
                "operation_id": "get_org_group",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "org_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_org_group_membership_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupMembershipResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_memberships/{org_group_membership_id}",
                "operation_id": "get_org_group_membership",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "org_group_membership_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_membership_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_group_memberships_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupMembershipListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_memberships",
                "operation_id": "list_org_group_memberships",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_org_group_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[org_group_id]",
                    "location": "query",
                },
                "filter_org_uuid": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[org_uuid]",
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
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (OrgGroupMembershipSortOption,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_group_policies_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policies",
                "operation_id": "list_org_group_policies",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_org_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "filter[org_group_id]",
                    "location": "query",
                },
                "filter_policy_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[policy_name]",
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
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (OrgGroupPolicySortOption,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_group_policy_configs_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyConfigListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policy_configs",
                "operation_id": "list_org_group_policy_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_group_policy_overrides_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyOverrideListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policy_overrides",
                "operation_id": "list_org_group_policy_overrides",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_org_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "filter[org_group_id]",
                    "location": "query",
                },
                "filter_policy_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[policy_id]",
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
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (OrgGroupPolicyOverrideSortOption,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_groups_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_groups",
                "operation_id": "list_org_groups",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (OrgGroupSortOption,),
                    "attribute": "sort",
                    "location": "query",
                },
                "include": {
                    "openapi_types": ([OrgGroupIncludeOption],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_org_group_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_groups/{org_group_id}",
                "operation_id": "update_org_group",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_org_group_membership_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupMembershipResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_memberships/{org_group_membership_id}",
                "operation_id": "update_org_group_membership",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_group_membership_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_membership_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupMembershipUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_org_group_policy_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policies/{org_group_policy_id}",
                "operation_id": "update_org_group_policy",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_group_policy_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_policy_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupPolicyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_org_group_policy_override_endpoint = _Endpoint(
            settings={
                "response_type": (OrgGroupPolicyOverrideResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/org_group_policy_overrides/{org_group_policy_override_id}",
                "operation_id": "update_org_group_policy_override",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_group_policy_override_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "org_group_policy_override_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgGroupPolicyOverrideUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def bulk_update_org_group_memberships(
        self,
        body: OrgGroupMembershipBulkUpdateRequest,
    ) -> OrgGroupMembershipListResponse:
        """Bulk update org group memberships.

        Move a batch of organizations from one org group to another. This is an atomic operation. Maximum 100 orgs per request.

        :type body: OrgGroupMembershipBulkUpdateRequest
        :rtype: OrgGroupMembershipListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._bulk_update_org_group_memberships_endpoint.call_with_http_info(**kwargs)

    def create_org_group(
        self,
        body: OrgGroupCreateRequest,
    ) -> OrgGroupResponse:
        """Create an org group.

        Create a new organization group.

        :type body: OrgGroupCreateRequest
        :rtype: OrgGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_org_group_endpoint.call_with_http_info(**kwargs)

    def create_org_group_policy(
        self,
        body: OrgGroupPolicyCreateRequest,
    ) -> OrgGroupPolicyResponse:
        """Create an org group policy.

        Create a new policy for an organization group.

        :type body: OrgGroupPolicyCreateRequest
        :rtype: OrgGroupPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_org_group_policy_endpoint.call_with_http_info(**kwargs)

    def create_org_group_policy_override(
        self,
        body: OrgGroupPolicyOverrideCreateRequest,
    ) -> OrgGroupPolicyOverrideResponse:
        """Create an org group policy override.

        Create a new policy override for an organization within an org group.

        :type body: OrgGroupPolicyOverrideCreateRequest
        :rtype: OrgGroupPolicyOverrideResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_org_group_policy_override_endpoint.call_with_http_info(**kwargs)

    def delete_org_group(
        self,
        org_group_id: UUID,
    ) -> None:
        """Delete an org group.

        Delete an organization group by its ID.

        :param org_group_id: The ID of the org group.
        :type org_group_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_id"] = org_group_id

        return self._delete_org_group_endpoint.call_with_http_info(**kwargs)

    def delete_org_group_policy(
        self,
        org_group_policy_id: UUID,
    ) -> None:
        """Delete an org group policy.

        Delete an organization group policy by its ID.

        :param org_group_policy_id: The ID of the org group policy.
        :type org_group_policy_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_policy_id"] = org_group_policy_id

        return self._delete_org_group_policy_endpoint.call_with_http_info(**kwargs)

    def delete_org_group_policy_override(
        self,
        org_group_policy_override_id: UUID,
    ) -> None:
        """Delete an org group policy override.

        Delete an organization group policy override by its ID.

        :param org_group_policy_override_id: The ID of the org group policy override.
        :type org_group_policy_override_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_policy_override_id"] = org_group_policy_override_id

        return self._delete_org_group_policy_override_endpoint.call_with_http_info(**kwargs)

    def get_org_group(
        self,
        org_group_id: UUID,
    ) -> OrgGroupResponse:
        """Get an org group.

        Get a specific organization group by its ID.

        :param org_group_id: The ID of the org group.
        :type org_group_id: UUID
        :rtype: OrgGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_id"] = org_group_id

        return self._get_org_group_endpoint.call_with_http_info(**kwargs)

    def get_org_group_membership(
        self,
        org_group_membership_id: UUID,
    ) -> OrgGroupMembershipResponse:
        """Get an org group membership.

        Get a specific organization group membership by its ID.

        :param org_group_membership_id: The ID of the org group membership.
        :type org_group_membership_id: UUID
        :rtype: OrgGroupMembershipResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_membership_id"] = org_group_membership_id

        return self._get_org_group_membership_endpoint.call_with_http_info(**kwargs)

    def list_org_group_memberships(
        self,
        *,
        filter_org_group_id: Union[UUID, UnsetType] = unset,
        filter_org_uuid: Union[UUID, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[OrgGroupMembershipSortOption, UnsetType] = unset,
    ) -> OrgGroupMembershipListResponse:
        """List org group memberships.

        List organization group memberships. Filter by org group ID or org UUID. At least one of ``filter[org_group_id]`` or ``filter[org_uuid]`` must be provided. When filtering by org UUID, returns a single-item list with the membership for that org.

        :param filter_org_group_id: Filter memberships by org group ID. Required when ``filter[org_uuid]`` is not provided.
        :type filter_org_group_id: UUID, optional
        :param filter_org_uuid: Filter memberships by org UUID. Returns a single-item list.
        :type filter_org_uuid: UUID, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :param page_size: The number of items per page. Maximum is 1000.
        :type page_size: int, optional
        :param sort: Field to sort memberships by. Supported values: ``name`` , ``uuid`` , ``-name`` , ``-uuid``. Defaults to ``uuid``.
        :type sort: OrgGroupMembershipSortOption, optional
        :rtype: OrgGroupMembershipListResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_org_group_id is not unset:
            kwargs["filter_org_group_id"] = filter_org_group_id

        if filter_org_uuid is not unset:
            kwargs["filter_org_uuid"] = filter_org_uuid

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_org_group_memberships_endpoint.call_with_http_info(**kwargs)

    def list_org_group_policies(
        self,
        filter_org_group_id: UUID,
        *,
        filter_policy_name: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[OrgGroupPolicySortOption, UnsetType] = unset,
    ) -> OrgGroupPolicyListResponse:
        """List org group policies.

        List policies for an organization group. Requires a filter on org group ID.

        :param filter_org_group_id: Filter policies by org group ID.
        :type filter_org_group_id: UUID
        :param filter_policy_name: Filter policies by policy name.
        :type filter_policy_name: str, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :param page_size: The number of items per page. Maximum is 1000.
        :type page_size: int, optional
        :param sort: Field to sort policies by. Supported values: ``id`` , ``name`` , ``-id`` , ``-name``. Defaults to ``id``.
        :type sort: OrgGroupPolicySortOption, optional
        :rtype: OrgGroupPolicyListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_org_group_id"] = filter_org_group_id

        if filter_policy_name is not unset:
            kwargs["filter_policy_name"] = filter_policy_name

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_org_group_policies_endpoint.call_with_http_info(**kwargs)

    def list_org_group_policy_configs(
        self,
    ) -> OrgGroupPolicyConfigListResponse:
        """List org group policy configs.

        List all org configs that are eligible to be used as organization group policies.

        :rtype: OrgGroupPolicyConfigListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_org_group_policy_configs_endpoint.call_with_http_info(**kwargs)

    def list_org_group_policy_overrides(
        self,
        filter_org_group_id: UUID,
        *,
        filter_policy_id: Union[UUID, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[OrgGroupPolicyOverrideSortOption, UnsetType] = unset,
    ) -> OrgGroupPolicyOverrideListResponse:
        """List org group policy overrides.

        List policy overrides for an organization group. Requires a filter on org group ID. Optionally filter by policy ID.

        :param filter_org_group_id: Filter policy overrides by org group ID.
        :type filter_org_group_id: UUID
        :param filter_policy_id: Filter policy overrides by policy ID.
        :type filter_policy_id: UUID, optional
        :param page_number: The page number to return.
        :type page_number: int, optional
        :param page_size: The number of items per page. Maximum is 1000.
        :type page_size: int, optional
        :param sort: Field to sort overrides by. Supported values: ``id`` , ``org_uuid`` , ``-id`` , ``-org_uuid``. Defaults to ``id``.
        :type sort: OrgGroupPolicyOverrideSortOption, optional
        :rtype: OrgGroupPolicyOverrideListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_org_group_id"] = filter_org_group_id

        if filter_policy_id is not unset:
            kwargs["filter_policy_id"] = filter_policy_id

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_org_group_policy_overrides_endpoint.call_with_http_info(**kwargs)

    def list_org_groups(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[OrgGroupSortOption, UnsetType] = unset,
        include: Union[List[OrgGroupIncludeOption], UnsetType] = unset,
    ) -> OrgGroupListResponse:
        """List org groups.

        List all organization groups that the requesting organization has access to.

        :param page_number: The page number to return.
        :type page_number: int, optional
        :param page_size: The number of items per page. Maximum is 1000.
        :type page_size: int, optional
        :param sort: Field to sort org groups by. Supported values: ``name`` , ``uuid`` , ``-name`` , ``-uuid``. Defaults to ``uuid``.
        :type sort: OrgGroupSortOption, optional
        :param include: List of related resources to include.
        :type include: [OrgGroupIncludeOption], optional
        :rtype: OrgGroupListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort is not unset:
            kwargs["sort"] = sort

        if include is not unset:
            kwargs["include"] = include

        return self._list_org_groups_endpoint.call_with_http_info(**kwargs)

    def update_org_group(
        self,
        org_group_id: UUID,
        body: OrgGroupUpdateRequest,
    ) -> OrgGroupResponse:
        """Update an org group.

        Update the name of an existing organization group.

        :param org_group_id: The ID of the org group.
        :type org_group_id: UUID
        :type body: OrgGroupUpdateRequest
        :rtype: OrgGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_id"] = org_group_id

        kwargs["body"] = body

        return self._update_org_group_endpoint.call_with_http_info(**kwargs)

    def update_org_group_membership(
        self,
        org_group_membership_id: UUID,
        body: OrgGroupMembershipUpdateRequest,
    ) -> OrgGroupMembershipResponse:
        """Update an org group membership.

        Move an organization to a different org group by updating its membership.

        :param org_group_membership_id: The ID of the org group membership.
        :type org_group_membership_id: UUID
        :type body: OrgGroupMembershipUpdateRequest
        :rtype: OrgGroupMembershipResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_membership_id"] = org_group_membership_id

        kwargs["body"] = body

        return self._update_org_group_membership_endpoint.call_with_http_info(**kwargs)

    def update_org_group_policy(
        self,
        org_group_policy_id: UUID,
        body: OrgGroupPolicyUpdateRequest,
    ) -> OrgGroupPolicyResponse:
        """Update an org group policy.

        Update the content of an existing organization group policy.

        :param org_group_policy_id: The ID of the org group policy.
        :type org_group_policy_id: UUID
        :type body: OrgGroupPolicyUpdateRequest
        :rtype: OrgGroupPolicyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_policy_id"] = org_group_policy_id

        kwargs["body"] = body

        return self._update_org_group_policy_endpoint.call_with_http_info(**kwargs)

    def update_org_group_policy_override(
        self,
        org_group_policy_override_id: UUID,
        body: OrgGroupPolicyOverrideUpdateRequest,
    ) -> OrgGroupPolicyOverrideResponse:
        """Update an org group policy override.

        Update an existing organization group policy override.

        :param org_group_policy_override_id: The ID of the org group policy override.
        :type org_group_policy_override_id: UUID
        :type body: OrgGroupPolicyOverrideUpdateRequest
        :rtype: OrgGroupPolicyOverrideResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_group_policy_override_id"] = org_group_policy_override_id

        kwargs["body"] = body

        return self._update_org_group_policy_override_endpoint.call_with_http_info(**kwargs)
