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
    from datadog_api_client.v2.model.shared_dashboard_relationship_dashboard import SharedDashboardRelationshipDashboard
    from datadog_api_client.v2.model.shared_dashboard_relationship_sharer import SharedDashboardRelationshipSharer


class SharedDashboardRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_relationship_dashboard import (
            SharedDashboardRelationshipDashboard,
        )
        from datadog_api_client.v2.model.shared_dashboard_relationship_sharer import SharedDashboardRelationshipSharer

        return {
            "dashboard": (SharedDashboardRelationshipDashboard,),
            "sharer": (SharedDashboardRelationshipSharer,),
        }

    attribute_map = {
        "dashboard": "dashboard",
        "sharer": "sharer",
    }

    def __init__(
        self_, dashboard: SharedDashboardRelationshipDashboard, sharer: SharedDashboardRelationshipSharer, **kwargs
    ):
        """
        Relationships of a shared dashboard.

        :param dashboard: Dashboard associated with the shared dashboard.
        :type dashboard: SharedDashboardRelationshipDashboard

        :param sharer: User who shared the dashboard.
        :type sharer: SharedDashboardRelationshipSharer
        """
        super().__init__(kwargs)

        self_.dashboard = dashboard
        self_.sharer = sharer
