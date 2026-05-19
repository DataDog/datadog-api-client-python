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
    from datadog_api_client.v2.model.model_lab_run_attributes import ModelLabRunAttributes
    from datadog_api_client.v2.model.model_lab_run_type import ModelLabRunType


class ModelLabRunData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_run_attributes import ModelLabRunAttributes
        from datadog_api_client.v2.model.model_lab_run_type import ModelLabRunType

        return {
            "attributes": (ModelLabRunAttributes,),
            "id": (str,),
            "type": (ModelLabRunType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ModelLabRunAttributes, id: str, type: ModelLabRunType, **kwargs):
        """
        A Model Lab run JSON:API resource object.

        :param attributes: Attributes of a Model Lab run.
        :type attributes: ModelLabRunAttributes

        :param id: The unique identifier of the run.
        :type id: str

        :param type: The JSON:API type for a Model Lab run resource.
        :type type: ModelLabRunType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
