# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.model_lab_metric_summary import ModelLabMetricSummary
    from datadog_api_client.v2.model.model_lab_run_param import ModelLabRunParam
    from datadog_api_client.v2.model.model_lab_run_status import ModelLabRunStatus
    from datadog_api_client.v2.model.model_lab_tag import ModelLabTag


class ModelLabRunAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_metric_summary import ModelLabMetricSummary
        from datadog_api_client.v2.model.model_lab_run_param import ModelLabRunParam
        from datadog_api_client.v2.model.model_lab_run_status import ModelLabRunStatus
        from datadog_api_client.v2.model.model_lab_tag import ModelLabTag

        return {
            "completed_at": (datetime, none_type),
            "created_at": (datetime,),
            "deleted_at": (datetime, none_type),
            "descendant_match": (bool,),
            "description": (str,),
            "duration": (float, none_type),
            "external_url": (str, none_type),
            "has_children": (bool,),
            "is_pinned": (bool,),
            "metric_summaries": ([ModelLabMetricSummary],),
            "mlflow_artifact_location": (str,),
            "name": (str,),
            "owner_id": (str, none_type),
            "params": ([ModelLabRunParam], none_type),
            "project_id": (int,),
            "started_at": (datetime,),
            "status": (ModelLabRunStatus,),
            "tags": ([ModelLabTag],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "completed_at": "completed_at",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "descendant_match": "descendant_match",
        "description": "description",
        "duration": "duration",
        "external_url": "external_url",
        "has_children": "has_children",
        "is_pinned": "is_pinned",
        "metric_summaries": "metric_summaries",
        "mlflow_artifact_location": "mlflow_artifact_location",
        "name": "name",
        "owner_id": "owner_id",
        "params": "params",
        "project_id": "project_id",
        "started_at": "started_at",
        "status": "status",
        "tags": "tags",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        descendant_match: bool,
        description: str,
        has_children: bool,
        is_pinned: bool,
        metric_summaries: List[ModelLabMetricSummary],
        mlflow_artifact_location: str,
        name: str,
        params: Union[List[ModelLabRunParam], none_type],
        project_id: int,
        started_at: datetime,
        status: ModelLabRunStatus,
        tags: List[ModelLabTag],
        updated_at: datetime,
        completed_at: Union[datetime, none_type, UnsetType] = unset,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        duration: Union[float, none_type, UnsetType] = unset,
        external_url: Union[str, none_type, UnsetType] = unset,
        owner_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Model Lab run.

        :param completed_at: The date and time the run completed.
        :type completed_at: datetime, none_type, optional

        :param created_at: The date and time the run was created.
        :type created_at: datetime

        :param deleted_at: The date and time the run was soft-deleted.
        :type deleted_at: datetime, none_type, optional

        :param descendant_match: Whether a descendant run matched the applied filters.
        :type descendant_match: bool

        :param description: A description of the run.
        :type description: str

        :param duration: The duration of the run in seconds.
        :type duration: float, none_type, optional

        :param external_url: An optional external URL associated with the run.
        :type external_url: str, none_type, optional

        :param has_children: Whether the run has child runs.
        :type has_children: bool

        :param is_pinned: Whether the run is pinned by the current user.
        :type is_pinned: bool

        :param metric_summaries: Summary statistics for metrics recorded during the run.
        :type metric_summaries: [ModelLabMetricSummary]

        :param mlflow_artifact_location: The MLflow artifact storage location for this run.
        :type mlflow_artifact_location: str

        :param name: The name of the run.
        :type name: str

        :param owner_id: The UUID of the run owner.
        :type owner_id: str, none_type, optional

        :param params: The list of parameters used for the run.
        :type params: [ModelLabRunParam], none_type

        :param project_id: The ID of the project this run belongs to.
        :type project_id: int

        :param started_at: The date and time the run started.
        :type started_at: datetime

        :param status: The status of a Model Lab run.
        :type status: ModelLabRunStatus

        :param tags: The list of tags associated with the run.
        :type tags: [ModelLabTag]

        :param updated_at: The date and time the run was last updated.
        :type updated_at: datetime
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if duration is not unset:
            kwargs["duration"] = duration
        if external_url is not unset:
            kwargs["external_url"] = external_url
        if owner_id is not unset:
            kwargs["owner_id"] = owner_id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.descendant_match = descendant_match
        self_.description = description
        self_.has_children = has_children
        self_.is_pinned = is_pinned
        self_.metric_summaries = metric_summaries
        self_.mlflow_artifact_location = mlflow_artifact_location
        self_.name = name
        self_.params = params
        self_.project_id = project_id
        self_.started_at = started_at
        self_.status = status
        self_.tags = tags
        self_.updated_at = updated_at
