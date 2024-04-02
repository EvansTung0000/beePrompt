import json
import boto3
import re
import os
from boto3.dynamodb.conditions import Key, Attr
from pytz import timezone
from datetime import datetime, timedelta
import common

client = boto3.client("dynamodb", region_name="ap-northeast-1")
dynamodb = boto3.resource("dynamodb")
table_name = common.table_name
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    userid = event["arguments"]["userid"]
    points_to_add = event["arguments"]["point"]
    effective_days = event["arguments"]["effective_days"]

    if points_to_add < 0:
        common.use_points(userid, abs(points_to_add))
    elif points_to_add > 0:
        common.add_points(userid, points_to_add, effective_days)
    return "Success"
