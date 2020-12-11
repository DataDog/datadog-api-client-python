# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from datadog_api_client.v1.model.alert_graph_widget_definition import AlertGraphWidgetDefinition
    from datadog_api_client.v1.model.alert_value_widget_definition import AlertValueWidgetDefinition
    from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition
    from datadog_api_client.v1.model.check_status_widget_definition import CheckStatusWidgetDefinition
    from datadog_api_client.v1.model.distribution_widget_definition import DistributionWidgetDefinition
    from datadog_api_client.v1.model.event_stream_widget_definition import EventStreamWidgetDefinition
    from datadog_api_client.v1.model.event_timeline_widget_definition import EventTimelineWidgetDefinition
    from datadog_api_client.v1.model.free_text_widget_definition import FreeTextWidgetDefinition
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
    globals()['AlertGraphWidgetDefinition'] = AlertGraphWidgetDefinition
    globals()['AlertValueWidgetDefinition'] = AlertValueWidgetDefinition
    globals()['ChangeWidgetDefinition'] = ChangeWidgetDefinition
    globals()['CheckStatusWidgetDefinition'] = CheckStatusWidgetDefinition
    globals()['DistributionWidgetDefinition'] = DistributionWidgetDefinition
    globals()['EventStreamWidgetDefinition'] = EventStreamWidgetDefinition
    globals()['EventTimelineWidgetDefinition'] = EventTimelineWidgetDefinition
    globals()['FreeTextWidgetDefinition'] = FreeTextWidgetDefinition
    globals()['GroupWidgetDefinition'] = GroupWidgetDefinition
    globals()['HeatMapWidgetDefinition'] = HeatMapWidgetDefinition
    globals()['HostMapWidgetDefinition'] = HostMapWidgetDefinition
    globals()['HostMapWidgetDefinitionStyle'] = HostMapWidgetDefinitionStyle
    globals()['IFrameWidgetDefinition'] = IFrameWidgetDefinition
    globals()['ImageWidgetDefinition'] = ImageWidgetDefinition
    globals()['LogStreamWidgetDefinition'] = LogStreamWidgetDefinition
    globals()['MonitorSummaryWidgetDefinition'] = MonitorSummaryWidgetDefinition
    globals()['NoteWidgetDefinition'] = NoteWidgetDefinition
    globals()['QueryValueWidgetDefinition'] = QueryValueWidgetDefinition
    globals()['SLOWidgetDefinition'] = SLOWidgetDefinition
    globals()['ScatterPlotWidgetDefinition'] = ScatterPlotWidgetDefinition
    globals()['ServiceMapWidgetDefinition'] = ServiceMapWidgetDefinition
    globals()['ServiceSummaryWidgetDefinition'] = ServiceSummaryWidgetDefinition
    globals()['TableWidgetDefinition'] = TableWidgetDefinition
    globals()['TableWidgetHasSearchBar'] = TableWidgetHasSearchBar
    globals()['TimeseriesWidgetDefinition'] = TimeseriesWidgetDefinition
    globals()['ToplistWidgetDefinition'] = ToplistWidgetDefinition
    globals()['ToplistWidgetDefinitionType'] = ToplistWidgetDefinitionType
    globals()['ToplistWidgetRequest'] = ToplistWidgetRequest
    globals()['Widget'] = Widget
    globals()['WidgetAxis'] = WidgetAxis
    globals()['WidgetColorPreference'] = WidgetColorPreference
    globals()['WidgetCustomLink'] = WidgetCustomLink
    globals()['WidgetEvent'] = WidgetEvent
    globals()['WidgetEventSize'] = WidgetEventSize
    globals()['WidgetGrouping'] = WidgetGrouping
    globals()['WidgetImageSizing'] = WidgetImageSizing
    globals()['WidgetLayoutType'] = WidgetLayoutType
    globals()['WidgetMargin'] = WidgetMargin
    globals()['WidgetMarker'] = WidgetMarker
    globals()['WidgetMessageDisplay'] = WidgetMessageDisplay
    globals()['WidgetMonitorSummarySort'] = WidgetMonitorSummarySort
    globals()['WidgetNodeType'] = WidgetNodeType
    globals()['WidgetServiceSummaryDisplayFormat'] = WidgetServiceSummaryDisplayFormat
    globals()['WidgetSizeFormat'] = WidgetSizeFormat
    globals()['WidgetSummaryType'] = WidgetSummaryType
    globals()['WidgetTextAlign'] = WidgetTextAlign
    globals()['WidgetTickEdge'] = WidgetTickEdge
    globals()['WidgetTime'] = WidgetTime
    globals()['WidgetTimeWindows'] = WidgetTimeWindows
    globals()['WidgetViewMode'] = WidgetViewMode
    globals()['WidgetVizType'] = WidgetVizType


