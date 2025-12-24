# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union
import warnings

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.teams_response import TeamsResponse
from datadog_api_client.v2.model.list_teams_sort import ListTeamsSort
from datadog_api_client.v2.model.list_teams_include import ListTeamsInclude
from datadog_api_client.v2.model.teams_field import TeamsField
from datadog_api_client.v2.model.team import Team
from datadog_api_client.v2.model.team_response import TeamResponse
from datadog_api_client.v2.model.team_create_request import TeamCreateRequest
from datadog_api_client.v2.model.team_hierarchy_links_response import TeamHierarchyLinksResponse
from datadog_api_client.v2.model.team_hierarchy_link import TeamHierarchyLink
from datadog_api_client.v2.model.team_hierarchy_link_response import TeamHierarchyLinkResponse
from datadog_api_client.v2.model.team_hierarchy_link_create_request import TeamHierarchyLinkCreateRequest
from datadog_api_client.v2.model.team_connection_delete_request import TeamConnectionDeleteRequest
from datadog_api_client.v2.model.team_connections_response import TeamConnectionsResponse
from datadog_api_client.v2.model.team_connection import TeamConnection
from datadog_api_client.v2.model.team_connection_create_request import TeamConnectionCreateRequest
from datadog_api_client.v2.model.team_sync_response import TeamSyncResponse
from datadog_api_client.v2.model.team_sync_attributes_source import TeamSyncAttributesSource
from datadog_api_client.v2.model.team_sync_request import TeamSyncRequest
from datadog_api_client.v2.model.add_member_team_request import AddMemberTeamRequest
from datadog_api_client.v2.model.team_update_request import TeamUpdateRequest
from datadog_api_client.v2.model.team_links_response import TeamLinksResponse
from datadog_api_client.v2.model.team_link_response import TeamLinkResponse
from datadog_api_client.v2.model.team_link_create_request import TeamLinkCreateRequest
from datadog_api_client.v2.model.user_teams_response import UserTeamsResponse
from datadog_api_client.v2.model.get_team_memberships_sort import GetTeamMembershipsSort
from datadog_api_client.v2.model.user_team import UserTeam
from datadog_api_client.v2.model.user_team_response import UserTeamResponse
from datadog_api_client.v2.model.user_team_request import UserTeamRequest
from datadog_api_client.v2.model.user_team_update_request import UserTeamUpdateRequest
from datadog_api_client.v2.model.team_notification_rules_response import TeamNotificationRulesResponse
from datadog_api_client.v2.model.team_notification_rule_response import TeamNotificationRuleResponse
from datadog_api_client.v2.model.team_notification_rule_request import TeamNotificationRuleRequest
from datadog_api_client.v2.model.team_permission_settings_response import TeamPermissionSettingsResponse
from datadog_api_client.v2.model.team_permission_setting_response import TeamPermissionSettingResponse
from datadog_api_client.v2.model.team_permission_setting_update_request import TeamPermissionSettingUpdateRequest


