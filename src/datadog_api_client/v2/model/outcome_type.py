# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class OutcomeType(StringEnum):
    """
    The JSON:API type for an outcome.

    :param value: If omitted defaults to "outcome". Must be one of ["outcome"].
    :type value: str
    """

    allowed_values = {
        "outcome",
    }
    OUTCOME: ClassVar["OutcomeType"]


OutcomeType.OUTCOME = OutcomeType("outcome")
