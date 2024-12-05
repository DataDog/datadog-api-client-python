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
from datadog_api_client.v2.model.create_data_deletion_response_body import CreateDataDeletionResponseBody
from datadog_api_client.v2.model.create_data_deletion_request_body import CreateDataDeletionRequestBody
from datadog_api_client.v2.model.get_data_deletions_response_body import GetDataDeletionsResponseBody
from datadog_api_client.v2.model.cancel_data_deletion_response_body import CancelDataDeletionResponseBody


class DataDeletionApi:
    """
    The Data Deletion API allows the user to target and delete data from the allowed products. It's currently enabled for Logs and RUM and depends on ``logs_delete_data`` and ``rum_delete_data`` permissions respectively.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_data_deletion_request_endpoint = _Endpoint(
            settings={
                "response_type": (CancelDataDeletionResponseBody,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deletion/requests/{id}/cancel",
                "operation_id": "cancel_data_deletion_request",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_data_deletion_request_endpoint = _Endpoint(
            settings={
                "response_type": (CreateDataDeletionResponseBody,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deletion/data/{product}",
                "operation_id": "create_data_deletion_request",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "product": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "product",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateDataDeletionRequestBody,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_data_deletion_requests_endpoint = _Endpoint(
            settings={
                "response_type": (GetDataDeletionsResponseBody,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/deletion/requests",
                "operation_id": "get_data_deletion_requests",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "next_page": {
                    "openapi_types": (str,),
                    "attribute": "next_page",
                    "location": "query",
                },
                "product": {
                    "openapi_types": (str,),
                    "attribute": "product",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "status": {
                    "openapi_types": (str,),
                    "attribute": "status",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 50,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_size",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def cancel_data_deletion_request(
        self,
        id: str,
    ) -> CancelDataDeletionResponseBody:
        """Cancels a data deletion request.

        Cancels a data deletion request by providing its ID.

        :param id: ID of the deletion request.
        :type id: str
        :rtype: CancelDataDeletionResponseBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._cancel_data_deletion_request_endpoint.call_with_http_info(**kwargs)

    def create_data_deletion_request(
        self,
        product: str,
        body: CreateDataDeletionRequestBody,
    ) -> CreateDataDeletionResponseBody:
        """Creates a data deletion request.

        Creates a data deletion request by providing a query and a timeframe targeting the proper data.

        :param product: Name of the product to be deleted, either ``logs`` or ``rum``.
        :type product: str
        :type body: CreateDataDeletionRequestBody
        :rtype: CreateDataDeletionResponseBody
        """
        kwargs: Dict[str, Any] = {}
        kwargs["product"] = product

        kwargs["body"] = body

        return self._create_data_deletion_request_endpoint.call_with_http_info(**kwargs)

    def get_data_deletion_requests(
        self,
        *,
        next_page: Union[str, UnsetType] = unset,
        product: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> GetDataDeletionsResponseBody:
        """Gets a list of data deletion requests.

        Gets a list of data deletion requests based on several filter parameters.

        :param next_page: The next page of the previous search. If the next_page parameter is included, the rest of the query elements are ignored.
        :type next_page: str, optional
        :param product: Retrieve only the requests related to the given product.
        :type product: str, optional
        :param query: Retrieve only the requests that matches the given query.
        :type query: str, optional
        :param status: Retrieve only the requests with the given status.
        :type status: str, optional
        :param page_size: Sets the page size of the search.
        :type page_size: int, optional
        :rtype: GetDataDeletionsResponseBody
        """
        kwargs: Dict[str, Any] = {}
        if next_page is not unset:
            kwargs["next_page"] = next_page

        if product is not unset:
            kwargs["product"] = product

        if query is not unset:
            kwargs["query"] = query

        if status is not unset:
            kwargs["status"] = status

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._get_data_deletion_requests_endpoint.call_with_http_info(**kwargs)
