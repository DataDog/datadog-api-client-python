# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudWorkloadSecurityAgentRuleActionSet(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "append": (bool,),
            "field": (str,),
            "name": (str,),
            "scope": (str,),
            "size": (int,),
            "ttl": (int,),
            "value": (str,),
        }

    attribute_map = {
        "append": "append",
        "field": "field",
        "name": "name",
        "scope": "scope",
        "size": "size",
        "ttl": "ttl",
        "value": "value",
    }

    def __init__(
        self_,
        append: Union[bool, UnsetType] = unset,
        field: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        ttl: Union[int, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The set action applied on the scope matching the rule

        :param append: Whether the value should be appended to the field
        :type append: bool, optional

        :param field: The field of the set action
        :type field: str, optional

        :param name: The name of the set action
        :type name: str, optional

        :param scope: The scope of the set action
        :type scope: str, optional

        :param size: The size of the set action
        :type size: int, optional

        :param ttl: The time to live of the set action
        :type ttl: int, optional

        :param value: The value of the set action
        :type value: str, optional
        """
        if append is not unset:
            kwargs["append"] = append
        if field is not unset:
            kwargs["field"] = field
        if name is not unset:
            kwargs["name"] = name
        if scope is not unset:
            kwargs["scope"] = scope
        if size is not unset:
            kwargs["size"] = size
        if ttl is not unset:
            kwargs["ttl"] = ttl
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
