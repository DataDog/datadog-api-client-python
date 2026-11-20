# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationGroupType(ModelSimple):
    """
    Remediation groups resource type.

    :param value: If omitted defaults to "remediation_groups". Must be one of ["remediation_groups"].
    :type value: str
    """

    allowed_values = {
        "remediation_groups",
    }
    REMEDIATION_GROUPS: ClassVar["RemediationGroupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationGroupType.REMEDIATION_GROUPS = RemediationGroupType("remediation_groups")
