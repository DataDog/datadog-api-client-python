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
    from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_create_attributes import (
        TerraformCloudAuthPersonaMappingCreateAttributes,
    )
    from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_type import (
        TerraformCloudAuthPersonaMappingType,
    )


class TerraformCloudAuthPersonaMappingCreateData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_create_attributes import (
            TerraformCloudAuthPersonaMappingCreateAttributes,
        )
        from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_type import (
            TerraformCloudAuthPersonaMappingType,
        )

        return {
            "attributes": (TerraformCloudAuthPersonaMappingCreateAttributes,),
            "type": (TerraformCloudAuthPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TerraformCloudAuthPersonaMappingCreateAttributes,
        type: TerraformCloudAuthPersonaMappingType,
        **kwargs,
    ):
        """
        Data for creating an HCP Terraform persona mapping.

        :param attributes: Attributes for creating an HCP Terraform persona mapping.
        :type attributes: TerraformCloudAuthPersonaMappingCreateAttributes

        :param type: Type identifier for an HCP Terraform persona mapping.
        :type type: TerraformCloudAuthPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
