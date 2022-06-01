# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ImageWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_horizontal_align import WidgetHorizontalAlign
        from datadog_api_client.v1.model.widget_margin import WidgetMargin
        from datadog_api_client.v1.model.widget_image_sizing import WidgetImageSizing
        from datadog_api_client.v1.model.image_widget_definition_type import ImageWidgetDefinitionType
        from datadog_api_client.v1.model.widget_vertical_align import WidgetVerticalAlign

        return {
            "has_background": (bool,),
            "has_border": (bool,),
            "horizontal_align": (WidgetHorizontalAlign,),
            "margin": (WidgetMargin,),
            "sizing": (WidgetImageSizing,),
            "type": (ImageWidgetDefinitionType,),
            "url": (str,),
            "url_dark_theme": (str,),
            "vertical_align": (WidgetVerticalAlign,),
        }

    attribute_map = {
        "has_background": "has_background",
        "has_border": "has_border",
        "horizontal_align": "horizontal_align",
        "margin": "margin",
        "sizing": "sizing",
        "type": "type",
        "url": "url",
        "url_dark_theme": "url_dark_theme",
        "vertical_align": "vertical_align",
    }

    def __init__(self, type, url, *args, **kwargs):
        """
        The image widget allows you to embed an image on your dashboard. An image can be a PNG, JPG, or animated GIF. Only available on FREE layout dashboards.

        :param has_background: Whether to display a background or not.
        :type has_background: bool, optional

        :param has_border: Whether to display a border or not.
        :type has_border: bool, optional

        :param horizontal_align: Horizontal alignment.
        :type horizontal_align: WidgetHorizontalAlign, optional

        :param margin: Size of the margins around the image.
            **Note** : ``small`` and ``large`` values are deprecated.
        :type margin: WidgetMargin, optional

        :param sizing: How to size the image on the widget. The values are based on the image ``object-fit`` CSS properties.
            **Note** : ``zoom`` , ``fit`` and ``center`` values are deprecated.
        :type sizing: WidgetImageSizing, optional

        :param type: Type of the image widget.
        :type type: ImageWidgetDefinitionType

        :param url: URL of the image.
        :type url: str

        :param url_dark_theme: URL of the image in dark mode.
        :type url_dark_theme: str, optional

        :param vertical_align: Vertical alignment.
        :type vertical_align: WidgetVerticalAlign, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type
        self.url = url

    @classmethod
    def _from_openapi_data(cls, type, url, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ImageWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        self.url = url
        return self
