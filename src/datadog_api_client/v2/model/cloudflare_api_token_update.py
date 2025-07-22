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
    from datadog_api_client.v2.model.cloudflare_api_token_type import CloudflareAPITokenType


class CloudflareAPITokenUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloudflare_api_token_type import CloudflareAPITokenType

        return {
            "api_token": (str,),
            "type": (CloudflareAPITokenType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(self_, type: CloudflareAPITokenType, api_token: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of the ``CloudflareAPIToken`` object.

        :param api_token: The ``CloudflareAPITokenUpdate`` ``api_token``.
        :type api_token: str, optional

        :param type: The definition of the ``CloudflareAPIToken`` object.
        :type type: CloudflareAPITokenType
        """
        if api_token is not unset:
            kwargs["api_token"] = api_token
        super().__init__(kwargs)

        self_.type = type
