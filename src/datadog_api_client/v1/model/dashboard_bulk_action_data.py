# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardBulkActionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_resource_type import DashboardResourceType

        return {
            "id": (str,),
            "type": (DashboardResourceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id, type, *args, **kwargs):
        """
        Dashboard bulk action request data.

        :param id: Dashboard resource ID.
        :type id: str

        :param type: Dashboard resource type.
        :type type: DashboardResourceType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.id = id
        self_.type = type
