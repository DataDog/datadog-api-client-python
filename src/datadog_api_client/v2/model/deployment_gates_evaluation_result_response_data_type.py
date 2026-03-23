# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGatesEvaluationResultResponseDataType(ModelSimple):
    """
    JSON:API type for a deployment gate evaluation result response.

    :param value: If omitted defaults to "deployment_gates_evaluation_result_response". Must be one of ["deployment_gates_evaluation_result_response"].
    :type value: str
    """

    allowed_values = {
        "deployment_gates_evaluation_result_response",
    }
    DEPLOYMENT_GATES_EVALUATION_RESULT_RESPONSE: ClassVar["DeploymentGatesEvaluationResultResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGatesEvaluationResultResponseDataType.DEPLOYMENT_GATES_EVALUATION_RESULT_RESPONSE = (
    DeploymentGatesEvaluationResultResponseDataType("deployment_gates_evaluation_result_response")
)
