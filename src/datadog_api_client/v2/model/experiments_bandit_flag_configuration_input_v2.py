# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_targeting_rule import ExperimentsTargetingRule


class ExperimentsBanditFlagConfigurationInputV2(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_targeting_rule import ExperimentsTargetingRule

        return {
            "environment_id": (UUID,),
            "feature_flag_id": (UUID,),
            "targeting_rules": ([ExperimentsTargetingRule],),
        }

    attribute_map = {
        "environment_id": "environment_id",
        "feature_flag_id": "feature_flag_id",
        "targeting_rules": "targeting_rules",
    }

    def __init__(
        self_,
        environment_id: Union[UUID, UnsetType] = unset,
        feature_flag_id: Union[UUID, UnsetType] = unset,
        targeting_rules: Union[List[ExperimentsTargetingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        The flag and environment the bandit serves on, and who it serves there. The server chooses the rule's ``allocation_key``. On create, ``feature_flag_id`` and ``environment_id`` are required, and ``null`` is the same as omitting it. On update, omitted fields are unchanged, and ``null`` takes a draft off its flag, which also clears its variants and scheduled end. Moving a draft to another flag clears its variants unless the request sets them. Only a draft can change it.

        :param environment_id: The environment the bandit serves in.
        :type environment_id: UUID, optional

        :param feature_flag_id: The flag the bandit serves through.
        :type feature_flag_id: UUID, optional

        :param targeting_rules: Who the bandit serves. When empty, the bandit serves everyone in the environment.
        :type targeting_rules: [ExperimentsTargetingRule], optional
        """
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if feature_flag_id is not unset:
            kwargs["feature_flag_id"] = feature_flag_id
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        super().__init__(kwargs)
