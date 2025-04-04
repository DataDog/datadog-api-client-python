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
    from datadog_api_client.v2.model.layer_relationships_members import LayerRelationshipsMembers


class LayerRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.layer_relationships_members import LayerRelationshipsMembers

        return {
            "members": (LayerRelationshipsMembers,),
        }

    attribute_map = {
        "members": "members",
    }

    def __init__(self_, members: Union[LayerRelationshipsMembers, UnsetType] = unset, **kwargs):
        """
        Holds references to objects related to the Layer entity, such as its members.

        :param members: Holds an array of references to the members of a Layer, each containing member IDs.
        :type members: LayerRelationshipsMembers, optional
        """
        if members is not unset:
            kwargs["members"] = members
        super().__init__(kwargs)