class TeamsApi:
    """
    View and manage teams within Datadog. See the `Teams page <https://docs.datadoghq.com/account_management/teams/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._add_member_team_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{super_team_id}/member_teams",
                "operation_id": "add_member_team",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "super_team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "super_team_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AddMemberTeamRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._add_team_hierarchy_link_endpoint = _Endpoint(
            settings={
                "response_type": (TeamHierarchyLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team-hierarchy-links",
                "operation_id": "add_team_hierarchy_link",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamHierarchyLinkCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_team_endpoint = _Endpoint(
            settings={
                "response_type": (TeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team",
                "operation_id": "create_team",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_team_connections_endpoint = _Endpoint(
            settings={
                "response_type": (TeamConnectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/connections",
                "operation_id": "create_team_connections",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamConnectionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_team_link_endpoint = _Endpoint(
            settings={
                "response_type": (TeamLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/links",
                "operation_id": "create_team_link",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamLinkCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_team_membership_endpoint = _Endpoint(
            settings={
                "response_type": (UserTeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/memberships",
                "operation_id": "create_team_membership",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UserTeamRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_team_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (TeamNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/notification-rules",
                "operation_id": "create_team_notification_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamNotificationRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_team_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}",
                "operation_id": "delete_team",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_team_connections_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/connections",
                "operation_id": "delete_team_connections",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamConnectionDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_team_link_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/links/{link_id}",
                "operation_id": "delete_team_link",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "link_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "link_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_team_membership_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/memberships/{user_id}",
                "operation_id": "delete_team_membership",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_team_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/notification-rules/{rule_id}",
                "operation_id": "delete_team_notification_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
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

        self._get_team_endpoint = _Endpoint(
            settings={
                "response_type": (TeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}",
                "operation_id": "get_team",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_hierarchy_link_endpoint = _Endpoint(
            settings={
                "response_type": (TeamHierarchyLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team-hierarchy-links/{link_id}",
                "operation_id": "get_team_hierarchy_link",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "link_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "link_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_link_endpoint = _Endpoint(
            settings={
                "response_type": (TeamLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/links/{link_id}",
                "operation_id": "get_team_link",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "link_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "link_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_links_endpoint = _Endpoint(
            settings={
                "response_type": (TeamLinksResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/links",
                "operation_id": "get_team_links",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_memberships_endpoint = _Endpoint(
            settings={
                "response_type": (UserTeamsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/memberships",
                "operation_id": "get_team_memberships",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
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
                "sort": {
                    "openapi_types": (GetTeamMembershipsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter_keyword": {
                    "openapi_types": (str,),
                    "attribute": "filter[keyword]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (TeamNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/notification-rules/{rule_id}",
                "operation_id": "get_team_notification_rule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_notification_rules_endpoint = _Endpoint(
            settings={
                "response_type": (TeamNotificationRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/notification-rules",
                "operation_id": "get_team_notification_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_permission_settings_endpoint = _Endpoint(
            settings={
                "response_type": (TeamPermissionSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/permission-settings",
                "operation_id": "get_team_permission_settings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_team_sync_endpoint = _Endpoint(
            settings={
                "response_type": (TeamSyncResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/sync",
                "operation_id": "get_team_sync",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_source": {
                    "required": True,
                    "openapi_types": (TeamSyncAttributesSource,),
                    "attribute": "filter[source]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_user_memberships_endpoint = _Endpoint(
            settings={
                "response_type": (UserTeamsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/users/{user_uuid}/memberships",
                "operation_id": "get_user_memberships",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "user_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_member_teams_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{super_team_id}/member_teams",
                "operation_id": "list_member_teams",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "super_team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "super_team_id",
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
                "fields_team": {
                    "openapi_types": ([TeamsField],),
                    "attribute": "fields[team]",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_team_connections_endpoint = _Endpoint(
            settings={
                "response_type": (TeamConnectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/connections",
                "operation_id": "list_team_connections",
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
                "filter_sources": {
                    "openapi_types": ([str],),
                    "attribute": "filter[sources]",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_team_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[team_ids]",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_connected_team_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[connected_team_ids]",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_connection_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[connection_ids]",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_team_hierarchy_links_endpoint = _Endpoint(
            settings={
                "response_type": (TeamHierarchyLinksResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team-hierarchy-links",
                "operation_id": "list_team_hierarchy_links",
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
                "filter_parent_team": {
                    "openapi_types": (str,),
                    "attribute": "filter[parent_team]",
                    "location": "query",
                },
                "filter_sub_team": {
                    "openapi_types": (str,),
                    "attribute": "filter[sub_team]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_teams_endpoint = _Endpoint(
            settings={
                "response_type": (TeamsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team",
                "operation_id": "list_teams",
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
                "sort": {
                    "openapi_types": (ListTeamsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "include": {
                    "openapi_types": ([ListTeamsInclude],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_keyword": {
                    "openapi_types": (str,),
                    "attribute": "filter[keyword]",
                    "location": "query",
                },
                "filter_me": {
                    "openapi_types": (bool,),
                    "attribute": "filter[me]",
                    "location": "query",
                },
                "fields_team": {
                    "openapi_types": ([TeamsField],),
                    "attribute": "fields[team]",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._remove_member_team_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{super_team_id}/member_teams/{member_team_id}",
                "operation_id": "remove_member_team",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "super_team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "super_team_id",
                    "location": "path",
                },
                "member_team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "member_team_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._remove_team_hierarchy_link_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team-hierarchy-links/{link_id}",
                "operation_id": "remove_team_hierarchy_link",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "link_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "link_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._sync_teams_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/sync",
                "operation_id": "sync_teams",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamSyncRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_team_endpoint = _Endpoint(
            settings={
                "response_type": (TeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}",
                "operation_id": "update_team",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_team_link_endpoint = _Endpoint(
            settings={
                "response_type": (TeamLinkResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/links/{link_id}",
                "operation_id": "update_team_link",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "link_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "link_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamLinkCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_team_membership_endpoint = _Endpoint(
            settings={
                "response_type": (UserTeamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/memberships/{user_id}",
                "operation_id": "update_team_membership",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UserTeamUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_team_notification_rule_endpoint = _Endpoint(
            settings={
                "response_type": (TeamNotificationRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/notification-rules/{rule_id}",
                "operation_id": "update_team_notification_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamNotificationRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_team_permission_setting_endpoint = _Endpoint(
            settings={
                "response_type": (TeamPermissionSettingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/{team_id}/permission-settings/{action}",
                "operation_id": "update_team_permission_setting",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "team_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "team_id",
                    "location": "path",
                },
                "action": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "action",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TeamPermissionSettingUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def add_member_team(
        self,
        super_team_id: str,
        body: AddMemberTeamRequest,
    ) -> None:
        """Add a member team. **Deprecated**.

        Add a member team.
        Adds the team given by the ``id`` in the body as a member team of the super team.

        **Note** : This API is deprecated. For creating team hierarchy links, use the team hierarchy links API: ``POST /api/v2/team-hierarchy-links``.

        :param super_team_id: None
        :type super_team_id: str
        :type body: AddMemberTeamRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["super_team_id"] = super_team_id

        kwargs["body"] = body

        warnings.warn("add_member_team is deprecated", DeprecationWarning, stacklevel=2)
        return self._add_member_team_endpoint.call_with_http_info(**kwargs)

    def add_team_hierarchy_link(
        self,
        body: TeamHierarchyLinkCreateRequest,
    ) -> TeamHierarchyLinkResponse:
        """Create a team hierarchy link.

        Create a new team hierarchy link between a parent team and a sub team.

        :type body: TeamHierarchyLinkCreateRequest
        :rtype: TeamHierarchyLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._add_team_hierarchy_link_endpoint.call_with_http_info(**kwargs)

    def create_team(
        self,
        body: TeamCreateRequest,
    ) -> TeamResponse:
        """Create a team.

        Create a new team.
        User IDs passed through the ``users`` relationship field are added to the team.

        :type body: TeamCreateRequest
        :rtype: TeamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_team_endpoint.call_with_http_info(**kwargs)

    def create_team_connections(
        self,
        body: TeamConnectionCreateRequest,
    ) -> TeamConnectionsResponse:
        """Create team connections.

        Create multiple team connections.

        :type body: TeamConnectionCreateRequest
        :rtype: TeamConnectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_team_connections_endpoint.call_with_http_info(**kwargs)

    def create_team_link(
        self,
        team_id: str,
        body: TeamLinkCreateRequest,
    ) -> TeamLinkResponse:
        """Create a team link.

        Add a new link to a team.

        :param team_id: None
        :type team_id: str
        :type body: TeamLinkCreateRequest
        :rtype: TeamLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["body"] = body

        return self._create_team_link_endpoint.call_with_http_info(**kwargs)

    def create_team_membership(
        self,
        team_id: str,
        body: UserTeamRequest,
    ) -> UserTeamResponse:
        """Add a user to a team.

        Add a user to a team.

        **Note** : Each team has a setting that determines who is allowed to modify membership of the team. The ``user_access_manage`` permission generally grants access to modify membership of any team. To get the full picture, see `Team Membership documentation <https://docs.datadoghq.com/account_management/teams/manage/#team-membership>`_.

        :param team_id: None
        :type team_id: str
        :type body: UserTeamRequest
        :rtype: UserTeamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["body"] = body

        return self._create_team_membership_endpoint.call_with_http_info(**kwargs)

    def create_team_notification_rule(
        self,
        team_id: str,
        body: TeamNotificationRuleRequest,
    ) -> TeamNotificationRuleResponse:
        """Create team notification rule.

        :param team_id: None
        :type team_id: str
        :type body: TeamNotificationRuleRequest
        :rtype: TeamNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["body"] = body

        return self._create_team_notification_rule_endpoint.call_with_http_info(**kwargs)

    def delete_team(
        self,
        team_id: str,
    ) -> None:
        """Remove a team.

        Remove a team using the team's ``id``.

        :param team_id: None
        :type team_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        return self._delete_team_endpoint.call_with_http_info(**kwargs)

    def delete_team_connections(
        self,
        body: TeamConnectionDeleteRequest,
    ) -> None:
        """Delete team connections.

        Delete multiple team connections.

        :type body: TeamConnectionDeleteRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_team_connections_endpoint.call_with_http_info(**kwargs)

    def delete_team_link(
        self,
        team_id: str,
        link_id: str,
    ) -> None:
        """Remove a team link.

        Remove a link from a team.

        :param team_id: None
        :type team_id: str
        :param link_id: None
        :type link_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["link_id"] = link_id

        return self._delete_team_link_endpoint.call_with_http_info(**kwargs)

    def delete_team_membership(
        self,
        team_id: str,
        user_id: str,
    ) -> None:
        """Remove a user from a team.

        Remove a user from a team.

        **Note** : Each team has a setting that determines who is allowed to modify membership of the team. The ``user_access_manage`` permission generally grants access to modify membership of any team. To get the full picture, see `Team Membership documentation <https://docs.datadoghq.com/account_management/teams/manage/#team-membership>`_.

        :param team_id: None
        :type team_id: str
        :param user_id: None
        :type user_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["user_id"] = user_id

        return self._delete_team_membership_endpoint.call_with_http_info(**kwargs)

    def delete_team_notification_rule(
        self,
        team_id: str,
        rule_id: str,
    ) -> None:
        """Delete team notification rule.

        :param team_id: None
        :type team_id: str
        :param rule_id: None
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["rule_id"] = rule_id

        return self._delete_team_notification_rule_endpoint.call_with_http_info(**kwargs)

    def get_team(
        self,
        team_id: str,
    ) -> TeamResponse:
        """Get a team.

        Get a single team using the team's ``id``.

        :param team_id: None
        :type team_id: str
        :rtype: TeamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        return self._get_team_endpoint.call_with_http_info(**kwargs)

    def get_team_hierarchy_link(
        self,
        link_id: str,
    ) -> TeamHierarchyLinkResponse:
        """Get a team hierarchy link.

        Get a single team hierarchy link for the given link_id.

        :param link_id: The team hierarchy link's identifier
        :type link_id: str
        :rtype: TeamHierarchyLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["link_id"] = link_id

        return self._get_team_hierarchy_link_endpoint.call_with_http_info(**kwargs)

    def get_team_link(
        self,
        team_id: str,
        link_id: str,
    ) -> TeamLinkResponse:
        """Get a team link.

        Get a single link for a team.

        :param team_id: None
        :type team_id: str
        :param link_id: None
        :type link_id: str
        :rtype: TeamLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["link_id"] = link_id

        return self._get_team_link_endpoint.call_with_http_info(**kwargs)

    def get_team_links(
        self,
        team_id: str,
    ) -> TeamLinksResponse:
        """Get links for a team.

        Get all links for a given team.

        :param team_id: None
        :type team_id: str
        :rtype: TeamLinksResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        return self._get_team_links_endpoint.call_with_http_info(**kwargs)

    def get_team_memberships(
        self,
        team_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[GetTeamMembershipsSort, UnsetType] = unset,
        filter_keyword: Union[str, UnsetType] = unset,
    ) -> UserTeamsResponse:
        """Get team memberships.

        Get a paginated list of members for a team

        :param team_id: None
        :type team_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Specifies the order of returned team memberships
        :type sort: GetTeamMembershipsSort, optional
        :param filter_keyword: Search query, can be user email or name
        :type filter_keyword: str, optional
        :rtype: UserTeamsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_keyword is not unset:
            kwargs["filter_keyword"] = filter_keyword

        return self._get_team_memberships_endpoint.call_with_http_info(**kwargs)

    def get_team_memberships_with_pagination(
        self,
        team_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[GetTeamMembershipsSort, UnsetType] = unset,
        filter_keyword: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[UserTeam]:
        """Get team memberships.

        Provide a paginated version of :meth:`get_team_memberships`, returning all items.

        :param team_id: None
        :type team_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Specifies the order of returned team memberships
        :type sort: GetTeamMembershipsSort, optional
        :param filter_keyword: Search query, can be user email or name
        :type filter_keyword: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[UserTeam]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_keyword is not unset:
            kwargs["filter_keyword"] = filter_keyword

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._get_team_memberships_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def get_team_notification_rule(
        self,
        team_id: str,
        rule_id: str,
    ) -> TeamNotificationRuleResponse:
        """Get team notification rule.

        :param team_id: None
        :type team_id: str
        :param rule_id: None
        :type rule_id: str
        :rtype: TeamNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["rule_id"] = rule_id

        return self._get_team_notification_rule_endpoint.call_with_http_info(**kwargs)

    def get_team_notification_rules(
        self,
        team_id: str,
    ) -> TeamNotificationRulesResponse:
        """Get team notification rules.

        :param team_id: None
        :type team_id: str
        :rtype: TeamNotificationRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        return self._get_team_notification_rules_endpoint.call_with_http_info(**kwargs)

    def get_team_permission_settings(
        self,
        team_id: str,
    ) -> TeamPermissionSettingsResponse:
        """Get permission settings for a team.

        Get all permission settings for a given team.

        :param team_id: None
        :type team_id: str
        :rtype: TeamPermissionSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        return self._get_team_permission_settings_endpoint.call_with_http_info(**kwargs)

    def get_team_sync(
        self,
        filter_source: TeamSyncAttributesSource,
    ) -> TeamSyncResponse:
        """Get team sync configurations.

        Get all team synchronization configurations.
        Returns a list of configurations used for linking or provisioning teams with external sources like GitHub.

        :param filter_source: Filter by the external source platform for team synchronization
        :type filter_source: TeamSyncAttributesSource
        :rtype: TeamSyncResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_source"] = filter_source

        return self._get_team_sync_endpoint.call_with_http_info(**kwargs)

    def get_user_memberships(
        self,
        user_uuid: str,
    ) -> UserTeamsResponse:
        """Get user memberships.

        Get a list of memberships for a user

        :param user_uuid: None
        :type user_uuid: str
        :rtype: UserTeamsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_uuid"] = user_uuid

        return self._get_user_memberships_endpoint.call_with_http_info(**kwargs)

    def list_member_teams(
        self,
        super_team_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        fields_team: Union[List[TeamsField], UnsetType] = unset,
    ) -> TeamsResponse:
        """Get all member teams. **Deprecated**.

        Get all member teams.

        **Note** : This API is deprecated. For team hierarchy relationships (parent-child
        teams), use the team hierarchy links API: ``GET /api/v2/team-hierarchy-links``.

        :param super_team_id: None
        :type super_team_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param fields_team: List of fields that need to be fetched.
        :type fields_team: [TeamsField], optional
        :rtype: TeamsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["super_team_id"] = super_team_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if fields_team is not unset:
            kwargs["fields_team"] = fields_team

        warnings.warn("list_member_teams is deprecated", DeprecationWarning, stacklevel=2)
        return self._list_member_teams_endpoint.call_with_http_info(**kwargs)

    def list_member_teams_with_pagination(
        self,
        super_team_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        fields_team: Union[List[TeamsField], UnsetType] = unset,
    ) -> collections.abc.Iterable[Team]:
        """Get all member teams.

        Provide a paginated version of :meth:`list_member_teams`, returning all items.

        :param super_team_id: None
        :type super_team_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param fields_team: List of fields that need to be fetched.
        :type fields_team: [TeamsField], optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Team]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["super_team_id"] = super_team_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if fields_team is not unset:
            kwargs["fields_team"] = fields_team

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_member_teams_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_team_connections(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_sources: Union[List[str], UnsetType] = unset,
        filter_team_ids: Union[List[str], UnsetType] = unset,
        filter_connected_team_ids: Union[List[str], UnsetType] = unset,
        filter_connection_ids: Union[List[str], UnsetType] = unset,
    ) -> TeamConnectionsResponse:
        """List team connections.

        Returns all team connections.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param filter_sources: Filter team connections by external source systems.
        :type filter_sources: [str], optional
        :param filter_team_ids: Filter team connections by Datadog team IDs.
        :type filter_team_ids: [str], optional
        :param filter_connected_team_ids: Filter team connections by connected team IDs from external systems.
        :type filter_connected_team_ids: [str], optional
        :param filter_connection_ids: Filter team connections by connection IDs.
        :type filter_connection_ids: [str], optional
        :rtype: TeamConnectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_sources is not unset:
            kwargs["filter_sources"] = filter_sources

        if filter_team_ids is not unset:
            kwargs["filter_team_ids"] = filter_team_ids

        if filter_connected_team_ids is not unset:
            kwargs["filter_connected_team_ids"] = filter_connected_team_ids

        if filter_connection_ids is not unset:
            kwargs["filter_connection_ids"] = filter_connection_ids

        return self._list_team_connections_endpoint.call_with_http_info(**kwargs)

    def list_team_connections_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_sources: Union[List[str], UnsetType] = unset,
        filter_team_ids: Union[List[str], UnsetType] = unset,
        filter_connected_team_ids: Union[List[str], UnsetType] = unset,
        filter_connection_ids: Union[List[str], UnsetType] = unset,
    ) -> collections.abc.Iterable[TeamConnection]:
        """List team connections.

        Provide a paginated version of :meth:`list_team_connections`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param filter_sources: Filter team connections by external source systems.
        :type filter_sources: [str], optional
        :param filter_team_ids: Filter team connections by Datadog team IDs.
        :type filter_team_ids: [str], optional
        :param filter_connected_team_ids: Filter team connections by connected team IDs from external systems.
        :type filter_connected_team_ids: [str], optional
        :param filter_connection_ids: Filter team connections by connection IDs.
        :type filter_connection_ids: [str], optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[TeamConnection]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_sources is not unset:
            kwargs["filter_sources"] = filter_sources

        if filter_team_ids is not unset:
            kwargs["filter_team_ids"] = filter_team_ids

        if filter_connected_team_ids is not unset:
            kwargs["filter_connected_team_ids"] = filter_connected_team_ids

        if filter_connection_ids is not unset:
            kwargs["filter_connection_ids"] = filter_connection_ids

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_team_connections_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_team_hierarchy_links(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        filter_parent_team: Union[str, UnsetType] = unset,
        filter_sub_team: Union[str, UnsetType] = unset,
    ) -> TeamHierarchyLinksResponse:
        """Get team hierarchy links.

        List all team hierarchy links that match the provided filters.

        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param filter_parent_team: Filter by parent team ID
        :type filter_parent_team: str, optional
        :param filter_sub_team: Filter by sub team ID
        :type filter_sub_team: str, optional
        :rtype: TeamHierarchyLinksResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if filter_parent_team is not unset:
            kwargs["filter_parent_team"] = filter_parent_team

        if filter_sub_team is not unset:
            kwargs["filter_sub_team"] = filter_sub_team

        return self._list_team_hierarchy_links_endpoint.call_with_http_info(**kwargs)

    def list_team_hierarchy_links_with_pagination(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        filter_parent_team: Union[str, UnsetType] = unset,
        filter_sub_team: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[TeamHierarchyLink]:
        """Get team hierarchy links.

        Provide a paginated version of :meth:`list_team_hierarchy_links`, returning all items.

        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param filter_parent_team: Filter by parent team ID
        :type filter_parent_team: str, optional
        :param filter_sub_team: Filter by sub team ID
        :type filter_sub_team: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[TeamHierarchyLink]
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if filter_parent_team is not unset:
            kwargs["filter_parent_team"] = filter_parent_team

        if filter_sub_team is not unset:
            kwargs["filter_sub_team"] = filter_sub_team

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_team_hierarchy_links_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_teams(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[ListTeamsSort, UnsetType] = unset,
        include: Union[List[ListTeamsInclude], UnsetType] = unset,
        filter_keyword: Union[str, UnsetType] = unset,
        filter_me: Union[bool, UnsetType] = unset,
        fields_team: Union[List[TeamsField], UnsetType] = unset,
    ) -> TeamsResponse:
        """Get all teams.

        Get all teams.
        Can be used to search for teams using the ``filter[keyword]`` and ``filter[me]`` query parameters.

        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param sort: Specifies the order of the returned teams
        :type sort: ListTeamsSort, optional
        :param include: Included related resources optionally requested. Allowed enum values: ``team_links, user_team_permissions``
        :type include: [ListTeamsInclude], optional
        :param filter_keyword: Search query. Can be team name, team handle, or email of team member
        :type filter_keyword: str, optional
        :param filter_me: When true, only returns teams the current user belongs to
        :type filter_me: bool, optional
        :param fields_team: List of fields that need to be fetched.
        :type fields_team: [TeamsField], optional
        :rtype: TeamsResponse
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

        if filter_keyword is not unset:
            kwargs["filter_keyword"] = filter_keyword

        if filter_me is not unset:
            kwargs["filter_me"] = filter_me

        if fields_team is not unset:
            kwargs["fields_team"] = fields_team

        return self._list_teams_endpoint.call_with_http_info(**kwargs)

    def list_teams_with_pagination(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort: Union[ListTeamsSort, UnsetType] = unset,
        include: Union[List[ListTeamsInclude], UnsetType] = unset,
        filter_keyword: Union[str, UnsetType] = unset,
        filter_me: Union[bool, UnsetType] = unset,
        fields_team: Union[List[TeamsField], UnsetType] = unset,
    ) -> collections.abc.Iterable[Team]:
        """Get all teams.

        Provide a paginated version of :meth:`list_teams`, returning all items.

        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param sort: Specifies the order of the returned teams
        :type sort: ListTeamsSort, optional
        :param include: Included related resources optionally requested. Allowed enum values: ``team_links, user_team_permissions``
        :type include: [ListTeamsInclude], optional
        :param filter_keyword: Search query. Can be team name, team handle, or email of team member
        :type filter_keyword: str, optional
        :param filter_me: When true, only returns teams the current user belongs to
        :type filter_me: bool, optional
        :param fields_team: List of fields that need to be fetched.
        :type fields_team: [TeamsField], optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Team]
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

        if filter_keyword is not unset:
            kwargs["filter_keyword"] = filter_keyword

        if filter_me is not unset:
            kwargs["filter_me"] = filter_me

        if fields_team is not unset:
            kwargs["fields_team"] = fields_team

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_teams_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def remove_member_team(
        self,
        super_team_id: str,
        member_team_id: str,
    ) -> None:
        """Remove a member team. **Deprecated**.

        Remove a super team's member team identified by ``member_team_id``.

        **Note** : This API is deprecated. For deleting team hierarchy links, use the team hierarchy links API: ``DELETE /api/v2/team-hierarchy-links/{link_id}``.

        :param super_team_id: None
        :type super_team_id: str
        :param member_team_id: None
        :type member_team_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["super_team_id"] = super_team_id

        kwargs["member_team_id"] = member_team_id

        warnings.warn("remove_member_team is deprecated", DeprecationWarning, stacklevel=2)
        return self._remove_member_team_endpoint.call_with_http_info(**kwargs)

    def remove_team_hierarchy_link(
        self,
        link_id: str,
    ) -> None:
        """Remove a team hierarchy link.

        Remove a team hierarchy link by the given link_id.

        :param link_id: The team hierarchy link's identifier
        :type link_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["link_id"] = link_id

        return self._remove_team_hierarchy_link_endpoint.call_with_http_info(**kwargs)

    def sync_teams(
        self,
        body: TeamSyncRequest,
    ) -> None:
        """Link Teams with GitHub Teams.

        This endpoint attempts to link your existing Datadog teams with GitHub teams by matching their names.
        It evaluates all current Datadog teams and compares them against teams in the GitHub organization
        connected to your Datadog account, based on Datadog Team handle and GitHub Team slug
        (lowercased and kebab-cased).

        This operation is read-only on the GitHub side, no teams will be modified or created.

        `A GitHub organization must be connected to your Datadog account <https://docs.datadoghq.com/integrations/github/>`_ ,
        and the GitHub App integrated with Datadog must have the ``Members Read`` permission. Matching is performed by comparing the Datadog team handle to the GitHub team slug
        using a normalized exact match; case is ignored and spaces are removed. No modifications are made
        to teams in GitHub. This only creates new teams in Datadog when type is set to ``provision``.

        :type body: TeamSyncRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._sync_teams_endpoint.call_with_http_info(**kwargs)

    def update_team(
        self,
        team_id: str,
        body: TeamUpdateRequest,
    ) -> TeamResponse:
        """Update a team.

        Update a team using the team's ``id``.
        If the ``team_links`` relationship is present, the associated links are updated to be in the order they appear in the array, and any existing team links not present are removed.

        :param team_id: None
        :type team_id: str
        :type body: TeamUpdateRequest
        :rtype: TeamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["body"] = body

        return self._update_team_endpoint.call_with_http_info(**kwargs)

    def update_team_link(
        self,
        team_id: str,
        link_id: str,
        body: TeamLinkCreateRequest,
    ) -> TeamLinkResponse:
        """Update a team link.

        Update a team link.

        :param team_id: None
        :type team_id: str
        :param link_id: None
        :type link_id: str
        :type body: TeamLinkCreateRequest
        :rtype: TeamLinkResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["link_id"] = link_id

        kwargs["body"] = body

        return self._update_team_link_endpoint.call_with_http_info(**kwargs)

    def update_team_membership(
        self,
        team_id: str,
        user_id: str,
        body: UserTeamUpdateRequest,
    ) -> UserTeamResponse:
        """Update a user's membership attributes on a team.

        Update a user's membership attributes on a team.

        **Note** : Each team has a setting that determines who is allowed to modify membership of the team. The ``user_access_manage`` permission generally grants access to modify membership of any team. To get the full picture, see `Team Membership documentation <https://docs.datadoghq.com/account_management/teams/manage/#team-membership>`_.

        :param team_id: None
        :type team_id: str
        :param user_id: None
        :type user_id: str
        :type body: UserTeamUpdateRequest
        :rtype: UserTeamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["user_id"] = user_id

        kwargs["body"] = body

        return self._update_team_membership_endpoint.call_with_http_info(**kwargs)

    def update_team_notification_rule(
        self,
        team_id: str,
        rule_id: str,
        body: TeamNotificationRuleRequest,
    ) -> TeamNotificationRuleResponse:
        """Update team notification rule.

        :param team_id: None
        :type team_id: str
        :param rule_id: None
        :type rule_id: str
        :type body: TeamNotificationRuleRequest
        :rtype: TeamNotificationRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_team_notification_rule_endpoint.call_with_http_info(**kwargs)

    def update_team_permission_setting(
        self,
        team_id: str,
        action: str,
        body: TeamPermissionSettingUpdateRequest,
    ) -> TeamPermissionSettingResponse:
        """Update permission setting for team.

        Update a team permission setting for a given team.

        :param team_id: None
        :type team_id: str
        :param action: None
        :type action: str
        :type body: TeamPermissionSettingUpdateRequest
        :rtype: TeamPermissionSettingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["team_id"] = team_id

        kwargs["action"] = action

        kwargs["body"] = body

        return self._update_team_permission_setting_endpoint.call_with_http_info(**kwargs)
