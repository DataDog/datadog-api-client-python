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


class OrgConfigReadAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "modified_at": (datetime, none_type),
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
            "value_type": (str,),
        }

    attribute_map = {
        "description": "description",
        "modified_at": "modified_at",
        "name": "name",
        "value": "value",
        "value_type": "value_type",
    }

    def __init__(
        self_,
        description: str,
        name: str,
        value: Any,
        value_type: str,
        modified_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Readable attributes of an Org Config.

        :param description: The description of an Org Config.
        :type description: str

        :param modified_at: The timestamp of the last Org Config update (if any).
        :type modified_at: datetime, none_type, optional

        :param name: The machine-friendly name of an Org Config.
        :type name: str

        :param value: The value of an Org Config.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param value_type: The type of an Org Config value.
        :type value_type: str
        """
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        super().__init__(kwargs)

        self_.description = description
        self_.name = name
        self_.value = value
        self_.value_type = value_type
