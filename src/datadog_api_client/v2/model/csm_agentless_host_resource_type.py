# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmAgentlessHostResourceType(ModelSimple):
    """
    The type of cloud resource for an agentless host.

    :param value: Must be one of ["aws_ec2_instance", "azure_virtual_machine_instance", "gcp_compute_instance", "oci_instance"].
    :type value: str
    """

    allowed_values = {
        "aws_ec2_instance",
        "azure_virtual_machine_instance",
        "gcp_compute_instance",
        "oci_instance",
    }
    AWS_EC2_INSTANCE: ClassVar["CsmAgentlessHostResourceType"]
    AZURE_VIRTUAL_MACHINE_INSTANCE: ClassVar["CsmAgentlessHostResourceType"]
    GCP_COMPUTE_INSTANCE: ClassVar["CsmAgentlessHostResourceType"]
    OCI_INSTANCE: ClassVar["CsmAgentlessHostResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmAgentlessHostResourceType.AWS_EC2_INSTANCE = CsmAgentlessHostResourceType("aws_ec2_instance")
CsmAgentlessHostResourceType.AZURE_VIRTUAL_MACHINE_INSTANCE = CsmAgentlessHostResourceType(
    "azure_virtual_machine_instance"
)
CsmAgentlessHostResourceType.GCP_COMPUTE_INSTANCE = CsmAgentlessHostResourceType("gcp_compute_instance")
CsmAgentlessHostResourceType.OCI_INSTANCE = CsmAgentlessHostResourceType("oci_instance")
