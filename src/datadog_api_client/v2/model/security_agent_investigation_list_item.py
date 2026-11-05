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
    from datadog_api_client.v2.model.security_agent_investigation_list_item_attributes import (
        SecurityAgentInvestigationListItemAttributes,
    )
    from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType


class SecurityAgentInvestigationListItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_list_item_attributes import (
            SecurityAgentInvestigationListItemAttributes,
        )
        from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType

        return {
            "attributes": (SecurityAgentInvestigationListItemAttributes,),
            "id": (str,),
            "type": (SecurityAgentInvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityAgentInvestigationListItemAttributes,
        id: str,
        type: SecurityAgentInvestigationType,
        **kwargs,
    ):
        """
        An investigation in a list.

        :param attributes: Attributes of an investigation in a list. To get an investigation's full content, use the get investigation
            endpoint.
        :type attributes: SecurityAgentInvestigationListItemAttributes

        :param id: The ID of the investigation.
        :type id: str

        :param type: Type of the investigation resource.
        :type type: SecurityAgentInvestigationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
