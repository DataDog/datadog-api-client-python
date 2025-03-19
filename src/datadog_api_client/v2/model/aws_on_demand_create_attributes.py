# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AwsOnDemandCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arn": (str,),
        }

    attribute_map = {
        "arn": "arn",
    }

    def __init__(self_, arn: str, **kwargs):
        """
        Attributes for the AWS on demand task.

        :param arn: The arn of the resource to scan. Agentless supports the scan of EC2 instances, lambda functions, AMI, ECR, RDS and S3 buckets.
        :type arn: str
        """
        super().__init__(kwargs)

        self_.arn = arn
