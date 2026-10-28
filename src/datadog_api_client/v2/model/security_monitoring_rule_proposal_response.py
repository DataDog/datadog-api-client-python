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
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_response_data import (
        SecurityMonitoringRuleProposalResponseData,
    )


class SecurityMonitoringRuleProposalResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_response_data import (
            SecurityMonitoringRuleProposalResponseData,
        )

        return {
            "data": (SecurityMonitoringRuleProposalResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringRuleProposalResponseData, **kwargs):
        """
        Response containing a rule proposal.

        :param data: Data of the rule proposal.
        :type data: SecurityMonitoringRuleProposalResponseData
        """
        super().__init__(kwargs)

        self_.data = data
