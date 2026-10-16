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
    from datadog_api_client.v2.model.outcomes_response_data_item import OutcomesResponseDataItem
    from datadog_api_client.v2.model.outcomes_response_included_item import OutcomesResponseIncludedItem
    from datadog_api_client.v2.model.outcomes_response_links import OutcomesResponseLinks
    from datadog_api_client.v2.model.paginated_response_meta import PaginatedResponseMeta


class OutcomesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.outcomes_response_data_item import OutcomesResponseDataItem
        from datadog_api_client.v2.model.outcomes_response_included_item import OutcomesResponseIncludedItem
        from datadog_api_client.v2.model.outcomes_response_links import OutcomesResponseLinks
        from datadog_api_client.v2.model.paginated_response_meta import PaginatedResponseMeta

        return {
            "data": ([OutcomesResponseDataItem],),
            "included": ([OutcomesResponseIncludedItem],),
            "links": (OutcomesResponseLinks,),
            "meta": (PaginatedResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[OutcomesResponseDataItem], UnsetType] = unset,
        included: Union[List[OutcomesResponseIncludedItem], UnsetType] = unset,
        links: Union[OutcomesResponseLinks, UnsetType] = unset,
        meta: Union[PaginatedResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Scorecard outcomes - the result of a rule for a service.

        :param data: List of rule outcomes.
        :type data: [OutcomesResponseDataItem], optional

        :param included: Array of rule details.
        :type included: [OutcomesResponseIncludedItem], optional

        :param links: Pagination links for rule outcomes.
        :type links: OutcomesResponseLinks, optional

        :param meta: Pagination metadata.
        :type meta: PaginatedResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
