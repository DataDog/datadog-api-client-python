# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AiGatewayBudgetInstanceDimensionValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_count": (int,),
            "spend_microcents": (int,),
            "value": (str,),
        }

    attribute_map = {
        "instance_count": "instance_count",
        "spend_microcents": "spend_microcents",
        "value": "value",
    }

    def __init__(self_, instance_count: int, spend_microcents: int, value: str, **kwargs):
        """
        One value of a budget split dimension.

        :param instance_count: Number of instance counters carrying this value.
        :type instance_count: int

        :param spend_microcents: Spend summed across those instance counters, in microcents.
        :type spend_microcents: int

        :param value: Raw dimension value. User and Team values are UUIDs. A counter with no value for the dimension carries the null character (U+0000).
        :type value: str
        """
        super().__init__(kwargs)

        self_.instance_count = instance_count
        self_.spend_microcents = spend_microcents
        self_.value = value
