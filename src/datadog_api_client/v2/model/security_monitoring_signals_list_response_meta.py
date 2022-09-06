# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalsListResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signals_list_response_meta_page import (
            SecurityMonitoringSignalsListResponseMetaPage,
        )

        return {
            "page": (SecurityMonitoringSignalsListResponseMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, *args, **kwargs):
        """
        Meta attributes.

        :param page: Paging attributes.
        :type page: SecurityMonitoringSignalsListResponseMetaPage, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
