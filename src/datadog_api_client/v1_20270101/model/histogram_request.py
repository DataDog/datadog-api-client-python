# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HistogramRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param number_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type number_format: WidgetNumberFormat, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: MetricsHistogramRequestQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: MetricsHistogramRequestRequestType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.metrics_histogram_request import MetricsHistogramRequest
        from datadog_api_client.v1_20270101.model.apm_stats_histogram_request import ApmStatsHistogramRequest
        from datadog_api_client.v1_20270101.model.apm_metrics_histogram_request import ApmMetricsHistogramRequest
        from datadog_api_client.v1_20270101.model.events_histogram_request import EventsHistogramRequest

        return {
            "oneOf": [
                MetricsHistogramRequest,
                ApmStatsHistogramRequest,
                ApmMetricsHistogramRequest,
                EventsHistogramRequest,
            ],
        }
