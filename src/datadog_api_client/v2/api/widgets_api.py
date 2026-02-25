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
from datadog_api_client.v2.model.widget_schema_jsonapi_list_document import WidgetSchemaJSONAPIListDocument
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType
from datadog_api_client.v2.model.widget_schema_jsonapi_document import WidgetSchemaJSONAPIDocument
from datadog_api_client.v2.model.create_or_update_widget_request_jsonapi_request_document import (
    CreateOrUpdateWidgetRequestJSONAPIRequestDocument,
)


class WidgetsApi:
    """
    Auto-generated tag Widgets
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_widget_api_v2_widgets_experience_type_post_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetSchemaJSONAPIDocument,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}",
                "operation_id": "create_widget_api_v2_widgets_experience_type_post",
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
                    "openapi_types": (CreateOrUpdateWidgetRequestJSONAPIRequestDocument,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_widget_api_v2_widgets_experience_type_uuid_delete_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}/{uuid}",
                "operation_id": "delete_widget_api_v2_widgets_experience_type_uuid_delete",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "uuid",
                    "location": "path",
                },
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_widget_api_v2_widgets_experience_type_uuid_get_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetSchemaJSONAPIDocument,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}/{uuid}",
                "operation_id": "get_widget_api_v2_widgets_experience_type_uuid_get",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "uuid",
                    "location": "path",
                },
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_widgets_api_v2_widgets_experience_type_get_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetSchemaJSONAPIListDocument,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}",
                "operation_id": "search_widgets_api_v2_widgets_experience_type_get",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_widget_api_v2_widgets_experience_type_uuid_put_endpoint = _Endpoint(
            settings={
                "response_type": (WidgetSchemaJSONAPIDocument,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/widgets/{experience_type}/{uuid}",
                "operation_id": "update_widget_api_v2_widgets_experience_type_uuid_put",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "uuid",
                    "location": "path",
                },
                "experience_type": {
                    "required": True,
                    "openapi_types": (WidgetExperienceType,),
                    "attribute": "experience_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateOrUpdateWidgetRequestJSONAPIRequestDocument,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_widget_api_v2_widgets_experience_type_post(
        self,
        experience_type: WidgetExperienceType,
        body: CreateOrUpdateWidgetRequestJSONAPIRequestDocument,
    ) -> WidgetSchemaJSONAPIDocument:
        """Create a widget.

        Create a new widget for a given experience type.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :type body: CreateOrUpdateWidgetRequestJSONAPIRequestDocument
        :rtype: WidgetSchemaJSONAPIDocument
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        kwargs["body"] = body

        return self._create_widget_api_v2_widgets_experience_type_post_endpoint.call_with_http_info(**kwargs)

    def delete_widget_api_v2_widgets_experience_type_uuid_delete(
        self,
        uuid: UUID,
        experience_type: WidgetExperienceType,
    ) -> None:
        """Delete a widget.

        Soft-delete a widget by its UUID for a given experience type.

        :param uuid: The UUID of the widget.
        :type uuid: UUID
        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["uuid"] = uuid

        kwargs["experience_type"] = experience_type

        return self._delete_widget_api_v2_widgets_experience_type_uuid_delete_endpoint.call_with_http_info(**kwargs)

    def get_widget_api_v2_widgets_experience_type_uuid_get(
        self,
        uuid: UUID,
        experience_type: WidgetExperienceType,
    ) -> WidgetSchemaJSONAPIDocument:
        """Get a widget.

        Retrieve a widget by its UUID for a given experience type.

        :param uuid: The UUID of the widget.
        :type uuid: UUID
        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :rtype: WidgetSchemaJSONAPIDocument
        """
        kwargs: Dict[str, Any] = {}
        kwargs["uuid"] = uuid

        kwargs["experience_type"] = experience_type

        return self._get_widget_api_v2_widgets_experience_type_uuid_get_endpoint.call_with_http_info(**kwargs)

    def search_widgets_api_v2_widgets_experience_type_get(
        self,
        experience_type: WidgetExperienceType,
    ) -> WidgetSchemaJSONAPIListDocument:
        """Search widgets.

        Search and list widgets for a given experience type. Supports filtering by widget type, creator, title, and tags, as well as sorting and pagination.

        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :rtype: WidgetSchemaJSONAPIListDocument
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experience_type"] = experience_type

        return self._search_widgets_api_v2_widgets_experience_type_get_endpoint.call_with_http_info(**kwargs)

    def update_widget_api_v2_widgets_experience_type_uuid_put(
        self,
        uuid: UUID,
        experience_type: WidgetExperienceType,
        body: CreateOrUpdateWidgetRequestJSONAPIRequestDocument,
    ) -> WidgetSchemaJSONAPIDocument:
        """Update a widget.

        Update a widget by its UUID for a given experience type. This performs a full replacement of the widget definition.

        :param uuid: The UUID of the widget.
        :type uuid: UUID
        :param experience_type: The experience type for the widget.
        :type experience_type: WidgetExperienceType
        :type body: CreateOrUpdateWidgetRequestJSONAPIRequestDocument
        :rtype: WidgetSchemaJSONAPIDocument
        """
        kwargs: Dict[str, Any] = {}
        kwargs["uuid"] = uuid

        kwargs["experience_type"] = experience_type

        kwargs["body"] = body

        return self._update_widget_api_v2_widgets_experience_type_uuid_put_endpoint.call_with_http_info(**kwargs)
