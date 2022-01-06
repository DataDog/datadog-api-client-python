# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.free_text_widget_definition_type import FreeTextWidgetDefinitionType
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

    globals()["FreeTextWidgetDefinitionType"] = FreeTextWidgetDefinitionType
    globals()["WidgetTextAlign"] = WidgetTextAlign


class FreeTextWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "color": (str,),
            "font_size": (str,),
            "text": (str,),
            "text_align": (WidgetTextAlign,),
            "type": (FreeTextWidgetDefinitionType,),
        }

    attribute_map = {
        "text": "text",
        "type": "type",
        "color": "color",
        "font_size": "font_size",
        "text_align": "text_align",
    }

    read_only_vars = {}

    def __init__(self, text, type, *args, **kwargs):
        """FreeTextWidgetDefinition - a model defined in OpenAPI

        Args:
            text (str): Text to display.
            type (FreeTextWidgetDefinitionType):

        Keyword Args:
            color (str): [optional] Color of the text.
            font_size (str): [optional] Size of the text.
            text_align (WidgetTextAlign): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.type = type

    @classmethod
    def _from_openapi_data(cls, text, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FreeTextWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.type = type
        return self
