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
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response_attributes import (
        WebhooksOAuth2ClientCredentialsResponseAttributes,
    )
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import WebhooksOAuth2ClientCredentialsType


class WebhooksOAuth2ClientCredentialsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response_attributes import (
            WebhooksOAuth2ClientCredentialsResponseAttributes,
        )
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import (
            WebhooksOAuth2ClientCredentialsType,
        )

        return {
            "attributes": (WebhooksOAuth2ClientCredentialsResponseAttributes,),
            "id": (str,),
            "type": (WebhooksOAuth2ClientCredentialsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: WebhooksOAuth2ClientCredentialsResponseAttributes,
        id: str,
        type: WebhooksOAuth2ClientCredentialsType,
        **kwargs,
    ):
        """
        OAuth2 client credentials data from a response.

        :param attributes: OAuth2 client credentials attributes returned by the API. The ``client_secret`` is never echoed.
        :type attributes: WebhooksOAuth2ClientCredentialsResponseAttributes

        :param id: The ID of the OAuth2 client credentials auth method.
        :type id: str

        :param type: OAuth2 client credentials resource type.
        :type type: WebhooksOAuth2ClientCredentialsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
