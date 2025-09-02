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
    from datadog_api_client.v2.model.cloudflare_global_api_token_type import CloudflareGlobalAPITokenType


class CloudflareGlobalAPITokenUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_global_api_token_type import CloudflareGlobalAPITokenType

        return {
            "auth_email": (str,),
            "global_api_key": (str,),
            "type": (CloudflareGlobalAPITokenType,),
        }

    attribute_map = {
        "auth_email": "auth_email",
        "global_api_key": "global_api_key",
        "type": "type",
    }

    def __init__(
        self_,
        type: CloudflareGlobalAPITokenType,
        auth_email: Union[str, UnsetType] = unset,
        global_api_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``CloudflareGlobalAPIToken`` object.

        :param auth_email: The ``CloudflareGlobalAPITokenUpdate`` ``auth_email``.
        :type auth_email: str, optional

        :param global_api_key: The ``CloudflareGlobalAPITokenUpdate`` ``global_api_key``.
        :type global_api_key: str, optional

        :param type: The definition of the ``CloudflareGlobalAPIToken`` object.
        :type type: CloudflareGlobalAPITokenType
        """
        if auth_email is not unset:
            kwargs["auth_email"] = auth_email
        if global_api_key is not unset:
            kwargs["global_api_key"] = global_api_key
        super().__init__(kwargs)

        self_.type = type
