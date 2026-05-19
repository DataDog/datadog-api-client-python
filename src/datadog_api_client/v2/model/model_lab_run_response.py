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
    from datadog_api_client.v2.model.model_lab_run_data import ModelLabRunData


class ModelLabRunResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_run_data import ModelLabRunData

        return {
            "data": (ModelLabRunData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ModelLabRunData, **kwargs):
        """
        Response containing a single Model Lab run.

        :param data: A Model Lab run JSON:API resource object.
        :type data: ModelLabRunData
        """
        super().__init__(kwargs)

        self_.data = data
