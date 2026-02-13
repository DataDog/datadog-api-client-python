# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentsTimestampOverridesType(ModelSimple):
    """
    The JSON:API type for timestamp overrides.

    :param value: If omitted defaults to "incidents_timestamp_overrides". Must be one of ["incidents_timestamp_overrides"].
    :type value: str
    """

    allowed_values = {
        "incidents_timestamp_overrides",
    }
    INCIDENTS_TIMESTAMP_OVERRIDES: ClassVar["IncidentsTimestampOverridesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentsTimestampOverridesType.INCIDENTS_TIMESTAMP_OVERRIDES = IncidentsTimestampOverridesType(
    "incidents_timestamp_overrides"
)
