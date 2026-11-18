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
    from datadog_api_client.v2.model.fleet_access_scope import FleetAccessScope


class FleetAccessScopeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_access_scope import FleetAccessScope

        return {
            "data": (FleetAccessScope,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetAccessScope, **kwargs):
        """
        Response containing one fleet access scope.

        :param data: A fleet access scope. Use ``fleet-scope:<id>`` as the restriction policy resource identifier.
        :type data: FleetAccessScope
        """
        super().__init__(kwargs)

        self_.data = data
