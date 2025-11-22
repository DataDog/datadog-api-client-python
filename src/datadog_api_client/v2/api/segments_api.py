# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.segment_array import SegmentArray
from datadog_api_client.v2.model.segment import Segment


class SegmentsApi:
    """
    API for segments.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_segment_endpoint = _Endpoint(
            settings={
                "response_type": (Segment,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/segment",
                "operation_id": "create_rum_segment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Segment,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._initialize_rum_segments_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": [],
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
                "response_type": (SegmentArray,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/segment",
                "operation_id": "list_rum_segments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_rum_segment(
        self,
        body: Segment,
    ) -> Segment:
        """Create rum segment.

        Create a new user segment for audience targeting

        :type body: Segment
        :rtype: Segment
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_segment_endpoint.call_with_http_info(**kwargs)

    def initialize_rum_segments(
        self,
    ) -> None:
        """Initialize rum segments.

        Initialize default segments for a new organization

        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        return self._initialize_rum_segments_endpoint.call_with_http_info(**kwargs)

    def list_rum_segments(
        self,
    ) -> SegmentArray:
        """List rum segments.

        List all available user segments for audience targeting

        :rtype: SegmentArray
        """
        kwargs: Dict[str, Any] = {}
        return self._list_rum_segments_endpoint.call_with_http_info(**kwargs)
