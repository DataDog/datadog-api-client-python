# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloudflare_api_token_api_token import CloudflareAPITokenApiToken
    from datadog_api_client.v2.model.cloudflare_api_token_type import CloudflareAPITokenType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class CloudflareAPIToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_api_token_api_token import CloudflareAPITokenApiToken
        from datadog_api_client.v2.model.cloudflare_api_token_type import CloudflareAPITokenType

        return {
            "api_token": (CloudflareAPITokenApiToken,),
            "type": (CloudflareAPITokenType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(
        self_,
        api_token: Union[CloudflareAPITokenApiToken, str, ActionConnectionAWSSecretsManagerReference],
        type: CloudflareAPITokenType,
        **kwargs,
    ):
        """
        The definition of the ``CloudflareAPIToken`` object.

        :param api_token: The ``CloudflareAPIToken`` ``api_token``.
        :type api_token: CloudflareAPITokenApiToken

        :param type: The definition of the ``CloudflareAPIToken`` object.
        :type type: CloudflareAPITokenType
        """
        super().__init__(kwargs)

        self_.api_token = api_token
        self_.type = type
