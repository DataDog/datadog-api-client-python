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
    from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_create_data import (
        GitHubCloudAuthIntakeMappingCreateData,
    )


class GitHubCloudAuthIntakeMappingCreateRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_create_data import (
            GitHubCloudAuthIntakeMappingCreateData,
        )

        return {
            "data": (GitHubCloudAuthIntakeMappingCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GitHubCloudAuthIntakeMappingCreateData, **kwargs):
        """
        Request used to create a GitHub cloud authentication intake mapping.

        :param data: Data for creating a GitHub cloud authentication intake mapping.
        :type data: GitHubCloudAuthIntakeMappingCreateData
        """
        super().__init__(kwargs)

        self_.data = data
