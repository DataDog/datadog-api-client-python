# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_control_detection_update_attributes import (
        GovernanceControlDetectionUpdateAttributes,
    )
    from datadog_api_client.v2.model.governance_control_detection_resource_type import (
        GovernanceControlDetectionResourceType,
    )


class GovernanceControlDetectionUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_detection_update_attributes import (
            GovernanceControlDetectionUpdateAttributes,
        )
        from datadog_api_client.v2.model.governance_control_detection_resource_type import (
            GovernanceControlDetectionResourceType,
        )

        return {
            "attributes": (GovernanceControlDetectionUpdateAttributes,),
            "type": (GovernanceControlDetectionResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: GovernanceControlDetectionResourceType,
        attributes: Union[GovernanceControlDetectionUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data of a governance control detection update request.

        :param attributes: The attributes of a governance control detection that can be updated. Only the attributes present in the request are modified.
        :type attributes: GovernanceControlDetectionUpdateAttributes, optional

        :param type: Governance control detection resource type.
        :type type: GovernanceControlDetectionResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
