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


class SecurityMonitoringSignalCase(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignee_id": (str,),
            "assignee_name": (str,),
            "id": (str,),
            "key": (str,),
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "assignee_id": "assigneeId",
        "assignee_name": "assigneeName",
        "id": "id",
        "key": "key",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        assignee_id: Union[str, UnsetType] = unset,
        assignee_name: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A case linked to a security signal.

        :param assignee_id: The UUID of the user assigned to the case.
        :type assignee_id: str, optional

        :param assignee_name: The name of the user assigned to the case.
        :type assignee_name: str, optional

        :param id: The unique ID of the case.
        :type id: str, optional

        :param key: The key of the case.
        :type key: str, optional

        :param status: The status of the case.
        :type status: str, optional

        :param title: The title of the case.
        :type title: str, optional
        """
        if assignee_id is not unset:
            kwargs["assignee_id"] = assignee_id
        if assignee_name is not unset:
            kwargs["assignee_name"] = assignee_name
        if id is not unset:
            kwargs["id"] = id
        if key is not unset:
            kwargs["key"] = key
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
