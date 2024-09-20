# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class PowerpackTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "available_values": ([str], none_type),
            "defaults": ([str],),
            "name": (str,),
            "prefix": (str, none_type),
        }

    attribute_map = {
        "available_values": "available_values",
        "defaults": "defaults",
        "name": "name",
        "prefix": "prefix",
    }

    def __init__(
        self_,
        name: str,
        available_values: Union[List[str], none_type, UnsetType] = unset,
        defaults: Union[List[str], UnsetType] = unset,
        prefix: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack template variables.

        :param available_values: The list of values that the template variable drop-down is limited to.
        :type available_values: [str], none_type, optional

        :param defaults: One or many template variable default values within the saved view, which are unioned together using ``OR`` if more than one is specified.
        :type defaults: [str], optional

        :param name: The name of the variable.
        :type name: str

        :param prefix: The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
        :type prefix: str, none_type, optional
        """
        if available_values is not unset:
            kwargs["available_values"] = available_values
        if defaults is not unset:
            kwargs["defaults"] = defaults
        if prefix is not unset:
            kwargs["prefix"] = prefix
        super().__init__(kwargs)

        self_.name = name
