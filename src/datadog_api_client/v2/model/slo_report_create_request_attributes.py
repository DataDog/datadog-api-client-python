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
    from datadog_api_client.v2.model.slo_report_interval import SLOReportInterval


class SloReportCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_report_interval import SLOReportInterval

        return {
            "from_ts": (int,),
            "interval": (SLOReportInterval,),
            "query": (str,),
            "timezone": (str,),
            "to_ts": (int,),
        }

    attribute_map = {
        "from_ts": "from_ts",
        "interval": "interval",
        "query": "query",
        "timezone": "timezone",
        "to_ts": "to_ts",
    }

    def __init__(
        self_,
        from_ts: int,
        query: str,
        to_ts: int,
        interval: Union[SLOReportInterval, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes portion of the SLO report request.

        :param from_ts: The ``from`` timestamp for the report in epoch seconds.
        :type from_ts: int

        :param interval: The frequency at which report data is to be generated.
        :type interval: SLOReportInterval, optional

        :param query: The query string used to filter SLO results. Some examples of queries include ``service:<service-name>`` and ``slo-name``.
        :type query: str

        :param timezone: The timezone used to determine the start and end of each interval. For example, weekly intervals start at 12am on Sunday in the specified timezone.
        :type timezone: str, optional

        :param to_ts: The ``to`` timestamp for the report in epoch seconds.
        :type to_ts: int
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.from_ts = from_ts
        self_.query = query
        self_.to_ts = to_ts
