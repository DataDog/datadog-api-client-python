# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.shared_dashboard_included_user_attributes import (
        SharedDashboardIncludedUserAttributes,
    )
    from datadog_api_client.v2.model.user_resource_type import UserResourceType


class SharedDashboardIncludedUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shared_dashboard_included_user_attributes import (
            SharedDashboardIncludedUserAttributes,
        )
        from datadog_api_client.v2.model.user_resource_type import UserResourceType

        return {
            "attributes": (SharedDashboardIncludedUserAttributes,),
            "id": (str,),
            "type": (UserResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SharedDashboardIncludedUserAttributes, id: str, type: UserResourceType, **kwargs):
        """
        Included user resource.

        :param attributes: Attributes of the included user.
        :type attributes: SharedDashboardIncludedUserAttributes

        :param id: ID of the user.
        :type id: str

        :param type: User resource type.
        :type type: UserResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
