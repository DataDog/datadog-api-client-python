# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DORADeploymentPatchRequestDataType(ModelSimple):
    """
    JSON:API type for DORA deployment patch request.

    :param value: If omitted defaults to "dora_deployment_patch_request". Must be one of ["dora_deployment_patch_request"].
    :type value: str
    """

    allowed_values = {
        "dora_deployment_patch_request",
    }
    DORA_DEPLOYMENT_PATCH_REQUEST: ClassVar["DORADeploymentPatchRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DORADeploymentPatchRequestDataType.DORA_DEPLOYMENT_PATCH_REQUEST = DORADeploymentPatchRequestDataType(
    "dora_deployment_patch_request"
)
