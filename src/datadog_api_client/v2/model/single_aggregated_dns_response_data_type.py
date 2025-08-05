# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SingleAggregatedDnsResponseDataType(ModelSimple):
    """
    Aggregated DNS resource type.

    :param value: If omitted defaults to "aggregated_dns". Must be one of ["aggregated_dns"].
    :type value: str
    """

    allowed_values = {
        "aggregated_dns",
    }
    AGGREGATED_DNS: ClassVar["SingleAggregatedDnsResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SingleAggregatedDnsResponseDataType.AGGREGATED_DNS = SingleAggregatedDnsResponseDataType("aggregated_dns")
