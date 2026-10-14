# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class DashboardWidgetValidationResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error_message": (str, none_type),
            "error_path": (str, none_type),
            "is_valid": (bool,),
            "widget_type": (str, none_type),
        }

    attribute_map = {
        "error_message": "error_message",
        "error_path": "error_path",
        "is_valid": "is_valid",
        "widget_type": "widget_type",
    }

    def __init__(
        self_,
        error_message: Union[str, none_type],
        error_path: Union[str, none_type],
        is_valid: bool,
        widget_type: Union[str, none_type],
        **kwargs,
    ):
        """
        Validation result for one dashboard widget.

        :param error_message: Validation error message, when the widget is invalid.
        :type error_message: str, none_type

        :param error_path: Path to the invalid value, when available.
        :type error_path: str, none_type

        :param is_valid: Whether the widget passed validation.
        :type is_valid: bool

        :param widget_type: Type of the validated widget, when available.
        :type widget_type: str, none_type
        """
        super().__init__(kwargs)

        self_.error_message = error_message
        self_.error_path = error_path
        self_.is_valid = is_valid
        self_.widget_type = widget_type
