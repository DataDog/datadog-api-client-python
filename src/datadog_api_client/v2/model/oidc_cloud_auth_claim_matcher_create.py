# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.oidc_cloud_auth_claim_match_mode import OIDCCloudAuthClaimMatchMode


class OIDCCloudAuthClaimMatcherCreate(ModelNormal):
    validations = {
        "values": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_claim_match_mode import OIDCCloudAuthClaimMatchMode

        return {
            "claim": (str,),
            "mode": (OIDCCloudAuthClaimMatchMode,),
            "values": ([str],),
        }

    attribute_map = {
        "claim": "claim",
        "mode": "mode",
        "values": "values",
    }

    def __init__(
        self_, claim: str, values: List[str], mode: Union[OIDCCloudAuthClaimMatchMode, UnsetType] = unset, **kwargs
    ):
        """
        Claim condition for creating a provider or persona mapping. A token claim must match at least one configured value.

        :param claim: Name of the token claim.
        :type claim: str

        :param mode: Case-sensitive matching mode. Exact compares strings. Glob matches the entire value: * matches any number of characters, including /, and ? matches one character. Other characters are literal; escaping is not supported.
        :type mode: OIDCCloudAuthClaimMatchMode, optional

        :param values: Accepted values for this claim. Each value is limited to 500 UTF-8 bytes when creating the resource.
        :type values: [str]
        """
        if mode is not unset:
            kwargs["mode"] = mode
        super().__init__(kwargs)

        self_.claim = claim
        self_.values = values
