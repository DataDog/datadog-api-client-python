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
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_relationship import (
        WebhooksOAuth2ClientCredentialsRelationship,
    )


class WebhooksAuthMethodRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_relationship import (
            WebhooksOAuth2ClientCredentialsRelationship,
        )

        return {
            "oauth2_client_credentials": (WebhooksOAuth2ClientCredentialsRelationship,),
        }

    attribute_map = {
        "oauth2_client_credentials": "oauth2-client-credentials",
    }

    def __init__(
        self_,
        oauth2_client_credentials: Union[WebhooksOAuth2ClientCredentialsRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of a webhooks auth method to its protocol-specific resource.

        :param oauth2_client_credentials: Relationship pointing to the OAuth2 client credentials resource for this auth method.
        :type oauth2_client_credentials: WebhooksOAuth2ClientCredentialsRelationship, optional
        """
        if oauth2_client_credentials is not unset:
            kwargs["oauth2_client_credentials"] = oauth2_client_credentials
        super().__init__(kwargs)
