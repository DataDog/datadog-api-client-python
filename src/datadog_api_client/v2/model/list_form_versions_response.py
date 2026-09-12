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
    from datadog_api_client.v2.model.list_form_versions_data import ListFormVersionsData


class ListFormVersionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_form_versions_data import ListFormVersionsData

        return {
            "data": (ListFormVersionsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ListFormVersionsData, **kwargs):
        """
        A response containing the list of versions for a form.

        :param data: A list-of-form-versions resource object.
        :type data: ListFormVersionsData
        """
        super().__init__(kwargs)

        self_.data = data
