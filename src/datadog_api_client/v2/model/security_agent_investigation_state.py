# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentInvestigationState(ModelSimple):
    """
    State of the investigation: `investigating` while it runs, `completed` after it has a result, or `failed`
        when it produced no result before its timeout.

    :param value: Must be one of ["investigating", "completed", "failed"].
    :type value: str
    """

    allowed_values = {
        "investigating",
        "completed",
        "failed",
    }
    INVESTIGATING: ClassVar["SecurityAgentInvestigationState"]
    COMPLETED: ClassVar["SecurityAgentInvestigationState"]
    FAILED: ClassVar["SecurityAgentInvestigationState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentInvestigationState.INVESTIGATING = SecurityAgentInvestigationState("investigating")
SecurityAgentInvestigationState.COMPLETED = SecurityAgentInvestigationState("completed")
SecurityAgentInvestigationState.FAILED = SecurityAgentInvestigationState("failed")
