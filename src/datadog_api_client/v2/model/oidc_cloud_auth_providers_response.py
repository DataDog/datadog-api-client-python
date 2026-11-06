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
    from datadog_api_client.v2.model.oidc_cloud_auth_provider_data_response import OIDCCloudAuthProviderDataResponse


class OIDCCloudAuthProvidersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_provider_data_response import OIDCCloudAuthProviderDataResponse

        return {
            "data": ([OIDCCloudAuthProviderDataResponse],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[OIDCCloudAuthProviderDataResponse], **kwargs):
        """
        List of Custom OIDC provider resources.

        :param data: Configured resources.
        :type data: [OIDCCloudAuthProviderDataResponse]
        """
        super().__init__(kwargs)

        self_.data = data
