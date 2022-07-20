# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalListRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_list_request_filter import (
            SecurityMonitoringSignalListRequestFilter,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_list_request_page import (
            SecurityMonitoringSignalListRequestPage,
        )
        from datadog_api_client.v2.model.security_monitoring_signals_sort import SecurityMonitoringSignalsSort

        return {
            "filter": (SecurityMonitoringSignalListRequestFilter,),
            "page": (SecurityMonitoringSignalListRequestPage,),
            "sort": (SecurityMonitoringSignalsSort,),
        }

    attribute_map = {
        "filter": "filter",
        "page": "page",
        "sort": "sort",
    }

    def __init__(self, *args, **kwargs):
        """
        The request for a security signal list.

        :param filter: Search filters for listing security signals.
        :type filter: SecurityMonitoringSignalListRequestFilter, optional

        :param page: The paging attributes for listing security signals.
        :type page: SecurityMonitoringSignalListRequestPage, optional

        :param sort: The sort parameters used for querying security signals.
        :type sort: SecurityMonitoringSignalsSort, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalListRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
