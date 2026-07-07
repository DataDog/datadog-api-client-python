# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IdentityProviderUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
        }

    attribute_map = {
        "enabled": "enabled",
    }

    def __init__(self_, enabled: bool, **kwargs):
        """
        Attributes for updating an organization identity provider.

        :param enabled: Whether to enable or disable this identity provider for the organization.
        :type enabled: bool
        """
        super().__init__(kwargs)

        self_.enabled = enabled
