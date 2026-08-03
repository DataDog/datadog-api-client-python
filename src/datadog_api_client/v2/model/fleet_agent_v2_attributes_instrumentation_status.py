# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetAgentV2AttributesInstrumentationStatus(ModelSimple):
    """
    The single-step instrumentation status of the Agent.

    :param value: Must be one of ["success", "failure"].
    :type value: str
    """

    allowed_values = {
        "success",
        "failure",
    }
    SUCCESS: ClassVar["FleetAgentV2AttributesInstrumentationStatus"]
    FAILURE: ClassVar["FleetAgentV2AttributesInstrumentationStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetAgentV2AttributesInstrumentationStatus.SUCCESS = FleetAgentV2AttributesInstrumentationStatus("success")
FleetAgentV2AttributesInstrumentationStatus.FAILURE = FleetAgentV2AttributesInstrumentationStatus("failure")
