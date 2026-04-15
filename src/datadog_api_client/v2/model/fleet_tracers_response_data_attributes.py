# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_tracer_attributes import FleetTracerAttributes


class FleetTracersResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_tracer_attributes import FleetTracerAttributes

        return {
            "tracers": ([FleetTracerAttributes],),
        }

    attribute_map = {
        "tracers": "tracers",
    }

    def __init__(self_, tracers: Union[List[FleetTracerAttributes], UnsetType] = unset, **kwargs):
        """
        Attributes of the fleet tracers response containing the list of tracers.

        :param tracers: Array of tracers matching the query criteria.
        :type tracers: [FleetTracerAttributes], optional
        """
        if tracers is not unset:
            kwargs["tracers"] = tracers
        super().__init__(kwargs)
