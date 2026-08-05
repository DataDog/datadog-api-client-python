# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceControlDetectionUpdateState(ModelSimple):
    """
    The new state to set for the detection. Set to `exception` to acknowledge the detection and exclude it from active counts, or `active` to reopen it.

    :param value: Must be one of ["exception", "active"].
    :type value: str
    """

    allowed_values = {
        "exception",
        "active",
    }
    EXCEPTION: ClassVar["GovernanceControlDetectionUpdateState"]
    ACTIVE: ClassVar["GovernanceControlDetectionUpdateState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceControlDetectionUpdateState.EXCEPTION = GovernanceControlDetectionUpdateState("exception")
GovernanceControlDetectionUpdateState.ACTIVE = GovernanceControlDetectionUpdateState("active")
