# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ManageStatusBackendDefinitionDisplayFormat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["counts", "countsAndList", "list"].
    :type value: str
    """

    allowed_values = {
        "counts",
        "countsAndList",
        "list",
    }
    COUNTS: ClassVar["ManageStatusBackendDefinitionDisplayFormat"]
    COUNTSANDLIST: ClassVar["ManageStatusBackendDefinitionDisplayFormat"]
    LIST: ClassVar["ManageStatusBackendDefinitionDisplayFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ManageStatusBackendDefinitionDisplayFormat.COUNTS = ManageStatusBackendDefinitionDisplayFormat("counts")
ManageStatusBackendDefinitionDisplayFormat.COUNTSANDLIST = ManageStatusBackendDefinitionDisplayFormat("countsAndList")
ManageStatusBackendDefinitionDisplayFormat.LIST = ManageStatusBackendDefinitionDisplayFormat("list")
