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
    from datadog_api_client.v2.model.service_account_access_token_update_attributes import (
        ServiceAccountAccessTokenUpdateAttributes,
    )
    from datadog_api_client.v2.model.service_access_tokens_type import ServiceAccessTokensType


class ServiceAccountAccessTokenUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_account_access_token_update_attributes import (
            ServiceAccountAccessTokenUpdateAttributes,
        )
        from datadog_api_client.v2.model.service_access_tokens_type import ServiceAccessTokensType

        return {
            "attributes": (ServiceAccountAccessTokenUpdateAttributes,),
            "id": (str,),
            "type": (ServiceAccessTokensType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ServiceAccountAccessTokenUpdateAttributes, id: str, type: ServiceAccessTokensType, **kwargs
    ):
        """
        Object used to update a service account access token.

        :param attributes: Attributes used to update a service account access token.
        :type attributes: ServiceAccountAccessTokenUpdateAttributes

        :param id: ID of the access token.
        :type id: str

        :param type: Service access tokens resource type.
        :type type: ServiceAccessTokensType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
