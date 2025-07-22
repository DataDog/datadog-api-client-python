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
    from datadog_api_client.v2.model.cloudflare_credentials_update import CloudflareCredentialsUpdate
    from datadog_api_client.v2.model.cloudflare_integration_type import CloudflareIntegrationType
    from datadog_api_client.v2.model.cloudflare_api_token_update import CloudflareAPITokenUpdate
    from datadog_api_client.v2.model.cloudflare_global_api_token_update import CloudflareGlobalAPITokenUpdate


class CloudflareIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_credentials_update import CloudflareCredentialsUpdate
        from datadog_api_client.v2.model.cloudflare_integration_type import CloudflareIntegrationType

        return {
            "credentials": (CloudflareCredentialsUpdate,),
            "type": (CloudflareIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: CloudflareIntegrationType,
        credentials: Union[
            CloudflareCredentialsUpdate, CloudflareAPITokenUpdate, CloudflareGlobalAPITokenUpdate, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of the ``CloudflareIntegrationUpdate`` object.

        :param credentials: The definition of the ``CloudflareCredentialsUpdate`` object.
        :type credentials: CloudflareCredentialsUpdate, optional

        :param type: The definition of the ``CloudflareIntegrationType`` object.
        :type type: CloudflareIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
