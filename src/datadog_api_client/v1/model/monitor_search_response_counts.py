# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorSearchResponseCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_search_count import MonitorSearchCount

        return {
            "muted": (MonitorSearchCount,),
            "status": (MonitorSearchCount,),
            "tag": (MonitorSearchCount,),
            "type": (MonitorSearchCount,),
        }

    attribute_map = {
        "muted": "muted",
        "status": "status",
        "tag": "tag",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The counts of monitors per different criteria.

        :param muted: Search facets.
        :type muted: MonitorSearchCount, optional

        :param status: Search facets.
        :type status: MonitorSearchCount, optional

        :param tag: Search facets.
        :type tag: MonitorSearchCount, optional

        :param type: Search facets.
        :type type: MonitorSearchCount, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorSearchResponseCounts, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
