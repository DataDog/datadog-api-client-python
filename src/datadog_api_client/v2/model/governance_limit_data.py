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
    from datadog_api_client.v2.model.governance_limit_attributes import GovernanceLimitAttributes
    from datadog_api_client.v2.model.governance_limit_resource_type import GovernanceLimitResourceType


class GovernanceLimitData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_limit_attributes import GovernanceLimitAttributes
        from datadog_api_client.v2.model.governance_limit_resource_type import GovernanceLimitResourceType

        return {
            "attributes": (GovernanceLimitAttributes,),
            "id": (str,),
            "type": (GovernanceLimitResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: GovernanceLimitAttributes, id: str, type: GovernanceLimitResourceType, **kwargs):
        """
        A governance limit resource.

        :param attributes: The attributes of a governance limit.
        :type attributes: GovernanceLimitAttributes

        :param id: The unique identifier of the limit.
        :type id: str

        :param type: Limit resource type.
        :type type: GovernanceLimitResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
