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
    from datadog_api_client.v2.model.on_call_page_user_relationship_data import OnCallPageUserRelationshipData


class OnCallPageRespondersRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_user_relationship_data import OnCallPageUserRelationshipData

        return {
            "data": ([OnCallPageUserRelationshipData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[OnCallPageUserRelationshipData], UnsetType] = unset, **kwargs):
        """
        The users responding to the Page.

        :param data: The list of responders.
        :type data: [OnCallPageUserRelationshipData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
