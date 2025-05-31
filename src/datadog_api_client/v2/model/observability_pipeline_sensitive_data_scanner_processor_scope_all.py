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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_all_target import (
        ObservabilityPipelineSensitiveDataScannerProcessorScopeAllTarget,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorScopeAll(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_all_target import (
            ObservabilityPipelineSensitiveDataScannerProcessorScopeAllTarget,
        )

        return {
            "target": (ObservabilityPipelineSensitiveDataScannerProcessorScopeAllTarget,),
        }

    attribute_map = {
        "target": "target",
    }

    def __init__(self_, target: ObservabilityPipelineSensitiveDataScannerProcessorScopeAllTarget, **kwargs):
        """
        Applies scanning across all available fields.

        :param target: Applies the rule to all fields.
        :type target: ObservabilityPipelineSensitiveDataScannerProcessorScopeAllTarget
        """
        super().__init__(kwargs)

        self_.target = target
