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
    from datadog_api_client.v2.model.temporary_grant_request_create_data import TemporaryGrantRequestCreateData


class TemporaryGrantRequestCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_create_data import TemporaryGrantRequestCreateData

        return {
            "data": (TemporaryGrantRequestCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TemporaryGrantRequestCreateData, **kwargs):
        """
        Create a request for the authenticated human user.

        :param data: The request resource to create. The server generates its ID.
        :type data: TemporaryGrantRequestCreateData
        """
        super().__init__(kwargs)

        self_.data = data
