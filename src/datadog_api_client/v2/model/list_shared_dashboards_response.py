# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.shared_dashboard_response import SharedDashboardResponse
    from datadog_api_client.v2.model.shared_dashboard_included import SharedDashboardIncluded
    from datadog_api_client.v2.model.shared_dashboard_included_dashboard import SharedDashboardIncludedDashboard
    from datadog_api_client.v2.model.shared_dashboard_included_user import SharedDashboardIncludedUser


class ListSharedDashboardsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_response import SharedDashboardResponse
        from datadog_api_client.v2.model.shared_dashboard_included import SharedDashboardIncluded

        return {
            "data": ([SharedDashboardResponse],),
            "included": ([SharedDashboardIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[SharedDashboardResponse],
        included: List[Union[SharedDashboardIncluded, SharedDashboardIncludedDashboard, SharedDashboardIncludedUser]],
        **kwargs,
    ):
        """
        Response containing shared dashboards for a dashboard.

        :param data: Shared dashboards for the dashboard.
        :type data: [SharedDashboardResponse]

        :param included: Users and dashboards related to the shared dashboards.
        :type included: [SharedDashboardIncluded]
        """
        super().__init__(kwargs)

        self_.data = data
        self_.included = included
