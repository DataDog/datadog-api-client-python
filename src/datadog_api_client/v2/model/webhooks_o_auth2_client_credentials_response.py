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
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response_data import (
        WebhooksOAuth2ClientCredentialsResponseData,
    )


class WebhooksOAuth2ClientCredentialsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response_data import (
            WebhooksOAuth2ClientCredentialsResponseData,
        )

        return {
            "data": (WebhooksOAuth2ClientCredentialsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: WebhooksOAuth2ClientCredentialsResponseData, **kwargs):
        """
        Response containing an OAuth2 client credentials auth method.

        :param data: OAuth2 client credentials data from a response.
        :type data: WebhooksOAuth2ClientCredentialsResponseData
        """
        super().__init__(kwargs)

        self_.data = data
