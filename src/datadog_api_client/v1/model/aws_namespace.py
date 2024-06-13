# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSNamespace(ModelSimple):
    """
    The namespace associated with the tag filter entry.

    :param value: Must be one of ["api_gateway", "application_elb", "apprunner", "appstream", "appsync", "athena", "auto_scaling", "backup", "bedrock", "billing", "budgeting", "certificatemanager", "cloudfront", "cloudhsm", "cloudsearch", "cloudwatch_events", "cloudwatch_logs", "codebuild", "codewhisperer", "cognito", "collect_custom_metrics", "config", "connect", "crawl_alarms", "custom", "directconnect", "dms", "documentdb", "dynamodb", "dynamodbaccelerator", "ebs", "ec2", "ec2api", "ec2spot", "ecr", "ecs", "efs", "elasticache", "elasticbeanstalk", "elasticinference", "elastictranscoder", "elb", "emr", "es", "firehose", "fsx", "gamelift", "globalaccelerator", "glue", "inspector", "iot", "keyspaces", "kinesis", "kinesis_analytics", "kms", "lambda", "lex", "mediaconnect", "mediaconvert", "medialive", "mediapackage", "mediastore", "mediatailor", "memorydb", "ml", "mq", "msk", "mwaa", "nat_gateway", "neptune", "network_elb", "networkfirewall", "networkmonitor", "opensearchserverless", "opsworks", "polly", "privatelinkendpoints", "privatelinkservices", "rds", "rdsproxy", "redshift", "rekognition", "route53", "route53resolver", "s3", "s3storagelens", "sagemaker", "sagemakerendpoints", "sagemakerlabelingjobs", "sagemakermodelbuildingpipeline", "sagemakerprocessingjobs", "sagemakertrainingjobs", "sagemakertransformjobs", "sagemakerworkteam", "service_quotas", "ses", "shield", "sns", "sqs", "step_functions", "storage_gateway", "swf", "textract", "transitgateway", "translate", "trusted_advisor", "usage", "vpn", "waf", "wafv2", "workspaces", "xray"].
    :type value: str
    """

    allowed_values = {
        "api_gateway",
        "application_elb",
        "apprunner",
        "appstream",
        "appsync",
        "athena",
        "auto_scaling",
        "backup",
        "bedrock",
        "billing",
        "budgeting",
        "certificatemanager",
        "cloudfront",
        "cloudhsm",
        "cloudsearch",
        "cloudwatch_events",
        "cloudwatch_logs",
        "codebuild",
        "codewhisperer",
        "cognito",
        "collect_custom_metrics",
        "config",
        "connect",
        "crawl_alarms",
        "custom",
        "directconnect",
        "dms",
        "documentdb",
        "dynamodb",
        "dynamodbaccelerator",
        "ebs",
        "ec2",
        "ec2api",
        "ec2spot",
        "ecr",
        "ecs",
        "efs",
        "elasticache",
        "elasticbeanstalk",
        "elasticinference",
        "elastictranscoder",
        "elb",
        "emr",
        "es",
        "firehose",
        "fsx",
        "gamelift",
        "globalaccelerator",
        "glue",
        "inspector",
        "iot",
        "keyspaces",
        "kinesis",
        "kinesis_analytics",
        "kms",
        "lambda",
        "lex",
        "mediaconnect",
        "mediaconvert",
        "medialive",
        "mediapackage",
        "mediastore",
        "mediatailor",
        "memorydb",
        "ml",
        "mq",
        "msk",
        "mwaa",
        "nat_gateway",
        "neptune",
        "network_elb",
        "networkfirewall",
        "networkmonitor",
        "opensearchserverless",
        "opsworks",
        "polly",
        "privatelinkendpoints",
        "privatelinkservices",
        "rds",
        "rdsproxy",
        "redshift",
        "rekognition",
        "route53",
        "route53resolver",
        "s3",
        "s3storagelens",
        "sagemaker",
        "sagemakerendpoints",
        "sagemakerlabelingjobs",
        "sagemakermodelbuildingpipeline",
        "sagemakerprocessingjobs",
        "sagemakertrainingjobs",
        "sagemakertransformjobs",
        "sagemakerworkteam",
        "service_quotas",
        "ses",
        "shield",
        "sns",
        "sqs",
        "step_functions",
        "storage_gateway",
        "swf",
        "textract",
        "transitgateway",
        "translate",
        "trusted_advisor",
        "usage",
        "vpn",
        "waf",
        "wafv2",
        "workspaces",
        "xray",
    }
    API_GATEWAY: ClassVar["AWSNamespace"]
    APPLICATION_ELB: ClassVar["AWSNamespace"]
    APPRUNNER: ClassVar["AWSNamespace"]
    APPSTREAM: ClassVar["AWSNamespace"]
    APPSYNC: ClassVar["AWSNamespace"]
    ATHENA: ClassVar["AWSNamespace"]
    AUTO_SCALING: ClassVar["AWSNamespace"]
    BACKUP: ClassVar["AWSNamespace"]
    BEDROCK: ClassVar["AWSNamespace"]
    BILLING: ClassVar["AWSNamespace"]
    BUDGETING: ClassVar["AWSNamespace"]
    CERTIFICATEMANAGER: ClassVar["AWSNamespace"]
    CLOUDFRONT: ClassVar["AWSNamespace"]
    CLOUDHSM: ClassVar["AWSNamespace"]
    CLOUDSEARCH: ClassVar["AWSNamespace"]
    CLOUDWATCH_EVENTS: ClassVar["AWSNamespace"]
    CLOUDWATCH_LOGS: ClassVar["AWSNamespace"]
    CODEBUILD: ClassVar["AWSNamespace"]
    CODEWHISPERER: ClassVar["AWSNamespace"]
    COGNITO: ClassVar["AWSNamespace"]
    COLLECT_CUSTOM_METRICS: ClassVar["AWSNamespace"]
    CONFIG: ClassVar["AWSNamespace"]
    CONNECT: ClassVar["AWSNamespace"]
    CRAWL_ALARMS: ClassVar["AWSNamespace"]
    CUSTOM: ClassVar["AWSNamespace"]
    DIRECTCONNECT: ClassVar["AWSNamespace"]
    DMS: ClassVar["AWSNamespace"]
    DOCUMENTDB: ClassVar["AWSNamespace"]
    DYNAMODB: ClassVar["AWSNamespace"]
    DYNAMODBACCELERATOR: ClassVar["AWSNamespace"]
    EBS: ClassVar["AWSNamespace"]
    EC2: ClassVar["AWSNamespace"]
    EC2API: ClassVar["AWSNamespace"]
    EC2SPOT: ClassVar["AWSNamespace"]
    ECR: ClassVar["AWSNamespace"]
    ECS: ClassVar["AWSNamespace"]
    EFS: ClassVar["AWSNamespace"]
    ELASTICACHE: ClassVar["AWSNamespace"]
    ELASTICBEANSTALK: ClassVar["AWSNamespace"]
    ELASTICINFERENCE: ClassVar["AWSNamespace"]
    ELASTICTRANSCODER: ClassVar["AWSNamespace"]
    ELB: ClassVar["AWSNamespace"]
    EMR: ClassVar["AWSNamespace"]
    ES: ClassVar["AWSNamespace"]
    FIREHOSE: ClassVar["AWSNamespace"]
    FSX: ClassVar["AWSNamespace"]
    GAMELIFT: ClassVar["AWSNamespace"]
    GLOBALACCELERATOR: ClassVar["AWSNamespace"]
    GLUE: ClassVar["AWSNamespace"]
    INSPECTOR: ClassVar["AWSNamespace"]
    IOT: ClassVar["AWSNamespace"]
    KEYSPACES: ClassVar["AWSNamespace"]
    KINESIS: ClassVar["AWSNamespace"]
    KINESIS_ANALYTICS: ClassVar["AWSNamespace"]
    KMS: ClassVar["AWSNamespace"]
    LAMBDA: ClassVar["AWSNamespace"]
    LEX: ClassVar["AWSNamespace"]
    MEDIACONNECT: ClassVar["AWSNamespace"]
    MEDIACONVERT: ClassVar["AWSNamespace"]
    MEDIALIVE: ClassVar["AWSNamespace"]
    MEDIAPACKAGE: ClassVar["AWSNamespace"]
    MEDIASTORE: ClassVar["AWSNamespace"]
    MEDIATAILOR: ClassVar["AWSNamespace"]
    MEMORYDB: ClassVar["AWSNamespace"]
    ML: ClassVar["AWSNamespace"]
    MQ: ClassVar["AWSNamespace"]
    MSK: ClassVar["AWSNamespace"]
    MWAA: ClassVar["AWSNamespace"]
    NAT_GATEWAY: ClassVar["AWSNamespace"]
    NEPTUNE: ClassVar["AWSNamespace"]
    NETWORK_ELB: ClassVar["AWSNamespace"]
    NETWORKFIREWALL: ClassVar["AWSNamespace"]
    NETWORKMONITOR: ClassVar["AWSNamespace"]
    OPENSEARCHSERVERLESS: ClassVar["AWSNamespace"]
    OPSWORKS: ClassVar["AWSNamespace"]
    POLLY: ClassVar["AWSNamespace"]
    PRIVATELINKENDPOINTS: ClassVar["AWSNamespace"]
    PRIVATELINKSERVICES: ClassVar["AWSNamespace"]
    RDS: ClassVar["AWSNamespace"]
    RDSPROXY: ClassVar["AWSNamespace"]
    REDSHIFT: ClassVar["AWSNamespace"]
    REKOGNITION: ClassVar["AWSNamespace"]
    ROUTE53: ClassVar["AWSNamespace"]
    ROUTE53RESOLVER: ClassVar["AWSNamespace"]
    S3: ClassVar["AWSNamespace"]
    S3STORAGELENS: ClassVar["AWSNamespace"]
    SAGEMAKER: ClassVar["AWSNamespace"]
    SAGEMAKERENDPOINTS: ClassVar["AWSNamespace"]
    SAGEMAKERLABELINGJOBS: ClassVar["AWSNamespace"]
    SAGEMAKERMODELBUILDINGPIPELINE: ClassVar["AWSNamespace"]
    SAGEMAKERPROCESSINGJOBS: ClassVar["AWSNamespace"]
    SAGEMAKERTRAININGJOBS: ClassVar["AWSNamespace"]
    SAGEMAKERTRANSFORMJOBS: ClassVar["AWSNamespace"]
    SAGEMAKERWORKTEAM: ClassVar["AWSNamespace"]
    SERVICE_QUOTAS: ClassVar["AWSNamespace"]
    SES: ClassVar["AWSNamespace"]
    SHIELD: ClassVar["AWSNamespace"]
    SNS: ClassVar["AWSNamespace"]
    SQS: ClassVar["AWSNamespace"]
    STEP_FUNCTIONS: ClassVar["AWSNamespace"]
    STORAGE_GATEWAY: ClassVar["AWSNamespace"]
    SWF: ClassVar["AWSNamespace"]
    TEXTRACT: ClassVar["AWSNamespace"]
    TRANSITGATEWAY: ClassVar["AWSNamespace"]
    TRANSLATE: ClassVar["AWSNamespace"]
    TRUSTED_ADVISOR: ClassVar["AWSNamespace"]
    USAGE: ClassVar["AWSNamespace"]
    VPN: ClassVar["AWSNamespace"]
    WAF: ClassVar["AWSNamespace"]
    WAFV2: ClassVar["AWSNamespace"]
    WORKSPACES: ClassVar["AWSNamespace"]
    XRAY: ClassVar["AWSNamespace"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSNamespace.API_GATEWAY = AWSNamespace("api_gateway")
AWSNamespace.APPLICATION_ELB = AWSNamespace("application_elb")
AWSNamespace.APPRUNNER = AWSNamespace("apprunner")
AWSNamespace.APPSTREAM = AWSNamespace("appstream")
AWSNamespace.APPSYNC = AWSNamespace("appsync")
AWSNamespace.ATHENA = AWSNamespace("athena")
AWSNamespace.AUTO_SCALING = AWSNamespace("auto_scaling")
AWSNamespace.BACKUP = AWSNamespace("backup")
AWSNamespace.BEDROCK = AWSNamespace("bedrock")
AWSNamespace.BILLING = AWSNamespace("billing")
AWSNamespace.BUDGETING = AWSNamespace("budgeting")
AWSNamespace.CERTIFICATEMANAGER = AWSNamespace("certificatemanager")
AWSNamespace.CLOUDFRONT = AWSNamespace("cloudfront")
AWSNamespace.CLOUDHSM = AWSNamespace("cloudhsm")
AWSNamespace.CLOUDSEARCH = AWSNamespace("cloudsearch")
AWSNamespace.CLOUDWATCH_EVENTS = AWSNamespace("cloudwatch_events")
AWSNamespace.CLOUDWATCH_LOGS = AWSNamespace("cloudwatch_logs")
AWSNamespace.CODEBUILD = AWSNamespace("codebuild")
AWSNamespace.CODEWHISPERER = AWSNamespace("codewhisperer")
AWSNamespace.COGNITO = AWSNamespace("cognito")
AWSNamespace.COLLECT_CUSTOM_METRICS = AWSNamespace("collect_custom_metrics")
AWSNamespace.CONFIG = AWSNamespace("config")
AWSNamespace.CONNECT = AWSNamespace("connect")
AWSNamespace.CRAWL_ALARMS = AWSNamespace("crawl_alarms")
AWSNamespace.CUSTOM = AWSNamespace("custom")
AWSNamespace.DIRECTCONNECT = AWSNamespace("directconnect")
AWSNamespace.DMS = AWSNamespace("dms")
AWSNamespace.DOCUMENTDB = AWSNamespace("documentdb")
AWSNamespace.DYNAMODB = AWSNamespace("dynamodb")
AWSNamespace.DYNAMODBACCELERATOR = AWSNamespace("dynamodbaccelerator")
AWSNamespace.EBS = AWSNamespace("ebs")
AWSNamespace.EC2 = AWSNamespace("ec2")
AWSNamespace.EC2API = AWSNamespace("ec2api")
AWSNamespace.EC2SPOT = AWSNamespace("ec2spot")
AWSNamespace.ECR = AWSNamespace("ecr")
AWSNamespace.ECS = AWSNamespace("ecs")
AWSNamespace.EFS = AWSNamespace("efs")
AWSNamespace.ELASTICACHE = AWSNamespace("elasticache")
AWSNamespace.ELASTICBEANSTALK = AWSNamespace("elasticbeanstalk")
AWSNamespace.ELASTICINFERENCE = AWSNamespace("elasticinference")
AWSNamespace.ELASTICTRANSCODER = AWSNamespace("elastictranscoder")
AWSNamespace.ELB = AWSNamespace("elb")
AWSNamespace.EMR = AWSNamespace("emr")
AWSNamespace.ES = AWSNamespace("es")
AWSNamespace.FIREHOSE = AWSNamespace("firehose")
AWSNamespace.FSX = AWSNamespace("fsx")
AWSNamespace.GAMELIFT = AWSNamespace("gamelift")
AWSNamespace.GLOBALACCELERATOR = AWSNamespace("globalaccelerator")
AWSNamespace.GLUE = AWSNamespace("glue")
AWSNamespace.INSPECTOR = AWSNamespace("inspector")
AWSNamespace.IOT = AWSNamespace("iot")
AWSNamespace.KEYSPACES = AWSNamespace("keyspaces")
AWSNamespace.KINESIS = AWSNamespace("kinesis")
AWSNamespace.KINESIS_ANALYTICS = AWSNamespace("kinesis_analytics")
AWSNamespace.KMS = AWSNamespace("kms")
AWSNamespace.LAMBDA = AWSNamespace("lambda")
AWSNamespace.LEX = AWSNamespace("lex")
AWSNamespace.MEDIACONNECT = AWSNamespace("mediaconnect")
AWSNamespace.MEDIACONVERT = AWSNamespace("mediaconvert")
AWSNamespace.MEDIALIVE = AWSNamespace("medialive")
AWSNamespace.MEDIAPACKAGE = AWSNamespace("mediapackage")
AWSNamespace.MEDIASTORE = AWSNamespace("mediastore")
AWSNamespace.MEDIATAILOR = AWSNamespace("mediatailor")
AWSNamespace.MEMORYDB = AWSNamespace("memorydb")
AWSNamespace.ML = AWSNamespace("ml")
AWSNamespace.MQ = AWSNamespace("mq")
AWSNamespace.MSK = AWSNamespace("msk")
AWSNamespace.MWAA = AWSNamespace("mwaa")
AWSNamespace.NAT_GATEWAY = AWSNamespace("nat_gateway")
AWSNamespace.NEPTUNE = AWSNamespace("neptune")
AWSNamespace.NETWORK_ELB = AWSNamespace("network_elb")
AWSNamespace.NETWORKFIREWALL = AWSNamespace("networkfirewall")
AWSNamespace.NETWORKMONITOR = AWSNamespace("networkmonitor")
AWSNamespace.OPENSEARCHSERVERLESS = AWSNamespace("opensearchserverless")
AWSNamespace.OPSWORKS = AWSNamespace("opsworks")
AWSNamespace.POLLY = AWSNamespace("polly")
AWSNamespace.PRIVATELINKENDPOINTS = AWSNamespace("privatelinkendpoints")
AWSNamespace.PRIVATELINKSERVICES = AWSNamespace("privatelinkservices")
AWSNamespace.RDS = AWSNamespace("rds")
AWSNamespace.RDSPROXY = AWSNamespace("rdsproxy")
AWSNamespace.REDSHIFT = AWSNamespace("redshift")
AWSNamespace.REKOGNITION = AWSNamespace("rekognition")
AWSNamespace.ROUTE53 = AWSNamespace("route53")
AWSNamespace.ROUTE53RESOLVER = AWSNamespace("route53resolver")
AWSNamespace.S3 = AWSNamespace("s3")
AWSNamespace.S3STORAGELENS = AWSNamespace("s3storagelens")
AWSNamespace.SAGEMAKER = AWSNamespace("sagemaker")
AWSNamespace.SAGEMAKERENDPOINTS = AWSNamespace("sagemakerendpoints")
AWSNamespace.SAGEMAKERLABELINGJOBS = AWSNamespace("sagemakerlabelingjobs")
AWSNamespace.SAGEMAKERMODELBUILDINGPIPELINE = AWSNamespace("sagemakermodelbuildingpipeline")
AWSNamespace.SAGEMAKERPROCESSINGJOBS = AWSNamespace("sagemakerprocessingjobs")
AWSNamespace.SAGEMAKERTRAININGJOBS = AWSNamespace("sagemakertrainingjobs")
AWSNamespace.SAGEMAKERTRANSFORMJOBS = AWSNamespace("sagemakertransformjobs")
AWSNamespace.SAGEMAKERWORKTEAM = AWSNamespace("sagemakerworkteam")
AWSNamespace.SERVICE_QUOTAS = AWSNamespace("service_quotas")
AWSNamespace.SES = AWSNamespace("ses")
AWSNamespace.SHIELD = AWSNamespace("shield")
AWSNamespace.SNS = AWSNamespace("sns")
AWSNamespace.SQS = AWSNamespace("sqs")
AWSNamespace.STEP_FUNCTIONS = AWSNamespace("step_functions")
AWSNamespace.STORAGE_GATEWAY = AWSNamespace("storage_gateway")
AWSNamespace.SWF = AWSNamespace("swf")
AWSNamespace.TEXTRACT = AWSNamespace("textract")
AWSNamespace.TRANSITGATEWAY = AWSNamespace("transitgateway")
AWSNamespace.TRANSLATE = AWSNamespace("translate")
AWSNamespace.TRUSTED_ADVISOR = AWSNamespace("trusted_advisor")
AWSNamespace.USAGE = AWSNamespace("usage")
AWSNamespace.VPN = AWSNamespace("vpn")
AWSNamespace.WAF = AWSNamespace("waf")
AWSNamespace.WAFV2 = AWSNamespace("wafv2")
AWSNamespace.WORKSPACES = AWSNamespace("workspaces")
AWSNamespace.XRAY = AWSNamespace("xray")
