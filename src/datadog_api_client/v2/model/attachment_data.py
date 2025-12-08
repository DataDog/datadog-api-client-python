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
    from datadog_api_client.v2.model.attachment_data_attributes import AttachmentDataAttributes
    from datadog_api_client.v2.model.attachment_data_relationships import AttachmentDataRelationships
    from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType


class AttachmentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attachment_data_attributes import AttachmentDataAttributes
        from datadog_api_client.v2.model.attachment_data_relationships import AttachmentDataRelationships
        from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType

        return {
            "attributes": (AttachmentDataAttributes,),
            "id": (str,),
            "relationships": (AttachmentDataRelationships,),
            "type": (IncidentAttachmentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AttachmentDataAttributes,
        id: str,
        relationships: AttachmentDataRelationships,
        type: IncidentAttachmentType,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: AttachmentDataAttributes

        :param id:
        :type id: str

        :param relationships:
        :type relationships: AttachmentDataRelationships

        :param type: The incident attachment resource type.
        :type type: IncidentAttachmentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
