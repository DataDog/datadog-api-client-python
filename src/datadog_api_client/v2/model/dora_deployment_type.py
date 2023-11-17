# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DORADeploymentType(ModelSimple):
    """
    JSON:API type for DORA deployment events.

    :param value: If omitted defaults to "dora_deployment". Must be one of ["dora_deployment"].
    :type value: str
    """

    allowed_values = {
        "dora_deployment",
    }
    DORA_DEPLOYMENT: ClassVar["DORADeploymentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DORADeploymentType.DORA_DEPLOYMENT = DORADeploymentType("dora_deployment")
