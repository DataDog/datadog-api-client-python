# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ContainerImageMetaPageType(StringEnum):
    """
    Type of Container Image pagination.

    :param value: If omitted defaults to "cursor_limit". Must be one of ["cursor_limit"].
    :type value: str
    """

    allowed_values = {
        "cursor_limit",
    }
    CURSOR_LIMIT: ClassVar["ContainerImageMetaPageType"]


ContainerImageMetaPageType.CURSOR_LIMIT = ContainerImageMetaPageType("cursor_limit")
