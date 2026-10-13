# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGateRuleEvaluationType(ModelSimple):
    """
    Type of deployment gate rule.

    :param value: Must be one of ["monitor", "faulty_deployment_detection"].
    :type value: str
    """

    allowed_values = {
        "monitor",
        "faulty_deployment_detection",
    }
    MONITOR: ClassVar["DeploymentGateRuleEvaluationType"]
    FAULTY_DEPLOYMENT_DETECTION: ClassVar["DeploymentGateRuleEvaluationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGateRuleEvaluationType.MONITOR = DeploymentGateRuleEvaluationType("monitor")
DeploymentGateRuleEvaluationType.FAULTY_DEPLOYMENT_DETECTION = DeploymentGateRuleEvaluationType(
    "faulty_deployment_detection"
)
