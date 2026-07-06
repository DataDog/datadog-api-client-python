# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UserAuthorizedClientRelationshipOAuth2ClientDataType(ModelSimple):
    """
    OAuth2 client resource type.

    :param value: If omitted defaults to "oauth2_clients". Must be one of ["oauth2_clients"].
    :type value: str
    """

    allowed_values = {
        "oauth2_clients",
    }
    OAUTH2_CLIENTS: ClassVar["UserAuthorizedClientRelationshipOAuth2ClientDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UserAuthorizedClientRelationshipOAuth2ClientDataType.OAUTH2_CLIENTS = (
    UserAuthorizedClientRelationshipOAuth2ClientDataType("oauth2_clients")
)
