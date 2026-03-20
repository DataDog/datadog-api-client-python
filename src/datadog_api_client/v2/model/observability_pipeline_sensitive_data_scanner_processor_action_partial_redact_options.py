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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact_options_direction import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact_options_direction import (
            ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection,
        )

        return {
            "characters": (int,),
            "direction": (ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection,),
        }

    attribute_map = {
        "characters": "characters",
        "direction": "direction",
    }

    def __init__(
        self_,
        characters: int,
        direction: ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection,
        **kwargs,
    ):
        """
        Controls how partial redaction is applied, including character count and direction.

        :param characters: The ``ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions`` ``characters``.
        :type characters: int

        :param direction: Indicates whether to redact characters from the first or last part of the matched value.
        :type direction: ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptionsDirection
        """
        super().__init__(kwargs)

        self_.characters = characters
        self_.direction = direction
