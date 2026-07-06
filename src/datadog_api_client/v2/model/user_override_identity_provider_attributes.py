# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserOverrideIdentityProviderAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "authentication_method": (str,),
        }

    attribute_map = {
        "authentication_method": "authentication_method",
    }

    def __init__(self_, authentication_method: str, **kwargs):
        """
        Attributes of an identity provider override for a user.

        :param authentication_method: The authentication method used by this identity provider.
        :type authentication_method: str
        """
        super().__init__(kwargs)

        self_.authentication_method = authentication_method
