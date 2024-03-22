# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.custom_destinations_response import CustomDestinationsResponse
from datadog_api_client.v2.model.custom_destination_response import CustomDestinationResponse
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_update_request import CustomDestinationUpdateRequest


class LogsCustomDestinationsApi:
    """
    Custom Destinations forward all the logs ingested to an external destination.

    **Note** : Log forwarding is not available for the Government (US1-FED) site. Contact your account representative for more information.

    See the `Custom Destinations Page <https://app.datadoghq.com/logs/pipelines/log-forwarding/custom-destinations>`_
    for a list of the custom destinations currently configured in web UI.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/custom-destinations",
                "operation_id": "create_logs_custom_destination",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CustomDestinationCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/custom-destinations/{custom_destination_id}",
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
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_logs_custom_destination_endpoint = _Endpoint(
            settings={
                "response_type": (CustomDestinationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/custom-destinations/{custom_destination_id}",
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
                "response_type": (CustomDestinationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/custom-destinations",
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/custom-destinations/{custom_destination_id}",
                "operation_id": "update_logs_custom_destination",
                "http_method": "PATCH",
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
                    "openapi_types": (CustomDestinationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_logs_custom_destination(
        self,
        body: CustomDestinationCreateRequest,
    ) -> CustomDestinationResponse:
        """Create a custom destination.

        Create a custom destination in your organization.

        :param body: The definition of the new custom destination.
        :type body: CustomDestinationCreateRequest
        :rtype: CustomDestinationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_logs_custom_destination_endpoint.call_with_http_info(**kwargs)

    def delete_logs_custom_destination(
        self,
        custom_destination_id: str,
    ) -> None:
        """Delete a custom destination.

        Delete a specific custom destination in your organization.

        :param custom_destination_id: The ID of the custom destination.
        :type custom_destination_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_destination_id"] = custom_destination_id

        return self._delete_logs_custom_destination_endpoint.call_with_http_info(**kwargs)

    def get_logs_custom_destination(
        self,
        custom_destination_id: str,
    ) -> CustomDestinationResponse:
        """Get a custom destination.

        Get a specific custom destination in your organization.

        :param custom_destination_id: The ID of the custom destination.
        :type custom_destination_id: str
        :rtype: CustomDestinationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_destination_id"] = custom_destination_id

        return self._get_logs_custom_destination_endpoint.call_with_http_info(**kwargs)

    def list_logs_custom_destinations(
        self,
    ) -> CustomDestinationsResponse:
        """Get all custom destinations.

        Get the list of configured custom destinations in your organization with their definitions.

        :rtype: CustomDestinationsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_logs_custom_destinations_endpoint.call_with_http_info(**kwargs)

    def update_logs_custom_destination(
        self,
        custom_destination_id: str,
        body: CustomDestinationUpdateRequest,
    ) -> CustomDestinationResponse:
        """Update a custom destination.

        Update the given fields of a specific custom destination in your organization.

        :param custom_destination_id: The ID of the custom destination.
        :type custom_destination_id: str
        :param body: New definition of the custom destination's fields.
        :type body: CustomDestinationUpdateRequest
        :rtype: CustomDestinationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_destination_id"] = custom_destination_id

        kwargs["body"] = body

        return self._update_logs_custom_destination_endpoint.call_with_http_info(**kwargs)
