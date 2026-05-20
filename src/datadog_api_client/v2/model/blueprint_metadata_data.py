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
    from datadog_api_client.v2.model.blueprint_metadata_attributes import BlueprintMetadataAttributes
    from datadog_api_client.v2.model.blueprint_data_type import BlueprintDataType


class BlueprintMetadataData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.blueprint_metadata_attributes import BlueprintMetadataAttributes
        from datadog_api_client.v2.model.blueprint_data_type import BlueprintDataType

        return {
            "attributes": (BlueprintMetadataAttributes,),
            "id": (UUID,),
            "type": (BlueprintDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: BlueprintMetadataAttributes, id: UUID, type: BlueprintDataType, **kwargs):
        """
        A blueprint metadata resource.

        :param attributes: The attributes of a blueprint metadata resource.
        :type attributes: BlueprintMetadataAttributes

        :param id: The ID of the blueprint.
        :type id: UUID

        :param type: The resource type for a blueprint.
        :type type: BlueprintDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
