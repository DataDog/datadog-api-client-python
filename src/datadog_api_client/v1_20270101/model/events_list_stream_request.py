# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class EventsListStreamRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [EventPlatformStreamRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: EventsPlatformListStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: EventPlatformStreamRequestResponseFormat
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
        from datadog_api_client.v1_20270101.model.event_platform_stream_request import EventPlatformStreamRequest
        from datadog_api_client.v1_20270101.model.logs_stream_request import LogsStreamRequest
        from datadog_api_client.v1_20270101.model.logs_pattern_stream_request import LogsPatternStreamRequest
        from datadog_api_client.v1_20270101.model.logs_transaction_stream_request import LogsTransactionStreamRequest
        from datadog_api_client.v1_20270101.model.audit_stream_request import AuditStreamRequest
        from datadog_api_client.v1_20270101.model.trace_stream_request import TraceStreamRequest
        from datadog_api_client.v1_20270101.model.errors_stream_request import ErrorsStreamRequest
        from datadog_api_client.v1_20270101.model.event_stream_request import EventStreamRequest
        from datadog_api_client.v1_20270101.model.event_pattern_stream_request import EventPatternStreamRequest
        from datadog_api_client.v1_20270101.model.security_runtime_pattern_stream_request import (
            SecurityRuntimePatternStreamRequest,
        )
        from datadog_api_client.v1_20270101.model.rum_stream_request import RumStreamRequest
        from datadog_api_client.v1_20270101.model.recommendations_stream_request import RecommendationsStreamRequest
        from datadog_api_client.v1_20270101.model.security_runtime_stream_request import SecurityRuntimeStreamRequest

        return {
            "oneOf": [
                EventPlatformStreamRequest,
                LogsStreamRequest,
                LogsPatternStreamRequest,
                LogsTransactionStreamRequest,
                AuditStreamRequest,
                TraceStreamRequest,
                ErrorsStreamRequest,
                EventStreamRequest,
                EventPatternStreamRequest,
                SecurityRuntimePatternStreamRequest,
                RumStreamRequest,
                RecommendationsStreamRequest,
                SecurityRuntimeStreamRequest,
            ],
        }
