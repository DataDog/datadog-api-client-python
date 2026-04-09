# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecureEmbedGetResponseType(ModelSimple):
    """
    Resource type for secure embed get responses.

    :param value: If omitted defaults to "secure_embed_get_response". Must be one of ["secure_embed_get_response"].
    :type value: str
    """

    allowed_values = {
        "secure_embed_get_response",
    }
    SECURE_EMBED_GET_RESPONSE: ClassVar["SecureEmbedGetResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecureEmbedGetResponseType.SECURE_EMBED_GET_RESPONSE = SecureEmbedGetResponseType("secure_embed_get_response")
