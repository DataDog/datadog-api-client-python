# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PersonalAccessTokensSort(ModelSimple):
    """
    Sorting options for personal access tokens.

    :param value: If omitted defaults to "name". Must be one of ["name", "-name", "created_at", "-created_at", "expires_at", "-expires_at"].
    :type value: str
    """

    allowed_values = {
        "name",
        "-name",
        "created_at",
        "-created_at",
        "expires_at",
        "-expires_at",
    }
    NAME_ASCENDING: ClassVar["PersonalAccessTokensSort"]
    NAME_DESCENDING: ClassVar["PersonalAccessTokensSort"]
    CREATED_AT_ASCENDING: ClassVar["PersonalAccessTokensSort"]
    CREATED_AT_DESCENDING: ClassVar["PersonalAccessTokensSort"]
    EXPIRES_AT_ASCENDING: ClassVar["PersonalAccessTokensSort"]
    EXPIRES_AT_DESCENDING: ClassVar["PersonalAccessTokensSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PersonalAccessTokensSort.NAME_ASCENDING = PersonalAccessTokensSort("name")
PersonalAccessTokensSort.NAME_DESCENDING = PersonalAccessTokensSort("-name")
PersonalAccessTokensSort.CREATED_AT_ASCENDING = PersonalAccessTokensSort("created_at")
PersonalAccessTokensSort.CREATED_AT_DESCENDING = PersonalAccessTokensSort("-created_at")
PersonalAccessTokensSort.EXPIRES_AT_ASCENDING = PersonalAccessTokensSort("expires_at")
PersonalAccessTokensSort.EXPIRES_AT_DESCENDING = PersonalAccessTokensSort("-expires_at")
