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
    from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query_time_frame import (
        QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame,
    )


class QueryEventFilteredUsersRequestDataAttributesEventQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query_time_frame import (
            QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame,
        )

        return {
            "query": (str,),
            "time_frame": (QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame,),
        }

    attribute_map = {
        "query": "query",
        "time_frame": "time_frame",
    }

    def __init__(
        self_,
        query: Union[str, UnsetType] = unset,
        time_frame: Union[QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param query:
        :type query: str, optional

        :param time_frame:
        :type time_frame: QueryEventFilteredUsersRequestDataAttributesEventQueryTimeFrame, optional
        """
        if query is not unset:
            kwargs["query"] = query
        if time_frame is not unset:
            kwargs["time_frame"] = time_frame
        super().__init__(kwargs)
