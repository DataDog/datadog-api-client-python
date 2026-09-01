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
    from datadog_api_client.v2.model.feature_flag_distribution_channel import FeatureFlagDistributionChannel
    from datadog_api_client.v2.model.create_feature_flag_staleness_status import CreateFeatureFlagStalenessStatus
    from datadog_api_client.v2.model.value_type import ValueType
    from datadog_api_client.v2.model.create_variant import CreateVariant


class CreateFeatureFlagAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_distribution_channel import FeatureFlagDistributionChannel
        from datadog_api_client.v2.model.create_feature_flag_staleness_status import CreateFeatureFlagStalenessStatus
        from datadog_api_client.v2.model.value_type import ValueType
        from datadog_api_client.v2.model.create_variant import CreateVariant

        return {
            "default_variant_key": (str, none_type),
            "description": (str,),
            "distribution_channel": (FeatureFlagDistributionChannel,),
            "json_schema": (str, none_type),
            "key": (str,),
            "name": (str,),
            "require_approval": (bool,),
            "staleness_status": (CreateFeatureFlagStalenessStatus,),
            "tags": ([str],),
            "value_type": (ValueType,),
            "variants": ([CreateVariant],),
        }

    attribute_map = {
        "default_variant_key": "default_variant_key",
        "description": "description",
        "distribution_channel": "distribution_channel",
        "json_schema": "json_schema",
        "key": "key",
        "name": "name",
        "require_approval": "require_approval",
        "staleness_status": "staleness_status",
        "tags": "tags",
        "value_type": "value_type",
        "variants": "variants",
    }

    def __init__(
        self_,
        key: str,
        name: str,
        value_type: ValueType,
        variants: List[CreateVariant],
        default_variant_key: Union[str, none_type, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        distribution_channel: Union[FeatureFlagDistributionChannel, UnsetType] = unset,
        json_schema: Union[str, none_type, UnsetType] = unset,
        require_approval: Union[bool, UnsetType] = unset,
        staleness_status: Union[CreateFeatureFlagStalenessStatus, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new feature flag.

        :param default_variant_key: The key of the default variant.
        :type default_variant_key: str, none_type, optional

        :param description: The description of the feature flag.
        :type description: str, optional

        :param distribution_channel: The distribution channel for the feature flag.
        :type distribution_channel: FeatureFlagDistributionChannel, optional

        :param json_schema: JSON schema for validation when value_type is JSON.
        :type json_schema: str, none_type, optional

        :param key: The unique key of the feature flag.
        :type key: str

        :param name: The name of the feature flag.
        :type name: str

        :param require_approval: Indicates whether this feature flag requires approval for changes.
        :type require_approval: bool, optional

        :param staleness_status: The staleness status for the feature flag at creation.
        :type staleness_status: CreateFeatureFlagStalenessStatus, optional

        :param tags: Tags associated with the feature flag.
        :type tags: [str], optional

        :param value_type: The type of values for the feature flag variants.
        :type value_type: ValueType

        :param variants: The variants of the feature flag.
        :type variants: [CreateVariant]
        """
        if default_variant_key is not unset:
            kwargs["default_variant_key"] = default_variant_key
        if description is not unset:
            kwargs["description"] = description
        if distribution_channel is not unset:
            kwargs["distribution_channel"] = distribution_channel
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        if require_approval is not unset:
            kwargs["require_approval"] = require_approval
        if staleness_status is not unset:
            kwargs["staleness_status"] = staleness_status
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.key = key
        self_.name = name
        self_.value_type = value_type
        self_.variants = variants
