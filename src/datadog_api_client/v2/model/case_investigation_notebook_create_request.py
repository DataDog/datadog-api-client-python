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
    from datadog_api_client.v2.model.case_investigation_notebook_create_data import CaseInvestigationNotebookCreateData


class CaseInvestigationNotebookCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_investigation_notebook_create_data import (
            CaseInvestigationNotebookCreateData,
        )

        return {
            "data": (CaseInvestigationNotebookCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseInvestigationNotebookCreateData, **kwargs):
        """
        Case investigation notebook creation request.

        :param data: Case investigation notebook creation data.
        :type data: CaseInvestigationNotebookCreateData
        """
        super().__init__(kwargs)

        self_.data = data
