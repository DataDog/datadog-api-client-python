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
    from datadog_api_client.v2.model.case_status import CaseStatus


class CaseUpdateStatusAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_status import CaseStatus

        return {
            "status": (CaseStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: CaseStatus, **kwargs):
        """
        Case update status attributes

        :param status: Case status
        :type status: CaseStatus
        """
        super().__init__(kwargs)

        self_.status = status
