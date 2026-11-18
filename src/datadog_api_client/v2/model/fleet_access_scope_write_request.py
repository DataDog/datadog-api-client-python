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
    from datadog_api_client.v2.model.fleet_access_scope_write import FleetAccessScopeWrite


class FleetAccessScopeWriteRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_access_scope_write import FleetAccessScopeWrite

        return {
            "data": (FleetAccessScopeWrite,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetAccessScopeWrite, **kwargs):
        """
        Request to create or replace a fleet access scope.

        :param data: A fleet access scope write payload. The update target is selected by the path ID.
        :type data: FleetAccessScopeWrite
        """
        super().__init__(kwargs)

        self_.data = data
