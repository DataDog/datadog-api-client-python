# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceControlResourceType(ModelSimple):
    """
    JSON:API resource type for a governance control.

    :param value: If omitted defaults to "governance_control". Must be one of ["governance_control"].
    :type value: str
    """

    allowed_values = {
        "governance_control",
    }
    GOVERNANCE_CONTROL: ClassVar["GovernanceControlResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceControlResourceType.GOVERNANCE_CONTROL = GovernanceControlResourceType("governance_control")
