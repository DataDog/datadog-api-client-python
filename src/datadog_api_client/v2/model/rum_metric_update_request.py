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
    from datadog_api_client.v2.model.rum_metric_update_data import RumMetricUpdateData


class RumMetricUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_update_data import RumMetricUpdateData

        return {
            "data": (RumMetricUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RumMetricUpdateData, **kwargs):
        """
        The RUM-based metric update body.

        :param data: The RUM-based metric properties to update. ``id`` is required by the API and must match the ``metric_id`` path parameter.
        :type data: RumMetricUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
