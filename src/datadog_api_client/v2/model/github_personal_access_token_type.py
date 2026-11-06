# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GithubPersonalAccessTokenType(ModelSimple):
    """
    The credential type for `GithubPersonalAccessToken`.

    :param value: If omitted defaults to "GithubPersonalAccessToken". Must be one of ["GithubPersonalAccessToken"].
    :type value: str
    """

    allowed_values = {
        "GithubPersonalAccessToken",
    }
    GITHUBPERSONALACCESSTOKEN: ClassVar["GithubPersonalAccessTokenType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GithubPersonalAccessTokenType.GITHUBPERSONALACCESSTOKEN = GithubPersonalAccessTokenType("GithubPersonalAccessToken")
