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
    from datadog_api_client.v2.model.readiness_gate_threshold_type import ReadinessGateThresholdType


class ReadinessGate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.readiness_gate_threshold_type import ReadinessGateThresholdType

        return {
            "threshold_type": (ReadinessGateThresholdType,),
        }

    attribute_map = {
        "threshold_type": "thresholdType",
    }

    def __init__(self_, threshold_type: ReadinessGateThresholdType, **kwargs):
        """
        Used to merge multiple branches into a single branch.

        :param threshold_type: The definition of ``ReadinessGateThresholdType`` object.
        :type threshold_type: ReadinessGateThresholdType
        """
        super().__init__(kwargs)

        self_.threshold_type = threshold_type
