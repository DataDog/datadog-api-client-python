# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentInvestigationVerdict(ModelSimple):
    """
    Verdict of the investigation. Only completed investigations have one.

    :param value: Must be one of ["benign", "suspicious", "malicious"].
    :type value: str
    """

    allowed_values = {
        "benign",
        "suspicious",
        "malicious",
    }
    BENIGN: ClassVar["SecurityAgentInvestigationVerdict"]
    SUSPICIOUS: ClassVar["SecurityAgentInvestigationVerdict"]
    MALICIOUS: ClassVar["SecurityAgentInvestigationVerdict"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentInvestigationVerdict.BENIGN = SecurityAgentInvestigationVerdict("benign")
SecurityAgentInvestigationVerdict.SUSPICIOUS = SecurityAgentInvestigationVerdict("suspicious")
SecurityAgentInvestigationVerdict.MALICIOUS = SecurityAgentInvestigationVerdict("malicious")
