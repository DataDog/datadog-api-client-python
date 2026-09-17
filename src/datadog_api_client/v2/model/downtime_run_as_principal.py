# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.downtime_run_as_principal_type import DowntimeRunAsPrincipalType


class DowntimeRunAsPrincipal(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_run_as_principal_type import DowntimeRunAsPrincipalType

        return {
            "id": (str,),
            "type": (DowntimeRunAsPrincipalType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: DowntimeRunAsPrincipalType, **kwargs):
        """
        A principal (user, role, or team) allowed to act on behalf of the downtime.

        :param id: The ID of the principal.
        :type id: str

        :param type: The type of principal allowed to act on behalf of the downtime.
        :type type: DowntimeRunAsPrincipalType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
