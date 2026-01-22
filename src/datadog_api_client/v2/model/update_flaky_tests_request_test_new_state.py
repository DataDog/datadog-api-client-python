# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UpdateFlakyTestsRequestTestNewState(ModelSimple):
    """
    The new state to set for the flaky test.

    :param value: Must be one of ["active", "quarantined", "disabled", "fixed"].
    :type value: str
    """

    allowed_values = {
        "active",
        "quarantined",
        "disabled",
        "fixed",
    }
    ACTIVE: ClassVar["UpdateFlakyTestsRequestTestNewState"]
    QUARANTINED: ClassVar["UpdateFlakyTestsRequestTestNewState"]
    DISABLED: ClassVar["UpdateFlakyTestsRequestTestNewState"]
    FIXED: ClassVar["UpdateFlakyTestsRequestTestNewState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UpdateFlakyTestsRequestTestNewState.ACTIVE = UpdateFlakyTestsRequestTestNewState("active")
UpdateFlakyTestsRequestTestNewState.QUARANTINED = UpdateFlakyTestsRequestTestNewState("quarantined")
UpdateFlakyTestsRequestTestNewState.DISABLED = UpdateFlakyTestsRequestTestNewState("disabled")
UpdateFlakyTestsRequestTestNewState.FIXED = UpdateFlakyTestsRequestTestNewState("fixed")
