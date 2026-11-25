# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineClientIdentityMode(ModelSimple):
    """
    What happens to a client that no rule allows. `enforce` rejects the TLS handshake. `audit` accepts the client and reports that it would have been rejected.

    :param value: If omitted defaults to "enforce". Must be one of ["enforce", "audit"].
    :type value: str
    """

    allowed_values = {
        "enforce",
        "audit",
    }
    ENFORCE: ClassVar["ObservabilityPipelineClientIdentityMode"]
    AUDIT: ClassVar["ObservabilityPipelineClientIdentityMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineClientIdentityMode.ENFORCE = ObservabilityPipelineClientIdentityMode("enforce")
ObservabilityPipelineClientIdentityMode.AUDIT = ObservabilityPipelineClientIdentityMode("audit")
