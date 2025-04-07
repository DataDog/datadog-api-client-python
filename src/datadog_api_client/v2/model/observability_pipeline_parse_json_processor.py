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
    from datadog_api_client.v2.model.observability_pipeline_parse_json_processor_type import (
        ObservabilityPipelineParseJSONProcessorType,
    )


class ObservabilityPipelineParseJSONProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_parse_json_processor_type import (
            ObservabilityPipelineParseJSONProcessorType,
        )

        return {
            "field": (str,),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineParseJSONProcessorType,),
        }

    attribute_map = {
        "field": "field",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        field: str,
        id: str,
        include: str,
        inputs: List[str],
        type: ObservabilityPipelineParseJSONProcessorType,
        **kwargs,
    ):
        """
        The ``parse_json`` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.

        :param field: The name of the log field that contains a JSON string.
        :type field: str

        :param id: A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The processor type. The value should always be ``parse_json``.
        :type type: ObservabilityPipelineParseJSONProcessorType
        """
        super().__init__(kwargs)

        self_.field = field
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
