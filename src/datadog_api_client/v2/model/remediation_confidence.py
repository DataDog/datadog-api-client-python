# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationConfidence(ModelSimple):
    """
    The agent's self-rated confidence in a plan.

    :param value: Must be one of ["low", "medium", "high"].
    :type value: str
    """

    allowed_values = {
        "low",
        "medium",
        "high",
    }
    LOW: ClassVar["RemediationConfidence"]
    MEDIUM: ClassVar["RemediationConfidence"]
    HIGH: ClassVar["RemediationConfidence"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationConfidence.LOW = RemediationConfidence("low")
RemediationConfidence.MEDIUM = RemediationConfidence("medium")
RemediationConfidence.HIGH = RemediationConfidence("high")
