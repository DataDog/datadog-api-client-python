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
    from datadog_api_client.v2.model.facet_info_request_data_attributes_search import (
        FacetInfoRequestDataAttributesSearch,
    )
    from datadog_api_client.v2.model.facet_info_request_data_attributes_term_search import (
        FacetInfoRequestDataAttributesTermSearch,
    )


class FacetInfoRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.facet_info_request_data_attributes_search import (
            FacetInfoRequestDataAttributesSearch,
        )
        from datadog_api_client.v2.model.facet_info_request_data_attributes_term_search import (
            FacetInfoRequestDataAttributesTermSearch,
        )

        return {
            "facet_id": (str,),
            "limit": (int,),
            "search": (FacetInfoRequestDataAttributesSearch,),
            "term_search": (FacetInfoRequestDataAttributesTermSearch,),
        }

    attribute_map = {
        "facet_id": "facet_id",
        "limit": "limit",
        "search": "search",
        "term_search": "term_search",
    }

    def __init__(
        self_,
        facet_id: str,
        limit: int,
        search: Union[FacetInfoRequestDataAttributesSearch, UnsetType] = unset,
        term_search: Union[FacetInfoRequestDataAttributesTermSearch, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param facet_id:
        :type facet_id: str

        :param limit:
        :type limit: int

        :param search:
        :type search: FacetInfoRequestDataAttributesSearch, optional

        :param term_search:
        :type term_search: FacetInfoRequestDataAttributesTermSearch, optional
        """
        if search is not unset:
            kwargs["search"] = search
        if term_search is not unset:
            kwargs["term_search"] = term_search
        super().__init__(kwargs)

        self_.facet_id = facet_id
        self_.limit = limit
