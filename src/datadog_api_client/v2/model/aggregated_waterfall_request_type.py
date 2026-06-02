# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AggregatedWaterfallRequestType(ModelSimple):
    """
    The JSON:API type for aggregated waterfall requests.

    :param value: If omitted defaults to "aggregated_waterfall". Must be one of ["aggregated_waterfall"].
    :type value: str
    """

    allowed_values = {
        "aggregated_waterfall",
    }
    AGGREGATED_WATERFALL: ClassVar["AggregatedWaterfallRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AggregatedWaterfallRequestType.AGGREGATED_WATERFALL = AggregatedWaterfallRequestType("aggregated_waterfall")
