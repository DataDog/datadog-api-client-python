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
    from datadog_api_client.v2.model.on_call_page_target_relationship_data_type import (
        OnCallPageTargetRelationshipDataType,
    )


class OnCallPageTargetRelationshipData(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_target_relationship_data_type import (
            OnCallPageTargetRelationshipDataType,
        )

        return {
            "id": (str,),
            "type": (OnCallPageTargetRelationshipDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: OnCallPageTargetRelationshipDataType, **kwargs):
        """
        Reference to the target of the page.

        :param id: The ID of the target.
        :type id: str

        :param type: The resource type of the page target.
        :type type: OnCallPageTargetRelationshipDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
