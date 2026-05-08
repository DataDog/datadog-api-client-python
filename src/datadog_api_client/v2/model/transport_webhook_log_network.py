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
    from datadog_api_client.v2.model.transport_webhook_log_network_ip import TransportWebhookLogNetworkIp


class TransportWebhookLogNetwork(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.transport_webhook_log_network_ip import TransportWebhookLogNetworkIp

        return {
            "ip": (TransportWebhookLogNetworkIp,),
        }

    attribute_map = {
        "ip": "ip",
    }

    def __init__(self_, ip: Union[TransportWebhookLogNetworkIp, UnsetType] = unset, **kwargs):
        """
        The network information for the event.

        :param ip: The IP address information.
        :type ip: TransportWebhookLogNetworkIp, optional
        """
        if ip is not unset:
            kwargs["ip"] = ip
        super().__init__(kwargs)
