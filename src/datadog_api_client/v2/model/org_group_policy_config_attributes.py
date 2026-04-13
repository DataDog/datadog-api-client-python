# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class OrgGroupPolicyConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "allowed_values": ([str],),
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
            "description": (str,),
            "name": (str,),
            "value_type": (str,),
        }

    attribute_map = {
        "allowed_values": "allowed_values",
        "default_value": "default_value",
        "description": "description",
        "name": "name",
        "value_type": "value_type",
    }

    def __init__(
        self_, allowed_values: List[str], default_value: Any, description: str, name: str, value_type: str, **kwargs
    ):
        """
        Attributes of an org group policy config.

        :param allowed_values: The allowed values for this config.
        :type allowed_values: [str]

        :param default_value: The default value for this config.
        :type default_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param description: The description of the policy config.
        :type description: str

        :param name: The name of the policy config.
        :type name: str

        :param value_type: The type of the value for this config.
        :type value_type: str
        """
        super().__init__(kwargs)

        self_.allowed_values = allowed_values
        self_.default_value = default_value
        self_.description = description
        self_.name = name
        self_.value_type = value_type
