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
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import WebhooksOAuth2ClientCredentialsType


class WebhooksOAuth2ClientCredentialsRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import (
            WebhooksOAuth2ClientCredentialsType,
        )

        return {
            "id": (str,),
            "type": (WebhooksOAuth2ClientCredentialsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        type: Union[WebhooksOAuth2ClientCredentialsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationship data referencing an OAuth2 client credentials resource.

        :param id: The ID of the OAuth2 client credentials resource.
        :type id: str, optional

        :param type: OAuth2 client credentials resource type.
        :type type: WebhooksOAuth2ClientCredentialsType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
