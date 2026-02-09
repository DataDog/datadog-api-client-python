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
    from datadog_api_client.v2.model.workflow_webhook_execution_response_attributes import (
        WorkflowWebhookExecutionResponseAttributes,
    )
    from datadog_api_client.v2.model.workflow_webhook_execution_response_type import (
        WorkflowWebhookExecutionResponseType,
    )


class WorkflowWebhookExecutionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_webhook_execution_response_attributes import (
            WorkflowWebhookExecutionResponseAttributes,
        )
        from datadog_api_client.v2.model.workflow_webhook_execution_response_type import (
            WorkflowWebhookExecutionResponseType,
        )

        return {
            "attributes": (WorkflowWebhookExecutionResponseAttributes,),
            "id": (str,),
            "type": (WorkflowWebhookExecutionResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: WorkflowWebhookExecutionResponseAttributes,
        id: str,
        type: WorkflowWebhookExecutionResponseType,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: WorkflowWebhookExecutionResponseAttributes

        :param id: The unique identifier of the execution
        :type id: str

        :param type: The type for workflow webhook execution response
        :type type: WorkflowWebhookExecutionResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
