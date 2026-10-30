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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.update_variant_attributes import UpdateVariantAttributes
    from datadog_api_client.v2.model.variant_data_type import VariantDataType


class UpdateVariantData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_variant_attributes import UpdateVariantAttributes
        from datadog_api_client.v2.model.variant_data_type import VariantDataType

        return {
            "attributes": (UpdateVariantAttributes,),
            "id": (UUID,),
            "type": (VariantDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: UpdateVariantAttributes, type: VariantDataType, id: Union[UUID, UnsetType] = unset, **kwargs
    ):
        """
        Data for updating a variant.

        :param attributes: Attributes for updating a variant.
        :type attributes: UpdateVariantAttributes

        :param id: The ID of the variant. If you include it, use the same value as the ``variant_id`` path parameter.
        :type id: UUID, optional

        :param type: The resource type for variants.
        :type type: VariantDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
