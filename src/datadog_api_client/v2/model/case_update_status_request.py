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
    from datadog_api_client.v2.model.case_update_status import CaseUpdateStatus


class CaseUpdateStatusRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_update_status import CaseUpdateStatus

        return {
            "data": (CaseUpdateStatus,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseUpdateStatus, **kwargs):
        """
        Case update status request

        :param data: Case update status
        :type data: CaseUpdateStatus
        """
        super().__init__(kwargs)

        self_.data = data
