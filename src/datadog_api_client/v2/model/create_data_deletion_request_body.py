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
    from datadog_api_client.v2.model.create_data_deletion_request_body_data import CreateDataDeletionRequestBodyData


class CreateDataDeletionRequestBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_data_deletion_request_body_data import CreateDataDeletionRequestBodyData

        return {
            "data": (CreateDataDeletionRequestBodyData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateDataDeletionRequestBodyData, **kwargs):
        """
        Object needed to create a data deletion request.

        :param data: Data needed to create a data deletion request.
        :type data: CreateDataDeletionRequestBodyData
        """
        super().__init__(kwargs)

        self_.data = data
