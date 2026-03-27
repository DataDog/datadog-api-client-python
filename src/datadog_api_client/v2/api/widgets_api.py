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
    UUID,
)
from datadog_api_client.v2.model.widget_list_response import WidgetListResponse
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType
from datadog_api_client.v2.model.widget_type import WidgetType
from datadog_api_client.v2.model.widget_response import WidgetResponse
from datadog_api_client.v2.model.create_or_update_widget_request import CreateOrUpdateWidgetRequest


class WidgetsApi:
    """
    Create, read, update, and delete saved widgets. Widgets are reusable
    visualization components stored independently from any dashboard or notebook,
    partitioned by experience type and identified by a UUID.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_widget_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}",
                "operation_id": "create_widget",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateOrUpdateWidgetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_widget_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}/{uuid}",
                "operation_id": "delete_widget",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
                "uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_widget_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}/{uuid}",
                "operation_id": "get_widget",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
                "uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_widgets_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}",
                "operation_id": "search_widgets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
                "filter_widget_type": {
                    "openapi_types": (WidgetType,),
                    "attribute": "filter[widgetType]",
                    "location": "query",
                },
                "filter_creator_handle": {
                    "openapi_types": (str,),
                    "attribute": "filter[creatorHandle]",
                    "location": "query",
                },
                "filter_is_favorited": {
                    "openapi_types": (bool,),
                    "attribute": "filter[isFavorited]",
                    "location": "query",
                },
                "filter_title": {
                    "openapi_types": (str,),
                    "attribute": "filter[title]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_widget_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}/{uuid}",
                "operation_id": "update_widget",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
                "uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "uuid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateOrUpdateWidgetRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_widget(
        self,
        experience_type: WidgetExperienceType,
        body: CreateOrUpdateWidgetRequest,
    ) -> WidgetResponse:
        """Create a widget.

        Create a new widget for a given experience type.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :param body: Widget request body.
        :type body: CreateOrUpdateWidgetRequest
        :rtype: WidgetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        kwargs["body"] = body

        return self._create_widget_endpoint.call_with_http_info(**kwargs)

    def delete_widget(
        self,
        experience_type: WidgetExperienceType,
        uuid: UUID,
    ) -> None:
        """Delete a widget.

        Soft-delete a widget by its UUID for a given experience type.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :param uuid: The UUID of the widget.
        :type uuid: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        kwargs["uuid"] = uuid

        return self._delete_widget_endpoint.call_with_http_info(**kwargs)

    def get_widget(
        self,
        experience_type: WidgetExperienceType,
        uuid: UUID,
    ) -> WidgetResponse:
        """Get a widget.

        Retrieve a widget by its UUID for a given experience type.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :param uuid: The UUID of the widget.
        :type uuid: UUID
        :rtype: WidgetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        kwargs["uuid"] = uuid

        return self._get_widget_endpoint.call_with_http_info(**kwargs)

    def search_widgets(
        self,
        experience_type: WidgetExperienceType,
        *,
        filter_widget_type: Union[WidgetType, UnsetType] = unset,
        filter_creator_handle: Union[str, UnsetType] = unset,
        filter_is_favorited: Union[bool, UnsetType] = unset,
        filter_title: Union[str, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> WidgetListResponse:
        """Search widgets.

        Search and list widgets for a given experience type. Supports filtering by widget type, creator, title, and tags, as well as sorting and pagination.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :param filter_widget_type: Filter widgets by widget type.
        :type filter_widget_type: WidgetType, optional
        :param filter_creator_handle: Filter widgets by the email handle of the creator.
        :type filter_creator_handle: str, optional
        :param filter_is_favorited: Filter to only widgets favorited by the current user.
        :type filter_is_favorited: bool, optional
        :param filter_title: Filter widgets by title (substring match).
        :type filter_title: str, optional
        :param filter_tags: Filter widgets by tags. Format as bracket-delimited CSV, e.g. ``[tag1,tag2]``.
        :type filter_tags: str, optional
        :param sort: Sort field for the results. Prefix with ``-`` for descending order.
            Allowed values: ``title`` , ``created_at`` , ``modified_at``.
        :type sort: str, optional
        :param page_number: Page number for pagination (0-indexed).
        :type page_number: int, optional
        :param page_size: Number of widgets per page.
        :type page_size: int, optional
        :rtype: WidgetListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        if filter_widget_type is not unset:
            kwargs["filter_widget_type"] = filter_widget_type

        if filter_creator_handle is not unset:
            kwargs["filter_creator_handle"] = filter_creator_handle

        if filter_is_favorited is not unset:
            kwargs["filter_is_favorited"] = filter_is_favorited

        if filter_title is not unset:
            kwargs["filter_title"] = filter_title

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if sort is not unset:
            kwargs["sort"] = sort

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._search_widgets_endpoint.call_with_http_info(**kwargs)

    def update_widget(
        self,
        experience_type: WidgetExperienceType,
        uuid: UUID,
        body: CreateOrUpdateWidgetRequest,
    ) -> WidgetResponse:
        """Update a widget.

        Update a widget by its UUID for a given experience type. This performs a full replacement of the widget definition.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :param uuid: The UUID of the widget.
        :type uuid: UUID
        :param body: Widget request body.
        :type body: CreateOrUpdateWidgetRequest
        :rtype: WidgetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        kwargs["uuid"] = uuid

        kwargs["body"] = body

        return self._update_widget_endpoint.call_with_http_info(**kwargs)
