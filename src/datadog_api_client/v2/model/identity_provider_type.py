# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IdentityProviderType(ModelSimple):
    """
    The resource type for identity providers.

    :param value: If omitted defaults to "identity_providers". Must be one of ["identity_providers"].
    :type value: str
    """

    allowed_values = {
        "identity_providers",
    }
    IDENTITY_PROVIDERS: ClassVar["IdentityProviderType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IdentityProviderType.IDENTITY_PROVIDERS = IdentityProviderType("identity_providers")
