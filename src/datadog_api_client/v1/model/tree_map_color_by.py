# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class TreeMapColorBy(StringEnum):
    """
    (deprecated) The attribute formerly used to determine color in the widget.

    :param value: If omitted defaults to "user". Must be one of ["user"].
    :type value: str
    """

    allowed_values = {
        "user",
    }
    USER: ClassVar["TreeMapColorBy"]


TreeMapColorBy.USER = TreeMapColorBy("user")
