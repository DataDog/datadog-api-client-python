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
    from datadog_api_client.v2.model.governance_control_detection_data import GovernanceControlDetectionData


class GovernanceControlDetectionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_detection_data import GovernanceControlDetectionData

        return {
            "data": ([GovernanceControlDetectionData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[GovernanceControlDetectionData], **kwargs):
        """
        A list of governance control detections.

        :param data: An array of governance control detection resources.
        :type data: [GovernanceControlDetectionData]
        """
        super().__init__(kwargs)

        self_.data = data
