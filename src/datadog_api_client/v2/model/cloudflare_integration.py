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
    from datadog_api_client.v2.model.cloudflare_credentials import CloudflareCredentials
    from datadog_api_client.v2.model.cloudflare_integration_type import CloudflareIntegrationType
    from datadog_api_client.v2.model.cloudflare_api_token import CloudflareAPIToken
    from datadog_api_client.v2.model.cloudflare_global_api_token import CloudflareGlobalAPIToken


class CloudflareIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_credentials import CloudflareCredentials
        from datadog_api_client.v2.model.cloudflare_integration_type import CloudflareIntegrationType

        return {
            "credentials": (CloudflareCredentials,),
            "type": (CloudflareIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        credentials: Union[CloudflareCredentials, CloudflareAPIToken, CloudflareGlobalAPIToken],
        type: CloudflareIntegrationType,
        **kwargs,
    ):
        """
        The definition of the ``CloudflareIntegration`` object.

        :param credentials: The definition of the ``CloudflareCredentials`` object.
        :type credentials: CloudflareCredentials

        :param type: The definition of the ``CloudflareIntegrationType`` object.
        :type type: CloudflareIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
