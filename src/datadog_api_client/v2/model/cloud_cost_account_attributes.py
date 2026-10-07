# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudCostAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "cloud": (str,),
            "created_at": (str,),
            "error_messages": ([str],),
            "status": (str,),
            "status_updated_at": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "cloud": "cloud",
        "created_at": "created_at",
        "error_messages": "error_messages",
        "status": "status",
        "status_updated_at": "status_updated_at",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        account_id: str,
        cloud: str,
        created_at: str,
        error_messages: List[str],
        status: str,
        status_updated_at: str,
        updated_at: str,
        **kwargs,
    ):
        """
        Read-only status and identifiers for a cloud cost account.

        :param account_id: The cloud provider account identifier, such as an OCI tenancy OCID or AWS account ID.
        :type account_id: str

        :param cloud: The cloud provider and cost report type. Currently supports ``oci`` and ``aws_cur2``.
        :type cloud: str

        :param created_at: The timestamp when the cloud account was created.
        :type created_at: str

        :param error_messages: Validation errors for the cloud account. Empty when there are no errors.
        :type error_messages: [str]

        :param status: The cloud account status, one of ``active`` , ``warn`` , ``error`` , or ``disabled``.
        :type status: str

        :param status_updated_at: The timestamp when the cloud account status was last updated.
        :type status_updated_at: str

        :param updated_at: The timestamp when the cloud account was last updated.
        :type updated_at: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.cloud = cloud
        self_.created_at = created_at
        self_.error_messages = error_messages
        self_.status = status
        self_.status_updated_at = status_updated_at
        self_.updated_at = updated_at
