# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditPolicyReason(ModelSimple):
    """
    Why the policy was applied.

    :param value: Must be one of ["ACTIVATION", "REFRESH", "ARM_CHANGE", "SCHEDULED_END", "STOP"].
    :type value: str
    """

    allowed_values = {
        "ACTIVATION",
        "REFRESH",
        "ARM_CHANGE",
        "SCHEDULED_END",
        "STOP",
    }
    ACTIVATION: ClassVar["ExperimentsBanditPolicyReason"]
    REFRESH: ClassVar["ExperimentsBanditPolicyReason"]
    ARM_CHANGE: ClassVar["ExperimentsBanditPolicyReason"]
    SCHEDULED_END: ClassVar["ExperimentsBanditPolicyReason"]
    STOP: ClassVar["ExperimentsBanditPolicyReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditPolicyReason.ACTIVATION = ExperimentsBanditPolicyReason("ACTIVATION")
ExperimentsBanditPolicyReason.REFRESH = ExperimentsBanditPolicyReason("REFRESH")
ExperimentsBanditPolicyReason.ARM_CHANGE = ExperimentsBanditPolicyReason("ARM_CHANGE")
ExperimentsBanditPolicyReason.SCHEDULED_END = ExperimentsBanditPolicyReason("SCHEDULED_END")
ExperimentsBanditPolicyReason.STOP = ExperimentsBanditPolicyReason("STOP")
