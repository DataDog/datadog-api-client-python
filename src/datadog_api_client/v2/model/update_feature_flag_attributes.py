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
    from datadog_api_client.v2.model.update_feature_flag_staleness_status import UpdateFeatureFlagStalenessStatus


class UpdateFeatureFlagAttributes(ModelNormal):
    validations = {
        "tags": {
            "max_items": 100,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_distribution_channel import FeatureFlagDistributionChannel
        from datadog_api_client.v2.model.update_feature_flag_staleness_status import UpdateFeatureFlagStalenessStatus

        return {
            "description": (str,),
            "distribution_channel": (FeatureFlagDistributionChannel,),
            "json_schema": (str, none_type),
            "name": (str,),
            "staleness_status": (UpdateFeatureFlagStalenessStatus,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "distribution_channel": "distribution_channel",
        "json_schema": "json_schema",
        "name": "name",
        "staleness_status": "staleness_status",
        "tags": "tags",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        distribution_channel: Union[FeatureFlagDistributionChannel, UnsetType] = unset,
        json_schema: Union[str, none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        staleness_status: Union[UpdateFeatureFlagStalenessStatus, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a feature flag.

        :param description: The description of the feature flag.
        :type description: str, optional

        :param distribution_channel: The distribution channel for the feature flag.
        :type distribution_channel: FeatureFlagDistributionChannel, optional

        :param json_schema: JSON schema for validation when value_type is JSON.
        :type json_schema: str, none_type, optional

        :param name: The name of the feature flag.
        :type name: str, optional

        :param staleness_status: The lifecycle to set. ``ACTIVE`` makes the flag temporary; ``PERMANENT`` excludes it from
            staleness detection. Either value clears any snooze; omit the field to keep the lifecycle.
            Do not copy the top-level ``staleness_status`` from a response into this field: that legacy
            response field is always ``ACTIVE``.
        :type staleness_status: UpdateFeatureFlagStalenessStatus, optional

        :param tags: Tags associated with the feature flag. This field replaces the full set of
            existing tags; omit it to leave tags unchanged, or pass an empty array to
            clear all tags. The owning team is set by including a tag of the form
            ``team:<team-handle>`` in this array.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if distribution_channel is not unset:
            kwargs["distribution_channel"] = distribution_channel
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        if name is not unset:
            kwargs["name"] = name
        if staleness_status is not unset:
            kwargs["staleness_status"] = staleness_status
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
