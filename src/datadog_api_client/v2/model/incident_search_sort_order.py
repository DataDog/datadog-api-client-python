# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class IncidentSearchSortOrder(StringEnum):
    """
    The ways searched incidents can be sorted.

    :param value: Must be one of ["created", "-created"].
    :type value: str
    """

    allowed_values = {
        "created",
        "-created",
    }
    CREATED_ASCENDING: ClassVar["IncidentSearchSortOrder"]
    CREATED_DESCENDING: ClassVar["IncidentSearchSortOrder"]


IncidentSearchSortOrder.CREATED_ASCENDING = IncidentSearchSortOrder("created")
IncidentSearchSortOrder.CREATED_DESCENDING = IncidentSearchSortOrder("-created")
