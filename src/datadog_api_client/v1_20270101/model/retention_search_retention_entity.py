# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionSearchRetentionEntity(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["@usr.id", "@account.id"].
    :type value: str
    """

    allowed_values = {
        "@usr.id",
        "@account.id",
    }
    USR_ID: ClassVar["RetentionSearchRetentionEntity"]
    ACCOUNT_ID: ClassVar["RetentionSearchRetentionEntity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionSearchRetentionEntity.USR_ID = RetentionSearchRetentionEntity("@usr.id")
RetentionSearchRetentionEntity.ACCOUNT_ID = RetentionSearchRetentionEntity("@account.id")
