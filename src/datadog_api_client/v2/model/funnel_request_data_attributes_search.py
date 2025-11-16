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
    from datadog_api_client.v2.model.funnel_request_data_attributes_search_steps_items import (
        FunnelRequestDataAttributesSearchStepsItems,
    )


class FunnelRequestDataAttributesSearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_request_data_attributes_search_steps_items import (
            FunnelRequestDataAttributesSearchStepsItems,
        )

        return {
            "cross_session_filter": (str,),
            "query_string": (str,),
            "steps": ([FunnelRequestDataAttributesSearchStepsItems],),
            "subquery_id": (str,),
        }

    attribute_map = {
        "cross_session_filter": "cross_session_filter",
        "query_string": "query_string",
        "steps": "steps",
        "subquery_id": "subquery_id",
    }

    def __init__(
        self_,
        cross_session_filter: Union[str, UnsetType] = unset,
        query_string: Union[str, UnsetType] = unset,
        steps: Union[List[FunnelRequestDataAttributesSearchStepsItems], UnsetType] = unset,
        subquery_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param cross_session_filter:
        :type cross_session_filter: str, optional

        :param query_string:
        :type query_string: str, optional

        :param steps:
        :type steps: [FunnelRequestDataAttributesSearchStepsItems], optional

        :param subquery_id:
        :type subquery_id: str, optional
        """
        if cross_session_filter is not unset:
            kwargs["cross_session_filter"] = cross_session_filter
        if query_string is not unset:
            kwargs["query_string"] = query_string
        if steps is not unset:
            kwargs["steps"] = steps
        if subquery_id is not unset:
            kwargs["subquery_id"] = subquery_id
        super().__init__(kwargs)
