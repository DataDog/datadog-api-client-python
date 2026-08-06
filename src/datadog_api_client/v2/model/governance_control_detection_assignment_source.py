# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceControlDetectionAssignmentSource(ModelSimple):
    """
    How the detection's current assignment was determined. Possible values are `auto_resolved`, `manual`, `reassigned`, and `cleared`.

    :param value: Must be one of ["auto_resolved", "manual", "reassigned", "cleared"].
    :type value: str
    """

    allowed_values = {
        "auto_resolved",
        "manual",
        "reassigned",
        "cleared",
    }
    AUTO_RESOLVED: ClassVar["GovernanceControlDetectionAssignmentSource"]
    MANUAL: ClassVar["GovernanceControlDetectionAssignmentSource"]
    REASSIGNED: ClassVar["GovernanceControlDetectionAssignmentSource"]
    CLEARED: ClassVar["GovernanceControlDetectionAssignmentSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceControlDetectionAssignmentSource.AUTO_RESOLVED = GovernanceControlDetectionAssignmentSource("auto_resolved")
GovernanceControlDetectionAssignmentSource.MANUAL = GovernanceControlDetectionAssignmentSource("manual")
GovernanceControlDetectionAssignmentSource.REASSIGNED = GovernanceControlDetectionAssignmentSource("reassigned")
GovernanceControlDetectionAssignmentSource.CLEARED = GovernanceControlDetectionAssignmentSource("cleared")
