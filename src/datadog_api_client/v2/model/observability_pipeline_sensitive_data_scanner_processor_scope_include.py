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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_options import (
        ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_include_target import (
        ObservabilityPipelineSensitiveDataScannerProcessorScopeIncludeTarget,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorScopeInclude(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_options import (
            ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_include_target import (
            ObservabilityPipelineSensitiveDataScannerProcessorScopeIncludeTarget,
        )

        return {
            "options": (ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions,),
            "target": (ObservabilityPipelineSensitiveDataScannerProcessorScopeIncludeTarget,),
        }

    attribute_map = {
        "options": "options",
        "target": "target",
    }

    def __init__(
        self_,
        options: ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions,
        target: ObservabilityPipelineSensitiveDataScannerProcessorScopeIncludeTarget,
        **kwargs,
    ):
        """
        Includes only specific fields for sensitive data scanning.

        :param options: Fields to which the scope rule applies.
        :type options: ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions

        :param target: Applies the rule only to included fields.
        :type target: ObservabilityPipelineSensitiveDataScannerProcessorScopeIncludeTarget
        """
        super().__init__(kwargs)

        self_.options = options
        self_.target = target
