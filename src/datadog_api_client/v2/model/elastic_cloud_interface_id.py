# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ElasticCloudInterfaceId(ModelSimple):
    """
    Supported Elastic Cloud interface (source-type) ids.

    :param value: Must be one of ["elastic-cloud", "elastic-cloud-ccm"].
    :type value: str
    """

    allowed_values = {
        "elastic-cloud",
        "elastic-cloud-ccm",
    }
    ELASTIC_CLOUD: ClassVar["ElasticCloudInterfaceId"]
    ELASTIC_CLOUD_CCM: ClassVar["ElasticCloudInterfaceId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ElasticCloudInterfaceId.ELASTIC_CLOUD = ElasticCloudInterfaceId("elastic-cloud")
ElasticCloudInterfaceId.ELASTIC_CLOUD_CCM = ElasticCloudInterfaceId("elastic-cloud-ccm")
