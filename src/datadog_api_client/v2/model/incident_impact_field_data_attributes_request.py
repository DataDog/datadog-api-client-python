# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_impact_field_choice import IncidentImpactFieldChoice
    from datadog_api_client.v2.model.incident_impact_field_value_type import IncidentImpactFieldValueType


class IncidentImpactFieldDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_field_choice import IncidentImpactFieldChoice
        from datadog_api_client.v2.model.incident_impact_field_value_type import IncidentImpactFieldValueType

        return {
            "display_name": (str,),
            "field_choices": ([IncidentImpactFieldChoice],),
            "field_type": (IncidentImpactFieldValueType,),
            "name": (str,),
            "tag_key": (str, none_type),
        }

    attribute_map = {
        "display_name": "display_name",
        "field_choices": "field_choices",
        "field_type": "field_type",
        "name": "name",
        "tag_key": "tag_key",
    }

    def __init__(
        self_,
        display_name: str,
        field_type: IncidentImpactFieldValueType,
        name: str,
        field_choices: Union[List[IncidentImpactFieldChoice], UnsetType] = unset,
        tag_key: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an impact field.

        :param display_name: The display name of the impact field.
        :type display_name: str

        :param field_choices: The choices for dropdown or multiselect fields.
        :type field_choices: [IncidentImpactFieldChoice], optional

        :param field_type: The type of an impact field.
        :type field_type: IncidentImpactFieldValueType

        :param name: The normalized name of the impact field (used as identifier).
        :type name: str

        :param tag_key: The tag key associated with the field (for metrictag type).
        :type tag_key: str, none_type, optional
        """
        if field_choices is not unset:
            kwargs["field_choices"] = field_choices
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        super().__init__(kwargs)

        self_.display_name = display_name
        self_.field_type = field_type
        self_.name = name
