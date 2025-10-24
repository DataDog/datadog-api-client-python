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


class ResolveVulnerableSymbolsResponseResultsVulnerableSymbolsSymbols(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
            "value": (str,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param name:
        :type name: str, optional

        :param type:
        :type type: str, optional

        :param value:
        :type value: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
