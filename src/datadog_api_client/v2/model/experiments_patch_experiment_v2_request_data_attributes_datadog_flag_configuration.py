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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_datadog_flag_configuration_targeting_rules_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems,
    )


class ExperimentsPatchExperimentV2RequestDataAttributesDatadogFlagConfiguration(ModelNormal):
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
            "environment_id": (str,),
            "feature_flag_id": (str,),
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
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint, none_type, UnsetType
        ] = unset,
        environment_id: Union[str, UnsetType] = unset,
        feature_flag_id: Union[str, UnsetType] = unset,
        reset_on_feature_flag_change: Union[bool, UnsetType] = unset,
        targeting_rules: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Feature flag, environment, and targeting configuration for the experiment.

        :param entry_point: Datadog measure and filters used to select analyzed subjects.
        :type entry_point: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPoint, none_type, optional

        :param environment_id: ID of the feature flag environment used by the experiment.
        :type environment_id: str, optional

        :param feature_flag_id: ID of the feature flag linked to the experiment.
        :type feature_flag_id: str, optional

        :param reset_on_feature_flag_change: Set true to replace an existing draft allocation when feature_flag_id changes. The replacement resets all flag-bound randomization state.
        :type reset_on_feature_flag_change: bool, optional

        :param targeting_rules: Omit to keep the stored rules. Use an empty array to remove targeting rules.
        :type targeting_rules: [ExperimentsCreateExperimentV2RequestDataAttributesDatadogFlagConfigurationTargetingRulesItems], optional
        """
        if entry_point is not unset:
            kwargs["entry_point"] = entry_point
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if feature_flag_id is not unset:
            kwargs["feature_flag_id"] = feature_flag_id
        if reset_on_feature_flag_change is not unset:
            kwargs["reset_on_feature_flag_change"] = reset_on_feature_flag_change
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        super().__init__(kwargs)
