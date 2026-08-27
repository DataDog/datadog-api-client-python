# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSplunkHecDestinationEndpointTarget(ModelSimple):
    """
    The Splunk HEC endpoint to send events to. Use `event` to send structured events to the `/event` endpoint, or `raw` to send the raw message to the `/raw` endpoint.

    :param value: Must be one of ["event", "raw"].
    :type value: str
    """

    allowed_values = {
        "event",
        "raw",
    }
    EVENT: ClassVar["ObservabilityPipelineSplunkHecDestinationEndpointTarget"]
    RAW: ClassVar["ObservabilityPipelineSplunkHecDestinationEndpointTarget"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSplunkHecDestinationEndpointTarget.EVENT = ObservabilityPipelineSplunkHecDestinationEndpointTarget(
    "event"
)
ObservabilityPipelineSplunkHecDestinationEndpointTarget.RAW = ObservabilityPipelineSplunkHecDestinationEndpointTarget(
    "raw"
)
