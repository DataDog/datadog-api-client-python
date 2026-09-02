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
    from datadog_api_client.v2.model.workflow_run_as_service_account_type import WorkflowRunAsServiceAccountType


class WorkflowRunAsServiceAccount(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_run_as_service_account_type import WorkflowRunAsServiceAccountType

        return {
            "id": (str,),
            "type": (WorkflowRunAsServiceAccountType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: WorkflowRunAsServiceAccountType, **kwargs):
        """
        Run the workflow as a service account.

        :param id: The service account identifier.
        :type id: str

        :param type: The service account run-as type.
        :type type: WorkflowRunAsServiceAccountType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
