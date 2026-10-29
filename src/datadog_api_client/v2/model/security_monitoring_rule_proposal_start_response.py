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
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_response_data import (
        SecurityMonitoringRuleProposalStartResponseData,
    )


class SecurityMonitoringRuleProposalStartResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_start_response_data import (
            SecurityMonitoringRuleProposalStartResponseData,
        )

        return {
            "data": (SecurityMonitoringRuleProposalStartResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringRuleProposalStartResponseData, **kwargs):
        """
        Response to a started rule proposal.

        :param data: Data of the started rule proposal.
        :type data: SecurityMonitoringRuleProposalStartResponseData
        """
        super().__init__(kwargs)

        self_.data = data
