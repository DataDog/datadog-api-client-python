# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentSearchIncidentsSortOrder(ModelSimple):
    """
    The ways searched incidents can be sorted.

    :param value: Must be one of ["created", "-created", "modified", "-modified"].
    :type value: str
    """

    allowed_values = {
        "created",
        "-created",
        "modified",
        "-modified",
    }
    CREATED_ASCENDING: ClassVar["IncidentSearchIncidentsSortOrder"]
    CREATED_DESCENDING: ClassVar["IncidentSearchIncidentsSortOrder"]
    MODIFIED_ASCENDING: ClassVar["IncidentSearchIncidentsSortOrder"]
    MODIFIED_DESCENDING: ClassVar["IncidentSearchIncidentsSortOrder"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentSearchIncidentsSortOrder.CREATED_ASCENDING = IncidentSearchIncidentsSortOrder("created")
IncidentSearchIncidentsSortOrder.CREATED_DESCENDING = IncidentSearchIncidentsSortOrder("-created")
IncidentSearchIncidentsSortOrder.MODIFIED_ASCENDING = IncidentSearchIncidentsSortOrder("modified")
IncidentSearchIncidentsSortOrder.MODIFIED_DESCENDING = IncidentSearchIncidentsSortOrder("-modified")
