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
    from datadog_api_client.v2.model.cloudflare_global_api_token_auth_email import CloudflareGlobalAPITokenAuthEmail
    from datadog_api_client.v2.model.cloudflare_global_api_token_global_api_key import (
        CloudflareGlobalAPITokenGlobalApiKey,
    )
    from datadog_api_client.v2.model.cloudflare_global_api_token_type import CloudflareGlobalAPITokenType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class CloudflareGlobalAPIToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_global_api_token_auth_email import CloudflareGlobalAPITokenAuthEmail
        from datadog_api_client.v2.model.cloudflare_global_api_token_global_api_key import (
            CloudflareGlobalAPITokenGlobalApiKey,
        )
        from datadog_api_client.v2.model.cloudflare_global_api_token_type import CloudflareGlobalAPITokenType

        return {
            "auth_email": (CloudflareGlobalAPITokenAuthEmail,),
            "global_api_key": (CloudflareGlobalAPITokenGlobalApiKey,),
            "type": (CloudflareGlobalAPITokenType,),
        }

    attribute_map = {
        "auth_email": "auth_email",
        "global_api_key": "global_api_key",
        "type": "type",
    }

    def __init__(
        self_,
        auth_email: Union[CloudflareGlobalAPITokenAuthEmail, str, ActionConnectionAWSSecretsManagerReference],
        global_api_key: Union[CloudflareGlobalAPITokenGlobalApiKey, str, ActionConnectionAWSSecretsManagerReference],
        type: CloudflareGlobalAPITokenType,
        **kwargs,
    ):
        """
        The definition of the ``CloudflareGlobalAPIToken`` object.

        :param auth_email: The ``CloudflareGlobalAPIToken`` ``auth_email``.
        :type auth_email: CloudflareGlobalAPITokenAuthEmail

        :param global_api_key: The ``CloudflareGlobalAPIToken`` ``global_api_key``.
        :type global_api_key: CloudflareGlobalAPITokenGlobalApiKey

        :param type: The definition of the ``CloudflareGlobalAPIToken`` object.
        :type type: CloudflareGlobalAPITokenType
        """
        super().__init__(kwargs)

        self_.auth_email = auth_email
        self_.global_api_key = global_api_key
        self_.type = type
