# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class EmbeddedAppWidgetInput(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self_, name: str, value: Any, **kwargs):
        """
        An input passed to the embedded app.

        :param name: Name of the app input.
        :type name: str

        :param value: Value of the app input. The API accepts a string, number, boolean, object, or a non-empty homogeneous array of those types.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
