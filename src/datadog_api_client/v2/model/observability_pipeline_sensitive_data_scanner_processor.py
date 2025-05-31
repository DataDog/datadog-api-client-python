# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_rule import (
        ObservabilityPipelineSensitiveDataScannerProcessorRule,
    )
    from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_type import (
        ObservabilityPipelineSensitiveDataScannerProcessorType,
    )


class ObservabilityPipelineSensitiveDataScannerProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_rule import (
            ObservabilityPipelineSensitiveDataScannerProcessorRule,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_type import (
            ObservabilityPipelineSensitiveDataScannerProcessorType,
        )

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "rules": ([ObservabilityPipelineSensitiveDataScannerProcessorRule],),
            "type": (ObservabilityPipelineSensitiveDataScannerProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "rules": "rules",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        rules: List[ObservabilityPipelineSensitiveDataScannerProcessorRule],
        type: ObservabilityPipelineSensitiveDataScannerProcessorType,
        **kwargs,
    ):
        """
        The ``sensitive_data_scanner`` processor detects and optionally redacts sensitive data in log events.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param rules: A list of rules for identifying and acting on sensitive data patterns.
        :type rules: [ObservabilityPipelineSensitiveDataScannerProcessorRule]

        :param type: The processor type. The value should always be ``sensitive_data_scanner``.
        :type type: ObservabilityPipelineSensitiveDataScannerProcessorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.rules = rules
        self_.type = type
