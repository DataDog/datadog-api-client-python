# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.saved_filter_creation_type import SavedFilterCreationType
    from datadog_api_client.v2.model.saved_filter_targeting_rule import SavedFilterTargetingRule


class SavedFilterAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_creation_type import SavedFilterCreationType
        from datadog_api_client.v2.model.saved_filter_targeting_rule import SavedFilterTargetingRule

        return {
            "archived_at": (datetime,),
            "created_at": (datetime,),
            "created_by": (str,),
            "creation_type": (SavedFilterCreationType,),
            "description": (str,),
            "migration_metadata": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "name": (str,),
            "targeting_rules": ([SavedFilterTargetingRule],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "created_at": "created_at",
        "created_by": "created_by",
        "creation_type": "creation_type",
        "description": "description",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "targeting_rules": "targeting_rules",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        creation_type: SavedFilterCreationType,
        name: str,
        targeting_rules: List[SavedFilterTargetingRule],
        updated_at: datetime,
        archived_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        Saved filter details, including the full targeting rules and conditions.

        :param archived_at: The time the saved filter was archived. Omitted when the filter is not archived.
        :type archived_at: datetime, optional

        :param created_at: The time the saved filter was created.
        :type created_at: datetime

        :param created_by: The ID of the user who created the saved filter.
        :type created_by: str

        :param creation_type: How the saved filter was authored. RULES indicates rule-based authoring and LIST indicates list import. Both types return targeting rules and conditions.
        :type creation_type: SavedFilterCreationType

        :param description: A description of the saved filter. Omitted when no description is set.
        :type description: str, optional

        :param migration_metadata: Optional JSON metadata supplied by migration tools for tracking the source of a saved filter.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: The name of the saved filter.
        :type name: str

        :param targeting_rules: Targeting rules combined with OR. Conditions within each rule are combined with AND. Both saved lists and saved rules use this structure.
        :type targeting_rules: [SavedFilterTargetingRule]

        :param updated_at: The time the saved filter was last updated.
        :type updated_at: datetime
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if description is not unset:
            kwargs["description"] = description
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.creation_type = creation_type
        self_.name = name
        self_.targeting_rules = targeting_rules
        self_.updated_at = updated_at
