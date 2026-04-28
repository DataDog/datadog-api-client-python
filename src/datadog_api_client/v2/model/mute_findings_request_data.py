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
    from datadog_api_client.v2.model.mute_findings_request_data_attributes import MuteFindingsRequestDataAttributes
    from datadog_api_client.v2.model.mute_findings_request_data_relationships import (
        MuteFindingsRequestDataRelationships,
    )
    from datadog_api_client.v2.model.mute_data_type import MuteDataType


class MuteFindingsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_findings_request_data_attributes import MuteFindingsRequestDataAttributes
        from datadog_api_client.v2.model.mute_findings_request_data_relationships import (
            MuteFindingsRequestDataRelationships,
        )
        from datadog_api_client.v2.model.mute_data_type import MuteDataType

        return {
            "attributes": (MuteFindingsRequestDataAttributes,),
            "id": (str,),
            "relationships": (MuteFindingsRequestDataRelationships,),
            "type": (MuteDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: MuteFindingsRequestDataAttributes,
        relationships: MuteFindingsRequestDataRelationships,
        type: MuteDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the mute request.

        :param attributes: Attributes of the mute request.
        :type attributes: MuteFindingsRequestDataAttributes

        :param id: Unique identifier of the mute request.
        :type id: str, optional

        :param relationships: Relationships of the mute request.
        :type relationships: MuteFindingsRequestDataRelationships

        :param type: Mute resource type.
        :type type: MuteDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
