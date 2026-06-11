# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IdentityProviderAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "authentication_method": (str,),
            "enabled": (bool,),
        }

    attribute_map = {
        "authentication_method": "authentication_method",
        "enabled": "enabled",
    }

    def __init__(self_, authentication_method: str, enabled: bool, **kwargs):
        """
        Attributes of an organization identity provider.

        :param authentication_method: The authentication method used by this identity provider.
        :type authentication_method: str

        :param enabled: Whether this identity provider is enabled for the organization.
        :type enabled: bool
        """
        super().__init__(kwargs)

        self_.authentication_method = authentication_method
        self_.enabled = enabled
