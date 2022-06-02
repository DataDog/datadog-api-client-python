# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardListAddItemsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_list_item_response import DashboardListItemResponse

        return {
            "added_dashboards_to_list": ([DashboardListItemResponse],),
        }

    attribute_map = {
        "added_dashboards_to_list": "added_dashboards_to_list",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing a list of added dashboards.

        :param added_dashboards_to_list: List of dashboards added to the dashboard list.
        :type added_dashboards_to_list: [DashboardListItemResponse], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardListAddItemsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
