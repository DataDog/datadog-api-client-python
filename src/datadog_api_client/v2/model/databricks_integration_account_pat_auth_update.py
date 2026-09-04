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
    from datadog_api_client.v2.model.databricks_integration_account_pat_auth_type import (
        DatabricksIntegrationAccountPatAuthType,
    )


class DatabricksIntegrationAccountPatAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_pat_auth_type import (
            DatabricksIntegrationAccountPatAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountPatAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(
        self_, auth_type: DatabricksIntegrationAccountPatAuthType, token: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Databricks personal access token authentication. Deprecated: accepted only on accounts that already use it, and never on creation. Use ``databricks-oauth`` or ``private-action-runner`` instead. Omit ``token`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountPatAuthType

        :param token: Secret Databricks personal access token.
        :type token: str, optional
        """
        if token is not unset:
            kwargs["token"] = token
        super().__init__(kwargs)

        self_.auth_type = auth_type
