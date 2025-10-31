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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_response_data_attributes import EntityResponseDataAttributes
    from datadog_api_client.v2.model.entity_response_data_relationships import EntityResponseDataRelationships
    from datadog_api_client.v2.model.entity_response_data_type import EntityResponseDataType


class PreviewEntityResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_data_attributes import EntityResponseDataAttributes
        from datadog_api_client.v2.model.entity_response_data_relationships import EntityResponseDataRelationships
        from datadog_api_client.v2.model.entity_response_data_type import EntityResponseDataType

        return {
            "attributes": (EntityResponseDataAttributes,),
            "id": (str,),
            "relationships": (EntityResponseDataRelationships,),
            "type": (EntityResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: EntityResponseDataType,
        attributes: Union[EntityResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[EntityResponseDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: EntityResponseDataAttributes, optional

        :param id:
        :type id: str, optional

        :param relationships:
        :type relationships: EntityResponseDataRelationships, optional

        :param type: Entity resource type.
        :type type: EntityResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
