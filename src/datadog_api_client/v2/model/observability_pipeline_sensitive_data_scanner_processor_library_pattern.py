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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_library_pattern_options import (
        ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_library_pattern_type import (
        ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorLibraryPattern(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_library_pattern_options import (
            ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternOptions,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_library_pattern_type import (
            ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType,
        )

        return {
            "options": (ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternOptions,),
            "type": (ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType,),
        }

    attribute_map = {
        "options": "options",
        "type": "type",
    }

    def __init__(
        self_,
        options: ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternOptions,
        type: ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType,
        **kwargs,
    ):
        """
        Specifies a pattern from Datadog’s sensitive data detection library to match known sensitive data types.

        :param options: Options for selecting a predefined library pattern and enabling keyword support.
        :type options: ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternOptions

        :param type: Indicates that a predefined library pattern is used.
        :type type: ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternType
        """
        super().__init__(kwargs)

        self_.options = options
        self_.type = type
