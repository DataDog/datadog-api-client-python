# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PipelineDataAttributesConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "destinations": ([DatadogLogsDestination],),
            "processors": ([FilterProcessor, ParseJSONProcessor],),
            "sources": ([DatadogAgentSource],),
        }

    attribute_map = {
        "destinations": "destinations",
        "processors": "processors",
        "sources": "sources",
    }

    def __init__(
        self_,
        destinations: List[Union[DatadogLogsDestination]],
        processors: List[Union[FilterProcessor, ParseJSONProcessor]],
        sources: List[Union[DatadogAgentSource]],
        **kwargs,
    ):
        """
        pipeline config

        :param destinations: The ``PipelineDataAttributesConfig`` ``destinations``.
        :type destinations: [DatadogLogsDestination]

        :param processors: The ``PipelineDataAttributesConfig`` ``processors``.
        :type processors: [FilterProcessor, ParseJSONProcessor]

        :param sources: The ``PipelineDataAttributesConfig`` ``sources``.
        :type sources: [DatadogAgentSource]
        """
        super().__init__(kwargs)

        self_.destinations = destinations
        self_.processors = processors
        self_.sources = sources
