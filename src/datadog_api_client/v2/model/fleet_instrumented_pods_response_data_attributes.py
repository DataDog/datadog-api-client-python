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
    from datadog_api_client.v2.model.fleet_instrumented_pod_group_attributes import FleetInstrumentedPodGroupAttributes


class FleetInstrumentedPodsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_instrumented_pod_group_attributes import (
            FleetInstrumentedPodGroupAttributes,
        )

        return {
            "groups": ([FleetInstrumentedPodGroupAttributes],),
        }

    attribute_map = {
        "groups": "groups",
    }

    def __init__(self_, groups: Union[List[FleetInstrumentedPodGroupAttributes], UnsetType] = unset, **kwargs):
        """
        Attributes of the instrumented pods response containing the list of pod groups.

        :param groups: Array of instrumented pod groups in the cluster.
        :type groups: [FleetInstrumentedPodGroupAttributes], optional
        """
        if groups is not unset:
            kwargs["groups"] = groups
        super().__init__(kwargs)
