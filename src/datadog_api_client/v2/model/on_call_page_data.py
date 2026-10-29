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
    from datadog_api_client.v2.model.on_call_page_data_attributes import OnCallPageDataAttributes
    from datadog_api_client.v2.model.on_call_page_data_relationships import OnCallPageDataRelationships
    from datadog_api_client.v2.model.on_call_page_data_type import OnCallPageDataType


class OnCallPageData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_data_attributes import OnCallPageDataAttributes
        from datadog_api_client.v2.model.on_call_page_data_relationships import OnCallPageDataRelationships
        from datadog_api_client.v2.model.on_call_page_data_type import OnCallPageDataType

        return {
            "attributes": (OnCallPageDataAttributes,),
            "id": (UUID,),
            "relationships": (OnCallPageDataRelationships,),
            "type": (OnCallPageDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: OnCallPageDataType,
        attributes: Union[OnCallPageDataAttributes, UnsetType] = unset,
        relationships: Union[OnCallPageDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An On-Call Page.

        :param attributes: The attributes of an On-Call Page.
        :type attributes: OnCallPageDataAttributes, optional

        :param id: The unique ID of the Page.
        :type id: UUID

        :param relationships: The relationships of an On-Call Page.
        :type relationships: OnCallPageDataRelationships, optional

        :param type: Indicates that the resource is of type ``pages``.
        :type type: OnCallPageDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
