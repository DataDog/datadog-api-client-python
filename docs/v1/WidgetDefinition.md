# WidgetDefinition

[Definition of the widget](https://docs.datadoghq.com/dashboards/widgets/).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | ID of the alert to use in the widget. | defaults to nulltype.Null
**type** | [**ToplistWidgetDefinitionType**](ToplistWidgetDefinitionType.md) |  | defaults to nulltype.Null
**viz_type** | [**WidgetVizType**](WidgetVizType.md) |  | defaults to nulltype.Null
**requests** | [**[ToplistWidgetRequest]**](ToplistWidgetRequest.md) | List of top list widget requests. | defaults to nulltype.Null
**check** | **str** | Name of the check to use in the widget. | defaults to nulltype.Null
**grouping** | [**WidgetGrouping**](WidgetGrouping.md) |  | defaults to nulltype.Null
**query** | **str** | Query to filter the monitors with. | defaults to nulltype.Null
**text** | **str** | Text to display. | defaults to nulltype.Null
**style** | [**HostMapWidgetDefinitionStyle**](HostMapWidgetDefinitionStyle.md) |  | defaults to nulltype.Null
**view** | [**GeomapWidgetDefinitionView**](GeomapWidgetDefinitionView.md) |  | defaults to nulltype.Null
**layout_type** | [**WidgetLayoutType**](WidgetLayoutType.md) |  | defaults to nulltype.Null
**widgets** | [**[Widget]**](Widget.md) | List of widget groups. | defaults to nulltype.Null
**url** | **str** | URL of the image. | defaults to nulltype.Null
**content** | **str** | Content of the note. | defaults to nulltype.Null
**view_type** | **str** | Type of view displayed by the widget. | defaults to nulltype.Null
**filters** | **[str]** | Your environment and primary tag (or * if enabled for your account). | defaults to nulltype.Null
**service** | **str** | APM service. | defaults to nulltype.Null
**env** | **str** | APM environment. | defaults to nulltype.Null
**span_name** | **str** | APM span name. | defaults to nulltype.Null
**time** | [**WidgetTime**](WidgetTime.md) |  | [optional] 
**title** | **str** | Title of your widget. | [optional] 
**title_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**title_size** | **str** | Size of the title. | [optional] 
**precision** | **int** | Number of decimals to show. If not defined, the widget uses the raw value. | [optional] 
**text_align** | [**WidgetTextAlign**](WidgetTextAlign.md) |  | [optional] 
**unit** | **str** | Unit to display with the value. | [optional] 
**custom_links** | [**[WidgetCustomLink]**](WidgetCustomLink.md) | List of custom links. | [optional] 
**group** | **[str]** | List of tag prefixes to group by. | [optional] 
**group_by** | **[str]** | List of tag prefixes to group by in the case of a cluster check. | [optional] 
**tags** | **[str]** | List of tags used to filter the groups reporting a cluster check. | [optional] 
**legend_size** | **str** | Available legend sizes for a widget. Should be one of \&quot;0\&quot;, \&quot;2\&quot;, \&quot;4\&quot;, \&quot;8\&quot;, \&quot;16\&quot;, or \&quot;auto\&quot;. | [optional] 
**show_legend** | **bool** | (screenboard only) Show the legend for this widget. | [optional] 
**event_size** | [**WidgetEventSize**](WidgetEventSize.md) |  | [optional] 
**tags_execution** | **str** | The execution method for multi-value filters. Can be either and or or. | [optional] 
**color** | **str** | Color of the text. | [optional] 
**font_size** | **str** | Size of the text. | [optional] 
**events** | [**[WidgetEvent]**](WidgetEvent.md) | List of widget events. | [optional] 
**yaxis** | [**WidgetAxis**](WidgetAxis.md) |  | [optional] 
**no_group_hosts** | **bool** | Whether to show the hosts that don’t fit in a group. | [optional] 
**no_metric_hosts** | **bool** | Whether to show the hosts with no metrics. | [optional] 
**node_type** | [**WidgetNodeType**](WidgetNodeType.md) |  | [optional] 
**notes** | **str** | Notes on the title. | [optional] 
**scope** | **[str]** | List of tags used to filter the map. | [optional] 
**margin** | [**WidgetMargin**](WidgetMargin.md) |  | [optional] 
**sizing** | [**WidgetImageSizing**](WidgetImageSizing.md) |  | [optional] 
**columns** | **[str]** | Which columns to display on the widget. | [optional] 
**indexes** | **[str]** | An array of index names to query in the stream. Use [] to query all indexes at once. | [optional] 
**logset** | **str** | ID of the log set to use. | [optional] 
**message_display** | [**WidgetMessageDisplay**](WidgetMessageDisplay.md) |  | [optional] 
**show_date_column** | **bool** | Whether to show the date column or not | [optional] 
**show_message_column** | **bool** | Whether to show the message column or not | [optional] 
**sort** | [**WidgetMonitorSummarySort**](WidgetMonitorSummarySort.md) |  | [optional] 
**color_preference** | [**WidgetColorPreference**](WidgetColorPreference.md) |  | [optional] 
**count** | **int** | The number of monitors to display. | [optional] 
**display_format** | [**WidgetServiceSummaryDisplayFormat**](WidgetServiceSummaryDisplayFormat.md) |  | [optional] 
**hide_zero_counts** | **bool** | Whether to show counts of 0 or not. | [optional] 
**show_last_triggered** | **bool** | Whether to show the time that has elapsed since the monitor/group triggered. | [optional] 
**start** | **int** | The start of the list. Typically 0. | [optional] 
**summary_type** | [**WidgetSummaryType**](WidgetSummaryType.md) |  | [optional] 
**background_color** | **str** | Background color of the note. | [optional] 
**show_tick** | **bool** | Whether to show a tick or not. | [optional] 
**tick_edge** | [**WidgetTickEdge**](WidgetTickEdge.md) |  | [optional] 
**tick_pos** | **str** | Where to position the tick on an edge. | [optional] 
**autoscale** | **bool** | Whether to use auto-scaling or not. | [optional] 
**custom_unit** | **str** | Display a unit of your choice on the widget. | [optional] 
**color_by_groups** | **[str]** | List of groups used for colors. | [optional] 
**xaxis** | [**WidgetAxis**](WidgetAxis.md) |  | [optional] 
**show_error_budget** | **bool** | Defined error budget. | [optional] 
**slo_id** | **str** | ID of the SLO displayed. | [optional] 
**time_windows** | [**[WidgetTimeWindows]**](WidgetTimeWindows.md) | Times being monitored. | [optional] 
**view_mode** | [**WidgetViewMode**](WidgetViewMode.md) |  | [optional] 
**show_breakdown** | **bool** | Whether to show the latency breakdown or not. | [optional] 
**show_distribution** | **bool** | Whether to show the latency distribution or not. | [optional] 
**show_errors** | **bool** | Whether to show the error metrics or not. | [optional] 
**show_hits** | **bool** | Whether to show the hits metrics or not. | [optional] 
**show_latency** | **bool** | Whether to show the latency metrics or not. | [optional] 
**show_resource_list** | **bool** | Whether to show the resource list or not. | [optional] 
**size_format** | [**WidgetSizeFormat**](WidgetSizeFormat.md) |  | [optional] 
**has_search_bar** | [**TableWidgetHasSearchBar**](TableWidgetHasSearchBar.md) |  | [optional] 
**markers** | [**[WidgetMarker]**](WidgetMarker.md) | List of markers. | [optional] 
**right_yaxis** | [**WidgetAxis**](WidgetAxis.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


