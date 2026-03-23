# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.query_users_request_data import QueryUsersRequestData


class QueryUsersRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_users_request_data import QueryUsersRequestData

        return {
            "data": (QueryUsersRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[QueryUsersRequestData, UnsetType] = unset, **kwargs):
        """
        Request body for querying users with optional filtering, column selection, and sorting.

        :param data: The data object containing the resource type and attributes for querying users.
        :type data: QueryUsersRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
