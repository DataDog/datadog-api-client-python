# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WebhooksAuthMethodProtocol(ModelSimple):
    """
    Authentication protocol used by the auth method.

    :param value: If omitted defaults to "oauth2-client-credentials". Must be one of ["oauth2-client-credentials"].
    :type value: str
    """

    allowed_values = {
        "oauth2-client-credentials",
    }
    OAUTH2_CLIENT_CREDENTIALS: ClassVar["WebhooksAuthMethodProtocol"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WebhooksAuthMethodProtocol.OAUTH2_CLIENT_CREDENTIALS = WebhooksAuthMethodProtocol("oauth2-client-credentials")
