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


class AiGatewayProviderUpdateAttributes(ModelNormal):
    validations = {
        "cost_multiplier": {
            "inclusive_maximum": 1000000,
            "exclusive_minimum": 0,
        },
        "name": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "cost_multiplier": (float,),
            "name": (str,),
        }

    attribute_map = {
        "cost_multiplier": "cost_multiplier",
        "name": "name",
    }

    def __init__(
        self_, cost_multiplier: Union[float, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes used to update an AI Gateway provider.

        :param cost_multiplier: Multiplier applied to provider costs. Must be greater than 0 and at most 1000000.
        :type cost_multiplier: float, optional

        :param name: Human-readable resource name.
        :type name: str, optional
        """
        if cost_multiplier is not unset:
            kwargs["cost_multiplier"] = cost_multiplier
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
