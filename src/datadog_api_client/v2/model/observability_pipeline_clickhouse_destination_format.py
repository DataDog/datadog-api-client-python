# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineClickhouseDestinationFormat(ModelSimple):
    """
    Insert format for events sent to ClickHouse.
        - `json_each_row`: Maps event fields to columns by name (ClickHouse `JSONEachRow`).
        - `json_as_object`: Inserts each event into a single `Object('json')` / `JSON` column (ClickHouse `JSONAsObject`).
        - `json_as_string`: Inserts each event into a single `String`-typed column as raw JSON (ClickHouse `JSONAsString`).
        - `arrow_stream`: Batches events using Apache Arrow IPC streaming format. Requires `batch_encoding`.

    :param value: Must be one of ["json_each_row", "json_as_object", "json_as_string", "arrow_stream"].
    :type value: str
    """

    allowed_values = {
        "json_each_row",
        "json_as_object",
        "json_as_string",
        "arrow_stream",
    }
    JSON_EACH_ROW: ClassVar["ObservabilityPipelineClickhouseDestinationFormat"]
    JSON_AS_OBJECT: ClassVar["ObservabilityPipelineClickhouseDestinationFormat"]
    JSON_AS_STRING: ClassVar["ObservabilityPipelineClickhouseDestinationFormat"]
    ARROW_STREAM: ClassVar["ObservabilityPipelineClickhouseDestinationFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineClickhouseDestinationFormat.JSON_EACH_ROW = ObservabilityPipelineClickhouseDestinationFormat(
    "json_each_row"
)
ObservabilityPipelineClickhouseDestinationFormat.JSON_AS_OBJECT = ObservabilityPipelineClickhouseDestinationFormat(
    "json_as_object"
)
ObservabilityPipelineClickhouseDestinationFormat.JSON_AS_STRING = ObservabilityPipelineClickhouseDestinationFormat(
    "json_as_string"
)
ObservabilityPipelineClickhouseDestinationFormat.ARROW_STREAM = ObservabilityPipelineClickhouseDestinationFormat(
    "arrow_stream"
)
