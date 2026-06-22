# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationLaunchType(ModelSimple):
    """
    ECS launch type.

    :param value: Must be one of ["EC2", "FARGATE"].
    :type value: str
    """

    allowed_values = {
        "EC2",
        "FARGATE",
    }
    EC2: ClassVar["RemediationLaunchType"]
    FARGATE: ClassVar["RemediationLaunchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationLaunchType.EC2 = RemediationLaunchType("EC2")
RemediationLaunchType.FARGATE = RemediationLaunchType("FARGATE")
