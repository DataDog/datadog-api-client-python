# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GitHubCloudAuthIntakeMappingType(ModelSimple):
    """
    Type identifier for GitHub cloud authentication intake mapping.

    :param value: If omitted defaults to "github_oidc_auth_intake_mapping". Must be one of ["github_oidc_auth_intake_mapping"].
    :type value: str
    """

    allowed_values = {
        "github_oidc_auth_intake_mapping",
    }
    GITHUB_OIDC_AUTH_INTAKE_MAPPING: ClassVar["GitHubCloudAuthIntakeMappingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GitHubCloudAuthIntakeMappingType.GITHUB_OIDC_AUTH_INTAKE_MAPPING = GitHubCloudAuthIntakeMappingType(
    "github_oidc_auth_intake_mapping"
)
