# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OktaAccountType(ModelSimple):
    """
    Account type for an Okta account.

    :param value: If omitted defaults to "okta-accounts". Must be one of ["okta-accounts"].
    :type value: str
    """

    allowed_values = {
        "okta-accounts",
    }
    OKTA_ACCOUNTS: ClassVar["OktaAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OktaAccountType.OKTA_ACCOUNTS = OktaAccountType("okta-accounts")
