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
    from datadog_api_client.v2.model.governance_config_attributes import GovernanceConfigAttributes
    from datadog_api_client.v2.model.governance_console_config_resource_type import GovernanceConsoleConfigResourceType


class GovernanceConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_config_attributes import GovernanceConfigAttributes
        from datadog_api_client.v2.model.governance_console_config_resource_type import (
            GovernanceConsoleConfigResourceType,
        )

        return {
            "attributes": (GovernanceConfigAttributes,),
            "id": (str,),
            "type": (GovernanceConsoleConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: GovernanceConfigAttributes, id: str, type: GovernanceConsoleConfigResourceType, **kwargs
    ):
        """
        A Governance Console configuration resource.

        :param attributes: The attributes of a Governance Console configuration.
        :type attributes: GovernanceConfigAttributes

        :param id: The unique identifier of the organization the Governance Console configuration applies to.
        :type id: str

        :param type: Governance console config resource type.
        :type type: GovernanceConsoleConfigResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
