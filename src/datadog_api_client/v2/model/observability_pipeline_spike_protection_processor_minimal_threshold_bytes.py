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
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_bytes_type import (
        ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType,
    )


class ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_minimal_threshold_bytes_type import (
            ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType,
        )

        return {
            "bytes": (int,),
            "type": (ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType,),
        }

    attribute_map = {
        "bytes": "bytes",
        "type": "type",
    }

    def __init__(
        self_, bytes: int, type: ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType, **kwargs
    ):
        """
        Sets a specific byte threshold for the matching partition.

        :param bytes: The minimal threshold, in bytes, for the matching partition.
        :type bytes: int

        :param type: The minimal threshold type. The value should always be ``threshold``.
        :type type: ObservabilityPipelineSpikeProtectionProcessorMinimalThresholdBytesType
        """
        super().__init__(kwargs)

        self_.bytes = bytes
        self_.type = type
