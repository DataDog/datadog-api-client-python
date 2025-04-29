# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSentinelOneDestinationRegion(ModelSimple):
    """
    The SentinelOne region to send logs to.

    :param value: Must be one of ["us", "eu", "ca", "data_set_us"].
    :type value: str
    """

    allowed_values = {
        "us",
        "eu",
        "ca",
        "data_set_us",
    }
    US: ClassVar["ObservabilityPipelineSentinelOneDestinationRegion"]
    EU: ClassVar["ObservabilityPipelineSentinelOneDestinationRegion"]
    CA: ClassVar["ObservabilityPipelineSentinelOneDestinationRegion"]
    DATA_SET_US: ClassVar["ObservabilityPipelineSentinelOneDestinationRegion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSentinelOneDestinationRegion.US = ObservabilityPipelineSentinelOneDestinationRegion("us")
ObservabilityPipelineSentinelOneDestinationRegion.EU = ObservabilityPipelineSentinelOneDestinationRegion("eu")
ObservabilityPipelineSentinelOneDestinationRegion.CA = ObservabilityPipelineSentinelOneDestinationRegion("ca")
ObservabilityPipelineSentinelOneDestinationRegion.DATA_SET_US = ObservabilityPipelineSentinelOneDestinationRegion(
    "data_set_us"
)
