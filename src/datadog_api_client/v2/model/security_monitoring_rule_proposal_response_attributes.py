# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_rule_proposal_error import SecurityMonitoringRuleProposalError


class SecurityMonitoringRuleProposalResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_proposal_error import (
            SecurityMonitoringRuleProposalError,
        )

        return {
            "error": (SecurityMonitoringRuleProposalError,),
            "rule": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "status": (str,),
        }

    attribute_map = {
        "error": "error",
        "rule": "rule",
        "status": "status",
    }

    def __init__(
        self_,
        status: str,
        error: Union[SecurityMonitoringRuleProposalError, UnsetType] = unset,
        rule: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the rule proposal.

        :param error: The reason no rule could be generated. Only present when the status is ``failed``.
        :type error: SecurityMonitoringRuleProposalError, optional

        :param rule: The proposed Cloud SIEM detection rule in the same format as the create a detection
            rule endpoint. It is not saved in Cloud SIEM. Only present when the status is
            ``completed``. Review the rule, then create it with the `create a
            detection rule <https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-detection-rule>`_
            endpoint.
        :type rule: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param status: The status of the rule proposal. ``pending`` and ``in_progress`` mean the proposed rule is
            still being generated. Poll the endpoint again later. ``completed`` and ``failed`` are final:
            ``completed`` proposals contain the proposed rule in ``rule`` , and ``failed`` proposals
            contain the reason in ``error``.
        :type status: str
        """
        if error is not unset:
            kwargs["error"] = error
        if rule is not unset:
            kwargs["rule"] = rule
        super().__init__(kwargs)

        self_.status = status
