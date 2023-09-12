# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.custom_destination_list_response import CustomDestinationListResponse
from datadog_api_client.v2.model.custom_destination_response import CustomDestinationResponse
from datadog_api_client.v2.model.custom_destination_create_payload import CustomDestinationCreatePayload
from datadog_api_client.v2.model.custom_destination_delete_response import CustomDestinationDeleteResponse
from datadog_api_client.v2.model.custom_destination_update_payload import CustomDestinationUpdatePayload


class LogsCustomDestinationsApi:
    """
    Note: This endpoint is in public beta. If you have any feedback, contact `Datadog support <https://docs.datadoghq.com/help/>`_.

    Manage configuration of `log-based custom destinations <https://app.datadoghq.com/logs/pipelines/log-forwarding/custom-destinations>`_ for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/custom_destinations",
                "operation_id": "create_logs_custom_destination",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CustomDestinationCreatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/custom_destinations/{custom_destination_id}",
                "operation_id": "delete_logs_custom_destination",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "custom_destination_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_destination_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/custom_destinations/{custom_destination_id}",
                "operation_id": "get_logs_custom_destination",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "custom_destination_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_destination_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_logs_custom_destinations_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/custom_destinations",
                "operation_id": "list_logs_custom_destinations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/custom_destinations/{custom_destination_id}",
                "operation_id": "update_logs_custom_destination",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "custom_destination_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_destination_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CustomDestinationUpdatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_logs_custom_destination(
        self,
        body: CustomDestinationCreatePayload,
    ) -> CustomDestinationResponse:
        """Create a custom destination.

        Create a new custom destination for your organization.

        :type body: CustomDestinationCreatePayload
        :rtype: CustomDestinationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_logs_custom_destination_endpoint.call_with_http_info(**kwargs)

    def delete_logs_custom_destination(
        self,
        custom_destination_id: str,
    ) -> CustomDestinationDeleteResponse:
        """Delete a custom destination.

        Deletes a custom destination.

        :param custom_destination_id: The ID of the custom destination.
        :type custom_destination_id: str
        :rtype: CustomDestinationDeleteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_destination_id"] = custom_destination_id

        return self._delete_logs_custom_destination_endpoint.call_with_http_info(**kwargs)

    def get_logs_custom_destination(
        self,
        custom_destination_id: str,
    ) -> CustomDestinationResponse:
        """Get a custom destination.

        Get a custom destination in the organization specified by the custom destination's ``custom_destination_id``.

        :param custom_destination_id: The ID of the custom destination.
        :type custom_destination_id: str
        :rtype: CustomDestinationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_destination_id"] = custom_destination_id

        return self._get_logs_custom_destination_endpoint.call_with_http_info(**kwargs)

    def list_logs_custom_destinations(
        self,
    ) -> CustomDestinationListResponse:
        """List custom destinations.

        Returns all custom destinations, including their attributes and IDs.

        :rtype: CustomDestinationListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_logs_custom_destinations_endpoint.call_with_http_info(**kwargs)

    def update_logs_custom_destination(
        self,
        custom_destination_id: str,
        body: CustomDestinationUpdatePayload,
    ) -> CustomDestinationResponse:
        """Update a custom destination.

        Edit a custom destination.

        :param custom_destination_id: The ID of the custom destination.
        :type custom_destination_id: str
        :type body: CustomDestinationUpdatePayload
        :rtype: CustomDestinationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_destination_id"] = custom_destination_id

        kwargs["body"] = body

        return self._update_logs_custom_destination_endpoint.call_with_http_info(**kwargs)
