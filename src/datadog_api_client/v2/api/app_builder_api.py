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
    UUID,
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
from datadog_api_client.v2.model.unpublish_app_response import UnpublishAppResponse
from datadog_api_client.v2.model.publish_app_response import PublishAppResponse


class AppBuilderApi:
    """
    Datadog App Builder provides a low-code solution to rapidly develop and integrate secure, customized applications into your monitoring stack that are built to accelerate remediation at scale. These API endpoints allow you to create, read, update, delete, and publish apps.
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
                    "openapi_types": (UUID,),
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
                    "openapi_types": (UUID,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "version": {
                    "openapi_types": (str,),
                    "attribute": "version",
                    "location": "query",
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
                    "openapi_types": (UUID,),
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
                "filter_self_service": {
                    "openapi_types": (bool,),
                    "attribute": "filter[self_service]",
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

        self._publish_app_endpoint = _Endpoint(
            settings={
                "response_type": (PublishAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}/deployment",
                "operation_id": "publish_app",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._unpublish_app_endpoint = _Endpoint(
            settings={
                "response_type": (UnpublishAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}/deployment",
                "operation_id": "unpublish_app",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "app_id",
                    "location": "path",
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
                    "openapi_types": (UUID,),
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

        Create a new app, returning the app ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :type body: CreateAppRequest
        :rtype: CreateAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_app_endpoint.call_with_http_info(**kwargs)

    def delete_app(
        self,
        app_id: UUID,
    ) -> DeleteAppResponse:
        """Delete App.

        Delete a single app. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param app_id: The ID of the app to delete.
        :type app_id: UUID
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

        Delete multiple apps in a single request from a list of app IDs. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :type body: DeleteAppsRequest
        :rtype: DeleteAppsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_apps_endpoint.call_with_http_info(**kwargs)

    def get_app(
        self,
        app_id: UUID,
        *,
        version: Union[str, UnsetType] = unset,
    ) -> GetAppResponse:
        """Get App.

        Get the full definition of an app. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param app_id: The ID of the app to retrieve.
        :type app_id: UUID
        :param version: The version number of the app to retrieve. If not specified, the latest version is returned. Version numbers start at 1 and increment with each update. The special values ``latest`` and ``deployed`` can be used to retrieve the latest version or the published version, respectively.
        :type version: str, optional
        :rtype: GetAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        if version is not unset:
            kwargs["version"] = version

        return self._get_app_endpoint.call_with_http_info(**kwargs)

    def list_apps(
        self,
        *,
        limit: Union[int, UnsetType] = unset,
        page: Union[int, UnsetType] = unset,
        filter_user_name: Union[str, UnsetType] = unset,
        filter_user_uuid: Union[UUID, UnsetType] = unset,
        filter_name: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        filter_deployed: Union[bool, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_favorite: Union[bool, UnsetType] = unset,
        filter_self_service: Union[bool, UnsetType] = unset,
        sort: Union[List[AppsSortField], UnsetType] = unset,
    ) -> ListAppsResponse:
        """List Apps.

        List all apps, with optional filters and sorting. This endpoint is paginated. Only basic app information such as the app ID, name, and description is returned by this endpoint. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param limit: The number of apps to return per page.
        :type limit: int, optional
        :param page: The page number to return.
        :type page: int, optional
        :param filter_user_name: Filter apps by the app creator. Usually the user's email.
        :type filter_user_name: str, optional
        :param filter_user_uuid: Filter apps by the app creator's UUID.
        :type filter_user_uuid: UUID, optional
        :param filter_name: Filter by app name.
        :type filter_name: str, optional
        :param filter_query: Filter apps by the app name or the app creator.
        :type filter_query: str, optional
        :param filter_deployed: Filter apps by whether they are published.
        :type filter_deployed: bool, optional
        :param filter_tags: Filter apps by tags.
        :type filter_tags: str, optional
        :param filter_favorite: Filter apps by whether you have added them to your favorites.
        :type filter_favorite: bool, optional
        :param filter_self_service: Filter apps by whether they are enabled for self-service.
        :type filter_self_service: bool, optional
        :param sort: The fields and direction to sort apps by.
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

        if filter_self_service is not unset:
            kwargs["filter_self_service"] = filter_self_service

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_apps_endpoint.call_with_http_info(**kwargs)

    def publish_app(
        self,
        app_id: UUID,
    ) -> PublishAppResponse:
        """Publish App.

        Publish an app for use by other users. To ensure the app is accessible to the correct users, you also need to set a `Restriction Policy <https://docs.datadoghq.com/api/latest/restriction-policies/>`_ on the app if a policy does not yet exist. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param app_id: The ID of the app to publish.
        :type app_id: UUID
        :rtype: PublishAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._publish_app_endpoint.call_with_http_info(**kwargs)

    def unpublish_app(
        self,
        app_id: UUID,
    ) -> UnpublishAppResponse:
        """Unpublish App.

        Unpublish an app, removing the live version of the app. Unpublishing creates a new instance of a ``deployment`` object on the app, with a nil ``app_version_id`` ( ``00000000-0000-0000-0000-000000000000`` ). The app can still be updated and published again in the future. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param app_id: The ID of the app to unpublish.
        :type app_id: UUID
        :rtype: UnpublishAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._unpublish_app_endpoint.call_with_http_info(**kwargs)

    def update_app(
        self,
        app_id: UUID,
        body: UpdateAppRequest,
    ) -> UpdateAppResponse:
        """Update App.

        Update an existing app. This creates a new version of the app. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param app_id: The ID of the app to update.
        :type app_id: UUID
        :type body: UpdateAppRequest
        :rtype: UpdateAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._update_app_endpoint.call_with_http_info(**kwargs)
