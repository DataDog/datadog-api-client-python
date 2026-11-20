# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentsStreamQueryDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "incidents_stream". Must be one of ["incidents_stream"].
    :type value: str
    """

    allowed_values = {
        "incidents_stream",
    }
    INCIDENTS_STREAM: ClassVar["IncidentsStreamQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentsStreamQueryDataSource.INCIDENTS_STREAM = IncidentsStreamQueryDataSource("incidents_stream")
