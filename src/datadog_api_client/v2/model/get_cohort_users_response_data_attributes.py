# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_cohort_users_response_data_attributes_users_items import (
        GetCohortUsersResponseDataAttributesUsersItems,
    )


class GetCohortUsersResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_users_response_data_attributes_users_items import (
            GetCohortUsersResponseDataAttributesUsersItems,
        )

        return {
            "users": ([GetCohortUsersResponseDataAttributesUsersItems],),
        }

    attribute_map = {
        "users": "users",
    }

    def __init__(
        self_, users: Union[List[GetCohortUsersResponseDataAttributesUsersItems], UnsetType] = unset, **kwargs
    ):
        """


        :param users:
        :type users: [GetCohortUsersResponseDataAttributesUsersItems], optional
        """
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
