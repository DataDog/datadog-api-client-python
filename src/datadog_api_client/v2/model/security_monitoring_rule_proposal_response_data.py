# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_response_attributes import (
        SecurityMonitoringRuleProposalResponseAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_type import SecurityMonitoringRuleProposalType


class SecurityMonitoringRuleProposalResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_response_attributes import (
            SecurityMonitoringRuleProposalResponseAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_type import (
            SecurityMonitoringRuleProposalType,
        )

        return {
            "attributes": (SecurityMonitoringRuleProposalResponseAttributes,),
            "id": (UUID,),
            "type": (SecurityMonitoringRuleProposalType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringRuleProposalResponseAttributes,
        id: UUID,
        type: SecurityMonitoringRuleProposalType,
        **kwargs,
    ):
        """
        Data of the rule proposal.

        :param attributes: Attributes of the rule proposal.
        :type attributes: SecurityMonitoringRuleProposalResponseAttributes

        :param id: The ID of the rule proposal.
        :type id: UUID

        :param type: The rule proposal resource type. The value is always ``rule_proposals``.
        :type type: SecurityMonitoringRuleProposalType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
