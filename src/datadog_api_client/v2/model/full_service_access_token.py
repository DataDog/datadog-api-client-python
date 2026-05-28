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
    from datadog_api_client.v2.model.full_service_access_token_attributes import FullServiceAccessTokenAttributes
    from datadog_api_client.v2.model.service_access_token_relationships import ServiceAccessTokenRelationships
    from datadog_api_client.v2.model.service_access_tokens_type import ServiceAccessTokensType


class FullServiceAccessToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.full_service_access_token_attributes import FullServiceAccessTokenAttributes
        from datadog_api_client.v2.model.service_access_token_relationships import ServiceAccessTokenRelationships
        from datadog_api_client.v2.model.service_access_tokens_type import ServiceAccessTokensType

        return {
            "attributes": (FullServiceAccessTokenAttributes,),
            "id": (str,),
            "relationships": (ServiceAccessTokenRelationships,),
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
        attributes: Union[FullServiceAccessTokenAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ServiceAccessTokenRelationships, UnsetType] = unset,
        type: Union[ServiceAccessTokensType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog access token, including the token key.

        :param attributes: Attributes of a full access token, including the token key.
        :type attributes: FullServiceAccessTokenAttributes, optional

        :param id: ID of the access token.
        :type id: str, optional

        :param relationships: Resources related to the access token.
        :type relationships: ServiceAccessTokenRelationships, optional

        :param type: Service access tokens resource type.
        :type type: ServiceAccessTokensType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
