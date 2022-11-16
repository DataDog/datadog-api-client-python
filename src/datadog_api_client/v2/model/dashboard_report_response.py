# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report import DashboardReport


class DashboardReportResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report import DashboardReport

        return {
            "data": (DashboardReport,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[DashboardReport, UnsetType] = unset, **kwargs):
        """
        Response body when creating, reading, or updating a dashboard report.

        :param data: Dashboard report schema.
        :type data: DashboardReport, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
