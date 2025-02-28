# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class StateVariableProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "default_value": (
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
        "default_value": "defaultValue",
    }

    def __init__(self_, default_value: Union[Any, UnsetType] = unset, **kwargs):
        """
        The properties of the state variable.

        :param default_value: The default value of the state variable.
        :type default_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if default_value is not unset:
            kwargs["default_value"] = default_value
        super().__init__(kwargs)
