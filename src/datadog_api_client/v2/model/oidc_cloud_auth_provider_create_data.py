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
    from datadog_api_client.v2.model.oidc_cloud_auth_provider_create_attributes import (
        OIDCCloudAuthProviderCreateAttributes,
    )
    from datadog_api_client.v2.model.oidc_cloud_auth_provider_type import OIDCCloudAuthProviderType


class OIDCCloudAuthProviderCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_provider_create_attributes import (
            OIDCCloudAuthProviderCreateAttributes,
        )
        from datadog_api_client.v2.model.oidc_cloud_auth_provider_type import OIDCCloudAuthProviderType

        return {
            "attributes": (OIDCCloudAuthProviderCreateAttributes,),
            "type": (OIDCCloudAuthProviderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: OIDCCloudAuthProviderCreateAttributes, type: OIDCCloudAuthProviderType, **kwargs):
        """
        Custom OIDC provider creation data.

        :param attributes: Attributes for creating a Custom OIDC provider.
        :type attributes: OIDCCloudAuthProviderCreateAttributes

        :param type: Resource type.
        :type type: OIDCCloudAuthProviderType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
