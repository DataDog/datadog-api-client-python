# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GroupWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_layout_type import WidgetLayoutType
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.group_widget_definition_type import GroupWidgetDefinitionType
        from datadog_api_client.v1.model.widget import Widget

        return {
            "background_color": (str,),
            "banner_img": (str,),
            "layout_type": (WidgetLayoutType,),
            "show_title": (bool,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "type": (GroupWidgetDefinitionType,),
            "widgets": ([Widget],),
        }

    attribute_map = {
        "background_color": "background_color",
        "banner_img": "banner_img",
        "layout_type": "layout_type",
        "show_title": "show_title",
        "title": "title",
        "title_align": "title_align",
        "type": "type",
        "widgets": "widgets",
    }

    def __init__(self, layout_type, type, widgets, *args, **kwargs):
        """
        The groups widget allows you to keep similar graphs together on your timeboard. Each group has a custom header, can hold one to many graphs, and is collapsible.

        :param background_color: Background color of the group title.
        :type background_color: str, optional

        :param banner_img: URL of image to display as a banner for the group.
        :type banner_img: str, optional

        :param layout_type: Layout type of the group.
        :type layout_type: WidgetLayoutType

        :param show_title: Whether to show the title or not.
        :type show_title: bool, optional

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param type: Type of the group widget.
        :type type: GroupWidgetDefinitionType

        :param widgets: List of widget groups.
        :type widgets: [Widget]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.layout_type = layout_type
        self.type = type
        self.widgets = widgets

    @classmethod
    def _from_openapi_data(cls, layout_type, type, widgets, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(GroupWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.layout_type = layout_type
        self.type = type
        self.widgets = widgets
        return self
