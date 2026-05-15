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
    from datadog_api_client.v2.model.cost_tag_key_metadata_attributes import CostTagKeyMetadataAttributes
    from datadog_api_client.v2.model.cost_tag_key_metadata_type import CostTagKeyMetadataType


class CostTagKeyMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_metadata_attributes import CostTagKeyMetadataAttributes
        from datadog_api_client.v2.model.cost_tag_key_metadata_type import CostTagKeyMetadataType

        return {
            "attributes": (CostTagKeyMetadataAttributes,),
            "id": (str,),
            "type": (CostTagKeyMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostTagKeyMetadataAttributes, id: str, type: CostTagKeyMetadataType, **kwargs):
        """
        A Cloud Cost Management tag key metadata entry, aggregating coverage and example values for a single tag key, metric, and period.

        :param attributes: Attributes of a Cloud Cost Management tag key metadata entry.
        :type attributes: CostTagKeyMetadataAttributes

        :param id: A composite identifier of the form ``tag_key:metric`` for monthly roll-ups, or ``tag_key:metric:YYYY-MM-DD`` when ``filter[daily]=true``.
        :type id: str

        :param type: Type of the Cloud Cost Management tag key metadata resource.
        :type type: CostTagKeyMetadataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
