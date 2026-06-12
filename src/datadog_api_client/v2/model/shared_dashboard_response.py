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
    from datadog_api_client.v2.model.shared_dashboard_response_attributes import SharedDashboardResponseAttributes
    from datadog_api_client.v2.model.shared_dashboard_relationships import SharedDashboardRelationships
    from datadog_api_client.v2.model.shared_dashboard_type import SharedDashboardType


class SharedDashboardResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_response_attributes import SharedDashboardResponseAttributes
        from datadog_api_client.v2.model.shared_dashboard_relationships import SharedDashboardRelationships
        from datadog_api_client.v2.model.shared_dashboard_type import SharedDashboardType

        return {
            "attributes": (SharedDashboardResponseAttributes,),
            "id": (str,),
            "relationships": (SharedDashboardRelationships,),
            "type": (SharedDashboardType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SharedDashboardResponseAttributes,
        id: str,
        relationships: SharedDashboardRelationships,
        type: SharedDashboardType,
        **kwargs,
    ):
        """
        A shared dashboard response resource.

        :param attributes: Attributes of a shared dashboard response.
        :type attributes: SharedDashboardResponseAttributes

        :param id: ID of the shared dashboard.
        :type id: str

        :param relationships: Relationships of a shared dashboard.
        :type relationships: SharedDashboardRelationships

        :param type: Shared dashboard resource type.
        :type type: SharedDashboardType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
