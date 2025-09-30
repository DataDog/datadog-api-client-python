# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlakyTestAttributesFlakyState(ModelSimple):
    """
    The current state of the flaky test.

    :param value: Must be one of ["active", "fixed", "quarantined", "disabled"].
    :type value: str
    """

    allowed_values = {
        "active",
        "fixed",
        "quarantined",
        "disabled",
    }
    ACTIVE: ClassVar["FlakyTestAttributesFlakyState"]
    FIXED: ClassVar["FlakyTestAttributesFlakyState"]
    QUARANTINED: ClassVar["FlakyTestAttributesFlakyState"]
    DISABLED: ClassVar["FlakyTestAttributesFlakyState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlakyTestAttributesFlakyState.ACTIVE = FlakyTestAttributesFlakyState("active")
FlakyTestAttributesFlakyState.FIXED = FlakyTestAttributesFlakyState("fixed")
FlakyTestAttributesFlakyState.QUARANTINED = FlakyTestAttributesFlakyState("quarantined")
FlakyTestAttributesFlakyState.DISABLED = FlakyTestAttributesFlakyState("disabled")
