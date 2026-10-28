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
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_response_attributes import (
        SecurityMonitoringRuleProposalStartResponseAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_type import SecurityMonitoringRuleProposalType


class SecurityMonitoringRuleProposalStartResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_response_attributes import (
            SecurityMonitoringRuleProposalStartResponseAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_type import (
            SecurityMonitoringRuleProposalType,
        )

        return {
            "attributes": (SecurityMonitoringRuleProposalStartResponseAttributes,),
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
        attributes: SecurityMonitoringRuleProposalStartResponseAttributes,
        id: UUID,
        type: SecurityMonitoringRuleProposalType,
        **kwargs,
    ):
        """
        Data of the started rule proposal.

        :param attributes: Attributes of the started rule proposal.
        :type attributes: SecurityMonitoringRuleProposalStartResponseAttributes

        :param id: The ID of the rule proposal. Use it as ``proposal_id`` to check the proposal status and get the proposed rule.
        :type id: UUID

        :param type: The rule proposal resource type. The value is always ``rule_proposals``.
        :type type: SecurityMonitoringRuleProposalType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
