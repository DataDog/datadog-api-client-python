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
    from datadog_api_client.v2.model.governance_control_attributes import GovernanceControlAttributes
    from datadog_api_client.v2.model.governance_control_resource_type import GovernanceControlResourceType


class GovernanceControlData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_attributes import GovernanceControlAttributes
        from datadog_api_client.v2.model.governance_control_resource_type import GovernanceControlResourceType

        return {
            "attributes": (GovernanceControlAttributes,),
            "id": (str,),
            "type": (GovernanceControlResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: GovernanceControlAttributes, id: str, type: GovernanceControlResourceType, **kwargs
    ):
        """
        A governance control resource.

        :param attributes: The attributes of a governance control.
        :type attributes: GovernanceControlAttributes

        :param id: The unique identifier of the control.
        :type id: str

        :param type: JSON:API resource type for a governance control.
        :type type: GovernanceControlResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
