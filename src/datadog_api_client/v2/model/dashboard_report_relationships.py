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
    from datadog_api_client.v2.model.dashboard_report_relationships_dashboard import (
        DashboardReportRelationshipsDashboard,
    )


class DashboardReportRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_relationships_dashboard import (
            DashboardReportRelationshipsDashboard,
        )

        return {
            "dashboard": (DashboardReportRelationshipsDashboard,),
        }

    attribute_map = {
        "dashboard": "dashboard",
    }

    def __init__(self_, dashboard: Union[DashboardReportRelationshipsDashboard, UnsetType] = unset, **kwargs):
        """
        Relationships of a dashboard report.

        :param dashboard: Dashboard associated with the report.
        :type dashboard: DashboardReportRelationshipsDashboard, optional
        """
        if dashboard is not unset:
            kwargs["dashboard"] = dashboard
        super().__init__(kwargs)
