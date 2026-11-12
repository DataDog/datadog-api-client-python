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
    from datadog_api_client.v2.model.create_on_call_page_comment_request_data import CreateOnCallPageCommentRequestData


class CreateOnCallPageCommentRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_on_call_page_comment_request_data import (
            CreateOnCallPageCommentRequestData,
        )

        return {
            "data": (CreateOnCallPageCommentRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateOnCallPageCommentRequestData, **kwargs):
        """
        Request to create a comment on an On-Call Page.

        :param data: Data for creating a comment on an On-Call Page.
        :type data: CreateOnCallPageCommentRequestData
        """
        super().__init__(kwargs)

        self_.data = data
