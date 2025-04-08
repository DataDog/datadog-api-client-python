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
    from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor_type import (
        ObservabilityPipelineRemoveFieldsProcessorType,
    )


class ObservabilityPipelineRemoveFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor_type import (
            ObservabilityPipelineRemoveFieldsProcessorType,
        )

        return {
            "fields": ([str],),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineRemoveFieldsProcessorType,),
        }

    attribute_map = {
        "fields": "fields",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        fields: List[str],
        id: str,
        include: str,
        inputs: List[str],
        type: ObservabilityPipelineRemoveFieldsProcessorType,
        **kwargs,
    ):
        """
        The ``remove_fields`` processor deletes specified fields from logs.

        :param fields: A list of field names to be removed from each log event.
        :type fields: [str]

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: The ``PipelineRemoveFieldsProcessor`` ``inputs``.
        :type inputs: [str]

        :param type: The processor type. The value should always be ``remove_fields``.
        :type type: ObservabilityPipelineRemoveFieldsProcessorType
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
