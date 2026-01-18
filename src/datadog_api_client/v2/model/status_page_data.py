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
    from datadog_api_client.v2.model.status_page_data_attributes import StatusPageDataAttributes
    from datadog_api_client.v2.model.status_page_data_relationships import StatusPageDataRelationships
    from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType


class StatusPageData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_data_attributes import StatusPageDataAttributes
        from datadog_api_client.v2.model.status_page_data_relationships import StatusPageDataRelationships
        from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

        return {
            "attributes": (StatusPageDataAttributes,),
            "id": (UUID,),
            "relationships": (StatusPageDataRelationships,),
            "type": (StatusPageDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: StatusPageDataType,
        attributes: Union[StatusPageDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        relationships: Union[StatusPageDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: The attributes of a status page.
        :type attributes: StatusPageDataAttributes, optional

        :param id: The ID of the status page.
        :type id: UUID, optional

        :param relationships: The relationships of a status page.
        :type relationships: StatusPageDataRelationships, optional

        :param type: Status pages resource type.
        :type type: StatusPageDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
