# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSAccountAndLambdaRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "lambda_arn": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "lambda_arn": "lambda_arn",
    }

    def __init__(self, account_id, lambda_arn, *args, **kwargs):
        """
        AWS account ID and Lambda ARN.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str

        :param lambda_arn: ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup.
        :type lambda_arn: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.lambda_arn = lambda_arn

    @classmethod
    def _from_openapi_data(cls, account_id, lambda_arn, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSAccountAndLambdaRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.lambda_arn = lambda_arn
        return self
