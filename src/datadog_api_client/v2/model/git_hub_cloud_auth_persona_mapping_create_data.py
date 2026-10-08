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
    from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_create_attributes import (
        GitHubCloudAuthPersonaMappingCreateAttributes,
    )
    from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_type import GitHubCloudAuthPersonaMappingType


class GitHubCloudAuthPersonaMappingCreateData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_create_attributes import (
            GitHubCloudAuthPersonaMappingCreateAttributes,
        )
        from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_type import (
            GitHubCloudAuthPersonaMappingType,
        )

        return {
            "attributes": (GitHubCloudAuthPersonaMappingCreateAttributes,),
            "type": (GitHubCloudAuthPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GitHubCloudAuthPersonaMappingCreateAttributes,
        type: GitHubCloudAuthPersonaMappingType,
        **kwargs,
    ):
        """
        Data for creating a GitHub cloud authentication persona mapping.

        :param attributes: Attributes for creating a GitHub cloud authentication persona mapping.
        :type attributes: GitHubCloudAuthPersonaMappingCreateAttributes

        :param type: Type identifier for GitHub cloud authentication persona mapping.
        :type type: GitHubCloudAuthPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
