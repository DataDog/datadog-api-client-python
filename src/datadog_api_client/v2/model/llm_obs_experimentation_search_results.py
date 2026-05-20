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
    from datadog_api_client.v2.model.llm_obs_dataset_record_data_response import LLMObsDatasetRecordDataResponse
    from datadog_api_client.v2.model.llm_obs_dataset_data_response import LLMObsDatasetDataResponse
    from datadog_api_client.v2.model.llm_obs_experiment_run_data_response import LLMObsExperimentRunDataResponse
    from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_response import (
        LLMObsExperimentDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_project_data_response import LLMObsProjectDataResponse


class LLMObsExperimentationSearchResults(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_record_data_response import LLMObsDatasetRecordDataResponse
        from datadog_api_client.v2.model.llm_obs_dataset_data_response import LLMObsDatasetDataResponse
        from datadog_api_client.v2.model.llm_obs_experiment_run_data_response import LLMObsExperimentRunDataResponse
        from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_response import (
            LLMObsExperimentDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_project_data_response import LLMObsProjectDataResponse

        return {
            "dataset_records": ([LLMObsDatasetRecordDataResponse], none_type),
            "datasets": ([LLMObsDatasetDataResponse], none_type),
            "experiment_runs": ([LLMObsExperimentRunDataResponse], none_type),
            "experiments": ([LLMObsExperimentDataAttributesResponse], none_type),
            "projects": ([LLMObsProjectDataResponse], none_type),
        }

    attribute_map = {
        "dataset_records": "dataset_records",
        "datasets": "datasets",
        "experiment_runs": "experiment_runs",
        "experiments": "experiments",
        "projects": "projects",
    }

    def __init__(
        self_,
        dataset_records: Union[List[LLMObsDatasetRecordDataResponse], none_type, UnsetType] = unset,
        datasets: Union[List[LLMObsDatasetDataResponse], none_type, UnsetType] = unset,
        experiment_runs: Union[List[LLMObsExperimentRunDataResponse], none_type, UnsetType] = unset,
        experiments: Union[List[LLMObsExperimentDataAttributesResponse], none_type, UnsetType] = unset,
        projects: Union[List[LLMObsProjectDataResponse], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The matching experimentation entities grouped by type.

        :param dataset_records: Matching dataset records. Present when ``dataset_records`` is included in ``filter.scope``.
        :type dataset_records: [LLMObsDatasetRecordDataResponse], none_type, optional

        :param datasets: Matching datasets. Present when ``datasets`` is included in ``filter.scope``.
        :type datasets: [LLMObsDatasetDataResponse], none_type, optional

        :param experiment_runs: Matching experiment runs. Present when ``experiment_runs`` is included in ``filter.scope``.
        :type experiment_runs: [LLMObsExperimentRunDataResponse], none_type, optional

        :param experiments: Matching experiments. Present when ``experiments`` is included in ``filter.scope``.
        :type experiments: [LLMObsExperimentDataAttributesResponse], none_type, optional

        :param projects: Matching projects. Present when ``projects`` is included in ``filter.scope``.
        :type projects: [LLMObsProjectDataResponse], none_type, optional
        """
        if dataset_records is not unset:
            kwargs["dataset_records"] = dataset_records
        if datasets is not unset:
            kwargs["datasets"] = datasets
        if experiment_runs is not unset:
            kwargs["experiment_runs"] = experiment_runs
        if experiments is not unset:
            kwargs["experiments"] = experiments
        if projects is not unset:
            kwargs["projects"] = projects
        super().__init__(kwargs)
