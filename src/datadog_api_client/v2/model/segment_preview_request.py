# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.segment_preview_data import SegmentPreviewData


class SegmentPreviewRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_preview_data import SegmentPreviewData

        return {
            "data": (SegmentPreviewData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SegmentPreviewData, **kwargs):
        """
        Request to preview the members of a segment definition.

        :param data: Data of the segment preview request.
        :type data: SegmentPreviewData
        """
        super().__init__(kwargs)

        self_.data = data
