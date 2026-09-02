# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WorkflowRunAsUserMode(ModelSimple):
    """
    The effective type of identity used to run the workflow.

    :param value: Must be one of ["owner", "service_account", "initiator"].
    :type value: str
    """

    allowed_values = {
        "owner",
        "service_account",
        "initiator",
    }
    OWNER: ClassVar["WorkflowRunAsUserMode"]
    SERVICE_ACCOUNT: ClassVar["WorkflowRunAsUserMode"]
    INITIATOR: ClassVar["WorkflowRunAsUserMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WorkflowRunAsUserMode.OWNER = WorkflowRunAsUserMode("owner")
WorkflowRunAsUserMode.SERVICE_ACCOUNT = WorkflowRunAsUserMode("service_account")
WorkflowRunAsUserMode.INITIATOR = WorkflowRunAsUserMode("initiator")
