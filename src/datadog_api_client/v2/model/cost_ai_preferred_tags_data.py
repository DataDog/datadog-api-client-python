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
    from datadog_api_client.v2.model.cost_ai_preferred_tags_attributes import CostAIPreferredTagsAttributes
    from datadog_api_client.v2.model.cost_ai_preferred_tags_type import CostAIPreferredTagsType


class CostAIPreferredTagsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_ai_preferred_tags_attributes import CostAIPreferredTagsAttributes
        from datadog_api_client.v2.model.cost_ai_preferred_tags_type import CostAIPreferredTagsType

        return {
            "attributes": (CostAIPreferredTagsAttributes,),
            "id": (str,),
            "type": (CostAIPreferredTagsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostAIPreferredTagsAttributes, id: str, type: CostAIPreferredTagsType, **kwargs):
        """
        Preferred tags data object.

        :param attributes: Attributes for the preferred tags response.
        :type attributes: CostAIPreferredTagsAttributes

        :param id: The unique identifier.
        :type id: str

        :param type: Preferred tags resource type.
        :type type: CostAIPreferredTagsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
