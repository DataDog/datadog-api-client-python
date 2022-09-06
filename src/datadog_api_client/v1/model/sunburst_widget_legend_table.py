# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SunburstWidgetLegendTable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.sunburst_widget_legend_table_type import SunburstWidgetLegendTableType

        return {
            "type": (SunburstWidgetLegendTableType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type, *args, **kwargs):
        """
        Configuration of table-based legend.

        :param type: Whether or not to show a table legend.
        :type type: SunburstWidgetLegendTableType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.type = type
