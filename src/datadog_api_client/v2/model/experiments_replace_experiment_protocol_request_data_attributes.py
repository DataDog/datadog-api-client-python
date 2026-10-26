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
    from datadog_api_client.v2.model.experiments_protocol_analysis_plan_input import (
        ExperimentsProtocolAnalysisPlanInput,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_assignment_source_default_properties_items import (
        ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems,
    )
    from datadog_api_client.v2.model.experiments_replace_protocol_enforcement_input import (
        ExperimentsReplaceProtocolEnforcementInput,
    )
    from datadog_api_client.v2.model.experiments_protocol_exposure_schedule_input import (
        ExperimentsProtocolExposureScheduleInput,
    )
    from datadog_api_client.v2.model.experiments_protocol_metric_group_input import ExperimentsProtocolMetricGroupInput
    from datadog_api_client.v2.model.experiments_protocol_targeting_rule_input import (
        ExperimentsProtocolTargetingRuleInput,
    )


class ExperimentsReplaceExperimentProtocolRequestDataAttributes(ModelNormal):
    validations = {
        "default_duration_days": {
            "inclusive_minimum": 0,
        },
        "metric_limit": {
            "inclusive_minimum": 0,
        },
        "minimum_duration_unit": {},
        "minimum_duration_value": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_protocol_analysis_plan_input import (
            ExperimentsProtocolAnalysisPlanInput,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_assignment_source_default_properties_items import (
            ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems,
        )
        from datadog_api_client.v2.model.experiments_replace_protocol_enforcement_input import (
            ExperimentsReplaceProtocolEnforcementInput,
        )
        from datadog_api_client.v2.model.experiments_protocol_exposure_schedule_input import (
            ExperimentsProtocolExposureScheduleInput,
        )
        from datadog_api_client.v2.model.experiments_protocol_metric_group_input import (
            ExperimentsProtocolMetricGroupInput,
        )
        from datadog_api_client.v2.model.experiments_protocol_targeting_rule_input import (
            ExperimentsProtocolTargetingRuleInput,
        )

        return {
            "analysis_plan": (ExperimentsProtocolAnalysisPlanInput,),
            "assignment_source_default_properties": (
                [ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems],
            ),
            "assignment_source_id": (UUID, none_type),
            "default_duration_days": (int, none_type),
            "enforcement": (ExperimentsReplaceProtocolEnforcementInput,),
            "environment_id": (UUID, none_type),
            "exposure_schedule": (ExperimentsProtocolExposureScheduleInput,),
            "is_duration_required_to_start": (bool,),
            "is_equal_split_enforced": (bool,),
            "is_metric_limit_enabled": (bool,),
            "is_minimum_duration_enabled": (bool,),
            "metric_groups": ([ExperimentsProtocolMetricGroupInput],),
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
            "primary_metric_id": (UUID, none_type),
            "subject_type_id": (UUID,),
            "targeting_rules": ([ExperimentsProtocolTargetingRuleInput],),
        }

    attribute_map = {
        "analysis_plan": "analysis_plan",
        "assignment_source_default_properties": "assignment_source_default_properties",
        "assignment_source_id": "assignment_source_id",
        "default_duration_days": "default_duration_days",
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
        "primary_metric_id": "primary_metric_id",
        "subject_type_id": "subject_type_id",
        "targeting_rules": "targeting_rules",
    }

    def __init__(
        self_,
        is_duration_required_to_start: bool,
        is_equal_split_enforced: bool,
        is_metric_limit_enabled: bool,
        is_minimum_duration_enabled: bool,
        metric_groups: List[ExperimentsProtocolMetricGroupInput],
        subject_type_id: UUID,
        analysis_plan: Union[ExperimentsProtocolAnalysisPlanInput, none_type, UnsetType] = unset,
        assignment_source_default_properties: Union[
            List[ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems], UnsetType
        ] = unset,
        assignment_source_id: Union[UUID, none_type, UnsetType] = unset,
        default_duration_days: Union[int, none_type, UnsetType] = unset,
        enforcement: Union[ExperimentsReplaceProtocolEnforcementInput, UnsetType] = unset,
        environment_id: Union[UUID, none_type, UnsetType] = unset,
        exposure_schedule: Union[ExperimentsProtocolExposureScheduleInput, none_type, UnsetType] = unset,
        metric_limit: Union[int, none_type, UnsetType] = unset,
        migration_metadata: Union[Dict[str, Any], none_type, UnsetType] = unset,
        minimum_duration_unit: Union[str, none_type, UnsetType] = unset,
        minimum_duration_value: Union[int, none_type, UnsetType] = unset,
        primary_metric_id: Union[UUID, none_type, UnsetType] = unset,
        targeting_rules: Union[List[ExperimentsProtocolTargetingRuleInput], UnsetType] = unset,
        **kwargs,
    ):
        """
        Replace a published protocol template. Omitted optional template fields are cleared. Omitted enforcement and migration_metadata are preserved. Enabled limits require their values; allocation settings require environment_id.

        :param analysis_plan: Statistical settings. Use ``default_duration_days`` for duration; ``target_duration_days`` is not accepted here.
        :type analysis_plan: ExperimentsProtocolAnalysisPlanInput, none_type, optional

        :param assignment_source_default_properties: Assignment properties.
        :type assignment_source_default_properties: [ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems], optional

        :param assignment_source_id: ID of the assignment source selected by the protocol.
        :type assignment_source_id: UUID, none_type, optional

        :param default_duration_days: Default experiment duration supplied by the protocol, in days.
        :type default_duration_days: int, none_type, optional

        :param enforcement: Complete lock map. Omit this object to preserve current locks. Null is rejected; every field is required.
        :type enforcement: ExperimentsReplaceProtocolEnforcementInput, optional

        :param environment_id: ID of the feature flag environment used by the experiment.
        :type environment_id: UUID, none_type, optional

        :param exposure_schedule: Traffic schedule. Publishing and replacement require ``NO_ROLLOUT`` with exactly one step, or ``UNIFORM_INTERVALS`` with a positive selection interval and at least one step. Requires ``environment_id``.
        :type exposure_schedule: ExperimentsProtocolExposureScheduleInput, none_type, optional

        :param is_duration_required_to_start: Whether the protocol requires a duration before an experiment can start.
        :type is_duration_required_to_start: bool

        :param is_equal_split_enforced: Whether the protocol requires equal traffic allocation across variants.
        :type is_equal_split_enforced: bool

        :param is_metric_limit_enabled: Whether the protocol limits the number of metrics.
        :type is_metric_limit_enabled: bool

        :param is_minimum_duration_enabled: Whether the protocol enforces a minimum experiment duration.
        :type is_minimum_duration_enabled: bool

        :param metric_groups: Metric groups.
        :type metric_groups: [ExperimentsProtocolMetricGroupInput]

        :param metric_limit: Maximum number of metrics allowed by the protocol.
        :type metric_limit: int, none_type, optional

        :param migration_metadata: Metadata for imported resources. Must encode to at most 4096 bytes. Null clears it; omission preserves it on update.
        :type migration_metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param minimum_duration_unit: Minimum duration unit, DAYS or WEEKS.
        :type minimum_duration_unit: str, none_type, optional

        :param minimum_duration_value: Minimum experiment duration in the specified unit.
        :type minimum_duration_value: int, none_type, optional

        :param primary_metric_id: ID of the primary metric supplied by the protocol.
        :type primary_metric_id: UUID, none_type, optional

        :param subject_type_id: ID of the subject type used by this configuration.
        :type subject_type_id: UUID

        :param targeting_rules: Targeting rules.
        :type targeting_rules: [ExperimentsProtocolTargetingRuleInput], optional
        """
        if analysis_plan is not unset:
            kwargs["analysis_plan"] = analysis_plan
        if assignment_source_default_properties is not unset:
            kwargs["assignment_source_default_properties"] = assignment_source_default_properties
        if assignment_source_id is not unset:
            kwargs["assignment_source_id"] = assignment_source_id
        if default_duration_days is not unset:
            kwargs["default_duration_days"] = default_duration_days
        if enforcement is not unset:
            kwargs["enforcement"] = enforcement
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if exposure_schedule is not unset:
            kwargs["exposure_schedule"] = exposure_schedule
        if metric_limit is not unset:
            kwargs["metric_limit"] = metric_limit
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if minimum_duration_unit is not unset:
            kwargs["minimum_duration_unit"] = minimum_duration_unit
        if minimum_duration_value is not unset:
            kwargs["minimum_duration_value"] = minimum_duration_value
        if primary_metric_id is not unset:
            kwargs["primary_metric_id"] = primary_metric_id
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        super().__init__(kwargs)

        self_.is_duration_required_to_start = is_duration_required_to_start
        self_.is_equal_split_enforced = is_equal_split_enforced
        self_.is_metric_limit_enabled = is_metric_limit_enabled
        self_.is_minimum_duration_enabled = is_minimum_duration_enabled
        self_.metric_groups = metric_groups
        self_.subject_type_id = subject_type_id
