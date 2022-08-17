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
        "value": {
            "BLUE": "blue",
            "CUSTOM_BACKGROUND": "custom_bg",
            "CUSTOM_IMAGE": "custom_image",
            "CUSTOM_TEXT": "custom_text",
            "GRAY_ON_WHITE": "gray_on_white",
            "GREY": "grey",
            "GREEN": "green",
            "ORANGE": "orange",
            "RED": "red",
            "RED_ON_WHITE": "red_on_white",
            "WHITE_ON_GRAY": "white_on_gray",
            "WHITE_ON_GREEN": "white_on_green",
            "GREEN_ON_WHITE": "green_on_white",
            "WHITE_ON_RED": "white_on_red",
            "WHITE_ON_YELLOW": "white_on_yellow",
            "YELLOW_ON_WHITE": "yellow_on_white",
            "BLACK_ON_LIGHT_YELLOW": "black_on_light_yellow",
            "BLACK_ON_LIGHT_GREEN": "black_on_light_green",
            "BLACK_ON_LIGHT_RED": "black_on_light_red",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
