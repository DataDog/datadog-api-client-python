# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AlertValueWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.alert_value_widget_definition_type import AlertValueWidgetDefinitionType

        return {
            "alert_id": (str,),
            "precision": (int,),
            "text_align": (WidgetTextAlign,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (AlertValueWidgetDefinitionType,),
            "unit": (str,),
        }

    attribute_map = {
        "alert_id": "alert_id",
        "precision": "precision",
        "text_align": "text_align",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "unit": "unit",
    }

    def __init__(self, alert_id, type, *args, **kwargs):
        """
        Alert values are query values showing the current value of the metric in any monitor defined on your system.

        :param alert_id: ID of the alert to use in the widget.
        :type alert_id: str

        :param precision: Number of decimal to show. If not defined, will use the raw value.
        :type precision: int, optional

        :param text_align: How to align the text on the widget.
        :type text_align: WidgetTextAlign, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of value in the widget.
        :type title_size: str, optional

        :param type: Type of the alert value widget.
        :type type: AlertValueWidgetDefinitionType

        :param unit: Unit to display with the value.
        :type unit: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.alert_id = alert_id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, alert_id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AlertValueWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.alert_id = alert_id
        self.type = type
        return self
