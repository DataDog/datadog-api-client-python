# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_targeting_rule import ExperimentsTargetingRule


class ExperimentsBanditFlagConfigurationV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_targeting_rule import ExperimentsTargetingRule

        return {
            "allocation_key": (str,),
            "environment_id": (UUID,),
            "feature_flag_id": (UUID,),
            "targeting_rules": ([ExperimentsTargetingRule],),
        }

    attribute_map = {
        "allocation_key": "allocation_key",
        "environment_id": "environment_id",
        "feature_flag_id": "feature_flag_id",
        "targeting_rules": "targeting_rules",
    }

    def __init__(
        self_,
        allocation_key: str,
        environment_id: UUID,
        feature_flag_id: UUID,
        targeting_rules: List[ExperimentsTargetingRule],
        **kwargs,
    ):
        """
        The flag rule the bandit serves through. Absent until a draft is put on a flag, and when the caller lacks feature flag and environment read permissions ( ``meta.warnings`` then says so).

        :param allocation_key: The key of the bandit's rule on the flag. Exposures log it.
        :type allocation_key: str

        :param environment_id: The environment the bandit serves in.
        :type environment_id: UUID

        :param feature_flag_id: The flag the bandit serves through.
        :type feature_flag_id: UUID

        :param targeting_rules: Who the bandit serves. Empty serves everyone in the environment.
        :type targeting_rules: [ExperimentsTargetingRule]
        """
        super().__init__(kwargs)

        self_.allocation_key = allocation_key
        self_.environment_id = environment_id
        self_.feature_flag_id = feature_flag_id
        self_.targeting_rules = targeting_rules
