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
    from datadog_api_client.v2.model.terraform_cloud_auth_issuer_url import TerraformCloudAuthIssuerURL


class TerraformCloudAuthPersonaMappingCreateAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_cloud_auth_issuer_url import TerraformCloudAuthIssuerURL

        return {
            "account_identifier": (str,),
            "issuer_url": (TerraformCloudAuthIssuerURL,),
            "sub_pattern": (str,),
        }

    attribute_map = {
        "account_identifier": "account_identifier",
        "issuer_url": "issuer_url",
        "sub_pattern": "sub_pattern",
    }

    def __init__(self_, account_identifier: str, issuer_url: TerraformCloudAuthIssuerURL, sub_pattern: str, **kwargs):
        """
        Attributes for creating an HCP Terraform persona mapping.

        :param account_identifier: Handle or email address of the Datadog user or service account that matching tokens authenticate as. Its permissions must not exceed the caller's.
        :type account_identifier: str

        :param issuer_url: HCP Terraform workload identity token issuer. Use ``https://app.terraform.io`` for HCP Terraform in the US or ``https://app.eu.terraform.io`` for HCP Terraform in Europe.
        :type issuer_url: TerraformCloudAuthIssuerURL

        :param sub_pattern: Pattern matched against the ``sub`` claim of HCP Terraform workload identity tokens. Use ``organization:<org>:project:<project>:workspace:<workspace>:run_phase:<plan|apply>`` for workspace runs, or ``organization:<org>:module:<module>:operation:test_run`` for module test runs. Segments are HCP Terraform names, not IDs.
            Any segment except the organization can be ``*`` to match any value.
        :type sub_pattern: str
        """
        super().__init__(kwargs)

        self_.account_identifier = account_identifier
        self_.issuer_url = issuer_url
        self_.sub_pattern = sub_pattern
