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
    from datadog_api_client.v2.model.report_schedule_list_response_pagination import (
        ReportScheduleListResponsePagination,
    )


class ReportScheduleListResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_list_response_pagination import (
            ReportScheduleListResponsePagination,
        )

        return {
            "pagination": (ReportScheduleListResponsePagination,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    def __init__(self_, pagination: Union[ReportScheduleListResponsePagination, UnsetType] = unset, **kwargs):
        """
        Metadata for a paginated report schedule list response.

        :param pagination: Offset and limit pagination metadata for a report schedule list response.
        :type pagination: ReportScheduleListResponsePagination, optional
        """
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
