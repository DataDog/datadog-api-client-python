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
    from datadog_api_client.v2.model.dem_variant_attributes import DemVariantAttributes
    from datadog_api_client.v2.model.dem_variant_type import DemVariantType


class DemVariantResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_variant_attributes import DemVariantAttributes
        from datadog_api_client.v2.model.dem_variant_type import DemVariantType

        return {
            "attributes": (DemVariantAttributes,),
            "id": (str,),
            "type": (DemVariantType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DemVariantAttributes, id: str, type: DemVariantType, **kwargs):
        """
        Data object returned for a DEM journey variant.

        :param attributes: Attributes of a DEM journey variant.
        :type attributes: DemVariantAttributes

        :param id: The unique identifier of the variant.
        :type id: str

        :param type: The type identifier for DEM journey variants.
        :type type: DemVariantType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
