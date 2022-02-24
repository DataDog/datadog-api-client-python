# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.monitor_search_count import MonitorSearchCount
    from datadog_api_client.v1.model.monitor_search_count import MonitorSearchCount

    globals()["MonitorSearchCount"] = MonitorSearchCount
    globals()["MonitorSearchCount"] = MonitorSearchCount


class MonitorGroupSearchResponseCounts(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "status": (MonitorSearchCount,),
            "type": (MonitorSearchCount,),
        }

    attribute_map = {
        "status": "status",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        The counts of monitor groups per different criteria.

        :param status: Search facets.
        :type status: MonitorSearchCount, optional

        :param type: Search facets.
        :type type: MonitorSearchCount, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorGroupSearchResponseCounts, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
