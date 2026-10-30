# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.variant_response_attributes import VariantResponseAttributes
    from datadog_api_client.v2.model.variant_data_type import VariantDataType


class VariantResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.variant_response_attributes import VariantResponseAttributes
        from datadog_api_client.v2.model.variant_data_type import VariantDataType

        return {
            "attributes": (VariantResponseAttributes,),
            "id": (UUID,),
            "type": (VariantDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: VariantResponseAttributes, id: UUID, type: VariantDataType, **kwargs):
        """
        A variant resource.

        :param attributes: Attributes of a variant.
        :type attributes: VariantResponseAttributes

        :param id: The unique identifier of the variant.
        :type id: UUID

        :param type: The resource type for variants.
        :type type: VariantDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
