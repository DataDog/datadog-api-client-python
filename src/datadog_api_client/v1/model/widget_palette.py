# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetPalette(ModelSimple):
    """
    Color palette to apply.

    :param value: Must be one of ["blue", "custom_bg", "custom_image", "custom_text", "gray_on_white", "grey", "green", "orange", "red", "red_on_white", "white_on_gray", "white_on_green", "green_on_white", "white_on_red", "white_on_yellow", "yellow_on_white", "black_on_light_yellow", "black_on_light_green", "black_on_light_red"].
    :type value: str
    """

    allowed_values = {
        "blue",
        "custom_bg",
        "custom_image",
        "custom_text",
        "gray_on_white",
        "grey",
        "green",
        "orange",
        "red",
        "red_on_white",
        "white_on_gray",
        "white_on_green",
        "green_on_white",
        "white_on_red",
        "white_on_yellow",
        "yellow_on_white",
        "black_on_light_yellow",
        "black_on_light_green",
        "black_on_light_red",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetPalette.BLUE = WidgetPalette("blue")
WidgetPalette.CUSTOM_BACKGROUND = WidgetPalette("custom_bg")
WidgetPalette.CUSTOM_IMAGE = WidgetPalette("custom_image")
WidgetPalette.CUSTOM_TEXT = WidgetPalette("custom_text")
WidgetPalette.GRAY_ON_WHITE = WidgetPalette("gray_on_white")
WidgetPalette.GREY = WidgetPalette("grey")
WidgetPalette.GREEN = WidgetPalette("green")
WidgetPalette.ORANGE = WidgetPalette("orange")
WidgetPalette.RED = WidgetPalette("red")
WidgetPalette.RED_ON_WHITE = WidgetPalette("red_on_white")
WidgetPalette.WHITE_ON_GRAY = WidgetPalette("white_on_gray")
WidgetPalette.WHITE_ON_GREEN = WidgetPalette("white_on_green")
WidgetPalette.GREEN_ON_WHITE = WidgetPalette("green_on_white")
WidgetPalette.WHITE_ON_RED = WidgetPalette("white_on_red")
WidgetPalette.WHITE_ON_YELLOW = WidgetPalette("white_on_yellow")
WidgetPalette.YELLOW_ON_WHITE = WidgetPalette("yellow_on_white")
WidgetPalette.BLACK_ON_LIGHT_YELLOW = WidgetPalette("black_on_light_yellow")
WidgetPalette.BLACK_ON_LIGHT_GREEN = WidgetPalette("black_on_light_green")
WidgetPalette.BLACK_ON_LIGHT_RED = WidgetPalette("black_on_light_red")
