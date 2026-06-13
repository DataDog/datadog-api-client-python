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


class ReportScheduleIndexTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "available_values": ([str], none_type),
            "defaults": ([str], none_type),
            "name": (str, none_type),
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
        available_values: Union[List[str], none_type, UnsetType] = unset,
        defaults: Union[List[str], none_type, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        prefix: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Template variable metadata from a dashboard index.

        :param available_values: Available values for the template variable.
        :type available_values: [str], none_type, optional

        :param defaults: Default values for the template variable.
        :type defaults: [str], none_type, optional

        :param name: The template variable name.
        :type name: str, none_type, optional

        :param prefix: The tag prefix for the template variable, when available.
        :type prefix: str, none_type, optional
        """
        if available_values is not unset:
            kwargs["available_values"] = available_values
        if defaults is not unset:
            kwargs["defaults"] = defaults
        if name is not unset:
            kwargs["name"] = name
        if prefix is not unset:
            kwargs["prefix"] = prefix
        super().__init__(kwargs)
