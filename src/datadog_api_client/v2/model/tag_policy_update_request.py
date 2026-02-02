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
    from datadog_api_client.v2.model.tag_policy_data_update_request import TagPolicyDataUpdateRequest


class TagPolicyUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_data_update_request import TagPolicyDataUpdateRequest

        return {
            "data": (TagPolicyDataUpdateRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TagPolicyDataUpdateRequest, **kwargs):
        """
        Request for updating a tag policy.

        :param data: Data envelope for tag policy update request.
        :type data: TagPolicyDataUpdateRequest
        """
        super().__init__(kwargs)

        self_.data = data
