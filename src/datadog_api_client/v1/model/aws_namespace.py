# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class AWSNamespace(ModelSimple):
    """
    The namespace associated with the tag filter entry.

    :param value: Must be one of ["elb", "application_elb", "sqs", "rds", "custom", "network_elb", "lambda"].
    :type value: str
    """

    allowed_values = {
        "elb",
        "application_elb",
        "sqs",
        "rds",
        "custom",
        "network_elb",
        "lambda",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSNamespace.ELB = AWSNamespace("elb")
AWSNamespace.APPLICATION_ELB = AWSNamespace("application_elb")
AWSNamespace.SQS = AWSNamespace("sqs")
AWSNamespace.RDS = AWSNamespace("rds")
AWSNamespace.CUSTOM = AWSNamespace("custom")
AWSNamespace.NETWORK_ELB = AWSNamespace("network_elb")
AWSNamespace.LAMBDA = AWSNamespace("lambda")
