# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_hash_action import (
        ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction,
    )


class ObservabilityPipelineSensitiveDataScannerProcessorActionHash(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_action_hash_action import (
            ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction,
        )

        return {
            "action": (ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction,),
            "options": (dict,),
        }

    attribute_map = {
        "action": "action",
        "options": "options",
    }

    def __init__(
        self_,
        action: ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction,
        options: Union[dict, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for hashing matched sensitive values.

        :param action: Action type that replaces the matched sensitive data with a hashed representation, preserving structure while securing content.
        :type action: ObservabilityPipelineSensitiveDataScannerProcessorActionHashAction

        :param options: The ``ObservabilityPipelineSensitiveDataScannerProcessorActionHash`` ``options``.
        :type options: dict, optional
        """
        if options is not unset:
            kwargs["options"] = options
        super().__init__(kwargs)

        self_.action = action
