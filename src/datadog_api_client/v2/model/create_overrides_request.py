# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_override_request_data import CreateOverrideRequestData


class CreateOverridesRequest(ModelNormal):
    validations = {
        "data": {
            "max_items": 25,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_override_request_data import CreateOverrideRequestData

        return {
            "data": ([CreateOverrideRequestData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CreateOverrideRequestData], **kwargs):
        """
        Request to create one or more on-call schedule overrides. You can create up to 25 overrides in a single request.

        :param data: A list of on-call schedule overrides to create.
        :type data: [CreateOverrideRequestData]
        """
        super().__init__(kwargs)

        self_.data = data
