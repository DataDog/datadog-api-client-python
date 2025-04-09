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
    from datadog_api_client.v2.model.observability_pipeline_throttle_processor_type import (
        ObservabilityPipelineThrottleProcessorType,
    )


class ObservabilityPipelineThrottleProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_throttle_processor_type import (
            ObservabilityPipelineThrottleProcessorType,
        )

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "threshold": (int,),
            "type": (ObservabilityPipelineThrottleProcessorType,),
            "window": (float,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "threshold": "threshold",
        "type": "type",
        "window": "window",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        threshold: int,
        type: ObservabilityPipelineThrottleProcessorType,
        window: float,
        **kwargs,
    ):
        """
        The ``throttle`` processor limits the rate of events using a time-based window.

        :param id: Unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param threshold: The number of events allowed within the window.
        :type threshold: int

        :param type: The processor type. The value should always be ``throttle``.
        :type type: ObservabilityPipelineThrottleProcessorType

        :param window: The time window in seconds used for throttling.
        :type window: float
        """
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.threshold = threshold
        self_.type = type
        self_.window = window
