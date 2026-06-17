# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GovernanceInsightEventCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "interval": (int,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
    }

    def __init__(self_, aggregation: str, interval: int, **kwargs):
        """
        The aggregation applied to an event query.

        :param aggregation: The aggregation function to apply.
        :type aggregation: str

        :param interval: The aggregation time window, in milliseconds.
        :type interval: int
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.interval = interval
