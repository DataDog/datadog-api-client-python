# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.run_chart_projection_dimension import RunChartProjectionDimension
    from datadog_api_client.v1_20270101.model.run_chart_projection_type import RunChartProjectionType
    from datadog_api_client.v1_20270101.model.run_chart_x_dimension import RunChartXDimension
    from datadog_api_client.v1_20270101.model.run_chart_value_dimension import RunChartValueDimension
    from datadog_api_client.v1_20270101.model.run_chart_group_dimension import RunChartGroupDimension


class RunChartProjection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.run_chart_projection_dimension import RunChartProjectionDimension
        from datadog_api_client.v1_20270101.model.run_chart_projection_type import RunChartProjectionType

        return {
            "dimensions": ([RunChartProjectionDimension],),
            "type": (RunChartProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(
        self_,
        dimensions: List[
            Union[RunChartProjectionDimension, RunChartXDimension, RunChartValueDimension, RunChartGroupDimension]
        ],
        type: RunChartProjectionType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [RunChartProjectionDimension]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: RunChartProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
