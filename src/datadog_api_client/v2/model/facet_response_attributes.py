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
    from datadog_api_client.v2.model.facet_item import FacetItem


class FacetResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.facet_item import FacetItem

        return {
            "items": ([FacetItem],),
            "key": (str,),
            "name": (str,),
        }

    attribute_map = {
        "items": "items",
        "key": "key",
        "name": "name",
    }

    def __init__(self_, items: List[FacetItem], key: str, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Facet attributes.

        :param items: Array of facet values.
        :type items: [FacetItem]

        :param key: The key of the facet.
        :type key: str

        :param name: The display name of the facet.
        :type name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.items = items
        self_.key = key
