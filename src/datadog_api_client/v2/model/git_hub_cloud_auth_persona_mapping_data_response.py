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
    from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_attributes_response import (
        GitHubCloudAuthPersonaMappingAttributesResponse,
    )
    from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_type import GitHubCloudAuthPersonaMappingType


class GitHubCloudAuthPersonaMappingDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_attributes_response import (
            GitHubCloudAuthPersonaMappingAttributesResponse,
        )
        from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_type import (
            GitHubCloudAuthPersonaMappingType,
        )

        return {
            "attributes": (GitHubCloudAuthPersonaMappingAttributesResponse,),
            "id": (str,),
            "type": (GitHubCloudAuthPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GitHubCloudAuthPersonaMappingAttributesResponse,
        id: str,
        type: GitHubCloudAuthPersonaMappingType,
        **kwargs,
    ):
        """
        Data for GitHub cloud authentication persona mapping response.

        :param attributes: Attributes for GitHub cloud authentication persona mapping response.
        :type attributes: GitHubCloudAuthPersonaMappingAttributesResponse

        :param id: Unique identifier for the persona mapping.
        :type id: str

        :param type: Type identifier for GitHub cloud authentication persona mapping.
        :type type: GitHubCloudAuthPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
