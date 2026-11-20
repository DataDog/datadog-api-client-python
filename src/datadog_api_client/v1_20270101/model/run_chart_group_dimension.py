# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.run_chart_group_dimension_dimension import RunChartGroupDimensionDimension


class RunChartGroupDimension(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.run_chart_group_dimension_dimension import (
            RunChartGroupDimensionDimension,
        )

        return {
            "alias": (str,),
            "column": (str,),
            "dimension": (RunChartGroupDimensionDimension,),
        }

    attribute_map = {
        "alias": "alias",
        "column": "column",
        "dimension": "dimension",
    }

    def __init__(
        self_, column: str, dimension: RunChartGroupDimensionDimension, alias: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: RunChartGroupDimensionDimension
        """
        if alias is not unset:
            kwargs["alias"] = alias
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
