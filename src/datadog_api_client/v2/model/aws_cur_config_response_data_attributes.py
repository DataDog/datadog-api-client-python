# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_cur_config_response_data_attributes_account_filters import (
        AwsCurConfigResponseDataAttributesAccountFilters,
    )


class AwsCurConfigResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cur_config_response_data_attributes_account_filters import (
            AwsCurConfigResponseDataAttributesAccountFilters,
        )

        return {
            "account_filters": (AwsCurConfigResponseDataAttributesAccountFilters,),
            "account_id": (str,),
            "bucket_name": (str,),
            "bucket_region": (str,),
            "created_at": (str,),
            "error_messages": ([str], none_type),
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
        account_filters: Union[AwsCurConfigResponseDataAttributesAccountFilters, UnsetType] = unset,
        account_id: Union[str, UnsetType] = unset,
        bucket_name: Union[str, UnsetType] = unset,
        bucket_region: Union[str, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], none_type, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        report_name: Union[str, UnsetType] = unset,
        report_prefix: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        status_updated_at: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AwsCurConfigResponseDataAttributes`` object.

        :param account_filters: The definition of ``AwsCurConfigResponseDataAttributesAccountFilters`` object.
        :type account_filters: AwsCurConfigResponseDataAttributesAccountFilters, optional

        :param account_id: The ``attributes`` ``account_id``.
        :type account_id: str, optional

        :param bucket_name: The ``attributes`` ``bucket_name``.
        :type bucket_name: str, optional

        :param bucket_region: The ``attributes`` ``bucket_region``.
        :type bucket_region: str, optional

        :param created_at: The ``attributes`` ``created_at``.
        :type created_at: str, optional

        :param error_messages: The ``attributes`` ``error_messages``.
        :type error_messages: [str], none_type, optional

        :param months: The ``attributes`` ``months``.
        :type months: int, optional

        :param report_name: The ``attributes`` ``report_name``.
        :type report_name: str, optional

        :param report_prefix: The ``attributes`` ``report_prefix``.
        :type report_prefix: str, optional

        :param status: The ``attributes`` ``status``.
        :type status: str, optional

        :param status_updated_at: The ``attributes`` ``status_updated_at``.
        :type status_updated_at: str, optional

        :param updated_at: The ``attributes`` ``updated_at``.
        :type updated_at: str, optional
        """
        if account_filters is not unset:
            kwargs["account_filters"] = account_filters
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if bucket_name is not unset:
            kwargs["bucket_name"] = bucket_name
        if bucket_region is not unset:
            kwargs["bucket_region"] = bucket_region
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if months is not unset:
            kwargs["months"] = months
        if report_name is not unset:
            kwargs["report_name"] = report_name
        if report_prefix is not unset:
            kwargs["report_prefix"] = report_prefix
        if status is not unset:
            kwargs["status"] = status
        if status_updated_at is not unset:
            kwargs["status_updated_at"] = status_updated_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
