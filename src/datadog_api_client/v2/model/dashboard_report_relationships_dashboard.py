# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report_relationships_dashboard_data import (
        DashboardReportRelationshipsDashboardData,
    )


class DashboardReportRelationshipsDashboard(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_relationships_dashboard_data import (
            DashboardReportRelationshipsDashboardData,
        )

        return {
            "data": (DashboardReportRelationshipsDashboardData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DashboardReportRelationshipsDashboardData, **kwargs):
        """
        Dashboard associated with the report.

        :param data: JSON:API data representing a report's associated dashboard.
        :type data: DashboardReportRelationshipsDashboardData
        """
        super().__init__(kwargs)

        self_.data = data
