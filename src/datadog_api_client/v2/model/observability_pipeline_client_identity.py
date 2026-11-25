# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_client_identity_allowlist import (
        ObservabilityPipelineClientIdentityAllowlist,
    )
    from datadog_api_client.v2.model.observability_pipeline_client_identity_mode import (
        ObservabilityPipelineClientIdentityMode,
    )


class ObservabilityPipelineClientIdentity(ModelNormal):
    validations = {
        "allowlist_file": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_client_identity_allowlist import (
            ObservabilityPipelineClientIdentityAllowlist,
        )
        from datadog_api_client.v2.model.observability_pipeline_client_identity_mode import (
            ObservabilityPipelineClientIdentityMode,
        )

        return {
            "allowlist": (ObservabilityPipelineClientIdentityAllowlist,),
            "allowlist_file": (str,),
            "mode": (ObservabilityPipelineClientIdentityMode,),
        }

    attribute_map = {
        "allowlist": "allowlist",
        "allowlist_file": "allowlist_file",
        "mode": "mode",
    }

    def __init__(
        self_,
        allowlist: Union[ObservabilityPipelineClientIdentityAllowlist, UnsetType] = unset,
        allowlist_file: Union[str, UnsetType] = unset,
        mode: Union[ObservabilityPipelineClientIdentityMode, UnsetType] = unset,
        **kwargs,
    ):
        """
        Restricts which clients may connect, based on the identities in their TLS certificate. Checks run during the TLS handshake, after the client certificate chain is validated against ``ca_file`` , and never relax that validation.
        Requires ``verify_certificate: true`` and ``ca_file``. Set exactly one of ``allowlist_file`` or ``allowlist``.
        When set, connections are closed after a maximum age of 300 seconds so that clients removed from the allowlist are disconnected.
        Requires Observability Pipelines Worker 2.27 or later.

        :param allowlist: An allowlist of client identities. A client is allowed when any rule matches.
        :type allowlist: ObservabilityPipelineClientIdentityAllowlist, optional

        :param allowlist_file: Path to an allowlist file, relative to the Worker's data directory. The Worker reloads the file when it changes. Must not contain parent directory ( ``..`` ) references.
        :type allowlist_file: str, optional

        :param mode: What happens to a client that no rule allows. ``enforce`` rejects the TLS handshake. ``audit`` accepts the client and reports that it would have been rejected.
        :type mode: ObservabilityPipelineClientIdentityMode, optional
        """
        if allowlist is not unset:
            kwargs["allowlist"] = allowlist
        if allowlist_file is not unset:
            kwargs["allowlist_file"] = allowlist_file
        if mode is not unset:
            kwargs["mode"] = mode
        super().__init__(kwargs)
