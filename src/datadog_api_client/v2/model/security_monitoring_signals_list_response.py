# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal import SecurityMonitoringSignal
        from datadog_api_client.v2.model.security_monitoring_signals_list_response_links import (
            SecurityMonitoringSignalsListResponseLinks,
        )
        from datadog_api_client.v2.model.security_monitoring_signals_list_response_meta import (
            SecurityMonitoringSignalsListResponseMeta,
        )

        return {
            "data": ([SecurityMonitoringSignal],),
            "links": (SecurityMonitoringSignalsListResponseLinks,),
            "meta": (SecurityMonitoringSignalsListResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        The response object with all security signals matching the request
        and pagination information.

        :param data: An array of security signals matching the request.
        :type data: [SecurityMonitoringSignal], optional

        :param links: Links attributes.
        :type links: SecurityMonitoringSignalsListResponseLinks, optional

        :param meta: Meta attributes.
        :type meta: SecurityMonitoringSignalsListResponseMeta, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalsListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
