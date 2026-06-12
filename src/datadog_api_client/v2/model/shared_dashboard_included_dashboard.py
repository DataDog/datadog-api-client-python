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
    from datadog_api_client.v2.model.shared_dashboard_included_dashboard_attributes import (
        SharedDashboardIncludedDashboardAttributes,
    )
    from datadog_api_client.v2.model.shared_dashboard_included_dashboard_type import (
        SharedDashboardIncludedDashboardType,
    )


class SharedDashboardIncludedDashboard(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_included_dashboard_attributes import (
            SharedDashboardIncludedDashboardAttributes,
        )
        from datadog_api_client.v2.model.shared_dashboard_included_dashboard_type import (
            SharedDashboardIncludedDashboardType,
        )

        return {
            "attributes": (SharedDashboardIncludedDashboardAttributes,),
            "id": (str,),
            "type": (SharedDashboardIncludedDashboardType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SharedDashboardIncludedDashboardAttributes,
        id: str,
        type: SharedDashboardIncludedDashboardType,
        **kwargs,
    ):
        """
        Included dashboard resource.

        :param attributes: Attributes of the included dashboard.
        :type attributes: SharedDashboardIncludedDashboardAttributes

        :param id: ID of the dashboard.
        :type id: str

        :param type: Included dashboard resource type.
        :type type: SharedDashboardIncludedDashboardType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
