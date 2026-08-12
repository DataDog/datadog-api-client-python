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
    from datadog_api_client.v1.model.scatterplot_data_projection_dimension import ScatterplotDataProjectionDimension
    from datadog_api_client.v1.model.scatterplot_data_projection_projection_type import (
        ScatterplotDataProjectionProjectionType,
    )


class ScatterplotDataProjectionProjection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.scatterplot_data_projection_dimension import ScatterplotDataProjectionDimension
        from datadog_api_client.v1.model.scatterplot_data_projection_projection_type import (
            ScatterplotDataProjectionProjectionType,
        )

        return {
            "dimensions": ([ScatterplotDataProjectionDimension],),
            "type": (ScatterplotDataProjectionProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(
        self_,
        dimensions: List[ScatterplotDataProjectionDimension],
        type: ScatterplotDataProjectionProjectionType,
        **kwargs,
    ):
        """
        The projection configuration for a scatterplot data projection request.

        :param dimensions: Dimension mappings for the scatterplot axes.
        :type dimensions: [ScatterplotDataProjectionDimension]

        :param type: The type of the scatterplot data projection.
        :type type: ScatterplotDataProjectionProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
