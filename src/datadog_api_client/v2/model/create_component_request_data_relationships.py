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
    from datadog_api_client.v2.model.create_component_request_data_relationships_group import (
        CreateComponentRequestDataRelationshipsGroup,
    )


class CreateComponentRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_component_request_data_relationships_group import (
            CreateComponentRequestDataRelationshipsGroup,
        )

        return {
            "group": (CreateComponentRequestDataRelationshipsGroup,),
        }

    attribute_map = {
        "group": "group",
    }

    def __init__(self_, group: Union[CreateComponentRequestDataRelationshipsGroup, UnsetType] = unset, **kwargs):
        """


        :param group:
        :type group: CreateComponentRequestDataRelationshipsGroup, optional
        """
        if group is not unset:
            kwargs["group"] = group
        super().__init__(kwargs)
