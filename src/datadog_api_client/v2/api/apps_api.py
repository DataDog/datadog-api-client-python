# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.delete_apps_response import DeleteAppsResponse
from datadog_api_client.v2.model.delete_apps_request import DeleteAppsRequest
from datadog_api_client.v2.model.list_apps_response import ListAppsResponse
from datadog_api_client.v2.model.apps_sort_field import AppsSortField
from datadog_api_client.v2.model.create_app_response import CreateAppResponse
from datadog_api_client.v2.model.create_app_request import CreateAppRequest
from datadog_api_client.v2.model.delete_app_response import DeleteAppResponse
from datadog_api_client.v2.model.get_app_response import GetAppResponse
from datadog_api_client.v2.model.update_app_response import UpdateAppResponse
from datadog_api_client.v2.model.update_app_request import UpdateAppRequest


class AppsApi:
    """
    Create, read, update, and delete apps in App Builder.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_app_endpoint = _Endpoint(
            settings={
                "response_type": (CreateAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps",
                "operation_id": "create_app",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateAppRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_app_endpoint = _Endpoint(
            settings={
                "response_type": (DeleteAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}",
                "operation_id": "delete_app",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_apps_endpoint = _Endpoint(
            settings={
                "response_type": (DeleteAppsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps",
                "operation_id": "delete_apps",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DeleteAppsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_app_endpoint = _Endpoint(
            settings={
                "response_type": (GetAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}",
                "operation_id": "get_app",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_apps_endpoint = _Endpoint(
            settings={
                "response_type": (ListAppsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps",
                "operation_id": "list_apps",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "page": {
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "filter_user_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[user_name]",
                    "location": "query",
                },
                "filter_user_uuid": {
                    "openapi_types": (str,),
                    "attribute": "filter[user_uuid]",
                    "location": "query",
                },
                "filter_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[name]",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_deployed": {
                    "openapi_types": (bool,),
                    "attribute": "filter[deployed]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "filter_favorite": {
                    "openapi_types": (bool,),
                    "attribute": "filter[favorite]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": ([AppsSortField],),
                    "attribute": "sort",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_app_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}",
                "operation_id": "update_app",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateAppRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_app(
        self,
        body: CreateAppRequest,
    ) -> CreateAppResponse:
        """Create App.

        Create a new app, returning the app ID

        :type body: CreateAppRequest
        :rtype: CreateAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_app_endpoint.call_with_http_info(**kwargs)

    def delete_app(
        self,
        app_id: str,
    ) -> DeleteAppResponse:
        """Delete App.

        Delete an app by ID

        :type app_id: str
        :rtype: DeleteAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._delete_app_endpoint.call_with_http_info(**kwargs)

    def delete_apps(
        self,
        body: DeleteAppsRequest,
    ) -> DeleteAppsResponse:
        """Delete Multiple Apps.

        Delete multiple apps by ID

        :type body: DeleteAppsRequest
        :rtype: DeleteAppsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_apps_endpoint.call_with_http_info(**kwargs)

    def get_app(
        self,
        app_id: str,
    ) -> GetAppResponse:
        """Get App.

        Get the full definition of an app by ID

        :type app_id: str
        :rtype: GetAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._get_app_endpoint.call_with_http_info(**kwargs)

    def list_apps(
        self,
        *,
        limit: Union[int, UnsetType] = unset,
        page: Union[int, UnsetType] = unset,
        filter_user_name: Union[str, UnsetType] = unset,
        filter_user_uuid: Union[str, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        filter_deployed: Union[bool, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_favorite: Union[bool, UnsetType] = unset,
        sort: Union[List[AppsSortField], UnsetType] = unset,
    ) -> ListAppsResponse:
        """List Apps.

        List all apps, with optional filters and sorting

        :param limit: The number of apps to return per page
        :type limit: int, optional
        :param page: The page number to return
        :type page: int, optional
        :param filter_user_name: The ``AppsFilter`` ``user_name``.
        :type filter_user_name: str, optional
        :param filter_user_uuid: The ``AppsFilter`` ``user_uuid``.
        :type filter_user_uuid: str, optional
        :param filter_name: The ``AppsFilter`` ``name``.
        :type filter_name: str, optional
        :param filter_query: The ``AppsFilter`` ``query``.
        :type filter_query: str, optional
        :param filter_deployed: The ``AppsFilter`` ``deployed``.
        :type filter_deployed: bool, optional
        :param filter_tags: The ``AppsFilter`` ``tags``.
        :type filter_tags: str, optional
        :param filter_favorite: The ``AppsFilter`` ``favorite``.
        :type filter_favorite: bool, optional
        :type sort: [AppsSortField], optional
        :rtype: ListAppsResponse
        """
        kwargs: Dict[str, Any] = {}
        if limit is not unset:
            kwargs["limit"] = limit

        if page is not unset:
            kwargs["page"] = page

        if filter_user_name is not unset:
            kwargs["filter_user_name"] = filter_user_name

        if filter_user_uuid is not unset:
            kwargs["filter_user_uuid"] = filter_user_uuid

        if filter_name is not unset:
            kwargs["filter_name"] = filter_name

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_deployed is not unset:
            kwargs["filter_deployed"] = filter_deployed

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_favorite is not unset:
            kwargs["filter_favorite"] = filter_favorite

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_apps_endpoint.call_with_http_info(**kwargs)

    def update_app(
        self,
        app_id: str,
        body: UpdateAppRequest,
    ) -> UpdateAppResponse:
        """Update App.

        Update an existing app by ID. Creates a new version of the app

        :type app_id: str
        :type body: UpdateAppRequest
        :rtype: UpdateAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._update_app_endpoint.call_with_http_info(**kwargs)
