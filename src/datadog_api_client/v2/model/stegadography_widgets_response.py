# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.stegadography_widget_data import StegadographyWidgetData


class StegadographyWidgetsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stegadography_widget_data import StegadographyWidgetData

        return {
            "data": ([StegadographyWidgetData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[StegadographyWidgetData], **kwargs):
        """
        Response containing the widgets recovered from the uploaded image.

        :param data: List of widgets matched to watermarks found in the image.
        :type data: [StegadographyWidgetData]
        """
        super().__init__(kwargs)

        self_.data = data
