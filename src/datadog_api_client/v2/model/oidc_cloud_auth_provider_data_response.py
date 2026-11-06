# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.oidc_cloud_auth_provider_attributes_response import (
        OIDCCloudAuthProviderAttributesResponse,
    )
    from datadog_api_client.v2.model.oidc_cloud_auth_provider_type import OIDCCloudAuthProviderType


class OIDCCloudAuthProviderDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_provider_attributes_response import (
            OIDCCloudAuthProviderAttributesResponse,
        )
        from datadog_api_client.v2.model.oidc_cloud_auth_provider_type import OIDCCloudAuthProviderType

        return {
            "attributes": (OIDCCloudAuthProviderAttributesResponse,),
            "id": (UUID,),
            "type": (OIDCCloudAuthProviderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: OIDCCloudAuthProviderAttributesResponse, id: UUID, type: OIDCCloudAuthProviderType, **kwargs
    ):
        """
        Custom OIDC provider resource.

        :param attributes: Stored Custom OIDC provider attributes.
        :type attributes: OIDCCloudAuthProviderAttributesResponse

        :param id: Unique resource identifier.
        :type id: UUID

        :param type: Resource type.
        :type type: OIDCCloudAuthProviderType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
