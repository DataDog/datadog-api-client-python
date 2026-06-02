# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    file_type,
)
from datadog_api_client.v2.model.stegadography_get_widgets_response import StegadographyGetWidgetsResponse


class StegadographyApi:
    """
    Extract watermarks embedded in dashboard screenshots to retrieve cached widget state.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_stegadography_widgets_endpoint = _Endpoint(
            settings={
                "response_type": (StegadographyGetWidgetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/stegadography/get-widgets",
                "operation_id": "get_stegadography_widgets",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "image": {
                    "required": True,
                    "openapi_types": (file_type,),
                    "attribute": "image",
                    "location": "form",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def get_stegadography_widgets(
        self,
        image: file_type,
    ) -> StegadographyGetWidgetsResponse:
        """Get widgets from an image.

        Extracts watermarks from a PNG image and returns the cached widget data
        associated with each watermark found. The image must be uploaded as a
        ``multipart/form-data`` request with the file in the ``image`` field.
        Only widgets belonging to the authenticated organization are returned.

        :param image: PNG image file to scan for embedded watermarks.
        :type image: file_type
        :rtype: StegadographyGetWidgetsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["image"] = image

        return self._get_stegadography_widgets_endpoint.call_with_http_info(**kwargs)
