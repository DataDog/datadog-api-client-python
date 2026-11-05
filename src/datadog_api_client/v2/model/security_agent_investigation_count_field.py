# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentInvestigationCountField(ModelSimple):
    """
    Field to count completed investigations by.

    :param value: Must be one of ["verdict", "rule_type", "signal_source", "entity"].
    :type value: str
    """

    allowed_values = {
        "verdict",
        "rule_type",
        "signal_source",
        "entity",
    }
    VERDICT: ClassVar["SecurityAgentInvestigationCountField"]
    RULE_TYPE: ClassVar["SecurityAgentInvestigationCountField"]
    SIGNAL_SOURCE: ClassVar["SecurityAgentInvestigationCountField"]
    ENTITY: ClassVar["SecurityAgentInvestigationCountField"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentInvestigationCountField.VERDICT = SecurityAgentInvestigationCountField("verdict")
SecurityAgentInvestigationCountField.RULE_TYPE = SecurityAgentInvestigationCountField("rule_type")
SecurityAgentInvestigationCountField.SIGNAL_SOURCE = SecurityAgentInvestigationCountField("signal_source")
SecurityAgentInvestigationCountField.ENTITY = SecurityAgentInvestigationCountField("entity")
