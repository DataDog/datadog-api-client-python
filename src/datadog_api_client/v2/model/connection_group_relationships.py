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
    from datadog_api_client.v2.model.created_by_relationship import CreatedByRelationship


class ConnectionGroupRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.created_by_relationship import CreatedByRelationship

        return {
            "created_by": (CreatedByRelationship,),
        }

    attribute_map = {
        "created_by": "created_by",
    }

    def __init__(self_, created_by: Union[CreatedByRelationship, UnsetType] = unset, **kwargs):
        """
        Relationships for a connection group.

        :param created_by: Relationship to the user who created the resource.
        :type created_by: CreatedByRelationship, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        super().__init__(kwargs)
