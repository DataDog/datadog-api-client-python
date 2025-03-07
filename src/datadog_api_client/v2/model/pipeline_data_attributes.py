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
    from datadog_api_client.v2.model.pipeline_data_attributes_config import PipelineDataAttributesConfig


class PipelineDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pipeline_data_attributes_config import PipelineDataAttributesConfig

        return {
            "config": (PipelineDataAttributesConfig,),
            "name": (str,),
        }

    attribute_map = {
        "config": "config",
        "name": "name",
    }

    def __init__(self_, config: PipelineDataAttributesConfig, name: str, **kwargs):
        """
        pipeline attributes

        :param config: pipeline config
        :type config: PipelineDataAttributesConfig

        :param name: The pipeline name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.config = config
        self_.name = name
