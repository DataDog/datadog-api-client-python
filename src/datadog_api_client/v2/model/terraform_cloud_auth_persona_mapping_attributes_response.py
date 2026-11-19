# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TerraformCloudAuthPersonaMappingAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_identifier": (str,),
            "account_uuid": (str,),
            "audience": (str,),
            "issuer_url": (str,),
            "sub_pattern": (str,),
        }

    attribute_map = {
        "account_identifier": "account_identifier",
        "account_uuid": "account_uuid",
        "audience": "audience",
        "issuer_url": "issuer_url",
        "sub_pattern": "sub_pattern",
    }
    read_only_vars = {
        "audience",
    }

    def __init__(
        self_,
        account_identifier: str,
        account_uuid: str,
        sub_pattern: str,
        audience: Union[str, UnsetType] = unset,
        issuer_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Stored HCP Terraform persona mapping attributes.

        :param account_identifier: Handle of the mapped Datadog account, resolved when the mapping was created.
        :type account_identifier: str

        :param account_uuid: UUID of the mapped Datadog user or service account.
        :type account_uuid: str

        :param audience: Audience to set as the ``TFC_WORKLOAD_IDENTITY_AUDIENCE_DATADOG`` environment variable in HCP Terraform. Datadog computes this value as ``datadog/<organization UUID>``.
        :type audience: str, optional

        :param issuer_url: HCP Terraform workload identity token issuer. Empty for mappings created before the issuer was required.
        :type issuer_url: str, optional

        :param sub_pattern: Pattern matched against the ``sub`` claim of HCP Terraform workload identity tokens.
        :type sub_pattern: str
        """
        if audience is not unset:
            kwargs["audience"] = audience
        if issuer_url is not unset:
            kwargs["issuer_url"] = issuer_url
        super().__init__(kwargs)

        self_.account_identifier = account_identifier
        self_.account_uuid = account_uuid
        self_.sub_pattern = sub_pattern
