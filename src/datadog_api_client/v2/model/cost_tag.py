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
    from datadog_api_client.v2.model.cost_tag_attributes import CostTagAttributes
    from datadog_api_client.v2.model.cost_tag_type import CostTagType


class CostTag(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_attributes import CostTagAttributes
        from datadog_api_client.v2.model.cost_tag_type import CostTagType

        return {
            "attributes": (CostTagAttributes,),
            "id": (str,),
            "type": (CostTagType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostTagAttributes, id: str, type: CostTagType, **kwargs):
        """
        A Cloud Cost Management tag.

        :param attributes: Attributes of a Cloud Cost Management tag.
        :type attributes: CostTagAttributes

        :param id: The tag identifier, equal to its ``key:value`` representation.
        :type id: str

        :param type: Type of the Cloud Cost Management tag resource.
        :type type: CostTagType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
