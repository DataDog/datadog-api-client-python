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
    from datadog_api_client.v2.model.governance_resource_limit_attributes import GovernanceResourceLimitAttributes
    from datadog_api_client.v2.model.governance_resource_limit_resource_type import GovernanceResourceLimitResourceType


class GovernanceResourceLimitData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_resource_limit_attributes import GovernanceResourceLimitAttributes
        from datadog_api_client.v2.model.governance_resource_limit_resource_type import (
            GovernanceResourceLimitResourceType,
        )

        return {
            "attributes": (GovernanceResourceLimitAttributes,),
            "id": (str,),
            "type": (GovernanceResourceLimitResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GovernanceResourceLimitAttributes,
        id: str,
        type: GovernanceResourceLimitResourceType,
        **kwargs,
    ):
        """
        A governance resource limit resource.

        :param attributes: The attributes of a governance resource limit.
        :type attributes: GovernanceResourceLimitAttributes

        :param id: The unique identifier of the resource limit.
        :type id: str

        :param type: Resource limit resource type.
        :type type: GovernanceResourceLimitResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
