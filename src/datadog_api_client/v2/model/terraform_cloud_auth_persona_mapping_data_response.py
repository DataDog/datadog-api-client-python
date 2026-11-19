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
    from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_attributes_response import (
        TerraformCloudAuthPersonaMappingAttributesResponse,
    )
    from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_type import (
        TerraformCloudAuthPersonaMappingType,
    )


class TerraformCloudAuthPersonaMappingDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_attributes_response import (
            TerraformCloudAuthPersonaMappingAttributesResponse,
        )
        from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_type import (
            TerraformCloudAuthPersonaMappingType,
        )

        return {
            "attributes": (TerraformCloudAuthPersonaMappingAttributesResponse,),
            "id": (str,),
            "type": (TerraformCloudAuthPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TerraformCloudAuthPersonaMappingAttributesResponse,
        id: str,
        type: TerraformCloudAuthPersonaMappingType,
        **kwargs,
    ):
        """
        HCP Terraform persona mapping resource.

        :param attributes: Stored HCP Terraform persona mapping attributes.
        :type attributes: TerraformCloudAuthPersonaMappingAttributesResponse

        :param id: Unique identifier of the persona mapping.
        :type id: str

        :param type: Type identifier for an HCP Terraform persona mapping.
        :type type: TerraformCloudAuthPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
