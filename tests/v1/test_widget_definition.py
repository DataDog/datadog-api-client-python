# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.alert_graph_widget_definition import AlertGraphWidgetDefinition
from datadog_api_client.v1.model.alert_value_widget_definition import AlertValueWidgetDefinition
from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
from datadog_api_client.v1.model.check_status_widget_definition import CheckStatusWidgetDefinition
from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
from datadog_api_client.v1.model.event_stream_widget_definition import EventStreamWidgetDefinition
from datadog_api_client.v1.model.event_timeline_widget_definition import EventTimelineWidgetDefinition
from datadog_api_client.v1.model.free_text_widget_definition import FreeTextWidgetDefinition
from datadog_api_client.v1.model.geomap_widget_definition import GeomapWidgetDefinition
from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
from datadog_api_client.v1.model.group_widget_definition import GroupWidgetDefinition
from datadog_api_client.v1.model.heat_map_widget_definition import HeatMapWidgetDefinition
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition
from datadog_api_client.v1.model.host_map_widget_definition_style import HostMapWidgetDefinitionStyle
from datadog_api_client.v1.model.i_frame_widget_definition import IFrameWidgetDefinition
from datadog_api_client.v1.model.image_widget_definition import ImageWidgetDefinition
from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
from datadog_api_client.v1.model.monitor_summary_widget_definition import MonitorSummaryWidgetDefinition
from datadog_api_client.v1.model.note_widget_definition import NoteWidgetDefinition
from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition
from datadog_api_client.v1.model.scatter_plot_widget_definition import ScatterPlotWidgetDefinition
from datadog_api_client.v1.model.service_map_widget_definition import ServiceMapWidgetDefinition
from datadog_api_client.v1.model.service_summary_widget_definition import ServiceSummaryWidgetDefinition
from datadog_api_client.v1.model.slo_widget_definition import SLOWidgetDefinition
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition
from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition
from datadog_api_client.v1.model.toplist_widget_definition_type import ToplistWidgetDefinitionType
from datadog_api_client.v1.model.toplist_widget_request import ToplistWidgetRequest
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_color_preference import WidgetColorPreference
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_event import WidgetEvent
from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
from datadog_api_client.v1.model.widget_grouping import WidgetGrouping
from datadog_api_client.v1.model.widget_image_sizing import WidgetImageSizing
from datadog_api_client.v1.model.widget_layout_type import WidgetLayoutType
from datadog_api_client.v1.model.widget_margin import WidgetMargin
from datadog_api_client.v1.model.widget_marker import WidgetMarker
from datadog_api_client.v1.model.widget_message_display import WidgetMessageDisplay
from datadog_api_client.v1.model.widget_monitor_summary_sort import WidgetMonitorSummarySort
from datadog_api_client.v1.model.widget_node_type import WidgetNodeType
from datadog_api_client.v1.model.widget_service_summary_display_format import WidgetServiceSummaryDisplayFormat
from datadog_api_client.v1.model.widget_size_format import WidgetSizeFormat
from datadog_api_client.v1.model.widget_summary_type import WidgetSummaryType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_tick_edge import WidgetTickEdge
from datadog_api_client.v1.model.widget_time import WidgetTime
from datadog_api_client.v1.model.widget_time_windows import WidgetTimeWindows
from datadog_api_client.v1.model.widget_view_mode import WidgetViewMode
from datadog_api_client.v1.model.widget_viz_type import WidgetVizType

globals()["AlertGraphWidgetDefinition"] = AlertGraphWidgetDefinition
globals()["AlertValueWidgetDefinition"] = AlertValueWidgetDefinition
globals()["ChangeWidgetDefinition"] = ChangeWidgetDefinition
globals()["CheckStatusWidgetDefinition"] = CheckStatusWidgetDefinition
globals()["DistributionWidgetDefinition"] = DistributionWidgetDefinition
globals()["EventStreamWidgetDefinition"] = EventStreamWidgetDefinition
globals()["EventTimelineWidgetDefinition"] = EventTimelineWidgetDefinition
globals()["FreeTextWidgetDefinition"] = FreeTextWidgetDefinition
globals()["GeomapWidgetDefinition"] = GeomapWidgetDefinition
globals()["GeomapWidgetDefinitionView"] = GeomapWidgetDefinitionView
globals()["GroupWidgetDefinition"] = GroupWidgetDefinition
globals()["HeatMapWidgetDefinition"] = HeatMapWidgetDefinition
globals()["HostMapWidgetDefinition"] = HostMapWidgetDefinition
globals()["HostMapWidgetDefinitionStyle"] = HostMapWidgetDefinitionStyle
globals()["IFrameWidgetDefinition"] = IFrameWidgetDefinition
globals()["ImageWidgetDefinition"] = ImageWidgetDefinition
globals()["LogStreamWidgetDefinition"] = LogStreamWidgetDefinition
globals()["MonitorSummaryWidgetDefinition"] = MonitorSummaryWidgetDefinition
globals()["NoteWidgetDefinition"] = NoteWidgetDefinition
globals()["QueryValueWidgetDefinition"] = QueryValueWidgetDefinition
globals()["SLOWidgetDefinition"] = SLOWidgetDefinition
globals()["ScatterPlotWidgetDefinition"] = ScatterPlotWidgetDefinition
globals()["ServiceMapWidgetDefinition"] = ServiceMapWidgetDefinition
globals()["ServiceSummaryWidgetDefinition"] = ServiceSummaryWidgetDefinition
globals()["TableWidgetDefinition"] = TableWidgetDefinition
globals()["TableWidgetHasSearchBar"] = TableWidgetHasSearchBar
globals()["TimeseriesWidgetDefinition"] = TimeseriesWidgetDefinition
globals()["ToplistWidgetDefinition"] = ToplistWidgetDefinition
globals()["ToplistWidgetDefinitionType"] = ToplistWidgetDefinitionType
globals()["ToplistWidgetRequest"] = ToplistWidgetRequest
globals()["Widget"] = Widget
globals()["WidgetAxis"] = WidgetAxis
globals()["WidgetColorPreference"] = WidgetColorPreference
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetEvent"] = WidgetEvent
globals()["WidgetEventSize"] = WidgetEventSize
globals()["WidgetGrouping"] = WidgetGrouping
globals()["WidgetImageSizing"] = WidgetImageSizing
globals()["WidgetLayoutType"] = WidgetLayoutType
globals()["WidgetMargin"] = WidgetMargin
globals()["WidgetMarker"] = WidgetMarker
globals()["WidgetMessageDisplay"] = WidgetMessageDisplay
globals()["WidgetMonitorSummarySort"] = WidgetMonitorSummarySort
globals()["WidgetNodeType"] = WidgetNodeType
globals()["WidgetServiceSummaryDisplayFormat"] = WidgetServiceSummaryDisplayFormat
globals()["WidgetSizeFormat"] = WidgetSizeFormat
globals()["WidgetSummaryType"] = WidgetSummaryType
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTickEdge"] = WidgetTickEdge
globals()["WidgetTime"] = WidgetTime
globals()["WidgetTimeWindows"] = WidgetTimeWindows
globals()["WidgetViewMode"] = WidgetViewMode
globals()["WidgetVizType"] = WidgetVizType
from datadog_api_client.v1.model.widget_definition import WidgetDefinition


class TestWidgetDefinition(unittest.TestCase):
    """WidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetDefinition(self):
        """Test WidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
