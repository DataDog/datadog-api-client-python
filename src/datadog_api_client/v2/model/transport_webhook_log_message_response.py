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


class TransportWebhookLogMessageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enhanced_smtp_code": (str,),
            "reason": (str,),
            "smtp_code": (str,),
        }

    attribute_map = {
        "enhanced_smtp_code": "enhanced_smtp_code",
        "reason": "reason",
        "smtp_code": "smtp_code",
    }

    def __init__(
        self_,
        enhanced_smtp_code: Union[str, UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        smtp_code: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The SMTP response information.

        :param enhanced_smtp_code: The enhanced SMTP status code.
        :type enhanced_smtp_code: str, optional

        :param reason: The SMTP response message.
        :type reason: str, optional

        :param smtp_code: The SMTP status code.
        :type smtp_code: str, optional
        """
        if enhanced_smtp_code is not unset:
            kwargs["enhanced_smtp_code"] = enhanced_smtp_code
        if reason is not unset:
            kwargs["reason"] = reason
        if smtp_code is not unset:
            kwargs["smtp_code"] = smtp_code
        super().__init__(kwargs)
