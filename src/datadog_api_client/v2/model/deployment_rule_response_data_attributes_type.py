# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentRuleResponseDataAttributesType(ModelSimple):
    """
    The type of the deployment rule.

    :param value: Must be one of ["faulty_deployment_detection", "monitor"].
    :type value: str
    """

    allowed_values = {
        "faulty_deployment_detection",
        "monitor",
    }
    FAULTY_DEPLOYMENT_DETECTION: ClassVar["DeploymentRuleResponseDataAttributesType"]
    MONITOR: ClassVar["DeploymentRuleResponseDataAttributesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentRuleResponseDataAttributesType.FAULTY_DEPLOYMENT_DETECTION = DeploymentRuleResponseDataAttributesType(
    "faulty_deployment_detection"
)
DeploymentRuleResponseDataAttributesType.MONITOR = DeploymentRuleResponseDataAttributesType("monitor")
