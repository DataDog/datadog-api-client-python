# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.transport_webhook_log_ip_attribute import TransportWebhookLogIpAttribute


class TransportWebhookLogNetworkIp(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.transport_webhook_log_ip_attribute import TransportWebhookLogIpAttribute

        return {
            "attributes": ([TransportWebhookLogIpAttribute],),
            "list": ([str],),
        }

    attribute_map = {
        "attributes": "attributes",
        "list": "list",
    }

    def __init__(
        self_,
        attributes: Union[List[TransportWebhookLogIpAttribute], UnsetType] = unset,
        list: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The IP address information.

        :param attributes: Per-IP attribute records, each pairing an IP address with the providers that observed it.
        :type attributes: [TransportWebhookLogIpAttribute], optional

        :param list: The list of IP addresses.
        :type list: [str], optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if list is not unset:
            kwargs["list"] = list
        super().__init__(kwargs)
