# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGateEvaluationDataType(ModelSimple):
    """
    JSON:API type for a deployment gate evaluation.

    :param value: If omitted defaults to "deployment_gate_evaluation". Must be one of ["deployment_gate_evaluation"].
    :type value: str
    """

    allowed_values = {
        "deployment_gate_evaluation",
    }
    DEPLOYMENT_GATE_EVALUATION: ClassVar["DeploymentGateEvaluationDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGateEvaluationDataType.DEPLOYMENT_GATE_EVALUATION = DeploymentGateEvaluationDataType(
    "deployment_gate_evaluation"
)
