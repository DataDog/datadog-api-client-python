# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import alert_graph_widget_definition
except ImportError:
    alert_graph_widget_definition = sys.modules[
        'datadog_api_client.v1.model.alert_graph_widget_definition']
try:
    from datadog_api_client.v1.model import alert_value_widget_definition
except ImportError:
    alert_value_widget_definition = sys.modules[
        'datadog_api_client.v1.model.alert_value_widget_definition']
try:
    from datadog_api_client.v1.model import change_widget_definition
except ImportError:
    change_widget_definition = sys.modules[
        'datadog_api_client.v1.model.change_widget_definition']
try:
    from datadog_api_client.v1.model import check_status_widget_definition
except ImportError:
    check_status_widget_definition = sys.modules[
        'datadog_api_client.v1.model.check_status_widget_definition']
try:
    from datadog_api_client.v1.model import distribution_widget_definition
except ImportError:
    distribution_widget_definition = sys.modules[
        'datadog_api_client.v1.model.distribution_widget_definition']
try:
    from datadog_api_client.v1.model import event_stream_widget_definition
except ImportError:
    event_stream_widget_definition = sys.modules[
        'datadog_api_client.v1.model.event_stream_widget_definition']
try:
    from datadog_api_client.v1.model import event_timeline_widget_definition
except ImportError:
    event_timeline_widget_definition = sys.modules[
        'datadog_api_client.v1.model.event_timeline_widget_definition']
try:
    from datadog_api_client.v1.model import free_text_widget_definition
except ImportError:
    free_text_widget_definition = sys.modules[
        'datadog_api_client.v1.model.free_text_widget_definition']
try:
    from datadog_api_client.v1.model import group_widget_definition
except ImportError:
    group_widget_definition = sys.modules[
        'datadog_api_client.v1.model.group_widget_definition']
try:
    from datadog_api_client.v1.model import heat_map_widget_definition
except ImportError:
    heat_map_widget_definition = sys.modules[
        'datadog_api_client.v1.model.heat_map_widget_definition']
try:
    from datadog_api_client.v1.model import host_map_widget_definition
except ImportError:
    host_map_widget_definition = sys.modules[
        'datadog_api_client.v1.model.host_map_widget_definition']
try:
    from datadog_api_client.v1.model import host_map_widget_definition_style
except ImportError:
    host_map_widget_definition_style = sys.modules[
        'datadog_api_client.v1.model.host_map_widget_definition_style']
try:
    from datadog_api_client.v1.model import i_frame_widget_definition
except ImportError:
    i_frame_widget_definition = sys.modules[
        'datadog_api_client.v1.model.i_frame_widget_definition']
try:
    from datadog_api_client.v1.model import image_widget_definition
except ImportError:
    image_widget_definition = sys.modules[
        'datadog_api_client.v1.model.image_widget_definition']
try:
    from datadog_api_client.v1.model import log_stream_widget_definition
except ImportError:
    log_stream_widget_definition = sys.modules[
        'datadog_api_client.v1.model.log_stream_widget_definition']
try:
    from datadog_api_client.v1.model import monitor_summary_widget_definition
except ImportError:
    monitor_summary_widget_definition = sys.modules[
        'datadog_api_client.v1.model.monitor_summary_widget_definition']
try:
    from datadog_api_client.v1.model import note_widget_definition
except ImportError:
    note_widget_definition = sys.modules[
        'datadog_api_client.v1.model.note_widget_definition']
try:
    from datadog_api_client.v1.model import query_value_widget_definition
except ImportError:
    query_value_widget_definition = sys.modules[
        'datadog_api_client.v1.model.query_value_widget_definition']
try:
    from datadog_api_client.v1.model import scatter_plot_widget_definition
except ImportError:
    scatter_plot_widget_definition = sys.modules[
        'datadog_api_client.v1.model.scatter_plot_widget_definition']
try:
    from datadog_api_client.v1.model import service_map_widget_definition
except ImportError:
    service_map_widget_definition = sys.modules[
        'datadog_api_client.v1.model.service_map_widget_definition']
try:
    from datadog_api_client.v1.model import service_summary_widget_definition
except ImportError:
    service_summary_widget_definition = sys.modules[
        'datadog_api_client.v1.model.service_summary_widget_definition']
try:
    from datadog_api_client.v1.model import slo_widget_definition
except ImportError:
    slo_widget_definition = sys.modules[
        'datadog_api_client.v1.model.slo_widget_definition']
try:
    from datadog_api_client.v1.model import table_widget_definition
except ImportError:
    table_widget_definition = sys.modules[
        'datadog_api_client.v1.model.table_widget_definition']
