# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ListStreamRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [CaseStreamRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: CaseStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: CaseStreamRequestResponseFormat
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
        from datadog_api_client.v1_20270101.model.events_list_stream_request import EventsListStreamRequest
        from datadog_api_client.v1_20270101.model.issue_stream_request import IssueStreamRequest
        from datadog_api_client.v1_20270101.model.case_stream_request import CaseStreamRequest
        from datadog_api_client.v1_20270101.model.watchdog_alerts_request import WatchdogAlertsRequest
        from datadog_api_client.v1_20270101.model.incidents_stream_request import IncidentsStreamRequest
        from datadog_api_client.v1_20270101.model.database_recommendations_stream_request import (
            DatabaseRecommendationsStreamRequest,
        )
        from datadog_api_client.v1_20270101.model.apm_recommendations_stream_request import (
            ApmRecommendationsStreamRequest,
        )
        from datadog_api_client.v1_20270101.model.detection_rule_stream_request import DetectionRuleStreamRequest
        from datadog_api_client.v1_20270101.model.data_observability_assets_request import (
            DataObservabilityAssetsRequest,
        )
        from datadog_api_client.v1_20270101.model.dora_list_stream_request import DoraListStreamRequest

        return {
            "oneOf": [
                EventsListStreamRequest,
                IssueStreamRequest,
                CaseStreamRequest,
                WatchdogAlertsRequest,
                IncidentsStreamRequest,
                DatabaseRecommendationsStreamRequest,
                ApmRecommendationsStreamRequest,
                DetectionRuleStreamRequest,
                DataObservabilityAssetsRequest,
                DoraListStreamRequest,
            ],
        }
