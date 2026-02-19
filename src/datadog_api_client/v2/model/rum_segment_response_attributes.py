# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_segment_user import RumSegmentUser
    from datadog_api_client.v2.model.rum_segment_data_query import RumSegmentDataQuery
    from datadog_api_client.v2.model.rum_segment_source import RumSegmentSource
    from datadog_api_client.v2.model.rum_segment_segment_type import RumSegmentSegmentType


class RumSegmentResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_user import RumSegmentUser
        from datadog_api_client.v2.model.rum_segment_data_query import RumSegmentDataQuery
        from datadog_api_client.v2.model.rum_segment_source import RumSegmentSource
        from datadog_api_client.v2.model.rum_segment_segment_type import RumSegmentSegmentType

        return {
            "created_at": (datetime,),
            "created_by": (RumSegmentUser,),
            "data_query": (RumSegmentDataQuery,),
            "description": (str,),
            "modified_at": (datetime,),
            "modified_by": (RumSegmentUser,),
            "name": (str,),
            "org_id": (int,),
            "row_count": (int,),
            "source": (RumSegmentSource,),
            "tags": ([str],),
            "type": (RumSegmentSegmentType,),
            "uuid": (str,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "data_query": "data_query",
        "description": "description",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "org_id": "org_id",
        "row_count": "row_count",
        "source": "source",
        "tags": "tags",
        "type": "type",
        "uuid": "uuid",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: RumSegmentUser,
        data_query: RumSegmentDataQuery,
        description: str,
        modified_at: datetime,
        modified_by: RumSegmentUser,
        name: str,
        org_id: int,
        row_count: int,
        source: RumSegmentSource,
        tags: List[str],
        type: RumSegmentSegmentType,
        uuid: str,
        version: int,
        **kwargs,
    ):
        """
        Attributes of a segment in a response.

        :param created_at: The creation timestamp in RFC 3339 format.
        :type created_at: datetime

        :param created_by: A user who performed an action on a segment.
        :type created_by: RumSegmentUser

        :param data_query: Query definition for the segment. Contains one or more query blocks and an optional combination formula.
        :type data_query: RumSegmentDataQuery

        :param description: A description of the segment.
        :type description: str

        :param modified_at: The last modification timestamp in RFC 3339 format.
        :type modified_at: datetime

        :param modified_by: A user who performed an action on a segment.
        :type modified_by: RumSegmentUser

        :param name: The name of the segment.
        :type name: str

        :param org_id: The organization identifier.
        :type org_id: int

        :param row_count: The number of users in the segment.
        :type row_count: int

        :param source: The source of a segment.
        :type source: RumSegmentSource

        :param tags: A list of tags for the segment.
        :type tags: [str]

        :param type: The type of a segment based on its data query configuration.
        :type type: RumSegmentSegmentType

        :param uuid: The unique identifier of the segment.
        :type uuid: str

        :param version: The version number of the segment.
        :type version: int
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.data_query = data_query
        self_.description = description
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.name = name
        self_.org_id = org_id
        self_.row_count = row_count
        self_.source = source
        self_.tags = tags
        self_.type = type
        self_.uuid = uuid
        self_.version = version
