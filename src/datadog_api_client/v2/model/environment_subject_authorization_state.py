# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EnvironmentSubjectAuthorizationState(ModelSimple):
    """
    Whether assignment requests for this environment require subject authorization. Allowed values are `disabled` and `enabled`. Enabling requires a provider ID formatted as a nonzero UUID. If omitted on create, defaults to `disabled`. If omitted on update, the stored state is preserved. `null` is not accepted. This setting applies only to the current Datadog site and is not copied to other sites. Before you enable it, configure an eligible Custom OIDC provider in the same organization and site, and verify that the provider's keys are published. Assignment requests fail when the required verification configuration is unavailable.

    :param value: Must be one of ["disabled", "enabled"].
    :type value: str
    """

    allowed_values = {
        "disabled",
        "enabled",
    }
    DISABLED: ClassVar["EnvironmentSubjectAuthorizationState"]
    ENABLED: ClassVar["EnvironmentSubjectAuthorizationState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EnvironmentSubjectAuthorizationState.DISABLED = EnvironmentSubjectAuthorizationState("disabled")
EnvironmentSubjectAuthorizationState.ENABLED = EnvironmentSubjectAuthorizationState("enabled")
