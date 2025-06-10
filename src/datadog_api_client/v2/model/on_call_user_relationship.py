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
    from datadog_api_client.v2.model.on_call_user_relationship_data import OnCallUserRelationshipData


class OnCallUserRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_user_relationship_data import OnCallUserRelationshipData

        return {
            "data": (OnCallUserRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[OnCallUserRelationshipData, UnsetType] = unset, **kwargs):
        """
        The definition of ``OnCallUserRelationship`` object.

        :param data: The definition of ``OnCallUserRelationshipData`` object.
        :type data: OnCallUserRelationshipData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
