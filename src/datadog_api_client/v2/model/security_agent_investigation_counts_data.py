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
    from datadog_api_client.v2.model.security_agent_investigation_counts_attributes import (
        SecurityAgentInvestigationCountsAttributes,
    )
    from datadog_api_client.v2.model.security_agent_investigation_counts_type import (
        SecurityAgentInvestigationCountsType,
    )


class SecurityAgentInvestigationCountsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_counts_attributes import (
            SecurityAgentInvestigationCountsAttributes,
        )
        from datadog_api_client.v2.model.security_agent_investigation_counts_type import (
            SecurityAgentInvestigationCountsType,
        )

        return {
            "attributes": (SecurityAgentInvestigationCountsAttributes,),
            "id": (str,),
            "type": (SecurityAgentInvestigationCountsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityAgentInvestigationCountsAttributes,
        id: str,
        type: SecurityAgentInvestigationCountsType,
        **kwargs,
    ):
        """
        Counts of completed investigations.

        :param attributes: The counts of each value of the field.
        :type attributes: SecurityAgentInvestigationCountsAttributes

        :param id: The counted field.
        :type id: str

        :param type: Type of the investigation counts resource.
        :type type: SecurityAgentInvestigationCountsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
