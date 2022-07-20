# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuditLogsSearchEventsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.audit_logs_query_filter import AuditLogsQueryFilter
        from datadog_api_client.v2.model.audit_logs_query_options import AuditLogsQueryOptions
        from datadog_api_client.v2.model.audit_logs_query_page_options import AuditLogsQueryPageOptions
        from datadog_api_client.v2.model.audit_logs_sort import AuditLogsSort

        return {
            "filter": (AuditLogsQueryFilter,),
            "options": (AuditLogsQueryOptions,),
            "page": (AuditLogsQueryPageOptions,),
            "sort": (AuditLogsSort,),
        }

    attribute_map = {
        "filter": "filter",
        "options": "options",
        "page": "page",
        "sort": "sort",
    }

    def __init__(self, *args, **kwargs):
        """
        The request for a Audit Logs events list.

        :param filter: Search and filter query settings.
        :type filter: AuditLogsQueryFilter, optional

        :param options: Global query options that are used during the query.
            Note: Specify either timezone or time offset, not both. Otherwise, the query fails.
        :type options: AuditLogsQueryOptions, optional

        :param page: Paging attributes for listing events.
        :type page: AuditLogsQueryPageOptions, optional

        :param sort: Sort parameters when querying events.
        :type sort: AuditLogsSort, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuditLogsSearchEventsRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
