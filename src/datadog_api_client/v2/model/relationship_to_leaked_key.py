# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_leaked_key_data import RelationshipToLeakedKeyData


class RelationshipToLeakedKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_leaked_key_data import RelationshipToLeakedKeyData

        return {
            "data": (RelationshipToLeakedKeyData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[RelationshipToLeakedKeyData, none_type], **kwargs):
        """
        Relationship to the leak the access token was found in. ``data`` is null when the access token has not been detected as leaked.

        :param data: Relationship to the leak the access token was found in.
        :type data: RelationshipToLeakedKeyData, none_type
        """
        super().__init__(kwargs)

        self_.data = data
