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
    from datadog_api_client.v2.model.webhooks_auth_method_protocol import WebhooksAuthMethodProtocol


class WebhooksAuthMethodAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_auth_method_protocol import WebhooksAuthMethodProtocol

        return {
            "protocol": (WebhooksAuthMethodProtocol,),
        }

    attribute_map = {
        "protocol": "protocol",
    }

    def __init__(self_, protocol: Union[WebhooksAuthMethodProtocol, UnsetType] = unset, **kwargs):
        """
        Attributes of a webhooks auth method.

        :param protocol: Authentication protocol used by the auth method.
        :type protocol: WebhooksAuthMethodProtocol, optional
        """
        if protocol is not unset:
            kwargs["protocol"] = protocol
        super().__init__(kwargs)
