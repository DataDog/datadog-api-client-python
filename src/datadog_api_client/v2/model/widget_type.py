# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetType(ModelSimple):
    """
    Widget types that are allowed to be stored as individual records in the 'widget' PG table.

        This is not a complete list of dashboards/notebooks widget types.

    :param value: Must be one of ["bar_chart", "change", "cloud_cost_summary", "cohort", "funnel", "geomap", "list_stream", "query_table", "query_value", "retention_curve", "sankey", "sunburst", "timeseries", "toplist", "treemap"].
    :type value: str
    """

    allowed_values = {
        "bar_chart",
        "change",
        "cloud_cost_summary",
        "cohort",
        "funnel",
        "geomap",
        "list_stream",
        "query_table",
        "query_value",
        "retention_curve",
        "sankey",
        "sunburst",
        "timeseries",
        "toplist",
        "treemap",
    }
    BAR_CHART: ClassVar["WidgetType"]
    CHANGE: ClassVar["WidgetType"]
    CLOUD_COST_SUMMARY: ClassVar["WidgetType"]
    COHORT: ClassVar["WidgetType"]
    FUNNEL: ClassVar["WidgetType"]
    GEOMAP: ClassVar["WidgetType"]
    LIST_STREAM: ClassVar["WidgetType"]
    QUERY_TABLE: ClassVar["WidgetType"]
    QUERY_VALUE: ClassVar["WidgetType"]
    RETENTION_CURVE: ClassVar["WidgetType"]
    SANKEY: ClassVar["WidgetType"]
    SUNBURST: ClassVar["WidgetType"]
    TIMESERIES: ClassVar["WidgetType"]
    TOPLIST: ClassVar["WidgetType"]
    TREEMAP: ClassVar["WidgetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetType.BAR_CHART = WidgetType("bar_chart")
WidgetType.CHANGE = WidgetType("change")
WidgetType.CLOUD_COST_SUMMARY = WidgetType("cloud_cost_summary")
WidgetType.COHORT = WidgetType("cohort")
WidgetType.FUNNEL = WidgetType("funnel")
WidgetType.GEOMAP = WidgetType("geomap")
WidgetType.LIST_STREAM = WidgetType("list_stream")
WidgetType.QUERY_TABLE = WidgetType("query_table")
WidgetType.QUERY_VALUE = WidgetType("query_value")
WidgetType.RETENTION_CURVE = WidgetType("retention_curve")
WidgetType.SANKEY = WidgetType("sankey")
WidgetType.SUNBURST = WidgetType("sunburst")
WidgetType.TIMESERIES = WidgetType("timeseries")
WidgetType.TOPLIST = WidgetType("toplist")
WidgetType.TREEMAP = WidgetType("treemap")
