# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StatusPageEmailAccessPolicyType(ModelSimple):
    """
    Status page email access policy resource type.

    :param value: If omitted defaults to "email_access_policies". Must be one of ["email_access_policies"].
    :type value: str
    """

    allowed_values = {
        "email_access_policies",
    }
    EMAIL_ACCESS_POLICIES: ClassVar["StatusPageEmailAccessPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StatusPageEmailAccessPolicyType.EMAIL_ACCESS_POLICIES = StatusPageEmailAccessPolicyType("email_access_policies")
