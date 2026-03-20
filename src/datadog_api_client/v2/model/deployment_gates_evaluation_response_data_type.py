# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGatesEvaluationResponseDataType(ModelSimple):
    """
    JSON:API type for a deployment gate evaluation response.

    :param value: If omitted defaults to "deployment_gates_evaluation_response". Must be one of ["deployment_gates_evaluation_response"].
    :type value: str
    """

    allowed_values = {
        "deployment_gates_evaluation_response",
    }
    DEPLOYMENT_GATES_EVALUATION_RESPONSE: ClassVar["DeploymentGatesEvaluationResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGatesEvaluationResponseDataType.DEPLOYMENT_GATES_EVALUATION_RESPONSE = (
    DeploymentGatesEvaluationResponseDataType("deployment_gates_evaluation_response")
)
