# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgAuthorizedClientUserAuthorizationsSort(ModelSimple):
    """
    Field to sort user authorizations by.

    :param value: Must be one of ["user.name", "user.email", "oauth2_client.name"].
    :type value: str
    """

    allowed_values = {
        "user.name",
        "user.email",
        "oauth2_client.name",
    }
    USER_NAME: ClassVar["OrgAuthorizedClientUserAuthorizationsSort"]
    USER_EMAIL: ClassVar["OrgAuthorizedClientUserAuthorizationsSort"]
    OAUTH2_CLIENT_NAME: ClassVar["OrgAuthorizedClientUserAuthorizationsSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgAuthorizedClientUserAuthorizationsSort.USER_NAME = OrgAuthorizedClientUserAuthorizationsSort("user.name")
OrgAuthorizedClientUserAuthorizationsSort.USER_EMAIL = OrgAuthorizedClientUserAuthorizationsSort("user.email")
OrgAuthorizedClientUserAuthorizationsSort.OAUTH2_CLIENT_NAME = OrgAuthorizedClientUserAuthorizationsSort(
    "oauth2_client.name"
)
