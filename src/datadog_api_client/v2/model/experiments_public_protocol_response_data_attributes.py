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
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_analysis_plan import (
        ExperimentsPublicProtocolResponseDataAttributesAnalysisPlan,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_assignment_source_default_properties_items import (
        ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_enforcement import (
        ExperimentsPublicProtocolResponseDataAttributesEnforcement,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_exposure_schedule import (
        ExperimentsPublicProtocolResponseDataAttributesExposureSchedule,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_metric_groups_items import (
        ExperimentsPublicProtocolResponseDataAttributesMetricGroupsItems,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_subject_type import (
        ExperimentsPublicProtocolResponseDataAttributesSubjectType,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_status import (
        ExperimentsPublicProtocolResponseDataAttributesStatus,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_targeting_rules_items import (
        ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItems,
    )


class ExperimentsPublicProtocolResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_analysis_plan import (
            ExperimentsPublicProtocolResponseDataAttributesAnalysisPlan,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_assignment_source_default_properties_items import (
            ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_enforcement import (
            ExperimentsPublicProtocolResponseDataAttributesEnforcement,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_exposure_schedule import (
            ExperimentsPublicProtocolResponseDataAttributesExposureSchedule,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_metric_groups_items import (
            ExperimentsPublicProtocolResponseDataAttributesMetricGroupsItems,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_subject_type import (
            ExperimentsPublicProtocolResponseDataAttributesSubjectType,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_status import (
            ExperimentsPublicProtocolResponseDataAttributesStatus,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_targeting_rules_items import (
            ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItems,
        )

        return {
            "analysis_plan": (ExperimentsPublicProtocolResponseDataAttributesAnalysisPlan,),
            "assignment_source_default_properties": (
                [ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems],
            ),
            "assignment_source_id": (str,),
            "default_duration_days": (int,),
            "description": (str,),
            "enforcement": (ExperimentsPublicProtocolResponseDataAttributesEnforcement,),
            "environment_id": (str,),
            "exposure_schedule": (ExperimentsPublicProtocolResponseDataAttributesExposureSchedule,),
            "is_duration_required_to_start": (bool,),
            "is_equal_split_enforced": (bool,),
            "is_metric_limit_enabled": (bool,),
            "is_minimum_duration_enabled": (bool,),
            "metric_groups": ([ExperimentsPublicProtocolResponseDataAttributesMetricGroupsItems],),
            "metric_limit": (int,),
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
            "minimum_duration_unit": (str,),
            "minimum_duration_value": (int,),
            "name": (str,),
            "primary_metric": (ExperimentsPublicProtocolResponseDataAttributesSubjectType,),
            "primary_metric_id": (str,),
            "published_at": (datetime,),
            "status": (ExperimentsPublicProtocolResponseDataAttributesStatus,),
            "subject_type": (ExperimentsPublicProtocolResponseDataAttributesSubjectType,),
            "subject_type_id": (str,),
            "targeting_rules": ([ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItems],),
            "updated_at": (str,),
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
        "primary_metric": "primary_metric",
        "primary_metric_id": "primary_metric_id",
        "published_at": "published_at",
        "status": "status",
        "subject_type": "subject_type",
        "subject_type_id": "subject_type_id",
        "targeting_rules": "targeting_rules",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        is_duration_required_to_start: bool,
        is_equal_split_enforced: bool,
        is_metric_limit_enabled: bool,
        is_minimum_duration_enabled: bool,
        metric_groups: List[ExperimentsPublicProtocolResponseDataAttributesMetricGroupsItems],
        name: str,
        status: ExperimentsPublicProtocolResponseDataAttributesStatus,
        updated_at: str,
        analysis_plan: Union[ExperimentsPublicProtocolResponseDataAttributesAnalysisPlan, UnsetType] = unset,
        assignment_source_default_properties: Union[
            List[ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems], UnsetType
        ] = unset,
        assignment_source_id: Union[str, UnsetType] = unset,
        default_duration_days: Union[int, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        enforcement: Union[ExperimentsPublicProtocolResponseDataAttributesEnforcement, UnsetType] = unset,
        environment_id: Union[str, UnsetType] = unset,
        exposure_schedule: Union[ExperimentsPublicProtocolResponseDataAttributesExposureSchedule, UnsetType] = unset,
        metric_limit: Union[int, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        minimum_duration_unit: Union[str, UnsetType] = unset,
        minimum_duration_value: Union[int, UnsetType] = unset,
        primary_metric: Union[ExperimentsPublicProtocolResponseDataAttributesSubjectType, UnsetType] = unset,
        primary_metric_id: Union[str, UnsetType] = unset,
        published_at: Union[datetime, UnsetType] = unset,
        subject_type: Union[ExperimentsPublicProtocolResponseDataAttributesSubjectType, UnsetType] = unset,
        subject_type_id: Union[str, UnsetType] = unset,
        targeting_rules: Union[
            List[ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItems], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Settings and defaults supplied by the protocol.

        :param analysis_plan: Default statistical settings supplied by the protocol.
        :type analysis_plan: ExperimentsPublicProtocolResponseDataAttributesAnalysisPlan, optional

        :param assignment_source_default_properties: Default properties supplied by the protocol's assignment source.
        :type assignment_source_default_properties: [ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems], optional

        :param assignment_source_id: ID of the assignment source selected by the protocol.
        :type assignment_source_id: str, optional

        :param default_duration_days: Default experiment duration supplied by the protocol, in days.
        :type default_duration_days: int, optional

        :param description: Text that explains the protocol.
        :type description: str, optional

        :param enforcement: Controls that determine which protocol settings can be changed in an experiment.
        :type enforcement: ExperimentsPublicProtocolResponseDataAttributesEnforcement, optional

        :param environment_id: ID of the feature flag environment used by the experiment.
        :type environment_id: str, optional

        :param exposure_schedule: Schedule that controls traffic exposure for experiments created from the protocol.
        :type exposure_schedule: ExperimentsPublicProtocolResponseDataAttributesExposureSchedule, optional

        :param is_duration_required_to_start: Whether the protocol requires a duration before an experiment can start.
        :type is_duration_required_to_start: bool

        :param is_equal_split_enforced: Whether the protocol requires equal traffic allocation across variants.
        :type is_equal_split_enforced: bool

        :param is_metric_limit_enabled: Whether the protocol limits the number of metrics.
        :type is_metric_limit_enabled: bool

        :param is_minimum_duration_enabled: Whether the protocol enforces a minimum experiment duration.
        :type is_minimum_duration_enabled: bool

        :param metric_groups: Metric groups supplied by the protocol.
        :type metric_groups: [ExperimentsPublicProtocolResponseDataAttributesMetricGroupsItems]

        :param metric_limit: Maximum number of metrics allowed by the protocol.
        :type metric_limit: int, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param minimum_duration_unit: Unit used to express the protocol's minimum duration.
        :type minimum_duration_unit: str, optional

        :param minimum_duration_value: Minimum experiment duration in the specified unit.
        :type minimum_duration_value: int, optional

        :param name: Display name of the protocol.
        :type name: str

        :param primary_metric: Subject type selected by the protocol.
        :type primary_metric: ExperimentsPublicProtocolResponseDataAttributesSubjectType, optional

        :param primary_metric_id: ID of the primary metric supplied by the protocol.
        :type primary_metric_id: str, optional

        :param published_at: Time when the protocol was published.
        :type published_at: datetime, optional

        :param status: Publication status of the protocol.
        :type status: ExperimentsPublicProtocolResponseDataAttributesStatus

        :param subject_type: Subject type selected by the protocol.
        :type subject_type: ExperimentsPublicProtocolResponseDataAttributesSubjectType, optional

        :param subject_type_id: ID of the subject type used by this configuration.
        :type subject_type_id: str, optional

        :param targeting_rules: Rules that select subjects for the experiment.
        :type targeting_rules: [ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItems], optional

        :param updated_at: RFC3339 update time. Preserve all fractional seconds when passing this value as expected_updated_at.
        :type updated_at: str
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
        if metric_limit is not unset:
            kwargs["metric_limit"] = metric_limit
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if minimum_duration_unit is not unset:
            kwargs["minimum_duration_unit"] = minimum_duration_unit
        if minimum_duration_value is not unset:
            kwargs["minimum_duration_value"] = minimum_duration_value
        if primary_metric is not unset:
            kwargs["primary_metric"] = primary_metric
        if primary_metric_id is not unset:
            kwargs["primary_metric_id"] = primary_metric_id
        if published_at is not unset:
            kwargs["published_at"] = published_at
        if subject_type is not unset:
            kwargs["subject_type"] = subject_type
        if subject_type_id is not unset:
            kwargs["subject_type_id"] = subject_type_id
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        super().__init__(kwargs)

        self_.is_duration_required_to_start = is_duration_required_to_start
        self_.is_equal_split_enforced = is_equal_split_enforced
        self_.is_metric_limit_enabled = is_metric_limit_enabled
        self_.is_minimum_duration_enabled = is_minimum_duration_enabled
        self_.metric_groups = metric_groups
        self_.name = name
        self_.status = status
        self_.updated_at = updated_at
