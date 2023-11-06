# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class IncidentSearchResultsType(StringEnum):
    """
    Incident search result type.

    :param value: If omitted defaults to "incidents_search_results". Must be one of ["incidents_search_results"].
    :type value: str
    """

    allowed_values = {
        "incidents_search_results",
    }
    INCIDENTS_SEARCH_RESULTS: ClassVar["IncidentSearchResultsType"]


IncidentSearchResultsType.INCIDENTS_SEARCH_RESULTS = IncidentSearchResultsType("incidents_search_results")
