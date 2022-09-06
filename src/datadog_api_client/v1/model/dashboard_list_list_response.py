# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardListListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_list import DashboardList

        return {
            "dashboard_lists": ([DashboardList],),
        }

    attribute_map = {
        "dashboard_lists": "dashboard_lists",
    }

    def __init__(self_, *args, **kwargs):
        """
        Information on your dashboard lists.

        :param dashboard_lists: List of all your dashboard lists.
        :type dashboard_lists: [DashboardList], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
