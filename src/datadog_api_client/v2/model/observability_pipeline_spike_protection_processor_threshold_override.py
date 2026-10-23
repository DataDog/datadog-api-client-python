# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold import (
        ObservabilityPipelineSpikeProtectionProcessorMinimalThreshold,
    )
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_bytes import (
        ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytes,
    )
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_always_keep import (
        ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeep,
    )


class ObservabilityPipelineSpikeProtectionProcessorThresholdOverride(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_field_value import ObservabilityPipelineFieldValue
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold import (
            ObservabilityPipelineSpikeProtectionProcessorMinimalThreshold,
        )

        return {
            "fields": ([ObservabilityPipelineFieldValue],),
            "minimal_threshold": (ObservabilityPipelineSpikeProtectionProcessorMinimalThreshold,),
        }

    attribute_map = {
        "fields": "fields",
        "minimal_threshold": "minimal_threshold",
    }

    def __init__(
        self_,
        fields: List[ObservabilityPipelineFieldValue],
        minimal_threshold: Union[
            ObservabilityPipelineSpikeProtectionProcessorMinimalThreshold,
            ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytes,
            ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdAlwaysKeep,
        ],
        **kwargs,
    ):
        """
        Defines a minimal threshold that applies to a specific partition instead of the processor-wide ``minimal_threshold``.

        :param fields: The set of field matchers that identifies the partition this override applies to. Every field name listed must also appear in ``partition_fields``.
        :type fields: [ObservabilityPipelineFieldValue]

        :param minimal_threshold: The minimal threshold to apply to the matching partition.
        :type minimal_threshold: ObservabilityPipelineSpikeProtectionProcessorMinimalThreshold
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.minimal_threshold = minimal_threshold
