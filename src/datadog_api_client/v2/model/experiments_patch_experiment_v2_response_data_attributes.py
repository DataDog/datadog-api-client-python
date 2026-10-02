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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_conclusion import (
        ExperimentsPatchExperimentV2ResponseDataAttributesConclusion,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfiguration,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_decision_metrics_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems,
    )
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_related_links_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems,
    )
    from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_split_by_properties_items import (
        ExperimentsExperimentV2DTODataAttributesSplitByPropertiesItems,
    )
    from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_status import (
        ExperimentsExperimentV2DTODataAttributesStatus,
    )
    from datadog_api_client.v2.model.experiments_structured_metadata_response import (
        ExperimentsStructuredMetadataResponse,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_traffic_exposure import (
        ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure,
    )
    from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_variants_items import (
        ExperimentsExperimentV2DTODataAttributesVariantsItems,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration import (
        ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfiguration,
    )


class ExperimentsPatchExperimentV2ResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_conclusion import (
            ExperimentsPatchExperimentV2ResponseDataAttributesConclusion,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration import (
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfiguration,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_decision_metrics_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_related_links_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems,
        )
        from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_split_by_properties_items import (
            ExperimentsExperimentV2DTODataAttributesSplitByPropertiesItems,
        )
        from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_status import (
            ExperimentsExperimentV2DTODataAttributesStatus,
        )
        from datadog_api_client.v2.model.experiments_structured_metadata_response import (
            ExperimentsStructuredMetadataResponse,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_traffic_exposure import (
            ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure,
        )
        from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_variants_items import (
            ExperimentsExperimentV2DTODataAttributesVariantsItems,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration import (
            ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfiguration,
        )

        return {
            "assignments_end_date": (datetime, none_type),
            "assignments_start_date": (datetime, none_type),
            "concluded_at": (datetime, none_type),
            "conclusion": (ExperimentsPatchExperimentV2ResponseDataAttributesConclusion,),
            "created_at": (datetime,),
            "datadog_flag_configuration": (ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfiguration,),
            "decision_metrics": ([ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems],),
            "decision_variant_key": (str,),
            "events_end_date": (datetime, none_type),
            "events_start_date": (datetime, none_type),
            "experiment_type": (str,),
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
            "pipeline_table_suffix": (str,),
            "protocol_id": (str,),
            "related_links": ([ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems],),
            "results_last_updated": (datetime, none_type),
            "split_by_properties": ([ExperimentsExperimentV2DTODataAttributesSplitByPropertiesItems],),
            "status": (ExperimentsExperimentV2DTODataAttributesStatus,),
            "structured_metadata": ([ExperimentsStructuredMetadataResponse],),
            "subject_type_id": (str, none_type),
            "summary": (str,),
            "tags": ([str],),
            "teams": ([str],),
            "traffic_exposure": (ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure,),
            "updated_at": (datetime,),
            "variants": ([ExperimentsExperimentV2DTODataAttributesVariantsItems],),
            "warehouse_exposure_configuration": (
                ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfiguration,
            ),
        }

    attribute_map = {
        "assignments_end_date": "assignments_end_date",
        "assignments_start_date": "assignments_start_date",
        "concluded_at": "concluded_at",
        "conclusion": "conclusion",
        "created_at": "created_at",
        "datadog_flag_configuration": "datadog_flag_configuration",
        "decision_metrics": "decision_metrics",
        "decision_variant_key": "decision_variant_key",
        "events_end_date": "events_end_date",
        "events_start_date": "events_start_date",
        "experiment_type": "experiment_type",
        "hypothesis": "hypothesis",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "pipeline_table_suffix": "pipeline_table_suffix",
        "protocol_id": "protocol_id",
        "related_links": "related_links",
        "results_last_updated": "results_last_updated",
        "split_by_properties": "split_by_properties",
        "status": "status",
        "structured_metadata": "structured_metadata",
        "subject_type_id": "subject_type_id",
        "summary": "summary",
        "tags": "tags",
        "teams": "teams",
        "traffic_exposure": "traffic_exposure",
        "updated_at": "updated_at",
        "variants": "variants",
        "warehouse_exposure_configuration": "warehouse_exposure_configuration",
    }

    def __init__(
        self_,
        assignments_end_date: Union[datetime, none_type, UnsetType] = unset,
        assignments_start_date: Union[datetime, none_type, UnsetType] = unset,
        concluded_at: Union[datetime, none_type, UnsetType] = unset,
        conclusion: Union[ExperimentsPatchExperimentV2ResponseDataAttributesConclusion, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        datadog_flag_configuration: Union[
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfiguration, none_type, UnsetType
        ] = unset,
        decision_metrics: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems], UnsetType
        ] = unset,
        decision_variant_key: Union[str, UnsetType] = unset,
        events_end_date: Union[datetime, none_type, UnsetType] = unset,
        events_start_date: Union[datetime, none_type, UnsetType] = unset,
        experiment_type: Union[str, UnsetType] = unset,
        hypothesis: Union[str, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pipeline_table_suffix: Union[str, UnsetType] = unset,
        protocol_id: Union[str, UnsetType] = unset,
        related_links: Union[
            List[ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems], UnsetType
        ] = unset,
        results_last_updated: Union[datetime, none_type, UnsetType] = unset,
        split_by_properties: Union[
            List[ExperimentsExperimentV2DTODataAttributesSplitByPropertiesItems], UnsetType
        ] = unset,
        status: Union[ExperimentsExperimentV2DTODataAttributesStatus, UnsetType] = unset,
        structured_metadata: Union[List[ExperimentsStructuredMetadataResponse], UnsetType] = unset,
        subject_type_id: Union[str, none_type, UnsetType] = unset,
        summary: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        traffic_exposure: Union[ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        variants: Union[List[ExperimentsExperimentV2DTODataAttributesVariantsItems], UnsetType] = unset,
        warehouse_exposure_configuration: Union[
            ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfiguration, none_type, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Details of the experiment.

        :param assignments_end_date: End of the time window for experiment assignments.
        :type assignments_end_date: datetime, none_type, optional

        :param assignments_start_date: Start of the time window for experiment assignments.
        :type assignments_start_date: datetime, none_type, optional

        :param concluded_at: Time when the experiment was concluded.
        :type concluded_at: datetime, none_type, optional

        :param conclusion: Outcome and supporting text recorded when the experiment is concluded.
        :type conclusion: ExperimentsPatchExperimentV2ResponseDataAttributesConclusion, optional

        :param created_at: Time when this resource was created.
        :type created_at: datetime, optional

        :param datadog_flag_configuration: Feature flag, environment, and targeting configuration for the experiment.
        :type datadog_flag_configuration: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfiguration, none_type, optional

        :param decision_metrics: Metrics used to decide the experiment outcome.
        :type decision_metrics: [ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems], optional

        :param decision_variant_key: Key of the variant selected in the experiment decision.
        :type decision_variant_key: str, optional

        :param events_end_date: End of the time window for metric events.
        :type events_end_date: datetime, none_type, optional

        :param events_start_date: Start of the time window for metric events.
        :type events_start_date: datetime, none_type, optional

        :param experiment_type: Kind of experiment. STANDARD is an ordinary experiment. Other values, such as CANARY and HOLDOUT, identify experiments owned by another workflow. New kinds may be added; treat unknown values as non-standard.
        :type experiment_type: str, optional

        :param hypothesis: Expected effect that the experiment is intended to test.
        :type hypothesis: str, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the experiment.
        :type name: str, optional

        :param pipeline_table_suffix: Suffix used to identify the experiment's pipeline output table.
        :type pipeline_table_suffix: str, optional

        :param protocol_id: ID of the protocol associated with the experiment.
        :type protocol_id: str, optional

        :param related_links: Links to supporting material for the experiment.
        :type related_links: [ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems], optional

        :param results_last_updated: Time of the most recent update to the experiment's results.
        :type results_last_updated: datetime, none_type, optional

        :param split_by_properties: Properties used to split the experiment results into groups.
        :type split_by_properties: [ExperimentsExperimentV2DTODataAttributesSplitByPropertiesItems], optional

        :param status: Current stage in the experiment lifecycle.
        :type status: ExperimentsExperimentV2DTODataAttributesStatus, optional

        :param structured_metadata: Values of structured metadata fields attached to the experiment.
        :type structured_metadata: [ExperimentsStructuredMetadataResponse], optional

        :param subject_type_id: ID of the subject type used by this configuration.
        :type subject_type_id: str, none_type, optional

        :param summary: Summary text recorded for the experiment.
        :type summary: str, optional

        :param tags: Tags attached to the experiment.
        :type tags: [str], optional

        :param teams: Teams associated with the experiment.
        :type teams: [str], optional

        :param traffic_exposure: Traffic exposure fraction or schedule configured for the experiment.
        :type traffic_exposure: ExperimentsPatchExperimentV2ResponseDataAttributesTrafficExposure, optional

        :param updated_at: Time when this resource was last updated.
        :type updated_at: datetime, optional

        :param variants: Variants configured for the experiment.
        :type variants: [ExperimentsExperimentV2DTODataAttributesVariantsItems], optional

        :param warehouse_exposure_configuration: Warehouse exposure model and settings used to identify experiment assignments.
        :type warehouse_exposure_configuration: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfiguration, none_type, optional
        """
        if assignments_end_date is not unset:
            kwargs["assignments_end_date"] = assignments_end_date
        if assignments_start_date is not unset:
            kwargs["assignments_start_date"] = assignments_start_date
        if concluded_at is not unset:
            kwargs["concluded_at"] = concluded_at
        if conclusion is not unset:
            kwargs["conclusion"] = conclusion
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if datadog_flag_configuration is not unset:
            kwargs["datadog_flag_configuration"] = datadog_flag_configuration
        if decision_metrics is not unset:
            kwargs["decision_metrics"] = decision_metrics
        if decision_variant_key is not unset:
            kwargs["decision_variant_key"] = decision_variant_key
        if events_end_date is not unset:
            kwargs["events_end_date"] = events_end_date
        if events_start_date is not unset:
            kwargs["events_start_date"] = events_start_date
        if experiment_type is not unset:
            kwargs["experiment_type"] = experiment_type
        if hypothesis is not unset:
            kwargs["hypothesis"] = hypothesis
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if pipeline_table_suffix is not unset:
            kwargs["pipeline_table_suffix"] = pipeline_table_suffix
        if protocol_id is not unset:
            kwargs["protocol_id"] = protocol_id
        if related_links is not unset:
            kwargs["related_links"] = related_links
        if results_last_updated is not unset:
            kwargs["results_last_updated"] = results_last_updated
        if split_by_properties is not unset:
            kwargs["split_by_properties"] = split_by_properties
        if status is not unset:
            kwargs["status"] = status
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
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if variants is not unset:
            kwargs["variants"] = variants
        if warehouse_exposure_configuration is not unset:
            kwargs["warehouse_exposure_configuration"] = warehouse_exposure_configuration
        super().__init__(kwargs)
