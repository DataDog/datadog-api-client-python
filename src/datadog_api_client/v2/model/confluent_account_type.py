# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ConfluentAccountType(StringEnum):
    """
    The JSON:API type for this API. Should always be `confluent-cloud-accounts`.

    :param value: If omitted defaults to "confluent-cloud-accounts". Must be one of ["confluent-cloud-accounts"].
    :type value: str
    """

    allowed_values = {
        "confluent-cloud-accounts",
    }
    CONFLUENT_CLOUD_ACCOUNTS: ClassVar["ConfluentAccountType"]


ConfluentAccountType.CONFLUENT_CLOUD_ACCOUNTS = ConfluentAccountType("confluent-cloud-accounts")
