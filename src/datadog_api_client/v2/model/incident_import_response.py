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
    from datadog_api_client.v2.model.incident_import_response_data import IncidentImportResponseData
    from datadog_api_client.v2.model.incident_import_response_included_item import IncidentImportResponseIncludedItem
    from datadog_api_client.v2.model.incident_user_data import IncidentUserData
    from datadog_api_client.v2.model.incident_type_object import IncidentTypeObject


class IncidentImportResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_import_response_data import IncidentImportResponseData
        from datadog_api_client.v2.model.incident_import_response_included_item import (
            IncidentImportResponseIncludedItem,
        )

        return {
            "data": (IncidentImportResponseData,),
            "included": ([IncidentImportResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    read_only_vars = {
        "included",
    }

    def __init__(
        self_,
        data: IncidentImportResponseData,
        included: Union[
            List[Union[IncidentImportResponseIncludedItem, IncidentUserData, IncidentTypeObject]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response with an incident.

        :param data: Incident data from an import response.
        :type data: IncidentImportResponseData

        :param included: Included related resources that the user requested.
        :type included: [IncidentImportResponseIncludedItem], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
