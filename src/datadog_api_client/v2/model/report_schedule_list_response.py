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
    from datadog_api_client.v2.model.report_schedule_list_response_data import ReportScheduleListResponseData
    from datadog_api_client.v2.model.report_schedule_included_resource import ReportScheduleIncludedResource
    from datadog_api_client.v2.model.report_schedule_list_response_links import ReportScheduleListResponseLinks
    from datadog_api_client.v2.model.report_schedule_list_response_meta import ReportScheduleListResponseMeta
    from datadog_api_client.v2.model.report_schedule_author import ReportScheduleAuthor
    from datadog_api_client.v2.model.report_schedule_resource import ReportScheduleResource


class ReportScheduleListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_list_response_data import ReportScheduleListResponseData
        from datadog_api_client.v2.model.report_schedule_included_resource import ReportScheduleIncludedResource
        from datadog_api_client.v2.model.report_schedule_list_response_links import ReportScheduleListResponseLinks
        from datadog_api_client.v2.model.report_schedule_list_response_meta import ReportScheduleListResponseMeta

        return {
            "data": ([ReportScheduleListResponseData],),
            "included": ([ReportScheduleIncludedResource],),
            "links": (ReportScheduleListResponseLinks,),
            "meta": (ReportScheduleListResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ReportScheduleListResponseData],
        included: Union[
            List[Union[ReportScheduleIncludedResource, ReportScheduleAuthor, ReportScheduleResource]], UnsetType
        ] = unset,
        links: Union[ReportScheduleListResponseLinks, UnsetType] = unset,
        meta: Union[ReportScheduleListResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of report schedules.

        :param data: The list of report schedules.
        :type data: [ReportScheduleListResponseData]

        :param included: Related resources included with the report schedules, such as authors and rendered resources.
        :type included: [ReportScheduleIncludedResource], optional

        :param links: Pagination links for navigating a report schedule list response.
        :type links: ReportScheduleListResponseLinks, optional

        :param meta: Metadata for a paginated report schedule list response.
        :type meta: ReportScheduleListResponseMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
