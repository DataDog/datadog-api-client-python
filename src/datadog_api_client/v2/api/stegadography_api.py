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
)
from datadog_api_client.v2.model.stegadography_widgets_response import StegadographyWidgetsResponse


class StegadographyApi:
    """
    Recover dashboard widget data from watermarks embedded in images.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_widgets_from_image_endpoint = _Endpoint(
            settings={
                "response_type": (StegadographyWidgetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/stegadography/get-widgets",
                "operation_id": "get_widgets_from_image",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "image": {
                    "openapi_types": (file_type,),
                    "attribute": "image",
                    "location": "form",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["multipart/form-data"]},
            api_client=api_client,
        )

    def get_widgets_from_image(
        self,
        *,
        image: Union[file_type, UnsetType] = unset,
    ) -> StegadographyWidgetsResponse:
        """Get widgets from an image.

        Extracts embedded watermarks from an uploaded PNG image (for example, a dashboard screenshot)
        and returns the cached widget state matching each watermark found.

        :param image: A PNG image (for example, a dashboard screenshot) containing embedded widget watermarks.
        :type image: file_type, optional
        :rtype: StegadographyWidgetsResponse
        """
        kwargs: Dict[str, Any] = {}
        if image is not unset:
            kwargs["image"] = image

        return self._get_widgets_from_image_endpoint.call_with_http_info(**kwargs)
