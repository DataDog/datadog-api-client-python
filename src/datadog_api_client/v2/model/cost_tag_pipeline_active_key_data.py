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
    from datadog_api_client.v2.model.cost_tag_pipeline_active_key_attributes import CostTagPipelineActiveKeyAttributes
    from datadog_api_client.v2.model.cost_tag_pipeline_active_key_type import CostTagPipelineActiveKeyType


class CostTagPipelineActiveKeyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_pipeline_active_key_attributes import (
            CostTagPipelineActiveKeyAttributes,
        )
        from datadog_api_client.v2.model.cost_tag_pipeline_active_key_type import CostTagPipelineActiveKeyType

        return {
            "attributes": (CostTagPipelineActiveKeyAttributes,),
            "id": (str,),
            "type": (CostTagPipelineActiveKeyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: CostTagPipelineActiveKeyAttributes, id: str, type: CostTagPipelineActiveKeyType, **kwargs
    ):
        """
        Active tag key data object.

        :param attributes: Attributes for an active tag pipeline key.
        :type attributes: CostTagPipelineActiveKeyAttributes

        :param id: The tag key name.
        :type id: str

        :param type: Active tag key resource type.
        :type type: CostTagPipelineActiveKeyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
