# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventStreamWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.event_stream_widget_definition_type import EventStreamWidgetDefinitionType

        return {
            "event_size": (WidgetEventSize,),
            "query": (str,),
            "tags_execution": (str,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (EventStreamWidgetDefinitionType,),
        }

    attribute_map = {
        "event_size": "event_size",
        "query": "query",
        "tags_execution": "tags_execution",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self, query, type, *args, **kwargs):
        """
        The event stream is a widget version of the stream of events
        on the Event Stream view. Only available on FREE layout dashboards.

        :param event_size: Size to use to display an event.
        :type event_size: WidgetEventSize, optional

        :param query: Query to filter the event stream with.
        :type query: str

        :param tags_execution: The execution method for multi-value filters. Can be either and or or.
        :type tags_execution: str, optional

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the event stream widget.
        :type type: EventStreamWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type

    @classmethod
    def _from_openapi_data(cls, query, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventStreamWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type
        return self
