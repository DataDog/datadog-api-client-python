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
    from datadog_api_client.v2.model.restriction_query_with_relationships import RestrictionQueryWithRelationships
    from datadog_api_client.v2.model.restriction_query_response_included_item import (
        RestrictionQueryResponseIncludedItem,
    )
    from datadog_api_client.v2.model.restriction_query_role import RestrictionQueryRole


class RestrictionQueryWithRelationshipsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_query_with_relationships import RestrictionQueryWithRelationships
        from datadog_api_client.v2.model.restriction_query_response_included_item import (
            RestrictionQueryResponseIncludedItem,
        )

        return {
            "data": (RestrictionQueryWithRelationships,),
            "included": ([RestrictionQueryResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[RestrictionQueryWithRelationships, UnsetType] = unset,
        included: Union[List[Union[RestrictionQueryResponseIncludedItem, RestrictionQueryRole]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing information about a single restriction query.

        :param data: Restriction query object returned by the API.
        :type data: RestrictionQueryWithRelationships, optional

        :param included: Array of objects related to the restriction query.
        :type included: [RestrictionQueryResponseIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
