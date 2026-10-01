# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GitHubCloudAuthPersonaMappingType(ModelSimple):
    """
    Type identifier for GitHub cloud authentication persona mapping.

    :param value: If omitted defaults to "github_oidc_auth_config". Must be one of ["github_oidc_auth_config"].
    :type value: str
    """

    allowed_values = {
        "github_oidc_auth_config",
    }
    GITHUB_OIDC_AUTH_CONFIG: ClassVar["GitHubCloudAuthPersonaMappingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GitHubCloudAuthPersonaMappingType.GITHUB_OIDC_AUTH_CONFIG = GitHubCloudAuthPersonaMappingType("github_oidc_auth_config")
