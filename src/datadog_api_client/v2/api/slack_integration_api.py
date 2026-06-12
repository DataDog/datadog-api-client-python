# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UUID,
)
from datadog_api_client.v2.model.slack_user_bindings_response import SlackUserBindingsResponse


class SlackIntegrationApi:
    """
    Configure your `Datadog Slack integration <https://docs.datadoghq.com/integrations/slack/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_slack_user_bindings_endpoint = _Endpoint(
            settings={
                "response_type": (SlackUserBindingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/slack/user-bindings",
                "operation_id": "list_slack_user_bindings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "user_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "user_uuid",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_slack_user_bindings(
        self,
        user_uuid: UUID,
    ) -> SlackUserBindingsResponse:
        """List Slack user bindings.

        List all Slack user bindings for a given Datadog user from the Datadog Slack integration.

        :param user_uuid: The UUID of the Datadog user to list Slack bindings for.
        :type user_uuid: UUID
        :rtype: SlackUserBindingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_uuid"] = user_uuid

        return self._list_slack_user_bindings_endpoint.call_with_http_info(**kwargs)
