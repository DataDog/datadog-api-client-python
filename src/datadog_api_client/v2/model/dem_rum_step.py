# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_rum_node import DemRumNode
    from datadog_api_client.v2.model.dem_rum_step_type import DemRumStepType


class DemRumStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_rum_node import DemRumNode
        from datadog_api_client.v2.model.dem_rum_step_type import DemRumStepType

        return {
            "nodes": ([DemRumNode],),
            "type": (DemRumStepType,),
        }

    attribute_map = {
        "nodes": "nodes",
        "type": "type",
    }

    def __init__(self_, nodes: List[DemRumNode], type: DemRumStepType, **kwargs):
        """
        A single step in a RUM journey definition.

        :param nodes: List of RUM nodes within a journey step.
        :type nodes: [DemRumNode]

        :param type: The type of a RUM journey step.
        :type type: DemRumStepType
        """
        super().__init__(kwargs)

        self_.nodes = nodes
        self_.type = type
