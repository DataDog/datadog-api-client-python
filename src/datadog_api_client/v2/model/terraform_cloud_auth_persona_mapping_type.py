# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TerraformCloudAuthPersonaMappingType(ModelSimple):
    """
    Type identifier for an HCP Terraform persona mapping.

    :param value: If omitted defaults to "terraform_cloud_auth_config". Must be one of ["terraform_cloud_auth_config"].
    :type value: str
    """

    allowed_values = {
        "terraform_cloud_auth_config",
    }
    TERRAFORM_CLOUD_AUTH_CONFIG: ClassVar["TerraformCloudAuthPersonaMappingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TerraformCloudAuthPersonaMappingType.TERRAFORM_CLOUD_AUTH_CONFIG = TerraformCloudAuthPersonaMappingType(
    "terraform_cloud_auth_config"
)
