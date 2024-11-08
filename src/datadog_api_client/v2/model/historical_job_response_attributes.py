# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.job_definition import JobDefinition


class HistoricalJobResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.job_definition import JobDefinition

        return {
            "created_at": (str,),
            "created_by_handle": (str,),
            "created_by_name": (str,),
            "created_from_rule_id": (str,),
            "job_definition": (JobDefinition,),
            "job_name": (str,),
            "job_status": (str,),
            "modified_at": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "created_by_handle": "createdByHandle",
        "created_by_name": "createdByName",
        "created_from_rule_id": "createdFromRuleId",
        "job_definition": "jobDefinition",
        "job_name": "jobName",
        "job_status": "jobStatus",
        "modified_at": "modifiedAt",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        created_by_handle: Union[str, UnsetType] = unset,
        created_by_name: Union[str, UnsetType] = unset,
        created_from_rule_id: Union[str, UnsetType] = unset,
        job_definition: Union[JobDefinition, UnsetType] = unset,
        job_name: Union[str, UnsetType] = unset,
        job_status: Union[str, UnsetType] = unset,
        modified_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Historical job attributes.

        :param created_at: Time when the job was created.
        :type created_at: str, optional

        :param created_by_handle: The handle of the user who created the job.
        :type created_by_handle: str, optional

        :param created_by_name: The name of the user who created the job.
        :type created_by_name: str, optional

        :param created_from_rule_id: ID of the rule used to create the job (if it is created from a rule).
        :type created_from_rule_id: str, optional

        :param job_definition: Definition of a historical job.
        :type job_definition: JobDefinition, optional

        :param job_name: Job name.
        :type job_name: str, optional

        :param job_status: Job status.
        :type job_status: str, optional

        :param modified_at: Last modification time of the job.
        :type modified_at: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if created_by_name is not unset:
            kwargs["created_by_name"] = created_by_name
        if created_from_rule_id is not unset:
            kwargs["created_from_rule_id"] = created_from_rule_id
        if job_definition is not unset:
            kwargs["job_definition"] = job_definition
        if job_name is not unset:
            kwargs["job_name"] = job_name
        if job_status is not unset:
            kwargs["job_status"] = job_status
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        super().__init__(kwargs)
