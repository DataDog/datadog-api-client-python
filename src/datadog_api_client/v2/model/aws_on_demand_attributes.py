# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AwsOnDemandAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arn": (str,),
            "assigned_at": (str,),
            "created_at": (str,),
            "status": (str,),
        }

    attribute_map = {
        "arn": "arn",
        "assigned_at": "assigned_at",
        "created_at": "created_at",
        "status": "status",
    }

    def __init__(
        self_,
        arn: Union[str, UnsetType] = unset,
        assigned_at: Union[str, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the AWS on demand task.

        :param arn: The arn of the resource to scan.
        :type arn: str, optional

        :param assigned_at: Specifies the assignment timestamp if the task has been already assigned to a scanner.
        :type assigned_at: str, optional

        :param created_at: The task submission timestamp.
        :type created_at: str, optional

        :param status: Indicates the status of the task.
            QUEUED: the task has been submitted successfully and the resource has not been assigned to a scanner yet.
            ASSIGNED: the task has been assigned.
            ABORTED: the scan has been aborted after a period of time due to technical reasons, such as resource not found, insufficient permissions, or the absence of a configured scanner.
        :type status: str, optional
        """
        if arn is not unset:
            kwargs["arn"] = arn
        if assigned_at is not unset:
            kwargs["assigned_at"] = assigned_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
