# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSpikeProtectionProcessorSpikeAction(ModelSimple):
    """
    The action to take with matching logs while spike protection is active. Options:
        - `drop`: Drop the event.
        - `no_action`: Let the event pass through.
        - `overflow_routing`: Route to an overflow destination.

        When `overflow_routing` is used, there must be a destination whose `inputs` reference this processor with the `<processor-id>.overflow_events` suffix to route the overflowing events.

    :param value: Must be one of ["drop", "no_action", "overflow_routing"].
    :type value: str
    """

    allowed_values = {
        "drop",
        "no_action",
        "overflow_routing",
    }
    DROP: ClassVar["ObservabilityPipelineSpikeProtectionProcessorSpikeAction"]
    NO_ACTION: ClassVar["ObservabilityPipelineSpikeProtectionProcessorSpikeAction"]
    OVERFLOW_ROUTING: ClassVar["ObservabilityPipelineSpikeProtectionProcessorSpikeAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSpikeProtectionProcessorSpikeAction.DROP = (
    ObservabilityPipelineSpikeProtectionProcessorSpikeAction("drop")
)
ObservabilityPipelineSpikeProtectionProcessorSpikeAction.NO_ACTION = (
    ObservabilityPipelineSpikeProtectionProcessorSpikeAction("no_action")
)
ObservabilityPipelineSpikeProtectionProcessorSpikeAction.OVERFLOW_ROUTING = (
    ObservabilityPipelineSpikeProtectionProcessorSpikeAction("overflow_routing")
)
