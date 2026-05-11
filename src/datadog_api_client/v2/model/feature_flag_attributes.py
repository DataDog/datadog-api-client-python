# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_environment import FeatureFlagEnvironment
    from datadog_api_client.v2.model.value_type import ValueType
    from datadog_api_client.v2.model.variant import Variant


class FeatureFlagAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_environment import FeatureFlagEnvironment
        from datadog_api_client.v2.model.value_type import ValueType
        from datadog_api_client.v2.model.variant import Variant

        return {
            "archived_at": (datetime, none_type),
            "created_at": (datetime,),
            "created_by": (UUID,),
            "description": (str,),
            "distribution_channel": (str,),
            "feature_flag_environments": ([FeatureFlagEnvironment],),
            "json_schema": (str, none_type),
            "key": (str,),
            "last_updated_by": (UUID,),
            "name": (str,),
            "require_approval": (bool,),
            "staleness_status": (str,),
            "tags": ([str],),
            "updated_at": (datetime,),
            "value_type": (ValueType,),
            "variants": ([Variant],),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "distribution_channel": "distribution_channel",
        "feature_flag_environments": "feature_flag_environments",
        "json_schema": "json_schema",
        "key": "key",
        "last_updated_by": "last_updated_by",
        "name": "name",
        "require_approval": "require_approval",
        "staleness_status": "staleness_status",
        "tags": "tags",
        "updated_at": "updated_at",
        "value_type": "value_type",
        "variants": "variants",
    }

    def __init__(
        self_,
        description: str,
        key: str,
        name: str,
        value_type: ValueType,
        variants: List[Variant],
        archived_at: Union[datetime, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[UUID, UnsetType] = unset,
        distribution_channel: Union[str, UnsetType] = unset,
        feature_flag_environments: Union[List[FeatureFlagEnvironment], UnsetType] = unset,
        json_schema: Union[str, none_type, UnsetType] = unset,
        last_updated_by: Union[UUID, UnsetType] = unset,
        require_approval: Union[bool, UnsetType] = unset,
        staleness_status: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a feature flag.

        :param archived_at: The timestamp when the feature flag was archived.
        :type archived_at: datetime, none_type, optional

        :param created_at: The timestamp when the feature flag was created.
        :type created_at: datetime, optional

        :param created_by: The ID of the user who created the feature flag.
        :type created_by: UUID, optional

        :param description: The description of the feature flag.
        :type description: str

        :param distribution_channel: Distribution channel for the feature flag.
        :type distribution_channel: str, optional

        :param feature_flag_environments: Environment-specific settings for the feature flag.
        :type feature_flag_environments: [FeatureFlagEnvironment], optional

        :param json_schema: JSON schema for validation when value_type is JSON.
        :type json_schema: str, none_type, optional

        :param key: The unique key of the feature flag.
        :type key: str

        :param last_updated_by: The ID of the user who last updated the feature flag.
        :type last_updated_by: UUID, optional

        :param name: The name of the feature flag.
        :type name: str

        :param require_approval: Indicates whether this feature flag requires approval for changes.
        :type require_approval: bool, optional

        :param staleness_status: Indicates the whether a feature flag is stale or not.
        :type staleness_status: str, optional

        :param tags: Tags associated with the feature flag.
        :type tags: [str], optional

        :param updated_at: The timestamp when the feature flag was last updated.
        :type updated_at: datetime, optional

        :param value_type: The type of values for the feature flag variants.
        :type value_type: ValueType

        :param variants: The variants of the feature flag.
        :type variants: [Variant]
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if distribution_channel is not unset:
            kwargs["distribution_channel"] = distribution_channel
        if feature_flag_environments is not unset:
            kwargs["feature_flag_environments"] = feature_flag_environments
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        if require_approval is not unset:
            kwargs["require_approval"] = require_approval
        if staleness_status is not unset:
            kwargs["staleness_status"] = staleness_status
        if tags is not unset:
            kwargs["tags"] = tags
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.description = description
        self_.key = key
        self_.name = name
        self_.value_type = value_type
        self_.variants = variants
