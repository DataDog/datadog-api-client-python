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
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "percentage": (float,),
            "rate": (int,),
            "type": (ObservabilityPipelineSampleProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "percentage": "percentage",
        "rate": "rate",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        type: ObservabilityPipelineSampleProcessorType,
        display_name: Union[str, UnsetType] = unset,
        percentage: Union[float, UnsetType] = unset,
        rate: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``sample`` processor allows probabilistic sampling of logs at a fixed rate.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param percentage: The percentage of logs to sample.
        :type percentage: float, optional

        :param rate: Number of events to sample (1 in N).
        :type rate: int, optional

        :param type: The processor type. The value should always be ``sample``.
        :type type: ObservabilityPipelineSampleProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if percentage is not unset:
            kwargs["percentage"] = percentage
        if rate is not unset:
            kwargs["rate"] = rate
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.type = type
