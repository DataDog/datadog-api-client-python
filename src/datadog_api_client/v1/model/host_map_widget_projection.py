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
    from datadog_api_client.v1.model.host_map_widget_projection_dimension_mapping import (
        HostMapWidgetProjectionDimensionMapping,
    )
    from datadog_api_client.v1.model.host_map_widget_projection_type import HostMapWidgetProjectionType


class HostMapWidgetProjection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_map_widget_projection_dimension_mapping import (
            HostMapWidgetProjectionDimensionMapping,
        )
        from datadog_api_client.v1.model.host_map_widget_projection_type import HostMapWidgetProjectionType

        return {
            "dimensions": ([HostMapWidgetProjectionDimensionMapping],),
            "type": (HostMapWidgetProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(
        self_, dimensions: List[HostMapWidgetProjectionDimensionMapping], type: HostMapWidgetProjectionType, **kwargs
    ):
        """
        Projection for the DDSQL host map request. Maps dataset columns to map dimensions: ``node`` identifies the entity, repeated ``group`` entries define the grouping hierarchy (outermost first), and ``fill`` / ``size`` drive the tile color and size.

        :param dimensions: List of column-to-dimension mappings for the projection.
        :type dimensions: [HostMapWidgetProjectionDimensionMapping]

        :param type: Type of the host map projection.
        :type type: HostMapWidgetProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
