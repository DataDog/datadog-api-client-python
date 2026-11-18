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
    from datadog_api_client.v2.model.segment_delete_data import SegmentDeleteData


class SegmentDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_delete_data import SegmentDeleteData

        return {
            "data": (SegmentDeleteData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SegmentDeleteData, **kwargs):
        """
        Response returned when a segment is deleted.

        :param data: A deleted segment.
        :type data: SegmentDeleteData
        """
        super().__init__(kwargs)

        self_.data = data
