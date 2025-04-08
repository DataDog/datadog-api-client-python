# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig


class ObservabilityPipelineDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_config import ObservabilityPipelineConfig

        return {
            "config": (ObservabilityPipelineConfig,),
            "name": (str,),
        }

    attribute_map = {
        "config": "config",
        "name": "name",
    }

    def __init__(self_, config: ObservabilityPipelineConfig, name: str, **kwargs):
        """
        Defines the pipeline’s name and its components (sources, processors, and destinations).

        :param config: Specifies the pipeline's configuration, including its sources, processors, and destinations.
        :type config: ObservabilityPipelineConfig

        :param name: Name of the pipeline.
        :type name: str
        """
        super().__init__(kwargs)

        self_.config = config
        self_.name = name
