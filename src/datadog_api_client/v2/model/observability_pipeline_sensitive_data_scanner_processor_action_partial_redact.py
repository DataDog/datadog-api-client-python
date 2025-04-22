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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact_action import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact_options import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedact(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact_action import (
            ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_partial_redact_options import (
            ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions,
        )

        return {
            "action": (ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction,),
            "options": (ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions,),
        }

    attribute_map = {
        "action": "action",
        "options": "options",
    }

    def __init__(
        self_,
        action: ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction,
        options: ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions,
        **kwargs,
    ):
        """
        The definition of ``ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedact`` object.

        :param action: The definition of ``ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction`` object.
        :type action: ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactAction

        :param options: The definition of ``ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions`` object.
        :type options: ObservabilityPipelineSensitiveDataScannerProcessorActionPartialRedactOptions
        """
        super().__init__(kwargs)

        self_.action = action
        self_.options = options
