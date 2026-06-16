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
    from datadog_api_client.v2.model.publish_form_data import PublishFormData


class PublishFormRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.publish_form_data import PublishFormData

        return {
            "data": (PublishFormData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PublishFormData, **kwargs):
        """
        A request to publish a form version.

        :param data: The data for publishing a form version.
        :type data: PublishFormData
        """
        super().__init__(kwargs)

        self_.data = data
