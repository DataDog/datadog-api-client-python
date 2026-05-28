# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplunkHecMetricsDestinationType(ModelSimple):
    """
    The destination type. Always `splunk_hec_metrics`.

    :param value: If omitted defaults to "splunk_hec_metrics". Must be one of ["splunk_hec_metrics"].
    :type value: str
    """

    allowed_values = {
        "splunk_hec_metrics",
    }
    SPLUNK_HEC_METRICS: ClassVar["ObservabilityPipelineSplunkHecMetricsDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplunkHecMetricsDestinationType.SPLUNK_HEC_METRICS = (
    ObservabilityPipelineSplunkHecMetricsDestinationType("splunk_hec_metrics")
)
