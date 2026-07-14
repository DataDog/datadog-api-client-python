# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_role_data_response import IncidentUserDefinedRoleDataResponse
    from datadog_api_client.v2.model.incident_user_defined_role_included_item import IncidentUserDefinedRoleIncludedItem
    from datadog_api_client.v2.model.incident_user_data import IncidentUserData
    from datadog_api_client.v2.model.incident_type_object import IncidentTypeObject


class IncidentUserDefinedRoleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_data_response import (
            IncidentUserDefinedRoleDataResponse,
        )
        from datadog_api_client.v2.model.incident_user_defined_role_included_item import (
            IncidentUserDefinedRoleIncludedItem,
        )

        return {
            "data": (IncidentUserDefinedRoleDataResponse,),
            "included": ([IncidentUserDefinedRoleIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: IncidentUserDefinedRoleDataResponse,
        included: Union[
            List[Union[IncidentUserDefinedRoleIncludedItem, IncidentUserData, IncidentTypeObject]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response with a single incident user-defined role.

        :param data: Data for an incident user-defined role response.
        :type data: IncidentUserDefinedRoleDataResponse

        :param included: Included resources for an incident user-defined role response.
        :type included: [IncidentUserDefinedRoleIncludedItem], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
