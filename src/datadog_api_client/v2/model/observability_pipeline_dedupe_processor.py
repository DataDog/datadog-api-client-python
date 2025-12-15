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
    from datadog_api_client.v2.model.observability_pipeline_dedupe_processor_mode import (
        ObservabilityPipelineDedupeProcessorMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_dedupe_processor_type import (
        ObservabilityPipelineDedupeProcessorType,
    )


class ObservabilityPipelineDedupeProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_dedupe_processor_mode import (
            ObservabilityPipelineDedupeProcessorMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_dedupe_processor_type import (
            ObservabilityPipelineDedupeProcessorType,
        )

        return {
            "enabled": (bool,),
            "fields": ([str],),
            "id": (str,),
            "include": (str,),
            "mode": (ObservabilityPipelineDedupeProcessorMode,),
            "type": (ObservabilityPipelineDedupeProcessorType,),
        }

    attribute_map = {
        "enabled": "enabled",
        "fields": "fields",
        "id": "id",
        "include": "include",
        "mode": "mode",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        fields: List[str],
        id: str,
        include: str,
        mode: ObservabilityPipelineDedupeProcessorMode,
        type: ObservabilityPipelineDedupeProcessorType,
        **kwargs,
    ):
        """
        The ``dedupe`` processor removes duplicate fields in log events.

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param fields: A list of log field paths to check for duplicates.
        :type fields: [str]

        :param id: The unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param mode: The deduplication mode to apply to the fields.
        :type mode: ObservabilityPipelineDedupeProcessorMode

        :param type: The processor type. The value should always be ``dedupe``.
        :type type: ObservabilityPipelineDedupeProcessorType
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.fields = fields
        self_.id = id
        self_.include = include
        self_.mode = mode
        self_.type = type
