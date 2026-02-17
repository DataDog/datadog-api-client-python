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
    from datadog_api_client.v2.model.incident_import_request_data import IncidentImportRequestData


class IncidentImportRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_import_request_data import IncidentImportRequestData

        return {
            "data": (IncidentImportRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentImportRequestData, **kwargs):
        """
        Import request for an incident. Used to import historical incidents from external systems.

        :param data: Incident data for an import request.
        :type data: IncidentImportRequestData
        """
        super().__init__(kwargs)

        self_.data = data
