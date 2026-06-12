# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGatesFDDRuleType(ModelSimple):
    """
    The type identifier for a faulty deployment detection rule.

    :param value: If omitted defaults to "faulty_deployment_detection". Must be one of ["faulty_deployment_detection"].
    :type value: str
    """

    allowed_values = {
        "faulty_deployment_detection",
    }
    FAULTY_DEPLOYMENT_DETECTION: ClassVar["DeploymentGatesFDDRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGatesFDDRuleType.FAULTY_DEPLOYMENT_DETECTION = DeploymentGatesFDDRuleType("faulty_deployment_detection")
