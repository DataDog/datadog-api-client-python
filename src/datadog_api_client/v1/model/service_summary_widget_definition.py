# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceSummaryWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_service_summary_display_format import WidgetServiceSummaryDisplayFormat
        from datadog_api_client.v1.model.widget_size_format import WidgetSizeFormat
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.service_summary_widget_definition_type import (
            ServiceSummaryWidgetDefinitionType,
        )

        return {
            "display_format": (WidgetServiceSummaryDisplayFormat,),
            "env": (str,),
            "service": (str,),
            "show_breakdown": (bool,),
            "show_distribution": (bool,),
            "show_errors": (bool,),
            "show_hits": (bool,),
            "show_latency": (bool,),
            "show_resource_list": (bool,),
            "size_format": (WidgetSizeFormat,),
            "span_name": (str,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ServiceSummaryWidgetDefinitionType,),
        }

    attribute_map = {
        "display_format": "display_format",
        "env": "env",
        "service": "service",
        "show_breakdown": "show_breakdown",
        "show_distribution": "show_distribution",
        "show_errors": "show_errors",
        "show_hits": "show_hits",
        "show_latency": "show_latency",
        "show_resource_list": "show_resource_list",
        "size_format": "size_format",
        "span_name": "span_name",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self, env, service, span_name, type, *args, **kwargs):
        """
        The service summary displays the graphs of a chosen service in your screenboard. Only available on FREE layout dashboards.

        :param display_format: Number of columns to display.
        :type display_format: WidgetServiceSummaryDisplayFormat, optional

        :param env: APM environment.
        :type env: str

        :param service: APM service.
        :type service: str

        :param show_breakdown: Whether to show the latency breakdown or not.
        :type show_breakdown: bool, optional

        :param show_distribution: Whether to show the latency distribution or not.
        :type show_distribution: bool, optional

        :param show_errors: Whether to show the error metrics or not.
        :type show_errors: bool, optional

        :param show_hits: Whether to show the hits metrics or not.
        :type show_hits: bool, optional

        :param show_latency: Whether to show the latency metrics or not.
        :type show_latency: bool, optional

        :param show_resource_list: Whether to show the resource list or not.
        :type show_resource_list: bool, optional

        :param size_format: Size of the widget.
        :type size_format: WidgetSizeFormat, optional

        :param span_name: APM span name.
        :type span_name: str

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the service summary widget.
        :type type: ServiceSummaryWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.env = env
        self.service = service
        self.span_name = span_name
        self.type = type

    @classmethod
    def _from_openapi_data(cls, env, service, span_name, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ServiceSummaryWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.env = env
        self.service = service
        self.span_name = span_name
        self.type = type
        return self
