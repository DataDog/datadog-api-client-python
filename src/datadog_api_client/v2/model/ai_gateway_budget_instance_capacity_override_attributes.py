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


class AiGatewayBudgetInstanceCapacityOverrideAttributes(ModelNormal):
    validations = {
        "capacity_microcents": {
            "inclusive_minimum": 1,
        },
        "instance_key": {
            "min_length": 1,
        },
        "reason": {
            "max_length": 1024,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "capacity_microcents": (int,),
            "instance_key": (str,),
            "reason": (str,),
        }

    attribute_map = {
        "capacity_microcents": "capacity_microcents",
        "instance_key": "instance_key",
        "reason": "reason",
    }

    def __init__(self_, capacity_microcents: int, instance_key: str, reason: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes used to override one budget instance's active-period capacity.

        :param capacity_microcents: New capacity for this instance in the active accounting period, in microcents.
        :type capacity_microcents: int

        :param instance_key: Counter key of the instance to override, as returned by the list budget instances endpoint.
        :type instance_key: str

        :param reason: Optional reason recorded with the capacity override.
        :type reason: str, optional
        """
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)

        self_.capacity_microcents = capacity_microcents
        self_.instance_key = instance_key
