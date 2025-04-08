# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDatadogAgentSourceType(ModelSimple):
    """
    The source type. The value should always be `datadog_agent`.

    :param value: If omitted defaults to "datadog_agent". Must be one of ["datadog_agent"].
    :type value: str
    """

    allowed_values = {
        "datadog_agent",
    }
    DATADOG_AGENT: ClassVar["ObservabilityPipelineDatadogAgentSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDatadogAgentSourceType.DATADOG_AGENT = ObservabilityPipelineDatadogAgentSourceType("datadog_agent")
