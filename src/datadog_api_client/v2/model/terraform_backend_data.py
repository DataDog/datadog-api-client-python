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
    from datadog_api_client.v2.model.terraform_backend_attributes import TerraformBackendAttributes
    from datadog_api_client.v2.model.terraform_backend_type import TerraformBackendType


class TerraformBackendData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_backend_attributes import TerraformBackendAttributes
        from datadog_api_client.v2.model.terraform_backend_type import TerraformBackendType

        return {
            "attributes": (TerraformBackendAttributes,),
            "id": (str,),
            "type": (TerraformBackendType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TerraformBackendAttributes, id: str, type: TerraformBackendType, **kwargs):
        """
        A Terraform backend sync configuration.

        :param attributes: Terraform backend sync configuration and bucket statuses.
        :type attributes: TerraformBackendAttributes

        :param id: Configuration ID, serialized as a string to preserve integer precision.
        :type id: str

        :param type: Terraform backend configuration resource type.
        :type type: TerraformBackendType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
