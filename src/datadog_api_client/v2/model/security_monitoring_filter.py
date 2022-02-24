# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.security_monitoring_filter_action import SecurityMonitoringFilterAction

    globals()["SecurityMonitoringFilterAction"] = SecurityMonitoringFilterAction


class SecurityMonitoringFilter(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "action": (SecurityMonitoringFilterAction,),
            "query": (str,),
        }

    attribute_map = {
        "action": "action",
        "query": "query",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        The rule's suppression filter.

        :param action: The type of filtering action.
        :type action: SecurityMonitoringFilterAction, optional

        :param query: Query for selecting logs to apply the filtering action.
        :type query: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringFilter, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
