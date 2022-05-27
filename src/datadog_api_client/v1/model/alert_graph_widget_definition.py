# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AlertGraphWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_time import WidgetTime
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.alert_graph_widget_definition_type import AlertGraphWidgetDefinitionType
        from datadog_api_client.v1.model.widget_viz_type import WidgetVizType

        return {
            "alert_id": (str,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (AlertGraphWidgetDefinitionType,),
            "viz_type": (WidgetVizType,),
        }

    attribute_map = {
        "alert_id": "alert_id",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "viz_type": "viz_type",
    }

    def __init__(self, alert_id, type, viz_type, *args, **kwargs):
        """
        Alert graphs are timeseries graphs showing the current status of any monitor defined on your system.

        :param alert_id: ID of the alert to use in the widget.
        :type alert_id: str

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

        :param title: The title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the alert graph widget.
        :type type: AlertGraphWidgetDefinitionType

        :param viz_type: Whether to display the Alert Graph as a timeseries or a top list.
        :type viz_type: WidgetVizType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.alert_id = alert_id
        self.type = type
        self.viz_type = viz_type

    @classmethod
    def _from_openapi_data(cls, alert_id, type, viz_type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AlertGraphWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.alert_id = alert_id
        self.type = type
        self.viz_type = viz_type
        return self
