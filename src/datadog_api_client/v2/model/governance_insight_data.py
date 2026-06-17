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
    from datadog_api_client.v2.model.governance_insight_attributes import GovernanceInsightAttributes
    from datadog_api_client.v2.model.governance_insight_resource_type import GovernanceInsightResourceType


class GovernanceInsightData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_attributes import GovernanceInsightAttributes
        from datadog_api_client.v2.model.governance_insight_resource_type import GovernanceInsightResourceType

        return {
            "attributes": (GovernanceInsightAttributes,),
            "id": (str,),
            "type": (GovernanceInsightResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: GovernanceInsightAttributes, id: str, type: GovernanceInsightResourceType, **kwargs
    ):
        """
        A governance insight resource.

        :param attributes: The attributes of a governance insight.
        :type attributes: GovernanceInsightAttributes

        :param id: The unique identifier of the insight.
        :type id: str

        :param type: JSON:API resource type for a governance insight.
        :type type: GovernanceInsightResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
