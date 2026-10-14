# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.experiments_patch_protocol_analysis_plan_input import (
        ExperimentsPatchProtocolAnalysisPlanInput,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_assignment_source_default_properties_items import (
        ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems,
    )
    from datadog_api_client.v2.model.experiments_patch_protocol_enforcement_input import (
        ExperimentsPatchProtocolEnforcementInput,
    )
    from datadog_api_client.v2.model.experiments_patch_protocol_exposure_schedule_input import (
        ExperimentsPatchProtocolExposureScheduleInput,
    )
    from datadog_api_client.v2.model.experiments_protocol_metric_group_input import ExperimentsProtocolMetricGroupInput
    from datadog_api_client.v2.model.experiments_protocol_targeting_rule_input import (
        ExperimentsProtocolTargetingRuleInput,
    )


class ExperimentsPatchExperimentProtocolRequestDataAttributes(ModelNormal):
    validations = {
        "assignment_source_id": {},
        "default_duration_days": {
            "inclusive_minimum": 0,
        },
        "environment_id": {},
        "metric_limit": {
            "inclusive_minimum": 0,
        },
        "minimum_duration_unit": {},
        "minimum_duration_value": {
            "inclusive_minimum": 0,
        },
        "name": {
            "min_length": 1,
        },
        "primary_metric_id": {},
        "subject_type_id": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_protocol_analysis_plan_input import (
            ExperimentsPatchProtocolAnalysisPlanInput,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_assignment_source_default_properties_items import (
            ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems,
        )
        from datadog_api_client.v2.model.experiments_patch_protocol_enforcement_input import (
            ExperimentsPatchProtocolEnforcementInput,
        )
        from datadog_api_client.v2.model.experiments_patch_protocol_exposure_schedule_input import (
            ExperimentsPatchProtocolExposureScheduleInput,
        )
        from datadog_api_client.v2.model.experiments_protocol_metric_group_input import (
            ExperimentsProtocolMetricGroupInput,
        )
        from datadog_api_client.v2.model.experiments_protocol_targeting_rule_input import (
            ExperimentsProtocolTargetingRuleInput,
        )

        return {
            "analysis_plan": (ExperimentsPatchProtocolAnalysisPlanInput,),
            "assignment_source_default_properties": (
                [ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems],
                none_type,
            ),
            "assignment_source_id": (str, none_type),
            "default_duration_days": (int, none_type),
            "description": (str, none_type),
            "enforcement": (ExperimentsPatchProtocolEnforcementInput,),
            "environment_id": (str, none_type),
            "exposure_schedule": (ExperimentsPatchProtocolExposureScheduleInput,),
            "is_duration_required_to_start": (bool, none_type),
            "is_equal_split_enforced": (bool, none_type),
            "is_metric_limit_enabled": (bool, none_type),
            "is_minimum_duration_enabled": (bool, none_type),
            "metric_groups": ([ExperimentsProtocolMetricGroupInput], none_type),
            "metric_limit": (int, none_type),
            "migration_metadata": (
                {
                    str: (
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
                    )
                },
                none_type,
            ),
            "minimum_duration_unit": (str, none_type),
            "minimum_duration_value": (int, none_type),
            "name": (str, none_type),
            "primary_metric_id": (str, none_type),
            "subject_type_id": (str, none_type),
            "targeting_rules": ([ExperimentsProtocolTargetingRuleInput], none_type),
        }

    attribute_map = {
        "analysis_plan": "analysis_plan",
        "assignment_source_default_properties": "assignment_source_default_properties",
        "assignment_source_id": "assignment_source_id",
        "default_duration_days": "default_duration_days",
        "description": "description",
        "enforcement": "enforcement",
        "environment_id": "environment_id",
        "exposure_schedule": "exposure_schedule",
        "is_duration_required_to_start": "is_duration_required_to_start",
        "is_equal_split_enforced": "is_equal_split_enforced",
        "is_metric_limit_enabled": "is_metric_limit_enabled",
        "is_minimum_duration_enabled": "is_minimum_duration_enabled",
        "metric_groups": "metric_groups",
        "metric_limit": "metric_limit",
        "migration_metadata": "migration_metadata",
        "minimum_duration_unit": "minimum_duration_unit",
        "minimum_duration_value": "minimum_duration_value",
        "name": "name",
        "primary_metric_id": "primary_metric_id",
        "subject_type_id": "subject_type_id",
        "targeting_rules": "targeting_rules",
    }

    def __init__(
        self_,
        analysis_plan: Union[ExperimentsPatchProtocolAnalysisPlanInput, none_type, UnsetType] = unset,
        assignment_source_default_properties: Union[
            List[ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems],
            none_type,
            UnsetType,
        ] = unset,
        assignment_source_id: Union[str, none_type, UnsetType] = unset,
        default_duration_days: Union[int, none_type, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        enforcement: Union[ExperimentsPatchProtocolEnforcementInput, none_type, UnsetType] = unset,
        environment_id: Union[str, none_type, UnsetType] = unset,
        exposure_schedule: Union[ExperimentsPatchProtocolExposureScheduleInput, none_type, UnsetType] = unset,
        is_duration_required_to_start: Union[bool, none_type, UnsetType] = unset,
        is_equal_split_enforced: Union[bool, none_type, UnsetType] = unset,
        is_metric_limit_enabled: Union[bool, none_type, UnsetType] = unset,
        is_minimum_duration_enabled: Union[bool, none_type, UnsetType] = unset,
        metric_groups: Union[List[ExperimentsProtocolMetricGroupInput], none_type, UnsetType] = unset,
        metric_limit: Union[int, none_type, UnsetType] = unset,
        migration_metadata: Union[Dict[str, Any], none_type, UnsetType] = unset,
        minimum_duration_unit: Union[str, none_type, UnsetType] = unset,
        minimum_duration_value: Union[int, none_type, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        primary_metric_id: Union[str, none_type, UnsetType] = unset,
        subject_type_id: Union[str, none_type, UnsetType] = unset,
        targeting_rules: Union[List[ExperimentsProtocolTargetingRuleInput], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Partial protocol update. Omitted attributes remain unchanged. Published protocols accept only name, description, and migration_metadata; archived protocols reject updates.

        :param analysis_plan: Partial statistical settings. Omitted fields remain unchanged. Null clears the whole plan. Null clears nullable fields; null or an empty string clears confidence_interval_method.
        :type analysis_plan: ExperimentsPatchProtocolAnalysisPlanInput, none_type, optional

        :param assignment_source_default_properties: Assignment properties. Omission or null preserves them; an array replaces them.
        :type assignment_source_default_properties: [ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems], none_type, optional

        :param assignment_source_id: ID of the assignment source selected by the protocol. Omission or null keeps the current value. An empty string clears it.
        :type assignment_source_id: str, none_type, optional

        :param default_duration_days: Default experiment duration supplied by the protocol, in days. Omission preserves it; null clears it. Sets analysis_plan.target_duration_days on experiments created from this protocol.
        :type default_duration_days: int, none_type, optional

        :param description: Description. Empty string clears it; omission or null preserves it.
        :type description: str, none_type, optional

        :param enforcement: Partial lock map. Omitted fields remain unchanged. Null clears the whole map. Empty or null field values become ``EDITABLE`` , except ``subject_type`` , ``flag_source`` , and ``confidence_interval_method`` , which remain ``LOCKED``.
        :type enforcement: ExperimentsPatchProtocolEnforcementInput, none_type, optional

        :param environment_id: ID of the feature flag environment used by the experiment. Omission or null keeps the current value. An empty string clears it.
        :type environment_id: str, none_type, optional

        :param exposure_schedule: Partial traffic schedule. Omitted fields remain unchanged. Null clears the whole schedule. Null clears nullable fields and rollout_steps; null sets strategy to an empty string and ``autostart`` to false.
        :type exposure_schedule: ExperimentsPatchProtocolExposureScheduleInput, none_type, optional

        :param is_duration_required_to_start: Whether the protocol requires a duration before an experiment can start. Omission or null preserves it.
        :type is_duration_required_to_start: bool, none_type, optional

        :param is_equal_split_enforced: Whether the protocol requires equal traffic allocation across variants. Omission or null preserves it.
        :type is_equal_split_enforced: bool, none_type, optional

        :param is_metric_limit_enabled: Whether the protocol limits the number of metrics. Omission or null preserves it.
        :type is_metric_limit_enabled: bool, none_type, optional

        :param is_minimum_duration_enabled: Whether the protocol enforces a minimum experiment duration. Omission or null preserves it.
        :type is_minimum_duration_enabled: bool, none_type, optional

        :param metric_groups: Metric groups. Omission or null preserves them; an array replaces them.
        :type metric_groups: [ExperimentsProtocolMetricGroupInput], none_type, optional

        :param metric_limit: Maximum number of metrics allowed by the protocol. Omission preserves it; null clears it.
        :type metric_limit: int, none_type, optional

        :param migration_metadata: Metadata for imported resources. Must encode to at most 4096 bytes. Null clears it; omission preserves it on update.
        :type migration_metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param minimum_duration_unit: Minimum duration unit, ``DAYS`` or ``WEEKS``. Empty string clears it. Omission or null preserves it.
        :type minimum_duration_unit: str, none_type, optional

        :param minimum_duration_value: Minimum experiment duration in the specified unit. Omission preserves it; null clears it.
        :type minimum_duration_value: int, none_type, optional

        :param name: Protocol name. Leading and trailing spaces are removed. The trimmed name must contain 1 to 255 characters.
        :type name: str, none_type, optional

        :param primary_metric_id: ID of the primary metric supplied by the protocol. Omission or null keeps the current value. An empty string clears it.
        :type primary_metric_id: str, none_type, optional

        :param subject_type_id: ID of the subject type used by this configuration. Omission or null keeps the current value. An empty string clears it.
        :type subject_type_id: str, none_type, optional

        :param targeting_rules: Targeting rules. Omission or null preserves them; an array replaces them.
        :type targeting_rules: [ExperimentsProtocolTargetingRuleInput], none_type, optional
        """
        if analysis_plan is not unset:
            kwargs["analysis_plan"] = analysis_plan
        if assignment_source_default_properties is not unset:
            kwargs["assignment_source_default_properties"] = assignment_source_default_properties
        if assignment_source_id is not unset:
            kwargs["assignment_source_id"] = assignment_source_id
        if default_duration_days is not unset:
            kwargs["default_duration_days"] = default_duration_days
        if description is not unset:
            kwargs["description"] = description
        if enforcement is not unset:
            kwargs["enforcement"] = enforcement
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if exposure_schedule is not unset:
            kwargs["exposure_schedule"] = exposure_schedule
        if is_duration_required_to_start is not unset:
            kwargs["is_duration_required_to_start"] = is_duration_required_to_start
        if is_equal_split_enforced is not unset:
            kwargs["is_equal_split_enforced"] = is_equal_split_enforced
        if is_metric_limit_enabled is not unset:
            kwargs["is_metric_limit_enabled"] = is_metric_limit_enabled
        if is_minimum_duration_enabled is not unset:
            kwargs["is_minimum_duration_enabled"] = is_minimum_duration_enabled
        if metric_groups is not unset:
            kwargs["metric_groups"] = metric_groups
        if metric_limit is not unset:
            kwargs["metric_limit"] = metric_limit
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if minimum_duration_unit is not unset:
            kwargs["minimum_duration_unit"] = minimum_duration_unit
        if minimum_duration_value is not unset:
            kwargs["minimum_duration_value"] = minimum_duration_value
        if name is not unset:
            kwargs["name"] = name
        if primary_metric_id is not unset:
            kwargs["primary_metric_id"] = primary_metric_id
        if subject_type_id is not unset:
            kwargs["subject_type_id"] = subject_type_id
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        super().__init__(kwargs)
