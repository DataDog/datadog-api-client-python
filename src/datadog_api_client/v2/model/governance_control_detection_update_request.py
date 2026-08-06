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
    from datadog_api_client.v2.model.governance_control_detection_update_data import (
        GovernanceControlDetectionUpdateData,
    )


class GovernanceControlDetectionUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_detection_update_data import (
            GovernanceControlDetectionUpdateData,
        )

        return {
            "data": (GovernanceControlDetectionUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GovernanceControlDetectionUpdateData, **kwargs):
        """
        A request to update a governance control detection.

        :param data: The data of a governance control detection update request.
        :type data: GovernanceControlDetectionUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
