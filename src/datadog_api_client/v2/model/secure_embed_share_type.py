# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecureEmbedShareType(ModelSimple):
    """
    The type of share. Always `secure_embed`.

    :param value: If omitted defaults to "secure_embed". Must be one of ["secure_embed"].
    :type value: str
    """

    allowed_values = {
        "secure_embed",
    }
    SECURE_EMBED: ClassVar["SecureEmbedShareType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecureEmbedShareType.SECURE_EMBED = SecureEmbedShareType("secure_embed")
