# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TerraformBackendType(ModelSimple):
    """
    Terraform backend configuration resource type.

    :param value: If omitted defaults to "terraform-backends". Must be one of ["terraform-backends"].
    :type value: str
    """

    allowed_values = {
        "terraform-backends",
    }
    TERRAFORM_BACKENDS: ClassVar["TerraformBackendType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TerraformBackendType.TERRAFORM_BACKENDS = TerraformBackendType("terraform-backends")
