# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UpsertOAuthScopesRestrictionType(ModelSimple):
    """
    JSON:API resource type for an upsert OAuth2 client scopes restriction request.

    :param value: If omitted defaults to "upsert_scopes_restriction". Must be one of ["upsert_scopes_restriction"].
    :type value: str
    """

    allowed_values = {
        "upsert_scopes_restriction",
    }
    UPSERT_SCOPES_RESTRICTION: ClassVar["UpsertOAuthScopesRestrictionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UpsertOAuthScopesRestrictionType.UPSERT_SCOPES_RESTRICTION = UpsertOAuthScopesRestrictionType(
    "upsert_scopes_restriction"
)
