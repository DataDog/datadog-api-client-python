# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.identity_provider_data import IdentityProviderData


class IdentityProviderResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.identity_provider_data import IdentityProviderData

        return {
            "data": (IdentityProviderData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IdentityProviderData, **kwargs):
        """
        Response containing a single organization identity provider.

        :param data: Data object representing an organization identity provider.
        :type data: IdentityProviderData
        """
        super().__init__(kwargs)

        self_.data = data
