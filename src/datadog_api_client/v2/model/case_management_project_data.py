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
    from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType


class CaseManagementProjectData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_management_project_data_type import CaseManagementProjectDataType

        return {
            "id": (str,),
            "type": (CaseManagementProjectDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: CaseManagementProjectDataType, **kwargs):
        """


        :param id: Unique identifier of the case management project.
        :type id: str

        :param type: Projects resource type.
        :type type: CaseManagementProjectDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
