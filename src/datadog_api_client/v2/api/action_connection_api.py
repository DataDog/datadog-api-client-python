# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.create_action_connection_response import CreateActionConnectionResponse
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.get_action_connection_response import GetActionConnectionResponse
from datadog_api_client.v2.model.update_action_connection_response import UpdateActionConnectionResponse
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest


class ActionConnectionApi:
    """
    Action connections extend your installed integrations and allow you to take action in your third-party systems
    (e.g. AWS, GitLab, and Statuspage) with Datadog’s Workflow Automation and App Builder products.

    Datadog’s Integrations automatically provide authentication for Slack, Microsoft Teams, PagerDuty, Opsgenie,
    JIRA, GitHub, and Statuspage. You do not need additional connections in order to access these tools within
    Workflow Automation and App Builder.

    We offer granular access control for editing and resolving connections.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": (CreateActionConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections",
                "operation_id": "create_action_connection",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateActionConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/{connection_id}",
                "operation_id": "delete_action_connection",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": (GetActionConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/{connection_id}",
                "operation_id": "get_action_connection",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_action_connection_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateActionConnectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/connections/{connection_id}",
                "operation_id": "update_action_connection",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "connection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "connection_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateActionConnectionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_action_connection(
        self,
        body: CreateActionConnectionRequest,
    ) -> CreateActionConnectionResponse:
        """Create a new Action Connection.

        Create a new Action Connection

        :type body: CreateActionConnectionRequest
        :rtype: CreateActionConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_action_connection_endpoint.call_with_http_info(**kwargs)

    def delete_action_connection(
        self,
        connection_id: str,
    ) -> None:
        """Delete an existing Action Connection.

        Delete an existing Action Connection

        :param connection_id: The ID of the action connection
        :type connection_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        return self._delete_action_connection_endpoint.call_with_http_info(**kwargs)

    def get_action_connection(
        self,
        connection_id: str,
    ) -> GetActionConnectionResponse:
        """Get an existing Action Connection.

        Get an existing Action Connection

        :param connection_id: The ID of the action connection
        :type connection_id: str
        :rtype: GetActionConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        return self._get_action_connection_endpoint.call_with_http_info(**kwargs)

    def update_action_connection(
        self,
        connection_id: str,
        body: UpdateActionConnectionRequest,
    ) -> UpdateActionConnectionResponse:
        """Update an existing Action Connection.

        Update an existing Action Connection

        :param connection_id: The ID of the action connection
        :type connection_id: str
        :param body: Update an existing Action Connection request body
        :type body: UpdateActionConnectionRequest
        :rtype: UpdateActionConnectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["connection_id"] = connection_id

        kwargs["body"] = body

        return self._update_action_connection_endpoint.call_with_http_info(**kwargs)
