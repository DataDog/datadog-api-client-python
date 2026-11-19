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
    from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_data_response import (
        TerraformCloudAuthPersonaMappingDataResponse,
    )


class TerraformCloudAuthPersonaMappingResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_data_response import (
            TerraformCloudAuthPersonaMappingDataResponse,
        )

        return {
            "data": (TerraformCloudAuthPersonaMappingDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TerraformCloudAuthPersonaMappingDataResponse, **kwargs):
        """
        Response containing a single HCP Terraform persona mapping.

        :param data: HCP Terraform persona mapping resource.
        :type data: TerraformCloudAuthPersonaMappingDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
