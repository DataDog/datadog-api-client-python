# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TransportWebhookLogMessageAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "delivered_with_tls": (str,),
        }

    attribute_map = {
        "delivered_with_tls": "delivered_with_tls",
    }

    def __init__(self_, delivered_with_tls: Union[str, UnsetType] = unset, **kwargs):
        """
        The message authentication details.

        :param delivered_with_tls: The TLS version or negotiation information.
        :type delivered_with_tls: str, optional
        """
        if delivered_with_tls is not unset:
            kwargs["delivered_with_tls"] = delivered_with_tls
        super().__init__(kwargs)
