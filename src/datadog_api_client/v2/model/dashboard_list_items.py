# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardListItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_list_item import DashboardListItem

        return {
            "dashboards": ([DashboardListItem],),
            "total": (int,),
        }

    attribute_map = {
        "dashboards": "dashboards",
        "total": "total",
    }
    read_only_vars = {
        "total",
    }

    def __init__(self, dashboards, *args, **kwargs):
        """
        Dashboards within a list.

        :param dashboards: List of dashboards in the dashboard list.
        :type dashboards: [DashboardListItem]

        :param total: Number of dashboards in the dashboard list.
        :type total: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.dashboards = dashboards

    @classmethod
    def _from_openapi_data(cls, dashboards, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardListItems, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.dashboards = dashboards
        return self
