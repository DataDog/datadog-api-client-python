# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_list_response_pagination_type import (
        ReportScheduleListResponsePaginationType,
    )


class ReportScheduleListResponsePagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_list_response_pagination_type import (
            ReportScheduleListResponsePaginationType,
        )

        return {
            "first_offset": (int,),
            "last_offset": (int, none_type),
            "limit": (int,),
            "next_offset": (int,),
            "offset": (int,),
            "prev_offset": (int,),
            "total": (int,),
            "type": (ReportScheduleListResponsePaginationType,),
        }

    attribute_map = {
        "first_offset": "first_offset",
        "last_offset": "last_offset",
        "limit": "limit",
        "next_offset": "next_offset",
        "offset": "offset",
        "prev_offset": "prev_offset",
        "total": "total",
        "type": "type",
    }

    def __init__(
        self_,
        first_offset: Union[int, UnsetType] = unset,
        last_offset: Union[int, none_type, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_offset: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        prev_offset: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        type: Union[ReportScheduleListResponsePaginationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Offset and limit pagination metadata for a report schedule list response.

        :param first_offset: The first offset.
        :type first_offset: int, optional

        :param last_offset: The last offset when the total count is known, or ``null`` if it is unavailable.
        :type last_offset: int, none_type, optional

        :param limit: The maximum number of schedules returned.
        :type limit: int, optional

        :param next_offset: The next offset.
        :type next_offset: int, optional

        :param offset: The current offset.
        :type offset: int, optional

        :param prev_offset: The previous offset.
        :type prev_offset: int, optional

        :param total: The total number of matching schedules.
        :type total: int, optional

        :param type: The pagination type.
        :type type: ReportScheduleListResponsePaginationType, optional
        """
        if first_offset is not unset:
            kwargs["first_offset"] = first_offset
        if last_offset is not unset:
            kwargs["last_offset"] = last_offset
        if limit is not unset:
            kwargs["limit"] = limit
        if next_offset is not unset:
            kwargs["next_offset"] = next_offset
        if offset is not unset:
            kwargs["offset"] = offset
        if prev_offset is not unset:
            kwargs["prev_offset"] = prev_offset
        if total is not unset:
            kwargs["total"] = total
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
