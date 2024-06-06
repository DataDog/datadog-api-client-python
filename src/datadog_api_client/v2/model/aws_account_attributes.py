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
    from datadog_api_client.v2.model.aws_auth_config import AWSAuthConfig
    from datadog_api_client.v2.model.aws_regions_list import AWSRegionsList
    from datadog_api_client.v2.model.aws_logs import AWSLogs
    from datadog_api_client.v2.model.aws_metrics import AWSMetrics
    from datadog_api_client.v2.model.aws_resources import AWSResources
    from datadog_api_client.v2.model.aws_traces import AWSTraces


class AWSAccountAttributes(ModelNormal):
    validations = {
        "aws_account_id": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_auth_config import AWSAuthConfig
        from datadog_api_client.v2.model.aws_regions_list import AWSRegionsList
        from datadog_api_client.v2.model.aws_logs import AWSLogs
        from datadog_api_client.v2.model.aws_metrics import AWSMetrics
        from datadog_api_client.v2.model.aws_resources import AWSResources
        from datadog_api_client.v2.model.aws_traces import AWSTraces

        return {
            "account_tags": ([str],),
            "auth_config": (AWSAuthConfig,),
            "aws_account_id": (str,),
            "aws_regions": (AWSRegionsList,),
            "created_at": (str,),
            "logs_config": (AWSLogs,),
            "metrics_config": (AWSMetrics,),
            "modified_at": (str,),
            "resources_config": (AWSResources,),
            "traces_config": (AWSTraces,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "auth_config": "auth_config",
        "aws_account_id": "aws_account_id",
        "aws_regions": "aws_regions",
        "created_at": "created_at",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "modified_at": "modified_at",
        "resources_config": "resources_config",
        "traces_config": "traces_config",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        aws_account_id: str,
        account_tags: Union[List[str], UnsetType] = unset,
        auth_config: Union[AWSAuthConfig, UnsetType] = unset,
        aws_regions: Union[AWSRegionsList, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        logs_config: Union[AWSLogs, UnsetType] = unset,
        metrics_config: Union[AWSMetrics, UnsetType] = unset,
        modified_at: Union[str, UnsetType] = unset,
        resources_config: Union[AWSResources, UnsetType] = unset,
        traces_config: Union[AWSTraces, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Account attributes

        :param account_tags: Tags to apply to all metrics in the account
        :type account_tags: [str], optional

        :param auth_config: AWS Authentication config
        :type auth_config: AWSAuthConfig, optional

        :param aws_account_id: AWS Account ID
        :type aws_account_id: str

        :param aws_regions: AWS Regions to collect data from
        :type aws_regions: AWSRegionsList, optional

        :param created_at: Creation date of the account
        :type created_at: str, optional

        :param logs_config: AWS Logs config
        :type logs_config: AWSLogs, optional

        :param metrics_config: AWS Metrics config
        :type metrics_config: AWSMetrics, optional

        :param modified_at: Last modification date of the account
        :type modified_at: str, optional

        :param resources_config: AWS Resources config
        :type resources_config: AWSResources, optional

        :param traces_config: AWS Traces config
        :type traces_config: AWSTraces, optional
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if auth_config is not unset:
            kwargs["auth_config"] = auth_config
        if aws_regions is not unset:
            kwargs["aws_regions"] = aws_regions
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if logs_config is not unset:
            kwargs["logs_config"] = logs_config
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if resources_config is not unset:
            kwargs["resources_config"] = resources_config
        if traces_config is not unset:
            kwargs["traces_config"] = traces_config
        super().__init__(kwargs)

        self_.aws_account_id = aws_account_id
