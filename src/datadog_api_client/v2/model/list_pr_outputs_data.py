# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_pr_outputs_attributes import ListPROutputsAttributes
    from datadog_api_client.v2.model.list_pr_outputs_data_type import ListPROutputsDataType


class ListPROutputsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_pr_outputs_attributes import ListPROutputsAttributes
        from datadog_api_client.v2.model.list_pr_outputs_data_type import ListPROutputsDataType

        return {
            "attributes": (ListPROutputsAttributes,),
            "id": (UUID,),
            "type": (ListPROutputsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ListPROutputsAttributes, id: UUID, type: ListPROutputsDataType, **kwargs):
        """
        Data for PR outputs response.

        :param attributes: Attributes of a PR outputs response.
        :type attributes: ListPROutputsAttributes

        :param id: The unique identifier of the workflow execution.
        :type id: UUID

        :param type: The resource type for workflow execution PR outputs.
        :type type: ListPROutputsDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
