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
    from datadog_api_client.v2.model.synthetics_downtime_data import SyntheticsDowntimeData


class SyntheticsDowntimeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_data import SyntheticsDowntimeData

        return {
            "data": (SyntheticsDowntimeData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SyntheticsDowntimeData, **kwargs):
        """
        Response containing a single Synthetics downtime.

        :param data: A Synthetics downtime object.
        :type data: SyntheticsDowntimeData
        """
        super().__init__(kwargs)

        self_.data = data
