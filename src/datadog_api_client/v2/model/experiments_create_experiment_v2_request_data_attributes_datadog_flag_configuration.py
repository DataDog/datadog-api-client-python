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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_datadog_flag_configuration_targeting_rules_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems,
    )


class ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfiguration(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point import (
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_datadog_flag_configuration_targeting_rules_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems,
        )

        return {
            "entry_point": (ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint,),
            "environment_id": (UUID,),
            "feature_flag_id": (UUID,),
            "reset_on_feature_flag_change": (bool,),
            "targeting_rules": (
                [ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems],
            ),
        }

    attribute_map = {
        "entry_point": "entry_point",
        "environment_id": "environment_id",
        "feature_flag_id": "feature_flag_id",
        "reset_on_feature_flag_change": "reset_on_feature_flag_change",
        "targeting_rules": "targeting_rules",
    }

    def __init__(
        self_,
        entry_point: Union[
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint, none_type
        ],
        environment_id: UUID,
        feature_flag_id: UUID,
        targeting_rules: List[
            ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems
        ],
        reset_on_feature_flag_change: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Feature flag, environment, and targeting configuration for a Datadog experiment.

        :param entry_point: Datadog measure and filters used to select analyzed subjects.
        :type entry_point: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint, none_type

        :param environment_id: Identifier of the feature flag environment.
        :type environment_id: UUID

        :param feature_flag_id: Identifier of the Datadog feature flag used by the experiment.
        :type feature_flag_id: UUID

        :param reset_on_feature_flag_change: Accepted on create but has no effect.
        :type reset_on_feature_flag_change: bool, optional

        :param targeting_rules: Use an empty array when no targeting rules apply.
        :type targeting_rules: [ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems]
        """
        if reset_on_feature_flag_change is not unset:
            kwargs["reset_on_feature_flag_change"] = reset_on_feature_flag_change
        super().__init__(kwargs)

        self_.entry_point = entry_point
        self_.environment_id = environment_id
        self_.feature_flag_id = feature_flag_id
        self_.targeting_rules = targeting_rules
