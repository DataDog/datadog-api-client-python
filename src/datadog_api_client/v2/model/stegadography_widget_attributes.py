# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class StegadographyWidgetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "locationx": (int,),
            "locationy": (int,),
            "raw_data": (str,),
            "watermark": (str,),
        }

    attribute_map = {
        "locationx": "locationx",
        "locationy": "locationy",
        "raw_data": "rawData",
        "watermark": "watermark",
    }

    def __init__(self_, locationx: int, locationy: int, raw_data: str, watermark: str, **kwargs):
        """
        Attributes of a watermarked widget recovered from an image.

        :param locationx: Horizontal pixel coordinate where the watermark was found in the image.
        :type locationx: int

        :param locationy: Vertical pixel coordinate where the watermark was found in the image.
        :type locationy: int

        :param raw_data: JSON-encoded string representing the widget state.
        :type raw_data: str

        :param watermark: Hex-encoded watermark string identifying the widget.
        :type watermark: str
        """
        super().__init__(kwargs)

        self_.locationx = locationx
        self_.locationy = locationy
        self_.raw_data = raw_data
        self_.watermark = watermark
