# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class MonitorUserTemplateTemplateVariablesItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "available_values": ([str],),
            "defaults": ([str],),
            "name": (str,),
            "tag_key": (str,),
        }

    attribute_map = {
        "available_values": "available_values",
        "defaults": "defaults",
        "name": "name",
        "tag_key": "tag_key",
    }

    def __init__(
        self_,
        name: str,
        available_values: Union[List[str], UnsetType] = unset,
        defaults: Union[List[str], UnsetType] = unset,
        tag_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of objects representing template variables on the monitor which can have selectable values.

        :param available_values: Available values for the variable.
        :type available_values: [str], optional

        :param defaults: Default values of the template variable.
        :type defaults: [str], optional

        :param name: The name of the template variable.
        :type name: str

        :param tag_key: The tag key associated with the variable. This works the same as dashboard template variables.
        :type tag_key: str, optional
        """
        if available_values is not unset:
            kwargs["available_values"] = available_values
        if defaults is not unset:
            kwargs["defaults"] = defaults
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        super().__init__(kwargs)

        self_.name = name
