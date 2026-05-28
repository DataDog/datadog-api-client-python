# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OAuthScopesRestrictionType(ModelSimple):
    """
    JSON:API resource type for an OAuth2 client scopes restriction.

    :param value: If omitted defaults to "scopes_restriction". Must be one of ["scopes_restriction"].
    :type value: str
    """

    allowed_values = {
        "scopes_restriction",
    }
    SCOPES_RESTRICTION: ClassVar["OAuthScopesRestrictionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OAuthScopesRestrictionType.SCOPES_RESTRICTION = OAuthScopesRestrictionType("scopes_restriction")
