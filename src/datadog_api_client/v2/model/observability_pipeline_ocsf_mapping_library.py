# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineOcsfMappingLibrary(ModelSimple):
    """
    Predefined library mappings for common log formats.

    :param value: Must be one of ["CloudTrail Account Change", "GCP Cloud Audit CreateBucket", "GCP Cloud Audit CreateSink", "GCP Cloud Audit SetIamPolicy", "GCP Cloud Audit UpdateSink", "Github Audit Log API Activity", "Google Workspace Admin Audit addPrivilege", "Microsoft 365 Defender Incident", "Microsoft 365 Defender UserLoggedIn", "Okta System Log Authentication", "Palo Alto Networks Firewall Traffic"].
    :type value: str
    """

    allowed_values = {
        "CloudTrail Account Change",
        "GCP Cloud Audit CreateBucket",
        "GCP Cloud Audit CreateSink",
        "GCP Cloud Audit SetIamPolicy",
        "GCP Cloud Audit UpdateSink",
        "Github Audit Log API Activity",
        "Google Workspace Admin Audit addPrivilege",
        "Microsoft 365 Defender Incident",
        "Microsoft 365 Defender UserLoggedIn",
        "Okta System Log Authentication",
        "Palo Alto Networks Firewall Traffic",
    }
    CLOUDTRAIL_ACCOUNT_CHANGE: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    GCP_CLOUD_AUDIT_CREATEBUCKET: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    GCP_CLOUD_AUDIT_CREATESINK: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    GCP_CLOUD_AUDIT_SETIAMPOLICY: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    GCP_CLOUD_AUDIT_UPDATESINK: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    GITHUB_AUDIT_LOG_API_ACTIVITY: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    GOOGLE_WORKSPACE_ADMIN_AUDIT_ADDPRIVILEGE: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    MICROSOFT_365_DEFENDER_INCIDENT: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    MICROSOFT_365_DEFENDER_USERLOGGEDIN: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    OKTA_SYSTEM_LOG_AUTHENTICATION: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]
    PALO_ALTO_NETWORKS_FIREWALL_TRAFFIC: ClassVar["ObservabilityPipelineOcsfMappingLibrary"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineOcsfMappingLibrary.CLOUDTRAIL_ACCOUNT_CHANGE = ObservabilityPipelineOcsfMappingLibrary(
    "CloudTrail Account Change"
)
ObservabilityPipelineOcsfMappingLibrary.GCP_CLOUD_AUDIT_CREATEBUCKET = ObservabilityPipelineOcsfMappingLibrary(
    "GCP Cloud Audit CreateBucket"
)
ObservabilityPipelineOcsfMappingLibrary.GCP_CLOUD_AUDIT_CREATESINK = ObservabilityPipelineOcsfMappingLibrary(
    "GCP Cloud Audit CreateSink"
)
ObservabilityPipelineOcsfMappingLibrary.GCP_CLOUD_AUDIT_SETIAMPOLICY = ObservabilityPipelineOcsfMappingLibrary(
    "GCP Cloud Audit SetIamPolicy"
)
ObservabilityPipelineOcsfMappingLibrary.GCP_CLOUD_AUDIT_UPDATESINK = ObservabilityPipelineOcsfMappingLibrary(
    "GCP Cloud Audit UpdateSink"
)
ObservabilityPipelineOcsfMappingLibrary.GITHUB_AUDIT_LOG_API_ACTIVITY = ObservabilityPipelineOcsfMappingLibrary(
    "Github Audit Log API Activity"
)
ObservabilityPipelineOcsfMappingLibrary.GOOGLE_WORKSPACE_ADMIN_AUDIT_ADDPRIVILEGE = (
    ObservabilityPipelineOcsfMappingLibrary("Google Workspace Admin Audit addPrivilege")
)
ObservabilityPipelineOcsfMappingLibrary.MICROSOFT_365_DEFENDER_INCIDENT = ObservabilityPipelineOcsfMappingLibrary(
    "Microsoft 365 Defender Incident"
)
ObservabilityPipelineOcsfMappingLibrary.MICROSOFT_365_DEFENDER_USERLOGGEDIN = ObservabilityPipelineOcsfMappingLibrary(
    "Microsoft 365 Defender UserLoggedIn"
)
ObservabilityPipelineOcsfMappingLibrary.OKTA_SYSTEM_LOG_AUTHENTICATION = ObservabilityPipelineOcsfMappingLibrary(
    "Okta System Log Authentication"
)
ObservabilityPipelineOcsfMappingLibrary.PALO_ALTO_NETWORKS_FIREWALL_TRAFFIC = ObservabilityPipelineOcsfMappingLibrary(
    "Palo Alto Networks Firewall Traffic"
)
