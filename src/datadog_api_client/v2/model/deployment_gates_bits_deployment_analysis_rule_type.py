# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGatesBitsDeploymentAnalysisRuleType(ModelSimple):
    """
    The type identifier for a Bits Deployment Analysis rule.

    :param value: If omitted defaults to "bits_deployment_analysis". Must be one of ["bits_deployment_analysis"].
    :type value: str
    """

    allowed_values = {
        "bits_deployment_analysis",
    }
    BITS_DEPLOYMENT_ANALYSIS: ClassVar["DeploymentGatesBitsDeploymentAnalysisRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGatesBitsDeploymentAnalysisRuleType.BITS_DEPLOYMENT_ANALYSIS = DeploymentGatesBitsDeploymentAnalysisRuleType(
    "bits_deployment_analysis"
)
