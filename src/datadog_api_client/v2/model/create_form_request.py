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
    from datadog_api_client.v2.model.create_form_data import CreateFormData


class CreateFormRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_form_data import CreateFormData

        return {
            "data": (CreateFormData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateFormData, **kwargs):
        """
        A request to create a form.

        :param data: The data for creating a form.
        :type data: CreateFormData
        """
        super().__init__(kwargs)

        self_.data = data
