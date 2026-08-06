# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceControlDetectionState(ModelSimple):
    """
    The current state of the detection. Possible values are `active`, `exception`, `mitigated`, `inactive`, `obsolete`, `resolved_externally`, and `mitigation_in_progress`.

    :param value: Must be one of ["active", "exception", "mitigated", "inactive", "obsolete", "resolved_externally", "mitigation_in_progress"].
    :type value: str
    """

    allowed_values = {
        "active",
        "exception",
        "mitigated",
        "inactive",
        "obsolete",
        "resolved_externally",
        "mitigation_in_progress",
    }
    ACTIVE: ClassVar["GovernanceControlDetectionState"]
    EXCEPTION: ClassVar["GovernanceControlDetectionState"]
    MITIGATED: ClassVar["GovernanceControlDetectionState"]
    INACTIVE: ClassVar["GovernanceControlDetectionState"]
    OBSOLETE: ClassVar["GovernanceControlDetectionState"]
    RESOLVED_EXTERNALLY: ClassVar["GovernanceControlDetectionState"]
    MITIGATION_IN_PROGRESS: ClassVar["GovernanceControlDetectionState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceControlDetectionState.ACTIVE = GovernanceControlDetectionState("active")
GovernanceControlDetectionState.EXCEPTION = GovernanceControlDetectionState("exception")
GovernanceControlDetectionState.MITIGATED = GovernanceControlDetectionState("mitigated")
GovernanceControlDetectionState.INACTIVE = GovernanceControlDetectionState("inactive")
GovernanceControlDetectionState.OBSOLETE = GovernanceControlDetectionState("obsolete")
GovernanceControlDetectionState.RESOLVED_EXTERNALLY = GovernanceControlDetectionState("resolved_externally")
GovernanceControlDetectionState.MITIGATION_IN_PROGRESS = GovernanceControlDetectionState("mitigation_in_progress")
