# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.terraform_backend_create_attributes import TerraformBackendCreateAttributes
    from datadog_api_client.v2.model.terraform_backend_type import TerraformBackendType


class TerraformBackendCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_backend_create_attributes import TerraformBackendCreateAttributes
        from datadog_api_client.v2.model.terraform_backend_type import TerraformBackendType

        return {
            "attributes": (TerraformBackendCreateAttributes,),
            "type": (TerraformBackendType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TerraformBackendCreateAttributes, type: TerraformBackendType, **kwargs):
        """
        Terraform backend configuration create data.

        :param attributes: Settings for a new Terraform backend sync configuration.
        :type attributes: TerraformBackendCreateAttributes

        :param type: Terraform backend configuration resource type.
        :type type: TerraformBackendType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
