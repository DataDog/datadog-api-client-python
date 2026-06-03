# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    file_type,
)


class StegadographyGetWidgetsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "image": (file_type,),
        }

    attribute_map = {
        "image": "image",
    }

    def __init__(self_, image: file_type, **kwargs):
        """
        Multipart form data containing the PNG image to scan for watermarks.

        :param image: PNG image file to scan for embedded watermarks.
        :type image: file_type
        """
        super().__init__(kwargs)

        self_.image = image
