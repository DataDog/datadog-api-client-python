# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WebhooksOAuth2ClientCredentialsType(ModelSimple):
    """
    OAuth2 client credentials resource type.

    :param value: If omitted defaults to "webhooks-auth-method-oauth2-client-credentials". Must be one of ["webhooks-auth-method-oauth2-client-credentials"].
    :type value: str
    """

    allowed_values = {
        "webhooks-auth-method-oauth2-client-credentials",
    }
    WEBHOOKS_AUTH_METHOD_OAUTH2_CLIENT_CREDENTIALS: ClassVar["WebhooksOAuth2ClientCredentialsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WebhooksOAuth2ClientCredentialsType.WEBHOOKS_AUTH_METHOD_OAUTH2_CLIENT_CREDENTIALS = (
    WebhooksOAuth2ClientCredentialsType("webhooks-auth-method-oauth2-client-credentials")
)
