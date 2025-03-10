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
    from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes


class PipelineData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pipeline_data_attributes import PipelineDataAttributes

        return {
            "attributes": (PipelineDataAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PipelineDataAttributes, type: str, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``PipelineData`` object.

        :param attributes: pipeline attributes
        :type attributes: PipelineDataAttributes

        :param id: Pipeline ID
        :type id: str, optional

        :param type: The type of the resource. The value should always be pipeline.
        :type type: str
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
