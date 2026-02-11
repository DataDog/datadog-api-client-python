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
from datadog_api_client.v2.model.unassign_seats_user_request import UnassignSeatsUserRequest
from datadog_api_client.v2.model.seat_user_data_array import SeatUserDataArray
from datadog_api_client.v2.model.assign_seats_user_response import AssignSeatsUserResponse
from datadog_api_client.v2.model.assign_seats_user_request import AssignSeatsUserRequest


class SeatsApi:
    """
    The seats API allows you to view, assign, and unassign seats for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._assign_seats_user_endpoint = _Endpoint(
            settings={
                "response_type": (AssignSeatsUserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/seats/users",
                "operation_id": "assign_seats_user",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AssignSeatsUserRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_seats_users_endpoint = _Endpoint(
            settings={
                "response_type": (SeatUserDataArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/seats/users",
                "operation_id": "get_seats_users",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "product_code": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "product_code",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._unassign_seats_user_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/seats/users",
                "operation_id": "unassign_seats_user",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UnassignSeatsUserRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def assign_seats_user(
        self,
        body: AssignSeatsUserRequest,
    ) -> AssignSeatsUserResponse:
        """Assign seats to users.

        Assign seats to users for a product code.

        :type body: AssignSeatsUserRequest
        :rtype: AssignSeatsUserResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._assign_seats_user_endpoint.call_with_http_info(**kwargs)

    def get_seats_users(
        self,
        product_code: str,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> SeatUserDataArray:
        """Get users with seats.

        Get the list of users assigned seats for a product code.

        :param product_code: The product code for which to retrieve seat users.
        :type product_code: str
        :param page_limit: Maximum number of results to return.
        :type page_limit: int, optional
        :param page_cursor: Cursor for pagination.
        :type page_cursor: str, optional
        :rtype: SeatUserDataArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["product_code"] = product_code

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._get_seats_users_endpoint.call_with_http_info(**kwargs)

    def unassign_seats_user(
        self,
        body: UnassignSeatsUserRequest,
    ) -> None:
        """Unassign seats from users.

        Unassign seats from users for a product code.

        :type body: UnassignSeatsUserRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._unassign_seats_user_endpoint.call_with_http_info(**kwargs)
