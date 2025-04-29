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
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_redact_action import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_redact_options import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorActionRedact(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_redact_action import (
            ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_redact_options import (
            ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions,
        )

        return {
            "action": (ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction,),
            "options": (ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions,),
        }

    attribute_map = {
        "action": "action",
        "options": "options",
    }

    def __init__(
        self_,
        action: ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction,
        options: ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions,
        **kwargs,
    ):
        """
        Configuration for completely redacting matched sensitive data.

        :param action: Action type that completely replaces the matched sensitive data with a fixed replacement string to remove all visibility.
        :type action: ObservabilityPipelineSensitiveDataScannerProcessorActionRedactAction

        :param options: Configuration for fully redacting sensitive data.
        :type options: ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions
        """
        super().__init__(kwargs)

        self_.action = action
        self_.options = options
