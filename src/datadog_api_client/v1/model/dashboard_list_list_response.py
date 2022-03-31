# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.dashboard_list import DashboardList

    globals()["DashboardList"] = DashboardList


class DashboardListListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "dashboard_lists": ([DashboardList],),
        }

    attribute_map = {
        "dashboard_lists": "dashboard_lists",
    }

    def __init__(self, *args, **kwargs):
        """
        Information on your dashboard lists.

        :param dashboard_lists: List of all your dashboard lists.
        :type dashboard_lists: [DashboardList], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardListListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
