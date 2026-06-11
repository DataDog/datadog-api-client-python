# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_context_entity import EntityContextEntity


class SingleEntityContextResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_entity import EntityContextEntity

        return {
            "data": (EntityContextEntity,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: EntityContextEntity, **kwargs):
        """
        Response from the single entity context endpoint, containing the matching entity.

        :param data: A single entity returned by the entity context endpoint.
        :type data: EntityContextEntity
        """
        super().__init__(kwargs)

        self_.data = data
