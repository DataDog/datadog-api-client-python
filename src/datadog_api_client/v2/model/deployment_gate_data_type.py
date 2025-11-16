# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeploymentGateDataType(ModelSimple):
    """
    Deployment gate resource type.

    :param value: If omitted defaults to "deployment_gate". Must be one of ["deployment_gate"].
    :type value: str
    """

    allowed_values = {
        "deployment_gate",
    }
    DEPLOYMENT_GATE: ClassVar["DeploymentGateDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeploymentGateDataType.DEPLOYMENT_GATE = DeploymentGateDataType("deployment_gate")
