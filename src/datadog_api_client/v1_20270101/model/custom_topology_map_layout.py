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
    from datadog_api_client.v1_20270101.model.custom_topology_map_layout_direction import (
        CustomTopologyMapLayoutDirection,
    )
    from datadog_api_client.v1_20270101.model.custom_topology_map_layout_type import CustomTopologyMapLayoutType


class CustomTopologyMapLayout(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_layout_direction import (
            CustomTopologyMapLayoutDirection,
        )
        from datadog_api_client.v1_20270101.model.custom_topology_map_layout_type import CustomTopologyMapLayoutType

        return {
            "direction": (CustomTopologyMapLayoutDirection,),
            "type": (CustomTopologyMapLayoutType,),
        }

    attribute_map = {
        "direction": "direction",
        "type": "type",
    }

    def __init__(self_, direction: CustomTopologyMapLayoutDirection, type: CustomTopologyMapLayoutType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param direction: Test-only generated schema for the dashboard versioning proof of concept.
        :type direction: CustomTopologyMapLayoutDirection

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CustomTopologyMapLayoutType
        """
        super().__init__(kwargs)

        self_.direction = direction
        self_.type = type
