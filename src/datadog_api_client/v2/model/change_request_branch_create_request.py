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
    from datadog_api_client.v2.model.change_request_branch_create_data import ChangeRequestBranchCreateData


class ChangeRequestBranchCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_branch_create_data import ChangeRequestBranchCreateData

        return {
            "data": (ChangeRequestBranchCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ChangeRequestBranchCreateData, **kwargs):
        """
        Request object to create a branch for a change request.

        :param data: Data object to create a change request branch.
        :type data: ChangeRequestBranchCreateData
        """
        super().__init__(kwargs)

        self_.data = data
