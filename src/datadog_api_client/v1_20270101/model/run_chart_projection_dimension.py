# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class RunChartProjectionDimension(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: RunChartXDimensionDimension

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RunChartLineStyle, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.run_chart_x_dimension import RunChartXDimension
        from datadog_api_client.v1_20270101.model.run_chart_value_dimension import RunChartValueDimension
        from datadog_api_client.v1_20270101.model.run_chart_group_dimension import RunChartGroupDimension

        return {
            "oneOf": [
                RunChartXDimension,
                RunChartValueDimension,
                RunChartGroupDimension,
            ],
        }
