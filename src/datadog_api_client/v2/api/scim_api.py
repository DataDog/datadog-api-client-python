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
from datadog_api_client.v2.model.list_external_user_group_response import ListExternalUserGroupResponse
from datadog_api_client.v2.model.external_user_group import ExternalUserGroup
from datadog_api_client.v2.model.external_user_group_patch_request import ExternalUserGroupPatchRequest


class ScimApi:
    """
    Provision Datadog teams using SCIM group APIs.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_scim_group_endpoint = _Endpoint(
            settings={
                "response_type": (ExternalUserGroup,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scim/Groups",
                "operation_id": "create_scim_group",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "openapi_types": (ExternalUserGroup,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_scim_group_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scim/Groups/{group_id}",
                "operation_id": "delete_scim_group",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "group_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "group_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_scim_group_endpoint = _Endpoint(
            settings={
                "response_type": (ExternalUserGroup,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scim/Groups/{group_id}",
                "operation_id": "get_scim_group",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "group_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "group_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scim_groups_endpoint = _Endpoint(
            settings={
                "response_type": (ListExternalUserGroupResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scim/Groups",
                "operation_id": "list_scim_groups",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "start_index": {
                    "openapi_types": (int,),
                    "attribute": "startIndex",
                    "location": "query",
                },
                "count": {
                    "openapi_types": (int,),
                    "attribute": "count",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._patch_scim_group_endpoint = _Endpoint(
            settings={
                "response_type": (ExternalUserGroup,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scim/Groups/{group_id}",
                "operation_id": "patch_scim_group",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "group_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "group_id",
                    "location": "path",
                },
                "body": {
                    "openapi_types": (ExternalUserGroupPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_scim_group_endpoint = _Endpoint(
            settings={
                "response_type": (ExternalUserGroup,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scim/Groups/{group_id}",
                "operation_id": "update_scim_group",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "group_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "group_id",
                    "location": "path",
                },
                "body": {
                    "openapi_types": (ExternalUserGroup,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_scim_group(
        self,
        *,
        body: Union[ExternalUserGroup, UnsetType] = unset,
    ) -> ExternalUserGroup:
        """Create SCIM group.

        :type body: ExternalUserGroup, optional
        :rtype: ExternalUserGroup
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._create_scim_group_endpoint.call_with_http_info(**kwargs)

    def delete_scim_group(
        self,
        group_id: str,
    ) -> None:
        """Delete SCIM group.

        :type group_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["group_id"] = group_id

        return self._delete_scim_group_endpoint.call_with_http_info(**kwargs)

    def get_scim_group(
        self,
        group_id: str,
    ) -> ExternalUserGroup:
        """Get SCIM group.

        :type group_id: str
        :rtype: ExternalUserGroup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["group_id"] = group_id

        return self._get_scim_group_endpoint.call_with_http_info(**kwargs)

    def list_scim_groups(
        self,
        *,
        start_index: Union[int, UnsetType] = unset,
        count: Union[int, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
    ) -> ListExternalUserGroupResponse:
        """List SCIM groups.

        List SCIM groups in the organization.
        Results are paginated by ``startIndex`` and ``count`` parameters.
        Results can be narrowed down by the ``filter`` parameter.

        :param start_index: Specifies the start index to fetch the results (1-indexed).
        :type start_index: int, optional
        :param count: Specifies the number of groups to be returned.
        :type count: int, optional
        :param filter: Specifies the url encoded filter to use to narrow down the results.
            Filters can be in the form of ``displayName eq <group name>`` or ``externalId eq <external id of group>``
            or ``id eq <group id> and members eq <user uuid>`` or ``members eq <user uuid> and id eq <group id>``.
        :type filter: str, optional
        :rtype: ListExternalUserGroupResponse
        """
        kwargs: Dict[str, Any] = {}
        if start_index is not unset:
            kwargs["start_index"] = start_index

        if count is not unset:
            kwargs["count"] = count

        if filter is not unset:
            kwargs["filter"] = filter

        return self._list_scim_groups_endpoint.call_with_http_info(**kwargs)

    def patch_scim_group(
        self,
        group_id: str,
        *,
        body: Union[ExternalUserGroupPatchRequest, UnsetType] = unset,
    ) -> ExternalUserGroup:
        """Patch SCIM group.

        :type group_id: str
        :type body: ExternalUserGroupPatchRequest, optional
        :rtype: ExternalUserGroup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["group_id"] = group_id

        if body is not unset:
            kwargs["body"] = body

        return self._patch_scim_group_endpoint.call_with_http_info(**kwargs)

    def update_scim_group(
        self,
        group_id: str,
        *,
        body: Union[ExternalUserGroup, UnsetType] = unset,
    ) -> ExternalUserGroup:
        """Update SCIM group.

        :type group_id: str
        :type body: ExternalUserGroup, optional
        :rtype: ExternalUserGroup
        """
        kwargs: Dict[str, Any] = {}
        kwargs["group_id"] = group_id

        if body is not unset:
            kwargs["body"] = body

        return self._update_scim_group_endpoint.call_with_http_info(**kwargs)
