# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.segment_user import SegmentUser
    from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery


class SegmentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_user import SegmentUser
        from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery

        return {
            "created_at": (datetime,),
            "created_by": (SegmentUser,),
            "data_query": (SegmentDataQuery,),
            "description": (str,),
            "disabled_at": (datetime,),
            "disabled_by": (SegmentUser,),
            "entity": (str,),
            "materialized_at": (datetime, none_type),
            "modified_at": (datetime,),
            "modified_by": (SegmentUser,),
            "name": (str,),
            "org_id": (int,),
            "row_count": (int,),
            "source": (int,),
            "tags": ([str], none_type),
            "type": (str,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "data_query": "data_query",
        "description": "description",
        "disabled_at": "disabled_at",
        "disabled_by": "disabled_by",
        "entity": "entity",
        "materialized_at": "materialized_at",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "org_id": "org_id",
        "row_count": "row_count",
        "source": "source",
        "tags": "tags",
        "type": "type",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        data_query: SegmentDataQuery,
        modified_at: datetime,
        name: str,
        created_by: Union[SegmentUser, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        disabled_at: Union[datetime, UnsetType] = unset,
        disabled_by: Union[SegmentUser, UnsetType] = unset,
        entity: Union[str, UnsetType] = unset,
        materialized_at: Union[datetime, none_type, UnsetType] = unset,
        modified_by: Union[SegmentUser, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        row_count: Union[int, UnsetType] = unset,
        source: Union[int, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a segment.

        :param created_at: Time the segment was created.
        :type created_at: datetime

        :param created_by: A Datadog user who created, modified, or disabled a segment.
        :type created_by: SegmentUser, optional

        :param data_query: Defines who belongs to the segment. It contains one or more blocks, up to 20 in total.
            Use ``combination`` to combine named blocks with a boolean formula such as ``A AND NOT B``.
        :type data_query: SegmentDataQuery

        :param description: Description of the segment.
        :type description: str, optional

        :param disabled_at: Time the segment was disabled, if it was.
        :type disabled_at: datetime, optional

        :param disabled_by: A Datadog user who created, modified, or disabled a segment.
        :type disabled_by: SegmentUser, optional

        :param entity: Kind of entity that the segment contains, ``user`` or ``account``.
        :type entity: str, optional

        :param materialized_at: Time the segment membership was last computed.
        :type materialized_at: datetime, none_type, optional

        :param modified_at: Time the segment was last modified.
        :type modified_at: datetime

        :param modified_by: A Datadog user who created, modified, or disabled a segment.
        :type modified_by: SegmentUser, optional

        :param name: Name of the segment.
        :type name: str

        :param org_id: ID of the organization that owns the segment.
        :type org_id: int, optional

        :param row_count: Number of entities in the segment when its membership was last computed. ``-1`` means the count is not
            available yet.
        :type row_count: int, optional

        :param source: Who created the segment. ``0`` for a user and ``1`` for Datadog.
        :type source: int, optional

        :param tags: Tags of the segment.
        :type tags: [str], none_type, optional

        :param type: Kind of segment, derived from its blocks, such as ``event_platform`` , ``user_store`` , or ``combination``.
        :type type: str, optional

        :param version: Version of the segment, increased on each update.
        :type version: int, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if disabled_at is not unset:
            kwargs["disabled_at"] = disabled_at
        if disabled_by is not unset:
            kwargs["disabled_by"] = disabled_by
        if entity is not unset:
            kwargs["entity"] = entity
        if materialized_at is not unset:
            kwargs["materialized_at"] = materialized_at
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if row_count is not unset:
            kwargs["row_count"] = row_count
        if source is not unset:
            kwargs["source"] = source
        if tags is not unset:
            kwargs["tags"] = tags
        if type is not unset:
            kwargs["type"] = type
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.data_query = data_query
        self_.modified_at = modified_at
        self_.name = name
