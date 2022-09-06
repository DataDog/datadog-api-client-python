# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorGroupSearchResponseCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_search_count import MonitorSearchCount

        return {
            "status": (MonitorSearchCount,),
            "type": (MonitorSearchCount,),
        }

    attribute_map = {
        "status": "status",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        The counts of monitor groups per different criteria.

        :param status: Search facets.
        :type status: MonitorSearchCount, optional

        :param type: Search facets.
        :type type: MonitorSearchCount, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
