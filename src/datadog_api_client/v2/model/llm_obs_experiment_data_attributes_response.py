# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.llm_obs_experiment_user import LLMObsExperimentUser
    from datadog_api_client.v2.model.llm_obs_experiment_status import LLMObsExperimentStatus


class LLMObsExperimentDataAttributesResponse(ModelNormal):
    validations = {
        "run_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_user import LLMObsExperimentUser
        from datadog_api_client.v2.model.llm_obs_experiment_status import LLMObsExperimentStatus

        return {
            "aggregate_data": (
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
            "author": (LLMObsExperimentUser,),
            "config": (
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
            "created_at": (datetime,),
            "dataset_id": (str,),
            "dataset_name": (str, none_type),
            "dataset_version": (int,),
            "deleted_at": (datetime, none_type),
            "description": (str, none_type),
            "error": (str, none_type),
            "experiment": (str,),
            "metadata": (
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
            "name": (str,),
            "parent_experiment_id": (str, none_type),
            "project_id": (str,),
            "run_count": (int,),
            "status": (LLMObsExperimentStatus,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "aggregate_data": "aggregate_data",
        "author": "author",
        "config": "config",
        "created_at": "created_at",
        "dataset_id": "dataset_id",
        "dataset_name": "dataset_name",
        "dataset_version": "dataset_version",
        "deleted_at": "deleted_at",
        "description": "description",
        "error": "error",
        "experiment": "experiment",
        "metadata": "metadata",
        "name": "name",
        "parent_experiment_id": "parent_experiment_id",
        "project_id": "project_id",
        "run_count": "run_count",
        "status": "status",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        config: Union[Dict[str, Any], none_type],
        created_at: datetime,
        dataset_id: str,
        description: Union[str, none_type],
        metadata: Union[Dict[str, Any], none_type],
        name: str,
        project_id: str,
        updated_at: datetime,
        aggregate_data: Union[Dict[str, Any], none_type, UnsetType] = unset,
        author: Union[LLMObsExperimentUser, UnsetType] = unset,
        dataset_name: Union[str, none_type, UnsetType] = unset,
        dataset_version: Union[int, UnsetType] = unset,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        error: Union[str, none_type, UnsetType] = unset,
        experiment: Union[str, UnsetType] = unset,
        parent_experiment_id: Union[str, none_type, UnsetType] = unset,
        run_count: Union[int, UnsetType] = unset,
        status: Union[LLMObsExperimentStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability experiment.

        :param aggregate_data: Pre-computed aggregate metrics for this experiment run, including eval score distributions, token costs, and error rates.
        :type aggregate_data: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param author: User data for the author of an experiment. Only present when ``include[user_data]`` is ``true``.
        :type author: LLMObsExperimentUser, optional

        :param config: Configuration parameters for the experiment.
        :type config: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type

        :param created_at: Timestamp when the experiment was created.
        :type created_at: datetime

        :param dataset_id: Identifier of the dataset used in this experiment.
        :type dataset_id: str

        :param dataset_name: Name of the dataset used in this experiment.
            Only present when ``include[dataset_names]`` is ``true``.
        :type dataset_name: str, none_type, optional

        :param dataset_version: Version of the dataset used in this experiment.
        :type dataset_version: int, optional

        :param deleted_at: Timestamp when the experiment was soft-deleted, if applicable.
        :type deleted_at: datetime, none_type, optional

        :param description: Description of the experiment.
        :type description: str, none_type

        :param error: Error message describing why the experiment failed, if applicable.
        :type error: str, none_type, optional

        :param experiment: Logical name of the experiment, shared across all runs of the same pipeline.
        :type experiment: str, optional

        :param metadata: Arbitrary metadata associated with the experiment.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type

        :param name: Name of the experiment.
        :type name: str

        :param parent_experiment_id: Identifier of the parent (baseline) experiment this experiment was run against, if any.
        :type parent_experiment_id: str, none_type, optional

        :param project_id: Identifier of the project this experiment belongs to.
        :type project_id: str

        :param run_count: Expected number of runs for this experiment.
        :type run_count: int, optional

        :param status: Execution status of an LLM Observability experiment.
        :type status: LLMObsExperimentStatus, optional

        :param updated_at: Timestamp when the experiment was last updated.
        :type updated_at: datetime
        """
        if aggregate_data is not unset:
            kwargs["aggregate_data"] = aggregate_data
        if author is not unset:
            kwargs["author"] = author
        if dataset_name is not unset:
            kwargs["dataset_name"] = dataset_name
        if dataset_version is not unset:
            kwargs["dataset_version"] = dataset_version
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if error is not unset:
            kwargs["error"] = error
        if experiment is not unset:
            kwargs["experiment"] = experiment
        if parent_experiment_id is not unset:
            kwargs["parent_experiment_id"] = parent_experiment_id
        if run_count is not unset:
            kwargs["run_count"] = run_count
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)

        self_.config = config
        self_.created_at = created_at
        self_.dataset_id = dataset_id
        self_.description = description
        self_.metadata = metadata
        self_.name = name
        self_.project_id = project_id
        self_.updated_at = updated_at
