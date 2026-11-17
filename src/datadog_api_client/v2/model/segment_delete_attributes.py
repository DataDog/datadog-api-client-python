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
    from datadog_api_client.v2.model.segment_user import SegmentUser


class SegmentDeleteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_user import SegmentUser

        return {
            "disabled_at": (datetime,),
            "disabled_by": (SegmentUser,),
            "name": (str,),
        }

    attribute_map = {
        "disabled_at": "disabled_at",
        "disabled_by": "disabled_by",
        "name": "name",
    }

    def __init__(self_, disabled_at: datetime, name: str, disabled_by: Union[SegmentUser, UnsetType] = unset, **kwargs):
        """
        Attributes of a deleted segment.

        :param disabled_at: Time the segment was deleted.
        :type disabled_at: datetime

        :param disabled_by: A Datadog user who created, modified, or disabled a segment.
        :type disabled_by: SegmentUser, optional

        :param name: Name of the segment.
        :type name: str
        """
        if disabled_by is not unset:
            kwargs["disabled_by"] = disabled_by
        super().__init__(kwargs)

        self_.disabled_at = disabled_at
        self_.name = name
