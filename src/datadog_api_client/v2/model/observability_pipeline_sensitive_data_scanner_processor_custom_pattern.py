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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_custom_pattern_options import (
        ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_custom_pattern_type import (
        ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternType,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorCustomPattern(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_custom_pattern_options import (
            ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_custom_pattern_type import (
            ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternType,
        )

        return {
            "options": (ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions,),
            "type": (ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternType,),
        }

    attribute_map = {
        "options": "options",
        "type": "type",
    }

    def __init__(
        self_,
        options: ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions,
        type: ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternType,
        **kwargs,
    ):
        """
        Defines a custom regex-based pattern for identifying sensitive data in logs.

        :param options: Options for defining a custom regex pattern.
        :type options: ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions

        :param type: Indicates a custom regular expression is used for matching.
        :type type: ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternType
        """
        super().__init__(kwargs)

        self_.options = options
        self_.type = type
