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
    from datadog_api_client.v2.model.attach_linear_issue_request_data import AttachLinearIssueRequestData


class AttachLinearIssueRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attach_linear_issue_request_data import AttachLinearIssueRequestData

        return {
            "data": (AttachLinearIssueRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AttachLinearIssueRequestData, **kwargs):
        """
        Request for attaching security findings to a Linear issue.

        :param data: Data of the Linear issue to attach security findings to.
        :type data: AttachLinearIssueRequestData
        """
        super().__init__(kwargs)

        self_.data = data
