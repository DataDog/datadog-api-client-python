# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class VercelTraceConfig(ModelNormal):
    validations = {
        "sampling_percentage": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "is_deprecated_otel": (bool,),
            "sampling_percentage": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "is_deprecated_otel": "isDeprecatedOtel",
        "sampling_percentage": "samplingPercentage",
    }

    def __init__(self_, enabled: bool, is_deprecated_otel: bool, sampling_percentage: int, **kwargs):
        """
        Tracing configuration for the Vercel integration.

        :param enabled: Whether tracing is enabled.
        :type enabled: bool

        :param is_deprecated_otel: Whether the configuration uses the deprecated OpenTelemetry tracing setup.
        :type is_deprecated_otel: bool

        :param sampling_percentage: Percentage of traces to forward to Datadog, between 0 and 100.
        :type sampling_percentage: int
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.is_deprecated_otel = is_deprecated_otel
        self_.sampling_percentage = sampling_percentage
