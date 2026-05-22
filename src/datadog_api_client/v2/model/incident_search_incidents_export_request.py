# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentSearchIncidentsExportRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fields": ([str],),
            "query": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "query": "query",
    }

    def __init__(self_, fields: List[str], query: str, **kwargs):
        """
        Request to export incidents as CSV.

        :param fields: The list of fields to include in the export.
        :type fields: [str]

        :param query: The search query to filter incidents for export.
        :type query: str
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.query = query
