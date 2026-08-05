# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceControlDetectionResourceType(ModelSimple):
    """
    Governance control detection resource type.

    :param value: If omitted defaults to "governance_control_detection". Must be one of ["governance_control_detection"].
    :type value: str
    """

    allowed_values = {
        "governance_control_detection",
    }
    GOVERNANCE_CONTROL_DETECTION: ClassVar["GovernanceControlDetectionResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceControlDetectionResourceType.GOVERNANCE_CONTROL_DETECTION = GovernanceControlDetectionResourceType(
    "governance_control_detection"
)
