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
from datadog_api_client.v2.model.restriction_query_list_response import RestrictionQueryListResponse
from datadog_api_client.v2.model.restriction_query_without_relationships_response import (
    RestrictionQueryWithoutRelationshipsResponse,
)
from datadog_api_client.v2.model.restriction_query_create_payload import RestrictionQueryCreatePayload
from datadog_api_client.v2.model.restriction_query_with_relationships_response import (
    RestrictionQueryWithRelationshipsResponse,
)
from datadog_api_client.v2.model.restriction_query_update_payload import RestrictionQueryUpdatePayload
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.restriction_query_roles_response import RestrictionQueryRolesResponse


class LogsRestrictionQueriesApi:
    """
    Note: This endpoint is in public beta. If you have any feedback, contact `Datadog support <https://docs.datadoghq.com/help/>`_.

    A Restriction Query is a logs query that restricts which logs the ``logs_read_data`` permission grants read access to.
    For users whose roles have Restriction Queries, any log query they make only returns those log events that also match
    one of their Restriction Queries. This is true whether the user queries log events from any log-related feature, including
    the log explorer, Live Tail, re-hydration, or a dashboard widget.

    Restriction Queries currently only support use of the following components of log events:

    * Reserved attributes
    * The log message
    * Tags

    To restrict read access on log data, add a team tag to log events to indicate which teams own them, and then scope Restriction Queries to the relevant values of the team tag. Tags can be applied to log events in many ways, and a log event can have multiple tags with the same key (like team) and different values. This means the same log event can be visible to roles whose restriction queries are scoped to different team values.

    See `How to Set Up RBAC for Logs <https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=api#restrict-access-to-logs>`_ for details on how to add restriction queries.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._add_role_to_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles",
                "operation_id": "add_role_to_restriction_query",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToRole,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryWithoutRelationshipsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries",
                "operation_id": "create_restriction_query",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RestrictionQueryCreatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}",
                "operation_id": "delete_restriction_query",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryWithRelationshipsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}",
                "operation_id": "get_restriction_query",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_role_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/role/{role_id}",
                "operation_id": "get_role_restriction_query",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "role_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "role_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_restriction_queries_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries",
                "operation_id": "list_restriction_queries",
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

        self._list_restriction_query_roles_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryRolesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles",
                "operation_id": "list_restriction_query_roles",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
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

        self._list_user_restriction_queries_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/user/{user_id}",
                "operation_id": "list_user_restriction_queries",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._remove_role_from_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}/roles",
                "operation_id": "remove_role_from_restriction_query",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RelationshipToRole,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._replace_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryWithoutRelationshipsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}",
                "operation_id": "replace_restriction_query",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RestrictionQueryUpdatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_restriction_query_endpoint = _Endpoint(
            settings={
                "response_type": (RestrictionQueryWithoutRelationshipsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/restriction_queries/{restriction_query_id}",
                "operation_id": "update_restriction_query",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "restriction_query_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "restriction_query_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RestrictionQueryUpdatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_role_to_restriction_query(
        self,
        restriction_query_id: str,
        body: RelationshipToRole,
    ) -> None:
        """Grant role to a restriction query.

        Adds a role to a restriction query.

        **Note** : This operation automatically grants the ``logs_read_data`` permission to the role if it doesn't already have it.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :type body: RelationshipToRole
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        kwargs["body"] = body

        return self._add_role_to_restriction_query_endpoint.call_with_http_info(**kwargs)

    def create_restriction_query(
        self,
        body: RestrictionQueryCreatePayload,
    ) -> RestrictionQueryWithoutRelationshipsResponse:
        """Create a restriction query.

        Create a new restriction query for your organization.

        :type body: RestrictionQueryCreatePayload
        :rtype: RestrictionQueryWithoutRelationshipsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_restriction_query_endpoint.call_with_http_info(**kwargs)

    def delete_restriction_query(
        self,
        restriction_query_id: str,
    ) -> None:
        """Delete a restriction query.

        Deletes a restriction query.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        return self._delete_restriction_query_endpoint.call_with_http_info(**kwargs)

    def get_restriction_query(
        self,
        restriction_query_id: str,
    ) -> RestrictionQueryWithRelationshipsResponse:
        """Get a restriction query.

        Get a restriction query in the organization specified by the restriction query's ``restriction_query_id``.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :rtype: RestrictionQueryWithRelationshipsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        return self._get_restriction_query_endpoint.call_with_http_info(**kwargs)

    def get_role_restriction_query(
        self,
        role_id: str,
    ) -> RestrictionQueryListResponse:
        """Get restriction query for a given role.

        Get restriction query for a given role.

        :param role_id: The ID of the role.
        :type role_id: str
        :rtype: RestrictionQueryListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["role_id"] = role_id

        return self._get_role_restriction_query_endpoint.call_with_http_info(**kwargs)

    def list_restriction_queries(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> RestrictionQueryListResponse:
        """List restriction queries.

        Returns all restriction queries, including their names and IDs.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: RestrictionQueryListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_restriction_queries_endpoint.call_with_http_info(**kwargs)

    def list_restriction_query_roles(
        self,
        restriction_query_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> RestrictionQueryRolesResponse:
        """List roles for a restriction query.

        Returns all roles that have a given restriction query.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: RestrictionQueryRolesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_restriction_query_roles_endpoint.call_with_http_info(**kwargs)

    def list_user_restriction_queries(
        self,
        user_id: str,
    ) -> RestrictionQueryListResponse:
        """Get all restriction queries for a given user.

        Get all restriction queries for a given user.

        :param user_id: The ID of the user.
        :type user_id: str
        :rtype: RestrictionQueryListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_id"] = user_id

        return self._list_user_restriction_queries_endpoint.call_with_http_info(**kwargs)

    def remove_role_from_restriction_query(
        self,
        restriction_query_id: str,
        body: RelationshipToRole,
    ) -> None:
        """Revoke role from a restriction query.

        Removes a role from a restriction query.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :type body: RelationshipToRole
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        kwargs["body"] = body

        return self._remove_role_from_restriction_query_endpoint.call_with_http_info(**kwargs)

    def replace_restriction_query(
        self,
        restriction_query_id: str,
        body: RestrictionQueryUpdatePayload,
    ) -> RestrictionQueryWithoutRelationshipsResponse:
        """Replace a restriction query.

        Replace a restriction query.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :type body: RestrictionQueryUpdatePayload
        :rtype: RestrictionQueryWithoutRelationshipsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        kwargs["body"] = body

        return self._replace_restriction_query_endpoint.call_with_http_info(**kwargs)

    def update_restriction_query(
        self,
        restriction_query_id: str,
        body: RestrictionQueryUpdatePayload,
    ) -> RestrictionQueryWithoutRelationshipsResponse:
        """Update a restriction query.

        Edit a restriction query.

        :param restriction_query_id: The ID of the restriction query.
        :type restriction_query_id: str
        :type body: RestrictionQueryUpdatePayload
        :rtype: RestrictionQueryWithoutRelationshipsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["restriction_query_id"] = restriction_query_id

        kwargs["body"] = body

        return self._update_restriction_query_endpoint.call_with_http_info(**kwargs)
