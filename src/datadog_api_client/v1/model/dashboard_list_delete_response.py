# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardListDeleteResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "deleted_dashboard_list_id": (int,),
        }

    attribute_map = {
        "deleted_dashboard_list_id": "deleted_dashboard_list_id",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Deleted dashboard details.

        :param deleted_dashboard_list_id: ID of the deleted dashboard list.
        :type deleted_dashboard_list_id: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardListDeleteResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
