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
    from datadog_api_client.v2.model.observability_pipeline_sample_processor_type import (
        ObservabilityPipelineSampleProcessorType,
    )


class ObservabilityPipelineSampleProcessor(ModelNormal):
    validations = {
        "rate": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sample_processor_type import (
            ObservabilityPipelineSampleProcessorType,
        )

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "rate": (int,),
            "type": (ObservabilityPipelineSampleProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "rate": "rate",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        rate: int,
        type: ObservabilityPipelineSampleProcessorType,
        **kwargs,
    ):
        """
        The ``sample`` processor allows probabilistic sampling of logs at a fixed rate.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param rate: Number of events to sample (1 in N).
        :type rate: int

        :param type: The processor type. The value should always be ``sample``.
        :type type: ObservabilityPipelineSampleProcessorType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.rate = rate
        self_.type = type
