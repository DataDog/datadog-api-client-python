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
    from datadog_api_client.v2.model.on_call_page_author_relationship_data import OnCallPageAuthorRelationshipData


class OnCallPageAuthorRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_author_relationship_data import OnCallPageAuthorRelationshipData

        return {
            "data": (OnCallPageAuthorRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[OnCallPageAuthorRelationshipData, none_type, UnsetType] = unset, **kwargs):
        """
        Reference to the entity that performed an action on the Page.

        :param data: Reference to the author of a Page action.
        :type data: OnCallPageAuthorRelationshipData, none_type, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
