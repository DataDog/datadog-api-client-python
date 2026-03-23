# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGatesEvaluationResultResponseAttributesGateStatus(ModelSimple):
    """
    The overall status of the gate evaluation.
        - `in_progress`: The evaluation is still running.
        - `pass`: All rules passed successfully and the deployment is allowed to proceed.
        - `fail`: One or more rules did not pass; the deployment should not proceed.

    :param value: Must be one of ["in_progress", "pass", "fail"].
    :type value: str
    """

    allowed_values = {
        "in_progress",
        "pass",
        "fail",
    }
    IN_PROGRESS: ClassVar["DeploymentGatesEvaluationResultResponseAttributesGateStatus"]
    PASS: ClassVar["DeploymentGatesEvaluationResultResponseAttributesGateStatus"]
    FAIL: ClassVar["DeploymentGatesEvaluationResultResponseAttributesGateStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGatesEvaluationResultResponseAttributesGateStatus.IN_PROGRESS = (
    DeploymentGatesEvaluationResultResponseAttributesGateStatus("in_progress")
)
DeploymentGatesEvaluationResultResponseAttributesGateStatus.PASS = (
    DeploymentGatesEvaluationResultResponseAttributesGateStatus("pass")
)
DeploymentGatesEvaluationResultResponseAttributesGateStatus.FAIL = (
    DeploymentGatesEvaluationResultResponseAttributesGateStatus("fail")
)
