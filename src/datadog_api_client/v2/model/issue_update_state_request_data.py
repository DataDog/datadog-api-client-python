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
    from datadog_api_client.v2.model.issue_update_state_request_data_attributes import (
        IssueUpdateStateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.issue_update_state_request_data_type import IssueUpdateStateRequestDataType


class IssueUpdateStateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_update_state_request_data_attributes import (
            IssueUpdateStateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.issue_update_state_request_data_type import IssueUpdateStateRequestDataType

        return {
            "attributes": (IssueUpdateStateRequestDataAttributes,),
            "id": (str,),
            "type": (IssueUpdateStateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IssueUpdateStateRequestDataAttributes,
        id: str,
        type: IssueUpdateStateRequestDataType,
        **kwargs,
    ):
        """
        Update issue state request.

        :param attributes: Object describing an issue state update request.
        :type attributes: IssueUpdateStateRequestDataAttributes

        :param id: Issue identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueUpdateStateRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
