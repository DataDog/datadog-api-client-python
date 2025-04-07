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
    from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
        ObservabilityPipelineFilterProcessorType,
    )


class ObservabilityPipelineFilterProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_filter_processor_type import (
            ObservabilityPipelineFilterProcessorType,
        )

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineFilterProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_, id: str, include: str, inputs: List[str], type: ObservabilityPipelineFilterProcessorType, **kwargs
    ):
        """
        The ``filter`` processor allows conditional processing of logs based on a Datadog search query. Logs that match the ``include`` query are passed through; others are discarded.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The processor type. The value should always be ``filter``.
        :type type: ObservabilityPipelineFilterProcessorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
