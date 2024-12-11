# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_auth_config import AWSAuthConfig
    from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
    from datadog_api_client.v2.model.aws_regions import AWSRegions
    from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
    from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
    from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
    from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig
    from datadog_api_client.v2.model.aws_auth_config_keys import AWSAuthConfigKeys
    from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole
    from datadog_api_client.v2.model.aws_regions_include_all import AWSRegionsIncludeAll
    from datadog_api_client.v2.model.aws_regions_include_only import AWSRegionsIncludeOnly


class AWSAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_auth_config import AWSAuthConfig
        from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
        from datadog_api_client.v2.model.aws_regions import AWSRegions
        from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
        from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
        from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
        from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig

        return {
            "account_tags": ([str],),
            "auth_config": (AWSAuthConfig,),
            "aws_account_id": (str,),
            "aws_partition": (AWSAccountPartition,),
            "aws_regions": (AWSRegions,),
            "created_at": (datetime,),
            "logs_config": (AWSLogsConfig,),
            "metrics_config": (AWSMetricsConfig,),
            "modified_at": (datetime,),
            "resources_config": (AWSResourcesConfig,),
            "traces_config": (AWSTracesConfig,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "auth_config": "auth_config",
        "aws_account_id": "aws_account_id",
        "aws_partition": "aws_partition",
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
        account_tags: Union[List[str], none_type, UnsetType] = unset,
        auth_config: Union[AWSAuthConfig, AWSAuthConfigKeys, AWSAuthConfigRole, UnsetType] = unset,
        aws_partition: Union[AWSAccountPartition, UnsetType] = unset,
        aws_regions: Union[AWSRegions, AWSRegionsIncludeAll, AWSRegionsIncludeOnly, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        logs_config: Union[AWSLogsConfig, UnsetType] = unset,
        metrics_config: Union[AWSMetricsConfig, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        resources_config: Union[AWSResourcesConfig, UnsetType] = unset,
        traces_config: Union[AWSTracesConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Account response attributes.

        :param account_tags: Tags to apply to all hosts and metrics reporting for this account. Defaults to ``[]``.
        :type account_tags: [str], none_type, optional

        :param auth_config: AWS Authentication config.
        :type auth_config: AWSAuthConfig, optional

        :param aws_account_id: AWS Account ID.
        :type aws_account_id: str

        :param aws_partition: AWS partition your AWS account is scoped to. Defaults to ``aws``.
            See `Partitions <https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html>`_ in the AWS documentation for more information.
        :type aws_partition: AWSAccountPartition, optional

        :param aws_regions: AWS Regions to collect data from. Defaults to ``include_all``.
        :type aws_regions: AWSRegions, optional

        :param created_at: Timestamp of when the account integration was created.
        :type created_at: datetime, optional

        :param logs_config: AWS Logs Collection config.
        :type logs_config: AWSLogsConfig, optional

        :param metrics_config: AWS Metrics Collection config.
        :type metrics_config: AWSMetricsConfig, optional

        :param modified_at: Timestamp of when the account integration was updated.
        :type modified_at: datetime, optional

        :param resources_config: AWS Resources Collection config.
        :type resources_config: AWSResourcesConfig, optional

        :param traces_config: AWS Traces Collection config.
        :type traces_config: AWSTracesConfig, optional
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if auth_config is not unset:
            kwargs["auth_config"] = auth_config
        if aws_partition is not unset:
            kwargs["aws_partition"] = aws_partition
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
