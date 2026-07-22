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
    from datadog_api_client.v2.model.governance_control_detection_attributes import GovernanceControlDetectionAttributes
    from datadog_api_client.v2.model.governance_control_detection_resource_type import (
        GovernanceControlDetectionResourceType,
    )


class GovernanceControlDetectionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_detection_attributes import (
            GovernanceControlDetectionAttributes,
        )
        from datadog_api_client.v2.model.governance_control_detection_resource_type import (
            GovernanceControlDetectionResourceType,
        )

        return {
            "attributes": (GovernanceControlDetectionAttributes,),
            "id": (str,),
            "type": (GovernanceControlDetectionResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GovernanceControlDetectionAttributes,
        id: str,
        type: GovernanceControlDetectionResourceType,
        **kwargs,
    ):
        """
        A governance control detection resource.

        :param attributes: The attributes of a governance control detection.
        :type attributes: GovernanceControlDetectionAttributes

        :param id: The unique identifier of the detection.
        :type id: str

        :param type: Governance control detection resource type.
        :type type: GovernanceControlDetectionResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
