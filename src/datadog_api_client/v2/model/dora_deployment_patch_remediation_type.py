# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DORADeploymentPatchRemediationType(ModelSimple):
    """
    The type of remediation action taken. Required when the failed deployment must be linked to a remediation deployment.

    :param value: Must be one of ["rollback", "rollforward"].
    :type value: str
    """

    allowed_values = {
        "rollback",
        "rollforward",
    }
    ROLLBACK: ClassVar["DORADeploymentPatchRemediationType"]
    ROLLFORWARD: ClassVar["DORADeploymentPatchRemediationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DORADeploymentPatchRemediationType.ROLLBACK = DORADeploymentPatchRemediationType("rollback")
DORADeploymentPatchRemediationType.ROLLFORWARD = DORADeploymentPatchRemediationType("rollforward")
