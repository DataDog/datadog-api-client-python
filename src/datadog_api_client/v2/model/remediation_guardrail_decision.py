# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.remediation_guardrail_verdict import RemediationGuardrailVerdict


class RemediationGuardrailDecision(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_guardrail_verdict import RemediationGuardrailVerdict

        return {
            "decision": (RemediationGuardrailVerdict,),
            "guardrail_id": (str,),
        }

    attribute_map = {
        "decision": "decision",
        "guardrail_id": "guardrail_id",
    }

    def __init__(
        self_,
        decision: Union[RemediationGuardrailVerdict, UnsetType] = unset,
        guardrail_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The guardrail decision applied to a plan or investigation.

        :param decision: The verdict a guardrail applied to a plan or investigation.
        :type decision: RemediationGuardrailVerdict, optional

        :param guardrail_id: ID of the matching guardrail. Set when the decision is not denied; may be empty when denied because no rule matched.
        :type guardrail_id: str, optional
        """
        if decision is not unset:
            kwargs["decision"] = decision
        if guardrail_id is not unset:
            kwargs["guardrail_id"] = guardrail_id
        super().__init__(kwargs)
