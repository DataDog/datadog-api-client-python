# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_agent_investigation_entity import SecurityAgentInvestigationEntity


class SecurityAgentInvestigationKeyEntities(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_entity import SecurityAgentInvestigationEntity

        return {
            "actors": ([SecurityAgentInvestigationEntity],),
            "targets": ([SecurityAgentInvestigationEntity],),
        }

    attribute_map = {
        "actors": "actors",
        "targets": "targets",
    }

    def __init__(
        self_, actors: List[SecurityAgentInvestigationEntity], targets: List[SecurityAgentInvestigationEntity], **kwargs
    ):
        """
        The entities the investigation found, by role.

        :param actors: Entities that performed the activity.
        :type actors: [SecurityAgentInvestigationEntity]

        :param targets: Entities the activity was aimed at.
        :type targets: [SecurityAgentInvestigationEntity]
        """
        super().__init__(kwargs)

        self_.actors = actors
        self_.targets = targets
