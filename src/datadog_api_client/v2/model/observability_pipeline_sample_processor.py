# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_sample_processor_type import (
        ObservabilityPipelineSampleProcessorType,
    )


class ObservabilityPipelineSampleProcessor(ModelNormal):
    validations = {
        "group_by": {
            "min_items": 1,
        },
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
            "group_by": ([str],),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "percentage": (float,),
            "rate": (int,),
            "type": (ObservabilityPipelineSampleProcessorType,),
        }

    attribute_map = {
        "group_by": "group_by",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "percentage": "percentage",
        "rate": "rate",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        type: ObservabilityPipelineSampleProcessorType,
        group_by: Union[List[str], UnsetType] = unset,
        percentage: Union[float, UnsetType] = unset,
        rate: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``sample`` processor allows probabilistic sampling of logs at a fixed rate.

        :param group_by: Optional list of fields to group events by. Each group is sampled independently.
        :type group_by: [str], optional

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param percentage: The percentage of logs to sample.
        :type percentage: float, optional

        :param rate: Number of events to sample (1 in N).
        :type rate: int, optional

        :param type: The processor type. The value should always be ``sample``.
        :type type: ObservabilityPipelineSampleProcessorType
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if percentage is not unset:
            kwargs["percentage"] = percentage
        if rate is not unset:
            kwargs["rate"] = rate
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.type = type
