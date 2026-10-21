# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_always_keep_type import (
        ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType,
    )


class ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_always_keep_type import (
            ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType,
        )

        return {
            "type": (ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType, **kwargs):
        """
        Never activates spike protection for the matching partition, regardless of volume.

        :param type: The minimal threshold type. The value should always be ``always_keep``.
        :type type: ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeepType
        """
        super().__init__(kwargs)

        self_.type = type
