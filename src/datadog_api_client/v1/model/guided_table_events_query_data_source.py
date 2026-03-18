# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableEventsQueryDataSource(ModelSimple):
    """
    Events data source.

    :param value: Must be one of ["logs", "rum", "spans", "ci_pipelines", "events", "product_analytics"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "rum",
        "spans",
        "ci_pipelines",
        "events",
        "product_analytics",
    }
    LOGS: ClassVar["GuidedTableEventsQueryDataSource"]
    RUM: ClassVar["GuidedTableEventsQueryDataSource"]
    SPANS: ClassVar["GuidedTableEventsQueryDataSource"]
    CI_PIPELINES: ClassVar["GuidedTableEventsQueryDataSource"]
    EVENTS: ClassVar["GuidedTableEventsQueryDataSource"]
    PRODUCT_ANALYTICS: ClassVar["GuidedTableEventsQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableEventsQueryDataSource.LOGS = GuidedTableEventsQueryDataSource("logs")
GuidedTableEventsQueryDataSource.RUM = GuidedTableEventsQueryDataSource("rum")
GuidedTableEventsQueryDataSource.SPANS = GuidedTableEventsQueryDataSource("spans")
GuidedTableEventsQueryDataSource.CI_PIPELINES = GuidedTableEventsQueryDataSource("ci_pipelines")
GuidedTableEventsQueryDataSource.EVENTS = GuidedTableEventsQueryDataSource("events")
GuidedTableEventsQueryDataSource.PRODUCT_ANALYTICS = GuidedTableEventsQueryDataSource("product_analytics")
