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


class PrintReportRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
        from datadog_api_client.v2.model.report_schedule_template_variable import ReportScheduleTemplateVariable

        return {
            "from_ts": (int,),
            "resource_id": (str,),
            "resource_type": (ReportScheduleResourceType,),
            "template_variables": ([ReportScheduleTemplateVariable],),
            "timeframe": (str,),
            "timezone": (str,),
            "to_ts": (int,),
        }

    attribute_map = {
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
        resource_id: str,
        resource_type: ReportScheduleResourceType,
        template_variables: List[ReportScheduleTemplateVariable],
        timezone: str,
        from_ts: Union[int, UnsetType] = unset,
        timeframe: Union[str, UnsetType] = unset,
        to_ts: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The configuration for a print-only report. Specify exactly one of ``timeframe`` (for a
        relative time window) or both ``from_ts`` and ``to_ts`` (for an absolute time range).

        :param from_ts: The start of an absolute time range, as a Unix timestamp in milliseconds.
            Required when ``timeframe`` is omitted.
        :type from_ts: int, optional

        :param resource_id: The identifier of the dashboard or integration dashboard to render.
        :type resource_id: str

        :param resource_type: The type of dashboard resource the report schedule targets.
        :type resource_type: ReportScheduleResourceType

        :param template_variables: The dashboard template variables applied when rendering the report.
        :type template_variables: [ReportScheduleTemplateVariable]

        :param timeframe: A relative time window (for example ``1w`` or ``calendar_month`` ). Mutually
            exclusive with ``from_ts`` and ``to_ts``.
        :type timeframe: str, optional

        :param timezone: The IANA time zone identifier used to evaluate the time window.
        :type timezone: str

        :param to_ts: The end of an absolute time range, as a Unix timestamp in milliseconds.
            Required when ``timeframe`` is omitted.
        :type to_ts: int, optional
        """
        if from_ts is not unset:
            kwargs["from_ts"] = from_ts
        if timeframe is not unset:
            kwargs["timeframe"] = timeframe
        if to_ts is not unset:
            kwargs["to_ts"] = to_ts
        super().__init__(kwargs)

        self_.resource_id = resource_id
        self_.resource_type = resource_type
        self_.template_variables = template_variables
        self_.timezone = timezone
