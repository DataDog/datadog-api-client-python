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
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_relationship_data import (
        WebhooksOAuth2ClientCredentialsRelationshipData,
    )


class WebhooksOAuth2ClientCredentialsRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_relationship_data import (
            WebhooksOAuth2ClientCredentialsRelationshipData,
        )

        return {
            "data": (WebhooksOAuth2ClientCredentialsRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[WebhooksOAuth2ClientCredentialsRelationshipData, UnsetType] = unset, **kwargs):
        """
        Relationship pointing to the OAuth2 client credentials resource for this auth method.

        :param data: Relationship data referencing an OAuth2 client credentials resource.
        :type data: WebhooksOAuth2ClientCredentialsRelationshipData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
