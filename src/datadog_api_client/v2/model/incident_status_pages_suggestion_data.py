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
    from datadog_api_client.v2.model.incident_status_pages_suggestion_data_attributes import (
        IncidentStatusPagesSuggestionDataAttributes,
    )
    from datadog_api_client.v2.model.incident_status_pages_suggestion_type import IncidentStatusPagesSuggestionType


class IncidentStatusPagesSuggestionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_status_pages_suggestion_data_attributes import (
            IncidentStatusPagesSuggestionDataAttributes,
        )
        from datadog_api_client.v2.model.incident_status_pages_suggestion_type import IncidentStatusPagesSuggestionType

        return {
            "attributes": (IncidentStatusPagesSuggestionDataAttributes,),
            "id": (str,),
            "type": (IncidentStatusPagesSuggestionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatusPagesSuggestionDataAttributes,
        id: str,
        type: IncidentStatusPagesSuggestionType,
        **kwargs,
    ):
        """
        Status pages suggestion data.

        :param attributes: Attributes of a status pages suggestion.
        :type attributes: IncidentStatusPagesSuggestionDataAttributes

        :param id: The suggestion title.
        :type id: str

        :param type: Incident status pages suggestion resource type.
        :type type: IncidentStatusPagesSuggestionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
