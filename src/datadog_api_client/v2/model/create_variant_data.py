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
    from datadog_api_client.v2.model.create_variant import CreateVariant
    from datadog_api_client.v2.model.variant_data_type import VariantDataType


class CreateVariantData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_variant import CreateVariant
        from datadog_api_client.v2.model.variant_data_type import VariantDataType

        return {
            "attributes": (CreateVariant,),
            "type": (VariantDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateVariant, type: VariantDataType, **kwargs):
        """
        Data for adding a variant to a feature flag.

        :param attributes: Attributes for creating a variant.
        :type attributes: CreateVariant

        :param type: The resource type for variants.
        :type type: VariantDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