class WidgetDefinition(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {}

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """WidgetDefinition - a model defined in OpenAPI

        Args:

        Keyword Args:
            alert_id (str): ID of the alert to use in the widget.. defaults to nulltype.Null  # noqa: E501
            type (ToplistWidgetDefinitionType): defaults to nulltype.Null, must be one of ["toplist", ]  # noqa: E501
            viz_type (WidgetVizType): defaults to nulltype.Null, must be one of ["timeseries", "toplist", ]  # noqa: E501
            requests ([ToplistWidgetRequest]): List of top list widget requests.. defaults to nulltype.Null  # noqa: E501
            check (str): Name of the check to use in the widget.. defaults to nulltype.Null  # noqa: E501
            grouping (WidgetGrouping): defaults to nulltype.Null, must be one of ["check", "cluster", ]  # noqa: E501
            query (str): Query to filter the monitors with.. defaults to nulltype.Null  # noqa: E501
            text (str): Text to display.. defaults to nulltype.Null  # noqa: E501
            layout_type (WidgetLayoutType): defaults to nulltype.Null, must be one of ["ordered", ]  # noqa: E501
            widgets ([Widget]): List of widget groups.. defaults to nulltype.Null  # noqa: E501
            url (str): URL of the image.. defaults to nulltype.Null  # noqa: E501
            content (str): Content of the note.. defaults to nulltype.Null  # noqa: E501
            view_type (str): Type of view displayed by the widget.. defaults to nulltype.Null  # noqa: E501
            filters ([str]): Your environment and primary tag (or * if enabled for your account).. defaults to nulltype.Null  # noqa: E501
            service (str): APM service.. defaults to nulltype.Null  # noqa: E501
            env (str): APM environment.. defaults to nulltype.Null  # noqa: E501
            span_name (str): APM span name.. defaults to nulltype.Null  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            time (WidgetTime): [optional]  # noqa: E501
            title (str): Title of your widget.. [optional]  # noqa: E501
            title_align (WidgetTextAlign): [optional]  # noqa: E501
            title_size (str): Size of the title.. [optional]  # noqa: E501
            precision (int): Number of decimals to show. If not defined, the widget uses the raw value.. [optional]  # noqa: E501
            text_align (WidgetTextAlign): [optional]  # noqa: E501
            unit (str): Unit to display with the value.. [optional]  # noqa: E501
            custom_links ([WidgetCustomLink]): List of custom links.. [optional]  # noqa: E501
            group ([str]): List of tag prefixes to group by.. [optional]  # noqa: E501
            group_by ([str]): List of tag prefixes to group by in the case of a cluster check.. [optional]  # noqa: E501
            tags ([str]): List of tags used to filter the groups reporting a cluster check.. [optional]  # noqa: E501
            legend_size (str): Available legend sizes for a widget. Should be one of \"0\", \"2\", \"4\", \"8\", \"16\", or \"auto\".. [optional]  # noqa: E501
            show_legend (bool): (screenboard only) Show the legend for this widget.. [optional]  # noqa: E501
            event_size (WidgetEventSize): [optional]  # noqa: E501
            tags_execution (str): The execution method for multi-value filters. Can be either and or or.. [optional]  # noqa: E501
            color (str): Color of the text.. [optional]  # noqa: E501
            font_size (str): Size of the text.. [optional]  # noqa: E501
            events ([WidgetEvent]): List of widget events.. [optional]  # noqa: E501
            yaxis (WidgetAxis): [optional]  # noqa: E501
            no_group_hosts (bool): Whether to show the hosts that don’t fit in a group.. [optional]  # noqa: E501
            no_metric_hosts (bool): Whether to show the hosts with no metrics.. [optional]  # noqa: E501
            node_type (WidgetNodeType): [optional]  # noqa: E501
            notes (str): Notes on the title.. [optional]  # noqa: E501
            scope ([str]): List of tags used to filter the map.. [optional]  # noqa: E501
            style (HostMapWidgetDefinitionStyle): [optional]  # noqa: E501
            margin (WidgetMargin): [optional]  # noqa: E501
            sizing (WidgetImageSizing): [optional]  # noqa: E501
            columns ([str]): Which columns to display on the widget.. [optional]  # noqa: E501
            indexes ([str]): An array of index names to query in the stream. Use [] to query all indexes at once.. [optional]  # noqa: E501
            logset (str): ID of the log set to use.. [optional]  # noqa: E501
            message_display (WidgetMessageDisplay): [optional]  # noqa: E501
            show_date_column (bool): Whether to show the date column or not. [optional]  # noqa: E501
            show_message_column (bool): Whether to show the message column or not. [optional]  # noqa: E501
            sort (WidgetMonitorSummarySort): [optional]  # noqa: E501
            color_preference (WidgetColorPreference): [optional]  # noqa: E501
            count (int): The number of monitors to display.. [optional]  # noqa: E501
            display_format (WidgetServiceSummaryDisplayFormat): [optional]  # noqa: E501
            hide_zero_counts (bool): Whether to show counts of 0 or not.. [optional]  # noqa: E501
            show_last_triggered (bool): Whether to show the time that has elapsed since the monitor/group triggered.. [optional]  # noqa: E501
            start (int): The start of the list. Typically 0.. [optional]  # noqa: E501
            summary_type (WidgetSummaryType): [optional]  # noqa: E501
            background_color (str): Background color of the note.. [optional]  # noqa: E501
            show_tick (bool): Whether to show a tick or not.. [optional]  # noqa: E501
            tick_edge (WidgetTickEdge): [optional]  # noqa: E501
            tick_pos (str): Where to position the tick on an edge.. [optional]  # noqa: E501
            autoscale (bool): Whether to use auto-scaling or not.. [optional]  # noqa: E501
            custom_unit (str): Display a unit of your choice on the widget.. [optional]  # noqa: E501
            color_by_groups ([str]): List of groups used for colors.. [optional]  # noqa: E501
            xaxis (WidgetAxis): [optional]  # noqa: E501
            show_error_budget (bool): Defined error budget.. [optional]  # noqa: E501
            slo_id (str): ID of the SLO displayed.. [optional]  # noqa: E501
            time_windows ([WidgetTimeWindows]): Times being monitored.. [optional]  # noqa: E501
            view_mode (WidgetViewMode): [optional]  # noqa: E501
            show_breakdown (bool): Whether to show the latency breakdown or not.. [optional]  # noqa: E501
            show_distribution (bool): Whether to show the latency distribution or not.. [optional]  # noqa: E501
            show_errors (bool): Whether to show the error metrics or not.. [optional]  # noqa: E501
            show_hits (bool): Whether to show the hits metrics or not.. [optional]  # noqa: E501
            show_latency (bool): Whether to show the latency metrics or not.. [optional]  # noqa: E501
            show_resource_list (bool): Whether to show the resource list or not.. [optional]  # noqa: E501
            size_format (WidgetSizeFormat): [optional]  # noqa: E501
            has_search_bar (TableWidgetHasSearchBar): [optional]  # noqa: E501
            markers ([WidgetMarker]): List of markers.. [optional]  # noqa: E501
            right_yaxis (WidgetAxis): [optional]  # noqa: E501
        """

        alert_id = kwargs.get('alert_id', nulltype.Null)
        type = kwargs.get('type', nulltype.Null)
        viz_type = kwargs.get('viz_type', nulltype.Null)
        requests = kwargs.get('requests', nulltype.Null)
        check = kwargs.get('check', nulltype.Null)
        grouping = kwargs.get('grouping', nulltype.Null)
        query = kwargs.get('query', nulltype.Null)
        text = kwargs.get('text', nulltype.Null)
        layout_type = kwargs.get('layout_type', nulltype.Null)
        widgets = kwargs.get('widgets', nulltype.Null)
        url = kwargs.get('url', nulltype.Null)
        content = kwargs.get('content', nulltype.Null)
        view_type = kwargs.get('view_type', nulltype.Null)
        filters = kwargs.get('filters', nulltype.Null)
        service = kwargs.get('service', nulltype.Null)
        env = kwargs.get('env', nulltype.Null)
        span_name = kwargs.get('span_name', nulltype.Null)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'alert_id': alert_id,
            'type': type,
            'viz_type': viz_type,
            'requests': requests,
            'check': check,
            'grouping': grouping,
            'query': query,
            'text': text,
            'layout_type': layout_type,
            'widgets': widgets,
            'url': url,
            'content': content,
            'view_type': view_type,
            'filters': filters,
            'service': service,
            'env': env,
            'span_name': span_name,
        }
        # remove args whose value is Null because they are unset
        required_arg_names = list(required_args.keys())
        for required_arg_name in required_arg_names:
            if required_args[required_arg_name] is nulltype.Null:
                del required_args[required_arg_name]
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              AlertGraphWidgetDefinition,
              AlertValueWidgetDefinition,
              ChangeWidgetDefinition,
              CheckStatusWidgetDefinition,
              DistributionWidgetDefinition,
              EventStreamWidgetDefinition,
              EventTimelineWidgetDefinition,
              FreeTextWidgetDefinition,
              GroupWidgetDefinition,
              HeatMapWidgetDefinition,
              HostMapWidgetDefinition,
              IFrameWidgetDefinition,
              ImageWidgetDefinition,
              LogStreamWidgetDefinition,
              MonitorSummaryWidgetDefinition,
              NoteWidgetDefinition,
              QueryValueWidgetDefinition,
              SLOWidgetDefinition,
              ScatterPlotWidgetDefinition,
              ServiceMapWidgetDefinition,
              ServiceSummaryWidgetDefinition,
              TableWidgetDefinition,
              TimeseriesWidgetDefinition,
              ToplistWidgetDefinition,
          ],
        }
