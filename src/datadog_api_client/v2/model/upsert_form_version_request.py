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
    from datadog_api_client.v2.model.upsert_form_version_data import UpsertFormVersionData


class UpsertFormVersionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_form_version_data import UpsertFormVersionData

        return {
            "data": (UpsertFormVersionData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpsertFormVersionData, **kwargs):
        """
        A request to create or update a form version.

        :param data: The data for creating or updating a form version.
        :type data: UpsertFormVersionData
        """
        super().__init__(kwargs)

        self_.data = data
