# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineQuotaProcessorOverflowAction(ModelSimple):
    """
    The action to take when the quota is exceeded. Options:
        - `drop`: Drop the event.
        - `no_action`: Let the event pass through.
        - `overflow_routing`: Route to an overflow destination.


    :param value: Must be one of ["drop", "no_action", "overflow_routing"].
    :type value: str
    """

    allowed_values = {
        "drop",
        "no_action",
        "overflow_routing",
    }
    DROP: ClassVar["ObservabilityPipelineQuotaProcessorOverflowAction"]
    NO_ACTION: ClassVar["ObservabilityPipelineQuotaProcessorOverflowAction"]
    OVERFLOW_ROUTING: ClassVar["ObservabilityPipelineQuotaProcessorOverflowAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineQuotaProcessorOverflowAction.DROP = ObservabilityPipelineQuotaProcessorOverflowAction("drop")
ObservabilityPipelineQuotaProcessorOverflowAction.NO_ACTION = ObservabilityPipelineQuotaProcessorOverflowAction(
    "no_action"
)
ObservabilityPipelineQuotaProcessorOverflowAction.OVERFLOW_ROUTING = ObservabilityPipelineQuotaProcessorOverflowAction(
    "overflow_routing"
)
