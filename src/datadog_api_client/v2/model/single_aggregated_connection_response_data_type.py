# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SingleAggregatedConnectionResponseDataType(ModelSimple):
    """
    Aggregated connection resource type.

    :param value: If omitted defaults to "aggregated_connection". Must be one of ["aggregated_connection"].
    :type value: str
    """

    allowed_values = {
        "aggregated_connection",
    }
    AGGREGATED_CONNECTION: ClassVar["SingleAggregatedConnectionResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SingleAggregatedConnectionResponseDataType.AGGREGATED_CONNECTION = SingleAggregatedConnectionResponseDataType(
    "aggregated_connection"
)
