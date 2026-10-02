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
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_related_links_items import (
        ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems,
    )
    from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_status import (
        ExperimentsExperimentV2DTODataAttributesStatus,
    )
    from datadog_api_client.v2.model.experiments_structured_metadata_response import (
        ExperimentsStructuredMetadataResponse,
    )


class ExperimentsExperimentV2ListDTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_conclusion import (
            ExperimentsPatchExperimentV2ResponseDataAttributesConclusion,
        )
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes_related_links_items import (
            ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems,
        )
        from datadog_api_client.v2.model.experiments_experiment_v2_dto_data_attributes_status import (
            ExperimentsExperimentV2DTODataAttributesStatus,
        )
        from datadog_api_client.v2.model.experiments_structured_metadata_response import (
            ExperimentsStructuredMetadataResponse,
        )

        return {
            "assignments_end_date": (datetime, none_type),
            "assignments_start_date": (datetime, none_type),
            "concluded_at": (datetime, none_type),
            "conclusion": (ExperimentsPatchExperimentV2ResponseDataAttributesConclusion,),
            "created_at": (datetime,),
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
            "status": (ExperimentsExperimentV2DTODataAttributesStatus,),
            "structured_metadata": ([ExperimentsStructuredMetadataResponse],),
            "subject_type_id": (str, none_type),
            "summary": (str,),
            "tags": ([str],),
            "teams": ([str],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "assignments_end_date": "assignments_end_date",
        "assignments_start_date": "assignments_start_date",
        "concluded_at": "concluded_at",
        "conclusion": "conclusion",
        "created_at": "created_at",
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
        "status": "status",
        "structured_metadata": "structured_metadata",
        "subject_type_id": "subject_type_id",
        "summary": "summary",
        "tags": "tags",
        "teams": "teams",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        assignments_end_date: Union[datetime, none_type, UnsetType] = unset,
        assignments_start_date: Union[datetime, none_type, UnsetType] = unset,
        concluded_at: Union[datetime, none_type, UnsetType] = unset,
        conclusion: Union[ExperimentsPatchExperimentV2ResponseDataAttributesConclusion, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
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
        status: Union[ExperimentsExperimentV2DTODataAttributesStatus, UnsetType] = unset,
        structured_metadata: Union[List[ExperimentsStructuredMetadataResponse], UnsetType] = unset,
        subject_type_id: Union[str, none_type, UnsetType] = unset,
        summary: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary fields for an experiment returned in a list.

        :param assignments_end_date: End of the window used to read experiment assignments.
        :type assignments_end_date: datetime, none_type, optional

        :param assignments_start_date: Start of the window used to read experiment assignments.
        :type assignments_start_date: datetime, none_type, optional

        :param concluded_at: Time when the experiment was concluded.
        :type concluded_at: datetime, none_type, optional

        :param conclusion: Outcome and supporting text recorded when the experiment is concluded.
        :type conclusion: ExperimentsPatchExperimentV2ResponseDataAttributesConclusion, optional

        :param created_at: Time when the experiment was created.
        :type created_at: datetime, optional

        :param events_end_date: End of the window used to read metric events.
        :type events_end_date: datetime, none_type, optional

        :param events_start_date: Start of the window used to read metric events.
        :type events_start_date: datetime, none_type, optional

        :param experiment_type: Kind of experiment. STANDARD is an ordinary experiment. Other values, such as CANARY and HOLDOUT, identify experiments owned by another workflow. New kinds may be added; treat unknown values as non-standard.
        :type experiment_type: str, optional

        :param hypothesis: Expected effect that the experiment is designed to test.
        :type hypothesis: str, optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the experiment.
        :type name: str, optional

        :param pipeline_table_suffix: Suffix used for the experiment tables in the analysis pipeline.
        :type pipeline_table_suffix: str, optional

        :param protocol_id: Identifier of the protocol associated with the experiment.
        :type protocol_id: str, optional

        :param related_links: External links associated with the experiment.
        :type related_links: [ExperimentsCreateExperimentV2RequestDataAttributesRelatedLinksItems], optional

        :param results_last_updated: Time when the experiment results were last updated.
        :type results_last_updated: datetime, none_type, optional

        :param status: Current stage in the experiment lifecycle.
        :type status: ExperimentsExperimentV2DTODataAttributesStatus, optional

        :param structured_metadata: Custom metadata fields and their values for the experiment.
        :type structured_metadata: [ExperimentsStructuredMetadataResponse], optional

        :param subject_type_id: Identifier of the subject type used for experiment assignments.
        :type subject_type_id: str, none_type, optional

        :param summary: Free-form summary of the experiment.
        :type summary: str, optional

        :param tags: Tag names associated with the experiment.
        :type tags: [str], optional

        :param teams: Team handles associated with the experiment.
        :type teams: [str], optional

        :param updated_at: Time when the experiment was last updated.
        :type updated_at: datetime, optional
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
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
