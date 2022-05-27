# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardListDeleteItemsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_list_item_response import DashboardListItemResponse

        return {
            "deleted_dashboards_from_list": ([DashboardListItemResponse],),
        }

    attribute_map = {
        "deleted_dashboards_from_list": "deleted_dashboards_from_list",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing a list of deleted dashboards.

        :param deleted_dashboards_from_list: List of dashboards deleted from the dashboard list.
        :type deleted_dashboards_from_list: [DashboardListItemResponse], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardListDeleteItemsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
