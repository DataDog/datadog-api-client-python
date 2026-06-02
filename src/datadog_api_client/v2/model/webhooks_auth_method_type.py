# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WebhooksAuthMethodType(ModelSimple):
    """
    Webhooks auth method resource type.

    :param value: If omitted defaults to "webhooks-auth-method". Must be one of ["webhooks-auth-method"].
    :type value: str
    """

    allowed_values = {
        "webhooks-auth-method",
    }
    WEBHOOKS_AUTH_METHOD: ClassVar["WebhooksAuthMethodType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WebhooksAuthMethodType.WEBHOOKS_AUTH_METHOD = WebhooksAuthMethodType("webhooks-auth-method")
