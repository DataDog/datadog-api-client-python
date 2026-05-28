# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplunkHecMetricsDestinationCompression(ModelSimple):
    """
    Compression algorithm applied when sending metrics to Splunk HEC.

    :param value: If omitted defaults to "none". Must be one of ["none", "gzip"].
    :type value: str
    """

    allowed_values = {
        "none",
        "gzip",
    }
    NONE: ClassVar["ObservabilityPipelineSplunkHecMetricsDestinationCompression"]
    GZIP: ClassVar["ObservabilityPipelineSplunkHecMetricsDestinationCompression"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplunkHecMetricsDestinationCompression.NONE = (
    ObservabilityPipelineSplunkHecMetricsDestinationCompression("none")
)
ObservabilityPipelineSplunkHecMetricsDestinationCompression.GZIP = (
    ObservabilityPipelineSplunkHecMetricsDestinationCompression("gzip")
)
