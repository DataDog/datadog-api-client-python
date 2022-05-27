# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ScatterPlotWidgetDefinitionRequests(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.scatterplot_table_request import ScatterplotTableRequest
        from datadog_api_client.v1.model.scatter_plot_request import ScatterPlotRequest

        return {
            "table": (ScatterplotTableRequest,),
            "x": (ScatterPlotRequest,),
            "y": (ScatterPlotRequest,),
        }

    attribute_map = {
        "table": "table",
        "x": "x",
        "y": "y",
    }

    def __init__(self, *args, **kwargs):
        """
        Widget definition.

        :param table: Scatterplot request containing formulas and functions.
        :type table: ScatterplotTableRequest, optional

        :param x: Updated scatter plot.
        :type x: ScatterPlotRequest, optional

        :param y: Updated scatter plot.
        :type y: ScatterPlotRequest, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ScatterPlotWidgetDefinitionRequests, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
