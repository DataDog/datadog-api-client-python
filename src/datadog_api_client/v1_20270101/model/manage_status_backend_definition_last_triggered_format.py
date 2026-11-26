# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ManageStatusBackendDefinitionLastTriggeredFormat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["both", "relative", "absolute"].
    :type value: str
    """

    allowed_values = {
        "both",
        "relative",
        "absolute",
    }
    BOTH: ClassVar["ManageStatusBackendDefinitionLastTriggeredFormat"]
    RELATIVE: ClassVar["ManageStatusBackendDefinitionLastTriggeredFormat"]
    ABSOLUTE: ClassVar["ManageStatusBackendDefinitionLastTriggeredFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ManageStatusBackendDefinitionLastTriggeredFormat.BOTH = ManageStatusBackendDefinitionLastTriggeredFormat("both")
ManageStatusBackendDefinitionLastTriggeredFormat.RELATIVE = ManageStatusBackendDefinitionLastTriggeredFormat("relative")
ManageStatusBackendDefinitionLastTriggeredFormat.ABSOLUTE = ManageStatusBackendDefinitionLastTriggeredFormat("absolute")
