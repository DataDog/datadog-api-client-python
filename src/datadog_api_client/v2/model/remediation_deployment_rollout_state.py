# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationDeploymentRolloutState(ModelSimple):
    """
    ECS deployment state, populated only for deployment failures.

    :param value: Must be one of ["IN_PROGRESS", "COMPLETED", "FAILED"].
    :type value: str
    """

    allowed_values = {
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    }
    IN_PROGRESS: ClassVar["RemediationDeploymentRolloutState"]
    COMPLETED: ClassVar["RemediationDeploymentRolloutState"]
    FAILED: ClassVar["RemediationDeploymentRolloutState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationDeploymentRolloutState.IN_PROGRESS = RemediationDeploymentRolloutState("IN_PROGRESS")
RemediationDeploymentRolloutState.COMPLETED = RemediationDeploymentRolloutState("COMPLETED")
RemediationDeploymentRolloutState.FAILED = RemediationDeploymentRolloutState("FAILED")
