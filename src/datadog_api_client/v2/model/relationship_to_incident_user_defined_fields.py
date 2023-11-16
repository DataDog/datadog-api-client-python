# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_incident_user_defined_field_data import (
        RelationshipToIncidentUserDefinedFieldData,
    )


class RelationshipToIncidentUserDefinedFields(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_user_defined_field_data import (
            RelationshipToIncidentUserDefinedFieldData,
        )

        return {
            "data": ([RelationshipToIncidentUserDefinedFieldData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[RelationshipToIncidentUserDefinedFieldData], **kwargs):
        """
        Relationship to incident user defined fields.

        :param data: An array of user defined fields.
        :type data: [RelationshipToIncidentUserDefinedFieldData]
        """
        super().__init__(kwargs)

        self_.data = data
