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
    from datadog_api_client.v2.model.case_bulk_update_request_data import CaseBulkUpdateRequestData


class CaseBulkUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_bulk_update_request_data import CaseBulkUpdateRequestData

        return {
            "data": (CaseBulkUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseBulkUpdateRequestData, **kwargs):
        """
        Request payload for applying a single action (such as changing priority, status, or assignment) to multiple cases at once.

        :param data: Data object wrapping the bulk update type and attributes.
        :type data: CaseBulkUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
