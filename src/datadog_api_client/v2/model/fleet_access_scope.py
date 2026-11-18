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
    from datadog_api_client.v2.model.fleet_access_scope_response_attributes import FleetAccessScopeResponseAttributes
    from datadog_api_client.v2.model.fleet_access_scope_resource_type import FleetAccessScopeResourceType


class FleetAccessScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_access_scope_response_attributes import (
            FleetAccessScopeResponseAttributes,
        )
        from datadog_api_client.v2.model.fleet_access_scope_resource_type import FleetAccessScopeResourceType

        return {
            "attributes": (FleetAccessScopeResponseAttributes,),
            "id": (str,),
            "type": (FleetAccessScopeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: FleetAccessScopeResponseAttributes, id: str, type: FleetAccessScopeResourceType, **kwargs
    ):
        """
        A fleet access scope. Use ``fleet-scope:<id>`` as the restriction policy resource identifier.

        :param attributes: Fleet access scope attributes and audit information.
        :type attributes: FleetAccessScopeResponseAttributes

        :param id: Unique identifier of the scope, also used in the restriction policy resource identifier ``fleet-scope:<id>``.
        :type id: str

        :param type: The JSON:API resource type for a fleet access scope.
        :type type: FleetAccessScopeResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
