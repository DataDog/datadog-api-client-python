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
from datadog_api_client.v2.model.rum_segment_list_response import RumSegmentListResponse
from datadog_api_client.v2.model.rum_segment_response import RumSegmentResponse
from datadog_api_client.v2.model.rum_segment_create_request import RumSegmentCreateRequest
from datadog_api_client.v2.model.rum_static_segment_create_request import RumStaticSegmentCreateRequest
from datadog_api_client.v2.model.rum_segment_template_list_response import RumSegmentTemplateListResponse
from datadog_api_client.v2.model.rum_segment_delete_response import RumSegmentDeleteResponse
from datadog_api_client.v2.model.rum_segment_update_request import RumSegmentUpdateRequest


class RUMUserSegmentsApi:
    """
    Manage RUM user segments for audience targeting and analysis.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_segment_endpoint = _Endpoint(
            settings={
                "response_type": (RumSegmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment",
                "operation_id": "create_rum_segment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumSegmentCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_rum_static_segment_endpoint = _Endpoint(
            settings={
                "response_type": (RumSegmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment/static",
                "operation_id": "create_rum_static_segment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumStaticSegmentCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rum_segment_endpoint = _Endpoint(
            settings={
                "response_type": (RumSegmentDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment/{segment_id}",
                "operation_id": "delete_rum_segment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "segment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "segment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_rum_segment_endpoint = _Endpoint(
            settings={
                "response_type": (RumSegmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment/{segment_id}",
                "operation_id": "get_rum_segment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "segment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "segment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._initialize_rum_segments_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment/initialize",
                "operation_id": "initialize_rum_segments",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._list_rum_segments_endpoint = _Endpoint(
            settings={
                "response_type": (RumSegmentListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment",
                "operation_id": "list_rum_segments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_segment_templates_endpoint = _Endpoint(
            settings={
                "response_type": (RumSegmentTemplateListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment/templates",
                "operation_id": "list_rum_segment_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_segment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/segment/{segment_id}",
                "operation_id": "update_rum_segment",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "segment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "segment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumSegmentUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_rum_segment(
        self,
        body: RumSegmentCreateRequest,
    ) -> RumSegmentResponse:
        """Create a RUM segment.

        Create a new user segment for the current organization.

        :type body: RumSegmentCreateRequest
        :rtype: RumSegmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_segment_endpoint.call_with_http_info(**kwargs)

    def create_rum_static_segment(
        self,
        body: RumStaticSegmentCreateRequest,
    ) -> RumSegmentResponse:
        """Create a static RUM segment.

        Create a new static user segment from a journey query. Static segments contain a fixed list of users computed from the query at creation time.

        :type body: RumStaticSegmentCreateRequest
        :rtype: RumSegmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_static_segment_endpoint.call_with_http_info(**kwargs)

    def delete_rum_segment(
        self,
        segment_id: str,
    ) -> RumSegmentDeleteResponse:
        """Delete a RUM segment.

        Delete a user segment by its identifier.

        :param segment_id: The identifier of the segment.
        :type segment_id: str
        :rtype: RumSegmentDeleteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["segment_id"] = segment_id

        return self._delete_rum_segment_endpoint.call_with_http_info(**kwargs)

    def get_rum_segment(
        self,
        segment_id: str,
    ) -> RumSegmentResponse:
        """Get a RUM segment.

        Get a specific user segment by its identifier.

        :param segment_id: The identifier of the segment.
        :type segment_id: str
        :rtype: RumSegmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["segment_id"] = segment_id

        return self._get_rum_segment_endpoint.call_with_http_info(**kwargs)

    def initialize_rum_segments(
        self,
    ) -> None:
        """Initialize RUM segments.

        Initialize default segments for the current organization. This creates a set of predefined segments if they do not already exist.

        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        return self._initialize_rum_segments_endpoint.call_with_http_info(**kwargs)

    def list_rum_segments(
        self,
        *,
        sort: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> RumSegmentListResponse:
        """List all RUM segments.

        List all user segments for the current organization. Supports sorting and pagination.

        :param sort: Sort order for the segments list.
        :type sort: str, optional
        :param limit: Maximum number of segments to return.
        :type limit: int, optional
        :rtype: RumSegmentListResponse
        """
        kwargs: Dict[str, Any] = {}
        if sort is not unset:
            kwargs["sort"] = sort

        if limit is not unset:
            kwargs["limit"] = limit

        return self._list_rum_segments_endpoint.call_with_http_info(**kwargs)

    def list_rum_segment_templates(
        self,
    ) -> RumSegmentTemplateListResponse:
        """List RUM segment templates.

        List all available segment templates. Templates provide predefined segment configurations that can be customized with parameters.

        :rtype: RumSegmentTemplateListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_rum_segment_templates_endpoint.call_with_http_info(**kwargs)

    def update_rum_segment(
        self,
        segment_id: str,
        body: RumSegmentUpdateRequest,
    ) -> None:
        """Update a RUM segment.

        Update an existing user segment. All fields in the request body are optional.

        :param segment_id: The identifier of the segment.
        :type segment_id: str
        :type body: RumSegmentUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["segment_id"] = segment_id

        kwargs["body"] = body

        return self._update_rum_segment_endpoint.call_with_http_info(**kwargs)
