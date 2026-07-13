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
    from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
    from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable


class PrintReportResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
        from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable

        return {
            "download_url": (str,),
            "from_ts": (int,),
            "resource_id": (str,),
            "resource_type": (ReportScheduleResourceType,),
            "template_variables": ([ReportScheduleTemplateVariable],),
            "timeframe": (str,),
            "timezone": (str,),
            "to_ts": (int,),
        }

    attribute_map = {
        "download_url": "download_url",
        "from_ts": "from_ts",
        "resource_id": "resource_id",
        "resource_type": "resource_type",
        "template_variables": "template_variables",
        "timeframe": "timeframe",
        "timezone": "timezone",
        "to_ts": "to_ts",
    }

    def __init__(
        self_,
        download_url: str,
        from_ts: int,
        resource_id: str,
        resource_type: ReportScheduleResourceType,
        template_variables: List[ReportScheduleTemplateVariable],
        timezone: str,
        to_ts: int,
        timeframe: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The configuration and download URL for the initiated print-only report.

        :param download_url: The URL from which the rendered PDF report can be downloaded.
        :type download_url: str

        :param from_ts: The start of the rendered time range, as a Unix timestamp in milliseconds.
        :type from_ts: int

        :param resource_id: The identifier of the dashboard or integration dashboard.
        :type resource_id: str

        :param resource_type: The type of dashboard resource the report schedule targets.
        :type resource_type: ReportScheduleResourceType

        :param template_variables: The dashboard template variables applied when rendering the report.
        :type template_variables: [ReportScheduleTemplateVariable]

        :param timeframe: The relative time window used, if one was specified in the request.
        :type timeframe: str, optional

        :param timezone: The IANA time zone identifier used when rendering the report.
        :type timezone: str

        :param to_ts: The end of the rendered time range, as a Unix timestamp in milliseconds.
        :type to_ts: int
        """
        if timeframe is not unset:
            kwargs["timeframe"] = timeframe
        super().__init__(kwargs)

        self_.download_url = download_url
        self_.from_ts = from_ts
        self_.resource_id = resource_id
        self_.resource_type = resource_type
        self_.template_variables = template_variables
        self_.timezone = timezone
        self_.to_ts = to_ts
