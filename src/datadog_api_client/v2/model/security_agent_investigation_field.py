# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentInvestigationField(ModelSimple):
    """
    An attribute of an investigation that `fields[investigations]` can select.

    :param value: Must be one of ["signal_id", "rule_id", "state", "verdict", "conclusion", "signal", "key_entities", "key_evidence", "steps", "response_suggestions", "created_at", "updated_at"].
    :type value: str
    """

    allowed_values = {
        "signal_id",
        "rule_id",
        "state",
        "verdict",
        "conclusion",
        "signal",
        "key_entities",
        "key_evidence",
        "steps",
        "response_suggestions",
        "created_at",
        "updated_at",
    }
    SIGNAL_ID: ClassVar["SecurityAgentInvestigationField"]
    RULE_ID: ClassVar["SecurityAgentInvestigationField"]
    STATE: ClassVar["SecurityAgentInvestigationField"]
    VERDICT: ClassVar["SecurityAgentInvestigationField"]
    CONCLUSION: ClassVar["SecurityAgentInvestigationField"]
    SIGNAL: ClassVar["SecurityAgentInvestigationField"]
    KEY_ENTITIES: ClassVar["SecurityAgentInvestigationField"]
    KEY_EVIDENCE: ClassVar["SecurityAgentInvestigationField"]
    STEPS: ClassVar["SecurityAgentInvestigationField"]
    RESPONSE_SUGGESTIONS: ClassVar["SecurityAgentInvestigationField"]
    CREATED_AT: ClassVar["SecurityAgentInvestigationField"]
    UPDATED_AT: ClassVar["SecurityAgentInvestigationField"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentInvestigationField.SIGNAL_ID = SecurityAgentInvestigationField("signal_id")
SecurityAgentInvestigationField.RULE_ID = SecurityAgentInvestigationField("rule_id")
SecurityAgentInvestigationField.STATE = SecurityAgentInvestigationField("state")
SecurityAgentInvestigationField.VERDICT = SecurityAgentInvestigationField("verdict")
SecurityAgentInvestigationField.CONCLUSION = SecurityAgentInvestigationField("conclusion")
SecurityAgentInvestigationField.SIGNAL = SecurityAgentInvestigationField("signal")
SecurityAgentInvestigationField.KEY_ENTITIES = SecurityAgentInvestigationField("key_entities")
SecurityAgentInvestigationField.KEY_EVIDENCE = SecurityAgentInvestigationField("key_evidence")
SecurityAgentInvestigationField.STEPS = SecurityAgentInvestigationField("steps")
SecurityAgentInvestigationField.RESPONSE_SUGGESTIONS = SecurityAgentInvestigationField("response_suggestions")
SecurityAgentInvestigationField.CREATED_AT = SecurityAgentInvestigationField("created_at")
SecurityAgentInvestigationField.UPDATED_AT = SecurityAgentInvestigationField("updated_at")
