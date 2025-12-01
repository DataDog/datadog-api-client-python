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
    from datadog_api_client.v2.model.restriction_query_attributes import RestrictionQueryAttributes
    from datadog_api_client.v2.model.user_relationships import UserRelationships
    from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType


class RestrictionQueryWithRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_query_attributes import RestrictionQueryAttributes
        from datadog_api_client.v2.model.user_relationships import UserRelationships
        from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType

        return {
            "attributes": (RestrictionQueryAttributes,),
            "id": (str,),
            "relationships": (UserRelationships,),
            "type": (LogsRestrictionQueriesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RestrictionQueryAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[UserRelationships, UnsetType] = unset,
        type: Union[LogsRestrictionQueriesType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Restriction query object returned by the API.

        :param attributes: Attributes of the restriction query.
        :type attributes: RestrictionQueryAttributes, optional

        :param id: ID of the restriction query.
        :type id: str, optional

        :param relationships: Relationships of the user object.
        :type relationships: UserRelationships, optional

        :param type: Restriction query resource type.
        :type type: LogsRestrictionQueriesType, optional
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
