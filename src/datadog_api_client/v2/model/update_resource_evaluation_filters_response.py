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
    from datadog_api_client.v2.model.update_resource_evaluation_filters_response_data import (
        UpdateResourceEvaluationFiltersResponseData,
    )


class UpdateResourceEvaluationFiltersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_resource_evaluation_filters_response_data import (
            UpdateResourceEvaluationFiltersResponseData,
        )

        return {
            "data": (UpdateResourceEvaluationFiltersResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpdateResourceEvaluationFiltersResponseData, **kwargs):
        """
        The definition of ``UpdateResourceEvaluationFiltersResponse`` object.

        :param data: The definition of ``UpdateResourceFilterResponseData`` object.
        :type data: UpdateResourceEvaluationFiltersResponseData
        """
        super().__init__(kwargs)

        self_.data = data
