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
    from datadog_api_client.v2.model.fleet_access_scope_attributes import FleetAccessScopeAttributes
    from datadog_api_client.v2.model.fleet_access_scope_resource_type import FleetAccessScopeResourceType


class FleetAccessScopeWrite(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_access_scope_attributes import FleetAccessScopeAttributes
        from datadog_api_client.v2.model.fleet_access_scope_resource_type import FleetAccessScopeResourceType

        return {
            "attributes": (FleetAccessScopeAttributes,),
            "type": (FleetAccessScopeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: FleetAccessScopeResourceType,
        attributes: Union[FleetAccessScopeAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A fleet access scope write payload. The update target is selected by the path ID.

        :param attributes: Mutable fleet access scope attributes. PUT replaces all mutable attributes; omitted strings become empty and omitted feature flags become false.
        :type attributes: FleetAccessScopeAttributes, optional

        :param type: The JSON:API resource type for a fleet access scope.
        :type type: FleetAccessScopeResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
