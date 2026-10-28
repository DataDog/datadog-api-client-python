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
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_input_type import (
        SecurityMonitoringRuleProposalInputType,
    )


class SecurityMonitoringRuleProposalStartRequestAttributes(ModelNormal):
    validations = {
        "input": {
            "max_length": 65536,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_input_type import (
            SecurityMonitoringRuleProposalInputType,
        )

        return {
            "input": (str,),
            "input_type": (SecurityMonitoringRuleProposalInputType,),
        }

    attribute_map = {
        "input": "input",
        "input_type": "inputType",
    }

    def __init__(self_, input: str, input_type: SecurityMonitoringRuleProposalInputType, **kwargs):
        """
        Attributes of the rule proposal to start.

        :param input: The natural-language description or rule to generate the proposed rule from, in the
            format given by ``inputType``.
        :type input: str

        :param input_type: The type of input to generate the proposed rule from: ``natural_language`` for a
            plain-English description of the behavior to detect, ``spl`` for a Splunk SPL search or
            saved search definition, or ``kql`` for a Microsoft KQL query. SPL inputs must be
            self-contained, with search macros expanded.
        :type input_type: SecurityMonitoringRuleProposalInputType
        """
        super().__init__(kwargs)

        self_.input = input
        self_.input_type = input_type
