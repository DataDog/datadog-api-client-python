# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppGitHubAccountType(ModelSimple):
    """
    JSON:API type for the GitHub account resource.
        The value must always be `ci_github_account`.

    :param value: If omitted defaults to "ci_github_account". Must be one of ["ci_github_account"].
    :type value: str
    """

    allowed_values = {
        "ci_github_account",
    }
    CI_GITHUB_ACCOUNT: ClassVar["CIAppGitHubAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppGitHubAccountType.CI_GITHUB_ACCOUNT = CIAppGitHubAccountType("ci_github_account")
