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
    from datadog_api_client.v2.model.case_status import CaseStatus


class CaseUpdateStatusAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_status import CaseStatus

        return {
            "status": (CaseStatus,),
            "status_name": (str,),
        }

    attribute_map = {
        "status": "status",
        "status_name": "status_name",
    }

    def __init__(
        self_, status: Union[CaseStatus, UnsetType] = unset, status_name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Case update status attributes

        :param status: Deprecated way of representing the case status, which only supports OPEN, IN_PROGRESS, and CLOSED statuses. Use ``status_name`` instead. **Deprecated**.
        :type status: CaseStatus, optional

        :param status_name: Status of the case. Must be one of the existing statuses for the case's type.
        :type status_name: str, optional
        """
        if status is not unset:
            kwargs["status"] = status
        if status_name is not unset:
            kwargs["status_name"] = status_name
        super().__init__(kwargs)
