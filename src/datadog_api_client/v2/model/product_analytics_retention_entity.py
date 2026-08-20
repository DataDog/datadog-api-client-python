# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionEntity(ModelSimple):
    """
    The entity whose retention is measured.

    :param value: Must be one of ["@usr.id", "@account.id"].
    :type value: str
    """

    allowed_values = {
        "@usr.id",
        "@account.id",
    }
    USER_ID: ClassVar["ProductAnalyticsRetentionEntity"]
    ACCOUNT_ID: ClassVar["ProductAnalyticsRetentionEntity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionEntity.USER_ID = ProductAnalyticsRetentionEntity("@usr.id")
ProductAnalyticsRetentionEntity.ACCOUNT_ID = ProductAnalyticsRetentionEntity("@account.id")
