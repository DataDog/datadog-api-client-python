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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_request_data_attributes_datadog_flag_configuration import (
        ExperimentsPatchExperimentV2RequestDataAttributesDatadogFlagConfiguration,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_decision_metrics_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_related_links_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_split_by_properties_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesSplitByPropertiesItems,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_structured_metadata_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesStructuredMetadataItems,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_traffic_exposure import (
        ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_variants_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesVariantsItems,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_warehouse_exposure_configuration import (
        ExperimentsCreateExperimentV2RequestDataAttributesWarehouseExposureConfiguration,
    )


class ExperimentsPatchExperimentV2RequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_request_data_attributes_datadog_flag_configuration import (
            ExperimentsPatchExperimentV2RequestDataAttributesDatadogFlagConfiguration,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_decision_metrics_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_related_links_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_split_by_properties_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesSplitByPropertiesItems,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_structured_metadata_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesStructuredMetadataItems,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_traffic_exposure import (
            ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_variants_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesVariantsItems,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_warehouse_exposure_configuration import (
            ExperimentsCreateExperimentV2RequestDataAttributesWarehouseExposureConfiguration,
        )

        return {
            "assignments_end_date": (datetime, none_type),
            "assignments_start_date": (datetime, none_type),
            "datadog_flag_configuration": (ExperimentsPatchExperimentV2RequestDataAttributesDatadogFlagConfiguration,),
            "decision_metrics": ([ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems],),
            "events_end_date": (datetime, none_type),
            "events_start_date": (datetime, none_type),
            "hypothesis": (str,),
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
            "name": (str,),
            "related_links": ([ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems],),
            "split_by_properties": ([ExperimentsCreateExperimentV2RequestDataAttributesSplitByPropertiesItems],),
            "structured_metadata": (
                [ExperimentsCreateExperimentV2RequestDataAttributesStructuredMetadataItems],
                none_type,
            ),
            "subject_type_id": (str,),
            "summary": (str, none_type),
            "tags": ([str],),
            "teams": ([str],),
            "traffic_exposure": (ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure,),
            "variants": ([ExperimentsCreateExperimentV2RequestDataAttributesVariantsItems],),
            "warehouse_exposure_configuration": (
                ExperimentsCreateExperimentV2RequestDataAttributesWarehouseExposureConfiguration,
            ),
        }

    attribute_map = {
        "assignments_end_date": "assignments_end_date",
        "assignments_start_date": "assignments_start_date",
        "datadog_flag_configuration": "datadog_flag_configuration",
        "decision_metrics": "decision_metrics",
        "events_end_date": "events_end_date",
        "events_start_date": "events_start_date",
        "hypothesis": "hypothesis",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "related_links": "related_links",
        "split_by_properties": "split_by_properties",
        "structured_metadata": "structured_metadata",
        "subject_type_id": "subject_type_id",
        "summary": "summary",
        "tags": "tags",
        "teams": "teams",
        "traffic_exposure": "traffic_exposure",
        "variants": "variants",
        "warehouse_exposure_configuration": "warehouse_exposure_configuration",
    }

    def __init__(
        self_,
        assignments_end_date: Union[datetime, none_type, UnsetType] = unset,
        assignments_start_date: Union[datetime, none_type, UnsetType] = unset,
        datadog_flag_configuration: Union[
            ExperimentsPatchExperimentV2RequestDataAttributesDatadogFlagConfiguration, none_type, UnsetType
        ] = unset,
        decision_metrics: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems], UnsetType
        ] = unset,
        events_end_date: Union[datetime, none_type, UnsetType] = unset,
        events_start_date: Union[datetime, none_type, UnsetType] = unset,
        hypothesis: Union[str, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        related_links: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems], UnsetType
        ] = unset,
        split_by_properties: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesSplitByPropertiesItems], UnsetType
        ] = unset,
        structured_metadata: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesStructuredMetadataItems], none_type, UnsetType
        ] = unset,
        subject_type_id: Union[str, UnsetType] = unset,
        summary: Union[str, none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        traffic_exposure: Union[ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure, UnsetType] = unset,
        variants: Union[List[ExperimentsCreateExperimentV2RequestDataAttributesVariantsItems], UnsetType] = unset,
        warehouse_exposure_configuration: Union[
            ExperimentsCreateExperimentV2RequestDataAttributesWarehouseExposureConfiguration, none_type, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Fields supplied to update the experiment.

        :param assignments_end_date: End of the time window for experiment assignments.
        :type assignments_end_date: datetime, none_type, optional

        :param assignments_start_date: Start of the time window for experiment assignments.
        :type assignments_start_date: datetime, none_type, optional

        :param datadog_flag_configuration: Feature flag, environment, and targeting configuration for the experiment.
        :type datadog_flag_configuration: ExperimentsPatchExperimentV2RequestDataAttributesDatadogFlagConfiguration, none_type, optional

        :param decision_metrics: Metrics used to decide the experiment outcome.
        :type decision_metrics: [ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems], optional

        :param events_end_date: End of the time window for metric events.
        :type events_end_date: datetime, none_type, optional

        :param events_start_date: Start of the time window for metric events.
        :type events_start_date: datetime, none_type, optional

        :param hypothesis: Expected effect that the experiment is intended to test.
        :type hypothesis: str, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the experiment.
        :type name: str, optional

        :param related_links: Links to supporting material for the experiment.
        :type related_links: [ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems], optional

        :param split_by_properties: Complete replacement for the Datadog split-by selection. Identify each property by column_name. Omit this field to leave the selection unchanged.
        :type split_by_properties: [ExperimentsCreateExperimentV2RequestDataAttributesSplitByPropertiesItems], optional

        :param structured_metadata: Metadata values to update. Omit this field, send null, or send an empty array to leave metadata unchanged.
        :type structured_metadata: [ExperimentsCreateExperimentV2RequestDataAttributesStructuredMetadataItems], none_type, optional

        :param subject_type_id: ID of the subject type used by this configuration.
        :type subject_type_id: str, optional

        :param summary: Summary text recorded for the experiment.
        :type summary: str, none_type, optional

        :param tags: Tags attached to the experiment.
        :type tags: [str], optional

        :param teams: Teams associated with the experiment.
        :type teams: [str], optional

        :param traffic_exposure: Traffic exposure fraction or schedule configured for the experiment.
        :type traffic_exposure: ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure, optional

        :param variants: Variants configured for the experiment.
        :type variants: [ExperimentsCreateExperimentV2RequestDataAttributesVariantsItems], optional

        :param warehouse_exposure_configuration: Warehouse model and experiment key used to read assignment data.
        :type warehouse_exposure_configuration: ExperimentsCreateExperimentV2RequestDataAttributesWarehouseExposureConfiguration, none_type, optional
        """
        if assignments_end_date is not unset:
            kwargs["assignments_end_date"] = assignments_end_date
        if assignments_start_date is not unset:
            kwargs["assignments_start_date"] = assignments_start_date
        if datadog_flag_configuration is not unset:
            kwargs["datadog_flag_configuration"] = datadog_flag_configuration
        if decision_metrics is not unset:
            kwargs["decision_metrics"] = decision_metrics
        if events_end_date is not unset:
            kwargs["events_end_date"] = events_end_date
        if events_start_date is not unset:
            kwargs["events_start_date"] = events_start_date
        if hypothesis is not unset:
            kwargs["hypothesis"] = hypothesis
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if related_links is not unset:
            kwargs["related_links"] = related_links
        if split_by_properties is not unset:
            kwargs["split_by_properties"] = split_by_properties
        if structured_metadata is not unset:
            kwargs["structured_metadata"] = structured_metadata
        if subject_type_id is not unset:
            kwargs["subject_type_id"] = subject_type_id
        if summary is not unset:
            kwargs["summary"] = summary
        if tags is not unset:
            kwargs["tags"] = tags
        if teams is not unset:
            kwargs["teams"] = teams
        if traffic_exposure is not unset:
            kwargs["traffic_exposure"] = traffic_exposure
        if variants is not unset:
            kwargs["variants"] = variants
        if warehouse_exposure_configuration is not unset:
            kwargs["warehouse_exposure_configuration"] = warehouse_exposure_configuration
        super().__init__(kwargs)
