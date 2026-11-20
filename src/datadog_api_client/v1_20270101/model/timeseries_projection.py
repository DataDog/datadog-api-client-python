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
    from datadog_api_client.v1_20270101.model.timeseries_projection_dimensions_items import (
        TimeseriesProjectionDimensionsItems,
    )
    from datadog_api_client.v1_20270101.model.timeseries_projection_type import TimeseriesProjectionType


class TimeseriesProjection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.timeseries_projection_dimensions_items import (
            TimeseriesProjectionDimensionsItems,
        )
        from datadog_api_client.v1_20270101.model.timeseries_projection_type import TimeseriesProjectionType

        return {
            "dimensions": ([TimeseriesProjectionDimensionsItems],),
            "type": (TimeseriesProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(
        self_, dimensions: List[TimeseriesProjectionDimensionsItems], type: TimeseriesProjectionType, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [TimeseriesProjectionDimensionsItems]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TimeseriesProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
