# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.report_schedule_response_data import ReportScheduleResponseData
    from datadog_api_client.v2.model.report_schedule_included_resource import ReportScheduleIncludedResource
    from datadog_api_client.v2.model.report_schedule_author import ReportScheduleAuthor
    from datadog_api_client.v2.model.report_schedule_resource import ReportScheduleResource


class ReportScheduleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_response_data import ReportScheduleResponseData
        from datadog_api_client.v2.model.report_schedule_included_resource import ReportScheduleIncludedResource

        return {
            "data": (ReportScheduleResponseData,),
            "included": ([ReportScheduleIncludedResource],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: ReportScheduleResponseData,
        included: Union[
            List[Union[ReportScheduleIncludedResource, ReportScheduleAuthor, ReportScheduleResource]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response containing a single report schedule.

        :param data: The JSON:API data object representing a report schedule.
        :type data: ReportScheduleResponseData

        :param included: Related resources included with the report schedule, such as the author.
        :type included: [ReportScheduleIncludedResource], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
