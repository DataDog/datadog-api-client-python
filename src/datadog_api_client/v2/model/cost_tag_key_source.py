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
    from datadog_api_client.v2.model.cost_tag_key_source_attributes import CostTagKeySourceAttributes
    from datadog_api_client.v2.model.cost_tag_key_source_type import CostTagKeySourceType


class CostTagKeySource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_source_attributes import CostTagKeySourceAttributes
        from datadog_api_client.v2.model.cost_tag_key_source_type import CostTagKeySourceType

        return {
            "attributes": (CostTagKeySourceAttributes,),
            "id": (str,),
            "type": (CostTagKeySourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostTagKeySourceAttributes, id: str, type: CostTagKeySourceType, **kwargs):
        """
        A Cloud Cost Management tag key paired with the sources that produced it.

        :param attributes: Attributes of a Cloud Cost Management tag source.
        :type attributes: CostTagKeySourceAttributes

        :param id: The tag key identifier. Equal to the empty-tag sentinel ``__empty_tag_key__`` when the tag key is empty.
        :type id: str

        :param type: Type of the Cloud Cost Management tag source resource.
        :type type: CostTagKeySourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
