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
    from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes


class PipelineCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes

        return {
            "attributes": (PipelineDataAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: PipelineDataAttributes, type: str, **kwargs):
        """
        Contains the pipeline’s ID, type, and configuration attributes.

        :param attributes: Defines the pipeline’s name and its components (sources, processors, and destinations).
        :type attributes: PipelineDataAttributes

        :param type: The resource type identifier. For pipeline resources, this should always be set to "pipelines".
        :type type: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
