# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationInvestigationStatus(ModelSimple):
    """
    Investigation status.

    :param value: Must be one of ["open", "approval_required", "executing", "succeeded", "failed"].
    :type value: str
    """

    allowed_values = {
        "open",
        "approval_required",
        "executing",
        "succeeded",
        "failed",
    }
    OPEN: ClassVar["RemediationInvestigationStatus"]
    APPROVAL_REQUIRED: ClassVar["RemediationInvestigationStatus"]
    EXECUTING: ClassVar["RemediationInvestigationStatus"]
    SUCCEEDED: ClassVar["RemediationInvestigationStatus"]
    FAILED: ClassVar["RemediationInvestigationStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationInvestigationStatus.OPEN = RemediationInvestigationStatus("open")
RemediationInvestigationStatus.APPROVAL_REQUIRED = RemediationInvestigationStatus("approval_required")
RemediationInvestigationStatus.EXECUTING = RemediationInvestigationStatus("executing")
RemediationInvestigationStatus.SUCCEEDED = RemediationInvestigationStatus("succeeded")
RemediationInvestigationStatus.FAILED = RemediationInvestigationStatus("failed")
