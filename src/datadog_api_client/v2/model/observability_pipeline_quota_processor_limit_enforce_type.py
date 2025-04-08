# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineQuotaProcessorLimitEnforceType(ModelSimple):
    """
    Unit for quota enforcement in bytes for data size or events for count.

    :param value: Must be one of ["bytes", "events"].
    :type value: str
    """

    allowed_values = {
        "bytes",
        "events",
    }
    BYTES: ClassVar["ObservabilityPipelineQuotaProcessorLimitEnforceType"]
    EVENTS: ClassVar["ObservabilityPipelineQuotaProcessorLimitEnforceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineQuotaProcessorLimitEnforceType.BYTES = ObservabilityPipelineQuotaProcessorLimitEnforceType("bytes")
ObservabilityPipelineQuotaProcessorLimitEnforceType.EVENTS = ObservabilityPipelineQuotaProcessorLimitEnforceType(
    "events"
)
