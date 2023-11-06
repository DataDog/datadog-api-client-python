# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class CloudflareAccountType(StringEnum):
    """
    The JSON:API type for this API. Should always be `cloudflare-accounts`.

    :param value: If omitted defaults to "cloudflare-accounts". Must be one of ["cloudflare-accounts"].
    :type value: str
    """

    allowed_values = {
        "cloudflare-accounts",
    }
    CLOUDFLARE_ACCOUNTS: ClassVar["CloudflareAccountType"]


CloudflareAccountType.CLOUDFLARE_ACCOUNTS = CloudflareAccountType("cloudflare-accounts")
