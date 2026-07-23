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
    from datadog_api_client.v2.model.create_degradation_request_data_relationships_template_data import (
        CreateDegradationRequestDataRelationshipsTemplateData,
    )


class CreateDegradationRequestDataRelationshipsTemplate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data_relationships_template_data import (
            CreateDegradationRequestDataRelationshipsTemplateData,
        )

        return {
            "data": (CreateDegradationRequestDataRelationshipsTemplateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateDegradationRequestDataRelationshipsTemplateData, **kwargs):
        """
        The template used to create the degradation.

        :param data: The data object identifying the template used to create the degradation.
        :type data: CreateDegradationRequestDataRelationshipsTemplateData
        """
        super().__init__(kwargs)

        self_.data = data
