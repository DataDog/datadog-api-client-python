# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_dashboard_id": (str,),
        }

    attribute_map = {
        "deleted_dashboard_id": "deleted_dashboard_id",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response from the delete dashboard call.

        :param deleted_dashboard_id: ID of the deleted dashboard.
        :type deleted_dashboard_id: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
