# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_segment_user import RumSegmentUser


class RumSegmentDeleteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_user import RumSegmentUser

        return {
            "disabled_at": (datetime,),
            "disabled_by": (RumSegmentUser,),
            "name": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "disabled_at": "disabled_at",
        "disabled_by": "disabled_by",
        "name": "name",
        "uuid": "uuid",
    }

    def __init__(self_, disabled_at: datetime, disabled_by: RumSegmentUser, name: str, uuid: str, **kwargs):
        """
        Attributes of a deleted segment response.

        :param disabled_at: The timestamp when the segment was disabled in RFC 3339 format.
        :type disabled_at: datetime

        :param disabled_by: A user who performed an action on a segment.
        :type disabled_by: RumSegmentUser

        :param name: The name of the deleted segment.
        :type name: str

        :param uuid: The unique identifier of the deleted segment.
        :type uuid: str
        """
        super().__init__(kwargs)

        self_.disabled_at = disabled_at
        self_.disabled_by = disabled_by
        self_.name = name
        self_.uuid = uuid
