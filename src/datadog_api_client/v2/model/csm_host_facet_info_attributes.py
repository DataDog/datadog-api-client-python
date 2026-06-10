# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.csm_host_facet_info_item import CsmHostFacetInfoItem


class CsmHostFacetInfoAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_host_facet_info_item import CsmHostFacetInfoItem

        return {
            "items": ([CsmHostFacetInfoItem],),
        }

    attribute_map = {
        "items": "items",
    }

    def __init__(self_, items: List[CsmHostFacetInfoItem], **kwargs):
        """
        Attributes of a facet info response, containing the value distribution for the requested facet.

        :param items: The list of facet value entries for the current page.
        :type items: [CsmHostFacetInfoItem]
        """
        super().__init__(kwargs)

        self_.items = items
