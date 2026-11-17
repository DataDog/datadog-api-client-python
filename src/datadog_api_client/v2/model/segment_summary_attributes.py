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


class SegmentSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_user import SegmentUser

        return {
            "created_at": (datetime,),
            "created_by": (SegmentUser,),
            "description": (str,),
            "entity": (str,),
            "modified_at": (datetime,),
            "modified_by": (SegmentUser,),
            "name": (str,),
            "org_id": (int,),
            "row_count": (int,),
            "source": (int,),
            "tags": ([str], none_type),
            "type": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "entity": "entity",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "org_id": "org_id",
        "row_count": "row_count",
        "source": "source",
        "tags": "tags",
        "type": "type",
    }

    def __init__(
        self_,
        created_at: datetime,
        modified_at: datetime,
        name: str,
        created_by: Union[SegmentUser, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        entity: Union[str, UnsetType] = unset,
        modified_by: Union[SegmentUser, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        row_count: Union[int, UnsetType] = unset,
        source: Union[int, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a segment in a list. The segment definition is not included.

        :param created_at: Time the segment was created.
        :type created_at: datetime

        :param created_by: A Datadog user who created, modified, or disabled a segment.
        :type created_by: SegmentUser, optional

        :param description: Description of the segment.
        :type description: str, optional

        :param entity: Kind of entity that the segment contains, ``user`` or ``account``.
        :type entity: str, optional

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

        :param type: Kind of segment, derived from its blocks.
        :type type: str, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if entity is not unset:
            kwargs["entity"] = entity
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
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.modified_at = modified_at
        self_.name = name
