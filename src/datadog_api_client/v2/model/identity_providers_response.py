# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.identity_provider_data import IdentityProviderData


class IdentityProvidersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.identity_provider_data import IdentityProviderData

        return {
            "data": ([IdentityProviderData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[IdentityProviderData], **kwargs):
        """
        Response containing a list of identity providers for an organization.

        :param data: List of organization identity provider data objects.
        :type data: [IdentityProviderData]
        """
        super().__init__(kwargs)

        self_.data = data
