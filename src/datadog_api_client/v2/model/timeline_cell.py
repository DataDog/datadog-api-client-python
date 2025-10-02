# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeline_cell_author import TimelineCellAuthor
    from datadog_api_client.v2.model.timeline_cell_content import TimelineCellContent
    from datadog_api_client.v2.model.timeline_cell_type import TimelineCellType
    from datadog_api_client.v2.model.timeline_cell_author_user import TimelineCellAuthorUser
    from datadog_api_client.v2.model.timeline_cell_content_comment import TimelineCellContentComment


class TimelineCell(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeline_cell_author import TimelineCellAuthor
        from datadog_api_client.v2.model.timeline_cell_content import TimelineCellContent
        from datadog_api_client.v2.model.timeline_cell_type import TimelineCellType

        return {
            "author": (TimelineCellAuthor,),
            "cell_content": (TimelineCellContent,),
            "created_at": (datetime,),
            "deleted_at": (datetime,),
            "modified_at": (datetime,),
            "type": (TimelineCellType,),
        }

    attribute_map = {
        "author": "author",
        "cell_content": "cell_content",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "modified_at": "modified_at",
        "type": "type",
    }
    read_only_vars = {
        "created_at",
        "deleted_at",
        "modified_at",
    }

    def __init__(
        self_,
        author: Union[TimelineCellAuthor, TimelineCellAuthorUser, UnsetType] = unset,
        cell_content: Union[TimelineCellContent, TimelineCellContentComment, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        deleted_at: Union[datetime, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        type: Union[TimelineCellType, UnsetType] = unset,
        **kwargs,
    ):
        """
        timeline cell

        :param author: author of the timeline cell
        :type author: TimelineCellAuthor, optional

        :param cell_content: timeline cell content
        :type cell_content: TimelineCellContent, optional

        :param created_at: Timestamp of when the cell was created
        :type created_at: datetime, optional

        :param deleted_at: Timestamp of when the cell was deleted
        :type deleted_at: datetime, optional

        :param modified_at: Timestamp of when the cell was last modified
        :type modified_at: datetime, optional

        :param type: Timeline cell content type
        :type type: TimelineCellType, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if cell_content is not unset:
            kwargs["cell_content"] = cell_content
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
