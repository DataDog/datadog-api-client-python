# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentOutreachDomainAddType(ModelSimple):
    """
    Type of an allowed outreach domain add request.

    :param value: If omitted defaults to "outreach_policy_domain_add". Must be one of ["outreach_policy_domain_add"].
    :type value: str
    """

    allowed_values = {
        "outreach_policy_domain_add",
    }
    OUTREACH_POLICY_DOMAIN_ADD: ClassVar["SecurityAgentOutreachDomainAddType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentOutreachDomainAddType.OUTREACH_POLICY_DOMAIN_ADD = SecurityAgentOutreachDomainAddType(
    "outreach_policy_domain_add"
)
