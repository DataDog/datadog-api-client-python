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
    from datadog_api_client.v1_20270101.model.hostmap_projection_dimensions_items import (
        HostmapProjectionDimensionsItems,
    )
    from datadog_api_client.v1_20270101.model.hostmap_projection_type import HostmapProjectionType


class HostmapProjection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.hostmap_projection_dimensions_items import (
            HostmapProjectionDimensionsItems,
        )
        from datadog_api_client.v1_20270101.model.hostmap_projection_type import HostmapProjectionType

        return {
            "dimensions": ([HostmapProjectionDimensionsItems],),
            "type": (HostmapProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(self_, dimensions: List[HostmapProjectionDimensionsItems], type: HostmapProjectionType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [HostmapProjectionDimensionsItems]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: HostmapProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
