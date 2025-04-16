# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment(ModelSimple):
    """
    Specifies how this escalation step will assign targets (example `default` or `round-robin`).

    :param value: Must be one of ["default", "round-robin"].
    :type value: str
    """

    allowed_values = {
        "default",
        "round-robin",
    }
    DEFAULT: ClassVar["EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment"]
    ROUND_ROBIN: ClassVar["EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment.DEFAULT = (
    EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment("default")
)
EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment.ROUND_ROBIN = (
    EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment("round-robin")
)