try:
    from datadog_api_client.v1.model import timeseries_widget_definition
except ImportError:
    timeseries_widget_definition = sys.modules[
        'datadog_api_client.v1.model.timeseries_widget_definition']
try:
    from datadog_api_client.v1.model import toplist_widget_definition
except ImportError:
    toplist_widget_definition = sys.modules[
        'datadog_api_client.v1.model.toplist_widget_definition']
try:
    from datadog_api_client.v1.model import toplist_widget_definition_type
except ImportError:
    toplist_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.toplist_widget_definition_type']
try:
    from datadog_api_client.v1.model import toplist_widget_request
except ImportError:
    toplist_widget_request = sys.modules[
        'datadog_api_client.v1.model.toplist_widget_request']
try:
    from datadog_api_client.v1.model import widget
except ImportError:
    widget = sys.modules[
        'datadog_api_client.v1.model.widget']
try:
    from datadog_api_client.v1.model import widget_axis
except ImportError:
    widget_axis = sys.modules[
        'datadog_api_client.v1.model.widget_axis']
try:
    from datadog_api_client.v1.model import widget_color_preference
except ImportError:
    widget_color_preference = sys.modules[
        'datadog_api_client.v1.model.widget_color_preference']
try:
    from datadog_api_client.v1.model import widget_event
except ImportError:
    widget_event = sys.modules[
        'datadog_api_client.v1.model.widget_event']
try:
    from datadog_api_client.v1.model import widget_event_size
except ImportError:
    widget_event_size = sys.modules[
        'datadog_api_client.v1.model.widget_event_size']
try:
    from datadog_api_client.v1.model import widget_grouping
except ImportError:
    widget_grouping = sys.modules[
        'datadog_api_client.v1.model.widget_grouping']
try:
    from datadog_api_client.v1.model import widget_image_sizing
except ImportError:
    widget_image_sizing = sys.modules[
        'datadog_api_client.v1.model.widget_image_sizing']
try:
    from datadog_api_client.v1.model import widget_layout_type
except ImportError:
    widget_layout_type = sys.modules[
        'datadog_api_client.v1.model.widget_layout_type']
try:
    from datadog_api_client.v1.model import widget_margin
except ImportError:
    widget_margin = sys.modules[
        'datadog_api_client.v1.model.widget_margin']
try:
    from datadog_api_client.v1.model import widget_marker
except ImportError:
    widget_marker = sys.modules[
        'datadog_api_client.v1.model.widget_marker']
try:
    from datadog_api_client.v1.model import widget_message_display
except ImportError:
    widget_message_display = sys.modules[
        'datadog_api_client.v1.model.widget_message_display']
try:
    from datadog_api_client.v1.model import widget_monitor_summary_sort
except ImportError:
    widget_monitor_summary_sort = sys.modules[
        'datadog_api_client.v1.model.widget_monitor_summary_sort']
try:
    from datadog_api_client.v1.model import widget_node_type
except ImportError:
    widget_node_type = sys.modules[
        'datadog_api_client.v1.model.widget_node_type']
try:
    from datadog_api_client.v1.model import widget_service_summary_display_format
except ImportError:
    widget_service_summary_display_format = sys.modules[
        'datadog_api_client.v1.model.widget_service_summary_display_format']
try:
    from datadog_api_client.v1.model import widget_size_format
except ImportError:
    widget_size_format = sys.modules[
        'datadog_api_client.v1.model.widget_size_format']
try:
    from datadog_api_client.v1.model import widget_summary_type
except ImportError:
    widget_summary_type = sys.modules[
        'datadog_api_client.v1.model.widget_summary_type']
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules[
        'datadog_api_client.v1.model.widget_text_align']
try:
    from datadog_api_client.v1.model import widget_tick_edge
except ImportError:
    widget_tick_edge = sys.modules[
        'datadog_api_client.v1.model.widget_tick_edge']
try:
    from datadog_api_client.v1.model import widget_time
except ImportError:
    widget_time = sys.modules[
        'datadog_api_client.v1.model.widget_time']
try:
    from datadog_api_client.v1.model import widget_time_windows
except ImportError:
    widget_time_windows = sys.modules[
        'datadog_api_client.v1.model.widget_time_windows']
try:
    from datadog_api_client.v1.model import widget_view_mode
except ImportError:
    widget_view_mode = sys.modules[
        'datadog_api_client.v1.model.widget_view_mode']
try:
    from datadog_api_client.v1.model import widget_viz_type
except ImportError:
    widget_viz_type = sys.modules[
        'datadog_api_client.v1.model.widget_viz_type']
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


if __name__ == '__main__':
    unittest.main()
