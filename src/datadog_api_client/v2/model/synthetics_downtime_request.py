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
    from datadog_api_client.v2.model.synthetics_downtime_data_request import SyntheticsDowntimeDataRequest


class SyntheticsDowntimeRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_data_request import SyntheticsDowntimeDataRequest

        return {
            "data": (SyntheticsDowntimeDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SyntheticsDowntimeDataRequest, **kwargs):
        """
        Request body for creating or updating a Synthetics downtime.

        :param data: The data object for a Synthetics downtime create or update request.
        :type data: SyntheticsDowntimeDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
