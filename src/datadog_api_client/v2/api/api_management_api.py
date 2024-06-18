# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    file_type,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.list_apis_response import ListAPIsResponse
from datadog_api_client.v2.model.update_open_api_response import UpdateOpenAPIResponse
from datadog_api_client.v2.model.create_open_api_response import CreateOpenAPIResponse


class APIManagementApi:
    """
    Configure your API endpoints through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_open_api_endpoint = _Endpoint(
            settings={
                "response_type": (CreateOpenAPIResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apicatalog/openapi",
                "operation_id": "create_open_api",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "openapi_spec_file": {
                    "openapi_types": (file_type,),
                    "attribute": "openapi_spec_file",
                    "location": "form",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

        self._delete_open_api_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apicatalog/api/{id}",
                "operation_id": "delete_open_api",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_open_api_endpoint = _Endpoint(
            settings={
                "response_type": (file_type,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apicatalog/api/{id}/openapi",
                "operation_id": "get_open_api",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["multipart/form-data", "application/json"],
            },
            api_client=api_client,
        )

        self._list_apis_endpoint = _Endpoint(
            settings={
                "response_type": (ListAPIsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apicatalog/api",
                "operation_id": "list_apis",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_open_api_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateOpenAPIResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apicatalog/api/{id}/openapi",
                "operation_id": "update_open_api",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "openapi_spec_file": {
                    "openapi_types": (file_type,),
                    "attribute": "openapi_spec_file",
                    "location": "form",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def create_open_api(
        self,
        *,
        openapi_spec_file: Union[file_type, UnsetType] = unset,
    ) -> CreateOpenAPIResponse:
        """Create a new API.

        Create a new API from the `OpenAPI <https://spec.openapis.org/oas/latest.html>`_ specification given.
        See the `API Catalog documentation <https://docs.datadoghq.com/api_catalog/add_metadata/>`_ for additional
        information about the possible metadata.
        It returns the created API ID.

        :param openapi_spec_file: Binary ``OpenAPI`` spec file
        :type openapi_spec_file: file_type, optional
        :rtype: CreateOpenAPIResponse
        """
        kwargs: Dict[str, Any] = {}
        if openapi_spec_file is not unset:
            kwargs["openapi_spec_file"] = openapi_spec_file

        return self._create_open_api_endpoint.call_with_http_info(**kwargs)

    def delete_open_api(
        self,
        id: UUID,
    ) -> None:
        """Delete an API.

        Delete a specific API by ID.

        :param id: ID of the API to delete
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_open_api_endpoint.call_with_http_info(**kwargs)

    def get_open_api(
        self,
        id: UUID,
    ) -> file_type:
        """Get an API.

        Retrieve information about a specific API in `OpenAPI <https://spec.openapis.org/oas/latest.html>`_ format file.

        :param id: ID of the API to retrieve
        :type id: UUID
        :rtype: file_type
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_open_api_endpoint.call_with_http_info(**kwargs)

    def list_apis(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> ListAPIsResponse:
        """List APIs.

        List APIs and their IDs.

        :param query: Filter APIs by name
        :type query: str, optional
        :param page_limit: Number of items per page.
        :type page_limit: int, optional
        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :rtype: ListAPIsResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_apis_endpoint.call_with_http_info(**kwargs)

    def update_open_api(
        self,
        id: UUID,
        *,
        openapi_spec_file: Union[file_type, UnsetType] = unset,
    ) -> UpdateOpenAPIResponse:
        """Update an API.

        Update information about a specific API. The given content will replace all API content of the given ID.
        The ID is returned by the create API, or can be found in the URL in the API catalog UI.

        :param id: ID of the API to modify
        :type id: UUID
        :param openapi_spec_file: Binary ``OpenAPI`` spec file
        :type openapi_spec_file: file_type, optional
        :rtype: UpdateOpenAPIResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if openapi_spec_file is not unset:
            kwargs["openapi_spec_file"] = openapi_spec_file

        return self._update_open_api_endpoint.call_with_http_info(**kwargs)
