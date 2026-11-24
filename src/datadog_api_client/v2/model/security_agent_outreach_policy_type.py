# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentOutreachPolicyType(ModelSimple):
    """
    Type of the outreach policy resource.

    :param value: If omitted defaults to "outreach_policy". Must be one of ["outreach_policy"].
    :type value: str
    """

    allowed_values = {
        "outreach_policy",
    }
    OUTREACH_POLICY: ClassVar["SecurityAgentOutreachPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentOutreachPolicyType.OUTREACH_POLICY = SecurityAgentOutreachPolicyType("outreach_policy")
