# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_access_token_attributes import ServiceAccessTokenAttributes
    from datadog_api_client.v2.model.updated_service_access_token_relationships import (
        UpdatedServiceAccessTokenRelationships,
    )
    from datadog_api_client.v2.model.service_access_tokens_type import ServiceAccessTokensType


class UpdatedServiceAccessToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_access_token_attributes import ServiceAccessTokenAttributes
        from datadog_api_client.v2.model.updated_service_access_token_relationships import (
            UpdatedServiceAccessTokenRelationships,
        )
        from datadog_api_client.v2.model.service_access_tokens_type import ServiceAccessTokensType

        return {
            "attributes": (ServiceAccessTokenAttributes,),
            "id": (str,),
            "relationships": (UpdatedServiceAccessTokenRelationships,),
            "type": (ServiceAccessTokensType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ServiceAccessTokensType,
        attributes: Union[ServiceAccessTokenAttributes, UnsetType] = unset,
        relationships: Union[UpdatedServiceAccessTokenRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog access token returned by the update endpoint.

        :param attributes: Attributes of an access token.
        :type attributes: ServiceAccessTokenAttributes, optional

        :param id: ID of the access token.
        :type id: str

        :param relationships: Resources related to the access token.
        :type relationships: UpdatedServiceAccessTokenRelationships, optional

        :param type: Service access tokens resource type.
        :type type: ServiceAccessTokensType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
