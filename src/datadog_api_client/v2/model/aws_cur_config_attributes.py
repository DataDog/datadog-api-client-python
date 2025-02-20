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
    from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig


class AwsCURConfigAttributes(ModelNormal):
    validations = {
        "created_at": {},
        "months": {
            "inclusive_maximum": 36,
        },
        "status_updated_at": {},
        "updated_at": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig

        return {
            "account_filters": (AccountFilteringConfig,),
            "account_id": (str,),
            "bucket_name": (str,),
            "bucket_region": (str,),
            "created_at": (str,),
            "error_messages": ([str],),
            "months": (int,),
            "report_name": (str,),
            "report_prefix": (str,),
            "status": (str,),
            "status_updated_at": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "account_filters": "account_filters",
        "account_id": "account_id",
        "bucket_name": "bucket_name",
        "bucket_region": "bucket_region",
        "created_at": "created_at",
        "error_messages": "error_messages",
        "months": "months",
        "report_name": "report_name",
        "report_prefix": "report_prefix",
        "status": "status",
        "status_updated_at": "status_updated_at",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        account_id: str,
        bucket_name: str,
        bucket_region: str,
        report_name: str,
        report_prefix: str,
        status: str,
        account_filters: Union[AccountFilteringConfig, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        status_updated_at: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for An AWS CUR config.

        :param account_filters: The account filtering configuration.
        :type account_filters: AccountFilteringConfig, optional

        :param account_id: The AWS account ID.
        :type account_id: str

        :param bucket_name: The AWS bucket name used to store the Cost and Usage Report.
        :type bucket_name: str

        :param bucket_region: The region the bucket is located in.
        :type bucket_region: str

        :param created_at: The timestamp when the AWS CUR config was created.
        :type created_at: str, optional

        :param error_messages: The error messages for the AWS CUR config.
        :type error_messages: [str], optional

        :param months: The number of months the report has been backfilled. **Deprecated**.
        :type months: int, optional

        :param report_name: The name of the Cost and Usage Report.
        :type report_name: str

        :param report_prefix: The report prefix used for the Cost and Usage Report.
        :type report_prefix: str

        :param status: The status of the AWS CUR.
        :type status: str

        :param status_updated_at: The timestamp when the AWS CUR config status was updated.
        :type status_updated_at: str, optional

        :param updated_at: The timestamp when the AWS CUR config status was updated.
        :type updated_at: str, optional
        """
        if account_filters is not unset:
            kwargs["account_filters"] = account_filters
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if months is not unset:
            kwargs["months"] = months
        if status_updated_at is not unset:
            kwargs["status_updated_at"] = status_updated_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.bucket_name = bucket_name
        self_.bucket_region = bucket_region
        self_.report_name = report_name
        self_.report_prefix = report_prefix
        self_.status = status
