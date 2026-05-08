# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TransportWebhookLogEmail(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "address": (str,),
            "domain": (str,),
            "subject": (str,),
            "type": ([str],),
        }

    attribute_map = {
        "address": "address",
        "domain": "domain",
        "subject": "subject",
        "type": "type",
    }

    def __init__(
        self_,
        address: Union[str, UnsetType] = unset,
        domain: Union[str, UnsetType] = unset,
        subject: Union[str, UnsetType] = unset,
        type: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The email address details.

        :param address: The recipient email address.
        :type address: str, optional

        :param domain: The recipient domain.
        :type domain: str, optional

        :param subject: The email subject line.
        :type subject: str, optional

        :param type: Email categorization tags applied by the transport provider (for example, "transactional", "marketing").
        :type type: [str], optional
        """
        if address is not unset:
            kwargs["address"] = address
        if domain is not unset:
            kwargs["domain"] = domain
        if subject is not unset:
            kwargs["subject"] = subject
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
