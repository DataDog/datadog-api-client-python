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


class AssigneeResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignee_id": (str,),
        }

    attribute_map = {
        "assignee_id": "assignee_id",
    }

    def __init__(self_, assignee_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of the assignee response.

        :param assignee_id: Unique identifier of the Datadog user assigned to the security findings. Omitted when the findings were unassigned.
        :type assignee_id: str, optional
        """
        if assignee_id is not unset:
            kwargs["assignee_id"] = assignee_id
        super().__init__(kwargs)
