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
    from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_attributes_response import (
        GitHubCloudAuthIntakeMappingAttributesResponse,
    )
    from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_type import GitHubCloudAuthIntakeMappingType


class GitHubCloudAuthIntakeMappingDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_attributes_response import (
            GitHubCloudAuthIntakeMappingAttributesResponse,
        )
        from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_type import GitHubCloudAuthIntakeMappingType

        return {
            "attributes": (GitHubCloudAuthIntakeMappingAttributesResponse,),
            "id": (str,),
            "type": (GitHubCloudAuthIntakeMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GitHubCloudAuthIntakeMappingAttributesResponse,
        id: str,
        type: GitHubCloudAuthIntakeMappingType,
        **kwargs,
    ):
        """
        Data for GitHub cloud authentication intake mapping response.

        :param attributes: Attributes for GitHub cloud authentication intake mapping response.
        :type attributes: GitHubCloudAuthIntakeMappingAttributesResponse

        :param id: Unique identifier for the intake mapping.
        :type id: str

        :param type: Type identifier for GitHub cloud authentication intake mapping.
        :type type: GitHubCloudAuthIntakeMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
