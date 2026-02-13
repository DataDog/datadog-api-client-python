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
    from datadog_api_client.v2.model.facet_response_attributes import FacetResponseAttributes
    from datadog_api_client.v2.model.facet_type import FacetType


class FacetResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.facet_response_attributes import FacetResponseAttributes
        from datadog_api_client.v2.model.facet_type import FacetType

        return {
            "attributes": (FacetResponseAttributes,),
            "id": (str,),
            "type": (FacetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FacetResponseAttributes, id: str, type: FacetType, **kwargs):
        """
        Facet data.

        :param attributes: Facet attributes.
        :type attributes: FacetResponseAttributes

        :param id: The unique ID of the facet.
        :type id: str

        :param type: The JSON:API type for facets.
        :type type: FacetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
