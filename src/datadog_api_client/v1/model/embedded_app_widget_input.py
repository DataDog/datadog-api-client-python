# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.embedded_app_widget_input_value import EmbeddedAppWidgetInputValue
    from datadog_api_client.v1.model.embedded_app_widget_input_value_object import EmbeddedAppWidgetInputValueObject


class EmbeddedAppWidgetInput(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.embedded_app_widget_input_value import EmbeddedAppWidgetInputValue

        return {
            "name": (str,),
            "value": (EmbeddedAppWidgetInputValue,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(
        self_,
        name: str,
        value: Union[
            EmbeddedAppWidgetInputValue,
            str,
            float,
            bool,
            EmbeddedAppWidgetInputValueObject,
            List[str],
            List[float],
            List[bool],
            List[Dict[str, Any]],
        ],
        **kwargs,
    ):
        """
        An input passed to the embedded app.

        :param name: Name of the app input.
        :type name: str

        :param value: Value of the app input. This can be a string, number, boolean, object, or a non-empty homogeneous array of those types.
        :type value: EmbeddedAppWidgetInputValue
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
