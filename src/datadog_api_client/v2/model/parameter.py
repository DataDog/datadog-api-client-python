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


class Parameter(ModelNormal):
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
        The definition of ``Parameter`` object.

        :param name: The ``Parameter`` ``name``.
        :type name: str

        :param value: The ``Parameter`` ``value``.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
