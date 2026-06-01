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
    from datadog_api_client.v2.model.incident_user_defined_role_patch_data_request import (
        IncidentUserDefinedRolePatchDataRequest,
    )


class IncidentUserDefinedRolePatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_patch_data_request import (
            IncidentUserDefinedRolePatchDataRequest,
        )

        return {
            "data": (IncidentUserDefinedRolePatchDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentUserDefinedRolePatchDataRequest, **kwargs):
        """
        Request for updating an incident user-defined role.

        :param data: Data for updating an incident user-defined role.
        :type data: IncidentUserDefinedRolePatchDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
