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
    from datadog_api_client.v2.model.status_page_as_included_attributes import StatusPageAsIncludedAttributes
    from datadog_api_client.v2.model.status_page_as_included_relationships import StatusPageAsIncludedRelationships
    from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType


class StatusPageAsIncluded(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_as_included_attributes import StatusPageAsIncludedAttributes
        from datadog_api_client.v2.model.status_page_as_included_relationships import StatusPageAsIncludedRelationships
        from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

        return {
            "attributes": (StatusPageAsIncludedAttributes,),
            "id": (str,),
            "relationships": (StatusPageAsIncludedRelationships,),
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
        attributes: Union[StatusPageAsIncludedAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[StatusPageAsIncludedRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: StatusPageAsIncludedAttributes, optional

        :param id:
        :type id: str, optional

        :param relationships:
        :type relationships: StatusPageAsIncludedRelationships, optional

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
