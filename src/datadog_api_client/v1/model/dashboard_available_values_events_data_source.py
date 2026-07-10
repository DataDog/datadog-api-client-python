# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardAvailableValuesEventsDataSource(ModelSimple):
    """
    The events-based data source for the query.

    :param value: Must be one of ["spans", "logs", "rum"].
    :type value: str
    """

    allowed_values = {
        "spans",
        "logs",
        "rum",
    }
    SPANS: ClassVar["DashboardAvailableValuesEventsDataSource"]
    LOGS: ClassVar["DashboardAvailableValuesEventsDataSource"]
    RUM: ClassVar["DashboardAvailableValuesEventsDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardAvailableValuesEventsDataSource.SPANS = DashboardAvailableValuesEventsDataSource("spans")
DashboardAvailableValuesEventsDataSource.LOGS = DashboardAvailableValuesEventsDataSource("logs")
DashboardAvailableValuesEventsDataSource.RUM = DashboardAvailableValuesEventsDataSource("rum")
