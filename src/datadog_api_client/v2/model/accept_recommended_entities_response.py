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
    from datadog_api_client.v2.model.accept_recommended_entity_item import AcceptRecommendedEntityItem


class AcceptRecommendedEntitiesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.accept_recommended_entity_item import AcceptRecommendedEntityItem

        return {
            "data": ([AcceptRecommendedEntityItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[AcceptRecommendedEntityItem], UnsetType] = unset, **kwargs):
        """
        Response after accepting recommended entities.

        :param data: Array of accepted entity data.
        :type data: [AcceptRecommendedEntityItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
