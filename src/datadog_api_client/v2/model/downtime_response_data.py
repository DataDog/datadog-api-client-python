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
    from datadog_api_client.v2.model.downtime_response_attributes import DowntimeResponseAttributes
    from datadog_api_client.v2.model.downtime_relationships import DowntimeRelationships
    from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType


class DowntimeResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_response_attributes import DowntimeResponseAttributes
        from datadog_api_client.v2.model.downtime_relationships import DowntimeRelationships
        from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType

        return {
            "attributes": (DowntimeResponseAttributes,),
            "id": (str,),
            "relationships": (DowntimeRelationships,),
            "type": (DowntimeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DowntimeResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[DowntimeRelationships, UnsetType] = unset,
        type: Union[DowntimeResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Downtime data.

        :param attributes: Downtime details.
        :type attributes: DowntimeResponseAttributes, optional

        :param id: The downtime ID.
        :type id: str, optional

        :param relationships: All relationships associated with downtime.
        :type relationships: DowntimeRelationships, optional

        :param type: Downtime resource type.
        :type type: DowntimeResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
