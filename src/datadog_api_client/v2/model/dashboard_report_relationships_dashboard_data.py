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
    from datadog_api_client.v2.model.dashboard_report_resource_type import DashboardReportResourceType


class DashboardReportRelationshipsDashboardData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_resource_type import DashboardReportResourceType

        return {
            "id": (str,),
            "type": (DashboardReportResourceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: DashboardReportResourceType, **kwargs):
        """
        JSON:API data representing a report's associated dashboard.

        :param id: ID of a report's associated dashboard. Screenboards (dashboards with layout_type=FREE) are not supported.
        :type id: str

        :param type: JSON:API type of the report's associated dashboard.
        :type type: DashboardReportResourceType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
