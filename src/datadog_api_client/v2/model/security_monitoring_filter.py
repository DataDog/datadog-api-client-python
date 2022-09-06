# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_filter_action import SecurityMonitoringFilterAction

        return {
            "action": (SecurityMonitoringFilterAction,),
            "query": (str,),
        }

    attribute_map = {
        "action": "action",
        "query": "query",
    }

    def __init__(self_, *args, **kwargs):
        """
        The rule's suppression filter.

        :param action: The type of filtering action.
        :type action: SecurityMonitoringFilterAction, optional

        :param query: Query for selecting logs to apply the filtering action.
        :type query: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
