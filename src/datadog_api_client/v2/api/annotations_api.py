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
from datadog_api_client.v2.model.annotations_response import AnnotationsResponse
from datadog_api_client.v2.model.annotation_response import AnnotationResponse
from datadog_api_client.v2.model.annotation_create_request import AnnotationCreateRequest
from datadog_api_client.v2.model.page_annotations_response import PageAnnotationsResponse
from datadog_api_client.v2.model.annotation_update_request import AnnotationUpdateRequest


class AnnotationsApi:
    """
    Add annotations to dashboards and notebooks to mark events such as deployments, incidents, or other notable moments in time.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_annotation_endpoint = _Endpoint(
            settings={
                "response_type": (AnnotationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/annotation",
                "operation_id": "create_annotation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AnnotationCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_annotation_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/annotation/{annotation_id}",
                "operation_id": "delete_annotation",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "annotation_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "annotation_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_page_annotations_endpoint = _Endpoint(
            settings={
                "response_type": (PageAnnotationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/annotation/page/{page_id}",
                "operation_id": "get_page_annotations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "page_id",
                    "location": "path",
                },
                "start_time": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "start_time",
                    "location": "query",
                },
                "end_time": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "end_time",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_annotations_endpoint = _Endpoint(
            settings={
                "response_type": (AnnotationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/annotation",
                "operation_id": "list_annotations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "page_id",
                    "location": "query",
                },
                "start_time": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "start_time",
                    "location": "query",
                },
                "end_time": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "end_time",
                    "location": "query",
                },
                "widget_id": {
                    "openapi_types": (str,),
                    "attribute": "widget_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_annotation_endpoint = _Endpoint(
            settings={
                "response_type": (AnnotationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/annotation/{annotation_id}",
                "operation_id": "update_annotation",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "annotation_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "annotation_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AnnotationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_annotation(
        self,
        body: AnnotationCreateRequest,
    ) -> AnnotationResponse:
        """Create an annotation.

        Creates a new annotation on a dashboard or notebook page.
        Valid ``color`` values: ``gray`` , ``blue`` , ``purple`` , ``green`` , ``yellow`` , ``red``.
        Valid ``type`` values: ``pointInTime`` (marks a single moment) or ``timeRegion`` (spans a range and requires ``end_time`` ).

        :param body: Annotation to create.
        :type body: AnnotationCreateRequest
        :rtype: AnnotationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_annotation_endpoint.call_with_http_info(**kwargs)

    def delete_annotation(
        self,
        annotation_id: UUID,
    ) -> None:
        """Delete an annotation.

        Deletes an existing annotation by ID.
        Returns ``204 No Content`` if the annotation does not exist (idempotent).

        :param annotation_id: The ID of the annotation.
        :type annotation_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["annotation_id"] = annotation_id

        return self._delete_annotation_endpoint.call_with_http_info(**kwargs)

    def get_page_annotations(
        self,
        page_id: str,
        start_time: int,
        end_time: int,
    ) -> PageAnnotationsResponse:
        """Get annotations for a page.

        Returns all annotations on a specific page for a given time window, grouped by widget.
        Unlike ``ListAnnotations`` , this endpoint returns a single structured object with annotations
        indexed by their ID and a widget-to-annotation mapping for easy UI rendering.

        :param page_id: The ID of the page, prefixed with the page type and joined by a colon
            (for example, ``dashboard:abc-def-xyz`` or ``notebook:1234567890`` ).
        :type page_id: str
        :param start_time: Start of the time window in milliseconds since the Unix epoch.
        :type start_time: int
        :param end_time: End of the time window in milliseconds since the Unix epoch.
        :type end_time: int
        :rtype: PageAnnotationsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["start_time"] = start_time

        kwargs["end_time"] = end_time

        return self._get_page_annotations_endpoint.call_with_http_info(**kwargs)

    def list_annotations(
        self,
        page_id: str,
        start_time: int,
        end_time: int,
        *,
        widget_id: Union[str, UnsetType] = unset,
    ) -> AnnotationsResponse:
        """List annotations.

        Returns a flat list of annotations matching the given page, time window, and optional widget filter.

        :param page_id: ID of the page to list annotations for, prefixed with the page type and joined by a colon
            (for example, ``dashboard:abc-def-xyz`` or ``notebook:1234567890`` ).
        :type page_id: str
        :param start_time: Start of the time window in milliseconds since the Unix epoch.
        :type start_time: int
        :param end_time: End of the time window in milliseconds since the Unix epoch.
        :type end_time: int
        :param widget_id: Optional widget ID to restrict results to annotations on a specific widget.
        :type widget_id: str, optional
        :rtype: AnnotationsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        kwargs["start_time"] = start_time

        kwargs["end_time"] = end_time

        if widget_id is not unset:
            kwargs["widget_id"] = widget_id

        return self._list_annotations_endpoint.call_with_http_info(**kwargs)

    def update_annotation(
        self,
        annotation_id: UUID,
        body: AnnotationUpdateRequest,
    ) -> AnnotationResponse:
        """Update an annotation.

        Updates an existing annotation.
        Valid ``color`` values: ``gray`` , ``blue`` , ``purple`` , ``green`` , ``yellow`` , ``red``.
        Valid ``type`` values: ``pointInTime`` (marks a single moment) or ``timeRegion`` (spans a range and requires ``end_time`` ).

        :param annotation_id: The ID of the annotation.
        :type annotation_id: UUID
        :param body: Updated annotation payload.
        :type body: AnnotationUpdateRequest
        :rtype: AnnotationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["annotation_id"] = annotation_id

        kwargs["body"] = body

        return self._update_annotation_endpoint.call_with_http_info(**kwargs)
