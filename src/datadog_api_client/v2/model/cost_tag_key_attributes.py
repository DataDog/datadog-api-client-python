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
    from datadog_api_client.v2.model.cost_tag_key_details import CostTagKeyDetails


class CostTagKeyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_details import CostTagKeyDetails

        return {
            "details": (CostTagKeyDetails,),
            "sources": ([str],),
            "value": (str,),
        }

    attribute_map = {
        "details": "details",
        "sources": "sources",
        "value": "value",
    }

    def __init__(self_, sources: List[str], value: str, details: Union[CostTagKeyDetails, UnsetType] = unset, **kwargs):
        """
        Attributes of a Cloud Cost Management tag key.

        :param details: Additional details for a Cloud Cost Management tag key, including its description and example tag values.
        :type details: CostTagKeyDetails, optional

        :param sources: List of sources that define this tag key.
        :type sources: [str]

        :param value: The tag key name.
        :type value: str
        """
        if details is not unset:
            kwargs["details"] = details
        super().__init__(kwargs)

        self_.sources = sources
        self_.value = value
