# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AccessTokenOwnerType(ModelSimple):
    """
    Owner resource type. Either a user or a service account.

    :param value: Must be one of ["users", "service_account"].
    :type value: str
    """

    allowed_values = {
        "users",
        "service_account",
    }
    USERS: ClassVar["AccessTokenOwnerType"]
    SERVICE_ACCOUNT: ClassVar["AccessTokenOwnerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AccessTokenOwnerType.USERS = AccessTokenOwnerType("users")
AccessTokenOwnerType.SERVICE_ACCOUNT = AccessTokenOwnerType("service_account")
