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
    from datadog_api_client.v2.model.cost_tag_key_attributes import CostTagKeyAttributes
    from datadog_api_client.v2.model.cost_tag_key_type import CostTagKeyType


class CostTagKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_attributes import CostTagKeyAttributes
        from datadog_api_client.v2.model.cost_tag_key_type import CostTagKeyType

        return {
            "attributes": (CostTagKeyAttributes,),
            "id": (str,),
            "type": (CostTagKeyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostTagKeyAttributes, id: str, type: CostTagKeyType, **kwargs):
        """
        A Cloud Cost Management tag key.

        :param attributes: Attributes of a Cloud Cost Management tag key.
        :type attributes: CostTagKeyAttributes

        :param id: The tag key identifier.
        :type id: str

        :param type: Type of the Cloud Cost Management tag key resource.
        :type type: CostTagKeyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
