# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_target_relationship_data import OnCallPageTargetRelationshipData


class OnCallPageTargetRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_target_relationship_data import OnCallPageTargetRelationshipData

        return {
            "data": (OnCallPageTargetRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[OnCallPageTargetRelationshipData, none_type, UnsetType] = unset, **kwargs):
        """
        The team, user, or cross-organization handle that was paged.

        :param data: Reference to the target of the page.
        :type data: OnCallPageTargetRelationshipData, none_type, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
