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
    from datadog_api_client.v2.model.model_lab_facet_keys_attributes import ModelLabFacetKeysAttributes
    from datadog_api_client.v2.model.model_lab_facet_keys_type import ModelLabFacetKeysType


class ModelLabFacetKeysData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_facet_keys_attributes import ModelLabFacetKeysAttributes
        from datadog_api_client.v2.model.model_lab_facet_keys_type import ModelLabFacetKeysType

        return {
            "attributes": (ModelLabFacetKeysAttributes,),
            "id": (str,),
            "type": (ModelLabFacetKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ModelLabFacetKeysAttributes, id: str, type: ModelLabFacetKeysType, **kwargs):
        """
        A facet keys JSON:API resource object.

        :param attributes: Available facet key names for filtering resources.
        :type attributes: ModelLabFacetKeysAttributes

        :param id: The unique identifier of the facet keys resource.
        :type id: str

        :param type: The JSON:API type for a facet keys resource.
        :type type: ModelLabFacetKeysType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
