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
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_update_attributes import (
        WebhooksOAuth2ClientCredentialsUpdateAttributes,
    )
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import WebhooksOAuth2ClientCredentialsType


class WebhooksOAuth2ClientCredentialsUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_update_attributes import (
            WebhooksOAuth2ClientCredentialsUpdateAttributes,
        )
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_type import (
            WebhooksOAuth2ClientCredentialsType,
        )

        return {
            "attributes": (WebhooksOAuth2ClientCredentialsUpdateAttributes,),
            "type": (WebhooksOAuth2ClientCredentialsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: WebhooksOAuth2ClientCredentialsUpdateAttributes,
        type: WebhooksOAuth2ClientCredentialsType,
        **kwargs,
    ):
        """
        OAuth2 client credentials data for an update request.

        :param attributes: OAuth2 client credentials attributes for an update request.
        :type attributes: WebhooksOAuth2ClientCredentialsUpdateAttributes

        :param type: OAuth2 client credentials resource type.
        :type type: WebhooksOAuth2ClientCredentialsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
