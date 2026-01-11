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
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sample_processor_type import (
            ObservabilityPipelineSampleProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "group_by": ([str],),
            "id": (str,),
            "include": (str,),
            "percentage": (float,),
            "type": (ObservabilityPipelineSampleProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "group_by": "group_by",
        "id": "id",
        "include": "include",
        "percentage": "percentage",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        percentage: float,
        type: ObservabilityPipelineSampleProcessorType,
        display_name: Union[str, UnsetType] = unset,
        group_by: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``sample`` processor allows probabilistic sampling of logs at a fixed rate.

        **Supported pipeline types:** logs

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param group_by: Optional list of fields to group events by. Each group is sampled independently.
        :type group_by: [str], optional

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param percentage: The percentage of logs to sample.
        :type percentage: float

        :param type: The processor type. The value should always be ``sample``.
        :type type: ObservabilityPipelineSampleProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.percentage = percentage
        self_.type = type
